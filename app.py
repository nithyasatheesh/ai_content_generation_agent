import streamlit as st

from agents.orchestrator import ContentOrchestrator


st.set_page_config(
    page_title="AI Video Generator",
    layout="wide",
)

st.title("🎥 AI Educational Video Generator")

st.write(
    "Generate AI educational content using OpenAI"
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
    placeholder="Example: Kubernetes for Beginners",
)

if st.button("Generate Content"):

    if not topic:
        st.warning("Please enter topic")
        st.stop()

    orchestrator = ContentOrchestrator(api_key)

    with st.spinner("Generating content..."):

        result = orchestrator.run(
            topic,
            category,
        )

    st.success("Content Generated Successfully")

    st.subheader("Generated Script")
    st.write(result["script"])

    st.subheader("Quiz")
    st.write(result["quiz"])

    st.subheader("Generated Narration")

    st.audio(result["audio"])

    with open(result["ppt"], "rb") as ppt_file:

        st.download_button(
            label="Download PPT",
            data=ppt_file,
            file_name="generated_slides.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        )
