import streamlit as st
import time
import random
from datetime import datetime

st.set_page_config(page_title="🎬 Live Demo", layout="wide")
st.title("🎬 CivicSpotter Live Demo")

st.markdown("""
### 🎯 **Hackathon Demo Simulation**
This page simulates the complete CivicSpotter workflow for demonstration purposes.
""")

# Demo Controls
col1, col2 = st.columns([3, 1])

with col1:
    demo_type = st.selectbox(
        "Choose Demo Scenario",
        ["🕳️ Pothole Report", "🗑️ Garbage Dump", "💡 Broken Streetlight", "🚧 Road Damage"]
    )

with col2:
    if st.button("🚀 Start Demo", type="primary"):
        st.session_state.demo_running = True
        st.session_state.demo_step = 0

# Demo Simulation
if st.session_state.get("demo_running", False):

    # Progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    steps = [
        "📸 Processing uploaded image...",
        "🗺️ Extracting GPS coordinates...",
        "🏠 Reverse geocoding address...",
        "🔍 Checking for similar issues...",
        "🧠 Discovering authority contacts...",
        "📧 Generating professional email...",
        "🐦 Creating social media post...",
        "✅ Issue submitted successfully!"
    ]

    # Simulate processing steps
    for i, step in enumerate(steps):
        progress_bar.progress((i + 1) / len(steps))
        status_text.text(step)
        time.sleep(1.5)  # Simulate processing time

    # Show results
    st.success("🎉 Demo completed successfully!")

    # Generate demo data
    demo_id = f"Demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Funny tweet templates for different issue types
    funny_tweets = {
        "🕳️ Pothole Report": [
            f"🕳️ BREAKING: MG Road pothole has achieved crater status! 🌙 NASA is reportedly interested for Mars training simulations 🚀\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\nLet's fill this before it becomes a tourist attraction! 😅\n\n#CivicIssue #PotholeProblems #BangaloreTraffic #SmartCity",

            f"🚨 POTHOLE ALERT: MG Road crater now accepting applications for permanent residents! 🏠 Amenities include: Free car alignment checks & suspension massage therapy! 💆‍♂️\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\n#CivicIssue #BangaloreTraffic #SmartCity #UrbanIndia",

            f"🕳️ MG Road pothole update: It's now deep enough to hide a small car! 🚗 Local residents have started a betting pool on when it'll reach Earth's core 🌍\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\n#CivicIssue #PotholeProblems #SmartCity"
        ],

        "🗑️ Garbage Dump": [
            f"🗑️ BREAKING: MG Road garbage dump has achieved landmark status! 📍 Local GPS now lists it as a 'point of interest' 🎯 Tourism board is confused! 🤔\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\n#CivicIssue #CleanIndia #BangaloreTraffic #SmartCity",

            f"🚨 GARBAGE ALERT: MG Road waste collection has evolved into modern art installation! 🎨 Museum curators are reportedly interested 🖼️\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\nLet's clean this masterpiece! 😄\n\n#CivicIssue #UrbanIndia #SmartCity",

            f"🗑️ MG Road garbage situation: We've officially created our own ecosystem! 🌱 Scientists are studying the new species discovered 🔬\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\n#CivicIssue #CleanIndia #SmartCity"
        ],

        "💡 Broken Streetlight": [
            f"💡 BREAKING: MG Road streetlight has been playing hide-and-seek for weeks! 🙈 Current score: Darkness 1, Citizens 0 🌙\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\nTime to light up the game! ⚡\n\n#CivicIssue #LightUp #BangaloreTraffic #SmartCity",

            f"🚨 LIGHT ALERT: MG Road streetlight is on permanent vacation! 🏖️ Residents now using phone flashlights as street lighting 📱\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\n#CivicIssue #UrbanIndia #SmartCity",

            f"💡 MG Road streetlight update: It's become a professional mime artist - completely silent and invisible! 🎭\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\nBreak a leg... or turn on! 🎪\n\n#CivicIssue #LightUp #SmartCity"
        ],

        "🚧 Road Damage": [
            f"🚧 BREAKING: MG Road has achieved off-road status while still being a road! 🏞️ Adventure sports enthusiasts are thrilled! 🚵‍♂️\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\nLet's bring it back to civilization! 🛣️\n\n#CivicIssue #RoadSafety #BangaloreTraffic #SmartCity",

            f"🚨 ROAD ALERT: MG Road surface now offers free massage therapy for car suspensions! 💆‍♂️ Chiropractors hate this one trick! 😂\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\n#CivicIssue #UrbanIndia #SmartCity",

            f"🚧 MG Road condition update: It's now officially a 4D driving experience! 🎢 Theme park designers are taking notes 📝\n\nIssue ID: {demo_id}\n📧 Details sent to @BangaloreMayor\n⏰ Reported: {datetime.now().strftime('%H:%M')}\n\n#CivicIssue #RoadSafety #SmartCity"
        ]
    }

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📋 Generated Issue Details")
        st.code(f"""
Issue ID: {demo_id}
Type: {demo_type.split(' ')[1]}
Location: MG Road, Bangalore, Karnataka
Coordinates: 12.9716° N, 77.5946° E
Status: Submitted for Review
        """)

        st.subheader("📧 Generated Email")
        st.text_area(
            "Email Content",
            f"""Subject: Civic Issue Report – {demo_id} – Bangalore

Dear Sir/Madam,

We are reaching out to bring a civic issue to your attention. 
The report was submitted by a citizen through the CivicSpotter platform.

Issue Details:
• Issue ID: {demo_id}
• Issue type: {demo_type.split(' ')[1]}
• Location: MG Road, Bangalore, Karnataka
• Date Reported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

We kindly request you to review and initiate appropriate action.

Sincerely,
CivicSpotter System
            """,
            height=200
        )

    with col2:
        st.subheader("🐦 Generated Tweet")

        # Select a random funny tweet for the chosen demo type
        selected_tweet = random.choice(funny_tweets[demo_type])

        st.text_area(
            "Tweet Content",
            selected_tweet,
            height=200
        )

        st.subheader("🎯 Authority Contact")
        st.info("""
**Discovered Authority:**
Bruhat Bengaluru Mahaanagara Palike (BBMP)
📧 commissioner@bbmp.gov.in
📞 080-22221188
        """)

        st.subheader("📊 Impact Metrics")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Processing Time", "12.3 sec")
            st.metric("Accuracy", "94%")
        with col_b:
            st.metric("Similar Issues", "3 found")
            st.metric("Auto-merged", "Yes")

    # Show additional funny tweet examples
    st.markdown("---")
    st.subheader("🎭 More Funny Tweet Examples")
    st.markdown("*CivicSpotter uses humor to increase social media engagement while maintaining professionalism*")

    col1, col2 = st.columns(2)
    with col1:
        st.info("🕳️ **Pothole Humor**: 'This crater could probably qualify for its own PIN code at this point 📮'")
        st.info(
            "🗑️ **Garbage Wit**: 'We've officially created our own ecosystem! Scientists are studying the new species 🔬'")

    with col2:
        st.info(
            "💡 **Light Jokes**: 'Streetlight has become a professional mime artist - completely silent and invisible! 🎭'")
        st.info(
            "🚧 **Road Humor**: 'Now offers free massage therapy for car suspensions! Chiropractors hate this trick! 😂'")

    # Reset demo
    if st.button("🔄 Reset Demo"):
        st.session_state.demo_running = False
        st.rerun()

# Demo Features Highlight
st.markdown("---")
st.subheader("🌟 Key Demo Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🧠 AI Intelligence
    - Smart authority discovery
    - Context-aware content generation
    - Automatic duplicate detection
    """)

with col2:
    st.markdown("""
    ### 🔄 Workflow Automation
    - Multi-stage approval process
    - Error handling & retry logic
    - Real-time status tracking
    """)

with col3:
    st.markdown("""
    ### 📊 Analytics & Insights
    - Geographic clustering
    - Issue trend analysis
    - Performance metrics
    """)

# Technical Architecture
st.markdown("---")
st.subheader("🏗️ Technical Architecture")

st.markdown("""
```mermaid
graph TD
    A[📸 Photo Upload] --> B[🗺️ Metadata Extraction]
    B --> C[🔍 Similar Issue Detection]
    C --> D[🧠 Authority Discovery]
    D --> E[📧 Email Generation]
    E --> F[🐦 Tweet Creation]
    F --> G[👨‍💼 Admin Review]
    G --> H[✅ Public Posting]
```
""")