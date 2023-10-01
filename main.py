import streamlit as st
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import os

# Set the Streamlit app layout width
st.set_page_config(layout="centered")

# Streamlit UI components

st.title("YTDownloader")
video_url = st.text_input("Enter YouTube Video URL:")
format_selected = st.selectbox("Select Format", ['MP4', 'MP3'])
download_button = st.button("Download")

if download_button:
    try:
        youtubeObject = YouTube(video_url)
        if not youtubeObject.streams:
            st.error("Video not found or URL is incorrect.")
        else:
            if format_selected == 'MP3':
                video = youtubeObject.streams.filter(only_audio=True).first()
                destination = 'Audios'
                out_file = video.download(output_path=destination)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                try:
                    os.rename(out_file, new_file)
                except WindowsError:
                    os.remove(new_file)
                    os.rename(out_file, new_file)
                st.success("Download Success")
            else:
                youtubeObject = youtubeObject.streams.get_highest_resolution()
                destination = 'Videos'
                out_file = youtubeObject.download(output_path=destination)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp4'
                try:
                    os.rename(out_file, new_file)
                except WindowsError:
                    os.remove(new_file)
                    os.rename(out_file, new_file)
                st.success("Download Success")
    except VideoUnavailable:
        st.error("Video not found or URL is incorrect.")
