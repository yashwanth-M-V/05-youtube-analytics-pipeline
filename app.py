import streamlit as st

st.title("YouTube Insights Dashboard")
st.write("🚀 Ready to analyze a YouTube video!")


from src.igestion import extract_video_id

url = st.text_input("YouTube URL")
if url:
    st.write("Video ID:", extract_video_id(url))