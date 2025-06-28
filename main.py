import json

import streamlit as st
import hashlib
import os
from dotenv import load_dotenv

# Load credentials
load_dotenv()
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH")

st.set_page_config(page_title="CivicSpotter", layout="centered")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Track login state
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

st.title("📍 Welcome to CivicSpotter")
st.markdown("---")
st.markdown("## 🌆 What is CivicSpotter?")
st.markdown("""
CivicSpotter is a lightweight civic issue tracking platform that allows everyday citizens to report local problems — like potholes, garbage, or streetlight issues — using a simple photo upload.

Meanwhile, local authorities (admins) can view, review, and act on these reports through an organized dashboard.

""")

st.markdown("## 🧑‍🤝‍🧑 Who Can Use This App?")
st.markdown("""
- **🙋 Public Users:** You can report issues by uploading a photo and submitting basic details.
- **🛠️ Admins:** Use the login panel on the left to review submitted issues, verify metadata, contact authorities, and approve tweets.
""")

st.markdown("## ⚙️ How It Works")
st.markdown("""
1. User uploads an image of a civic issue.
2. The system auto-generates location metadata and authority email.
3. Admins verify details and optionally edit the information.
4. A tweet and email are prepared for outreach.
5. Upon approval, the system contacts the concerned civic authority.

""")

st.info("Use the **sidebar** to log in as Admin or explore the User Dashboard.")

st.markdown("---")
st.markdown("Built with ❤️ using Python, Streamlit, and CivicTech principles.")


# --- Sidebar Login --- #
with st.sidebar:
    st.header("🔐 Admin Login")
    if not st.session_state.admin_logged_in:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == ADMIN_USERNAME and hash_password(password) == ADMIN_PASSWORD_HASH:
                st.session_state.admin_logged_in = True
                st.success("✅ Logged in as admin")
                st.switch_page("pages/_2_Admin_Dashboard.py")
            else:
                st.error("❌ Invalid credentials")
    else:
        st.success(f"✅ Logged in as {ADMIN_USERNAME}")
        if st.button("Go to Admin Dashboard"):
            st.switch_page("pages/_2_Admin_Dashboard.py")
        if st.button("Logout"):
            st.session_state.admin_logged_in = False
            st.rerun()

# Public user message
st.markdown("### 🙋 Public Access")
st.info("Click below to explore civic issues.")
if st.button("Go to User Dashboard"):
    st.switch_page("pages/_1_User_Dashboard.py")

st.markdown("## 🔍 Search Your Submitted Issue")

search_id = st.text_input("Enter your Issue ID (e.g., Mumbai_20250628_001)")

if st.button("Search"):
    found = False
    for folder in ["issues/active", "issues/completed"]:
        try:
            for file in os.listdir(folder):
                if file.endswith(".json"):
                    path = os.path.join(folder, file)
                    with open(path, "r") as f:
                        state = json.load(f)
                    if state.get("issue_id") == search_id:
                        found = True
                        st.success("✅ Issue Found")
                        st.markdown(f"**🆔 ID**: `{state['issue_id']}`")
                        st.markdown(f"**📌 Type**: {state.get('issue_type')}")
                        st.markdown(
                            f"**📍 Location**: {state.get('metadata', {}).get('Address', {}).get('city', 'N/A')}")
                        st.markdown(f"**📷 Images**: {len(state.get('image_paths', []))} uploaded")

                        if state.get("tweet", {}).get("url"):
                            st.markdown(f"**🐦 Tweet**: [View Tweet]({state['tweet']['url']})")

                        st.markdown(f"**📄 Status**: `{state['status']}`")
                        break
            if found:
                break
        except Exception as e:
            st.error(f"Error reading files in {folder}: {e}")

    if not found:
        st.warning("❌ No issue found with that ID.")

