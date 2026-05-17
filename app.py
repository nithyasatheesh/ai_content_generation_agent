import os

st.write(
    "Generate AI educational videos for technical and soft skill topics"
)


api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    st.error("OPENAI_API_KEY not found in .env")
    st.stop()


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


if st.button("Generate Video"):
    if not topic:
        st.warning("Please enter a topic")
        st.stop()

    orchestrator = ContentOrchestrator(api_key)

    with st.spinner("Generating content..."):
        result = orchestrator.run(topic, category)

    st.success("Content Generated Successfully")

    st.subheader("Generated Script")
    st.write(result["script"])

    st.subheader("Quiz")
    st.write(result["quiz"])

    st.subheader("Video")

    with open(result["video"], "rb") as video_file:
        st.video(video_file.read())

    with open(result["ppt"], "rb") as ppt_file:
        st.download_button(
            label="Download PPT",
            data=ppt_file,
            file_name="generated_slides.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        )

    with open(result["audio"], "rb") as audio_file:
        st.download_button(
            label="Download Narration",
            data=audio_file,
            file_name="narration.mp3",
            mime="audio/mp3",
        )