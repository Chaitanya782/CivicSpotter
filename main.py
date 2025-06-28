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

# Hero Section
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="font-size: 3rem; margin-bottom: 0;">🏙️ CivicSpotter</h1>
    <p style="font-size: 1.5rem; color: #666; margin-top: 0;">Smart Civic Issue Reporting Platform</p>
</div>
""", unsafe_allow_html=True)

# Quick Stats
col1, col2, col3, col4 = st.columns(4)
os.makedirs("issues/active", exist_ok=True)
os.makedirs("issues/completed", exist_ok=True)
# Count issues for stats
active_count = len([f for f in os.listdir("issues/active") if f.endswith(".json")]) if os.path.exists(
    "issues/active") else 0
completed_count = len([f for f in os.listdir("issues/completed") if f.endswith(".json")]) if os.path.exists(
    "issues/completed") else 0

with col1:
    st.metric("🔴 Active Issues", active_count)
with col2:
    st.metric("✅ Resolved Issues", completed_count)
with col3:
    st.metric("🏙️ Cities Covered", "50+")
with col4:
    st.metric("⚡ Avg Response", "2.3 hrs")

st.markdown("---")

# Value Proposition
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 🌆 What is CivicSpotter?")
    st.markdown("""
    CivicSpotter is an **AI-powered civic engagement platform** that transforms how citizens report local issues and how governments respond to them.

    **🚀 For Citizens:**
    - 📸 **Just take a photo** - We handle the rest
    - 🗺️ **Automatic location detection** from GPS or image metadata
    - 🔍 **Track your issues** with unique IDs
    - 🤝 **Smart duplicate prevention** - similar issues get grouped

    **🛠️ For Governments:**
    - 📧 **Automated professional emails** to the right departments
    - 🐦 **Social media amplification** for public accountability
    - 📊 **Analytics dashboard** for data-driven decisions
    - ⚡ **Streamlined workflow** from report to resolution
    """)

with col2:
    st.markdown("### 🎯 How It Works")
    st.markdown("""
    1. **📸 Upload Photo**
       Citizen takes photo of issue

    2. **🧠 AI Processing**
       Extract location, find authority

    3. **👨‍💼 Admin Review**
       Verify details, approve actions

    4. **📧 Auto-Contact**
       Email sent to civic authority

    5. **🐦 Public Post**
       Tweet for transparency

    6. **📊 Track Progress**
       Monitor until resolution
    """)

# Navigation Buttons
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🙋 Report Issue", type="primary", use_container_width=True):
        st.switch_page("pages/_1_User_Dashboard.py")

with col2:
    if st.button("📊 View Analytics", use_container_width=True):
        st.switch_page("pages/_3_Analytics_Dashboard.py")

with col3:
    if st.button("🎬 Live Demo", use_container_width=True):
        st.switch_page("pages/_4_Live_Demo.py")

with col4:
    if st.session_state.admin_logged_in:
        if st.button("🛠️ Admin Panel", use_container_width=True):
            st.switch_page("pages/_2_Admin_Dashboard.py")
    else:
        st.button("🔒 Admin Login", disabled=True, use_container_width=True)

# --- Sidebar Login --- #
with st.sidebar:
    st.header("🔐 Admin Access")
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

# Issue Search
st.markdown("---")
st.markdown("## 🔍 Track Your Issue")

search_id = st.text_input("Enter your Issue ID (e.g., Mumbai_20250628_001)", placeholder="City_YYYYMMDD_XXX")

if st.button("🔍 Search Issue"):
    found = False
    for folder in ["issues/active", "issues/completed"]:
        try:
            if os.path.exists(folder):
                for file in os.listdir(folder):
                    if file.endswith(".json"):
                        path = os.path.join(folder, file)
                        with open(path, "r") as f:
                            state = json.load(f)
                        if state.get("issue_id") == search_id:
                            found = True

                            # Status indicator
                            status_color = "🟢" if folder.endswith("completed") else "🟡"
                            status_text = "Completed" if folder.endswith("completed") else "In Progress"

                            st.success(f"{status_color} Issue Found - Status: {status_text}")

                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown(f"**🆔 ID**: `{state['issue_id']}`")
                                st.markdown(f"**📌 Type**: {state.get('issue_type')}")
                                st.markdown(
                                    f"**📍 Location**: {state.get('metadata', {}).get('Address', {}).get('city', 'N/A')}")

                            with col2:
                                st.markdown(f"**📷 Images**: {len(state.get('image_paths', []))} uploaded")
                                st.markdown(f"**🔄 Similar Reports**: {state.get('similar_count', 0)}")

                                if state.get("tweet", {}).get("url"):
                                    st.markdown(f"**🐦 Tweet**: [View Tweet]({state['tweet']['url']})")
                                else:
                                    st.markdown("**🐦 Tweet**: Not posted yet")

                            break
            if found:
                break
        except Exception as e:
            st.error(f"Error reading files in {folder}: {e}")

    if not found:
        st.warning("❌ No issue found with that ID. Please check the ID and try again.")

# Footer

st.markdown("---", unsafe_allow_html=True)

st.markdown("""
<div style="margin: 2rem 0; text-align: center;">
    <a href="https://bolt.new" target="_blank" style="text-decoration: none;">
        <img src="https://img.shields.io/badge/Built%20with-Bolt.new-FF6B6B?style=for-the-badge&logo=thunderstorm&logoColor=white" 
             alt="Built with Bolt.new" 
             style="border-radius: 8px; box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3); height: 40px;">
    </a>
</div>

<p style="margin-top: 1rem; font-size: 0.9rem; color: #888; font-style: italic; text-align: center;">
    ⚡ Powered by AI • 🎯 Built for Impact • 🚀 Deployed with Bolt
</p>
""", unsafe_allow_html=True)