import streamlit as st
import os

from agents.orchestrator import ContentOrchestrator


st.set_page_config(
    page_title="AI Video Generator",
    layout="wide",
)

st.title("🎥 AI Educational Video Generator")

st.write(
    "Generate AI educational videos using OpenAI"
)

api_key = st.secrets["OPENAI_API_KEY"]

category = st.selectbox(
    "Select Category",
    [
        "Technical",
        "Soft Skills",
    ],
)

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Docker for Beginners",
)

if st.button("Generate Video"):

    if not topic:
        st.warning("Please enter topic")
        st.stop()

    orchestrator = ContentOrchestrator(api_key)

    with st.spinner("Generating content..."):

        result = orchestrator.run(
            topic,
            category,
        )

    st.success("Video Generated")

    st.subheader("Generated Script")
    st.write(result["script"])

    st.subheader("Quiz")
    st.write(result["quiz"])

    with open(result["video"], "rb") as video_file:
        st.video(video_file.read())

    with open(result["ppt"], "rb") as ppt_file:
        st.download_button(
            label="Download PPT",
            data=ppt_file,
            file_name="generated_slides.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        )
