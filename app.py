import streamlit as st
from PodInsightAI.helper import *
from PodInsightAI.utils import *


# Streamlit App
st.set_page_config(layout="wide")


st.title("Podcast Summarization and Insights 🦜🎥📄")

# Input URL
youtube_link = st.text_input("Enter YouTube Video URL:")

if youtube_link:
        # Extract the video ID correctly from both youtube.com and youtu.be URLs
        if "youtube.com" in youtube_link:
            video_id = youtube_link.split("v=")[1].split("&")[0]  # Extract video ID after 'v='
        elif "youtu.be" in youtube_link:
            video_id = youtube_link.split("/")[-1]  # Extract video ID after the last '/'
        else:
            raise ValueError("Invalid YouTube URL format.")
        
        # Display the video thumbnail
        st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
        st.success(f"Video ID: {video_id}")  # For debugging purposes (you can remove this later)


if st.button("Generate Summary and Insights"):
    with st.spinner("Processing..."):
            try:
                # Extract Transcript
                transcript_text = extract_transcript(youtube_link)
                st.text_area("Transcript",transcript_text,height=300)
                 
                    

                # Generate Summary and Insights
                summary_and_insights = generate_summary_and_insights(transcript_text)

                if summary_and_insights:
                        st.subheader("Generated Summary and Insights")
                        st.write(summary_and_insights)

                # Download options for word or Text
                if summary_and_insights:
                    result = f"Generated Output:\n\n{summary_and_insights}"
                    st.download_button(
                        label="Download Results as TXT",
                        data=convert_to_txt(result),
                        file_name="Insight.txt",
                        mime="text/plain",
                    )
                    st.download_button(
                        label="Download Results as DOCX",
                        data=convert_to_docx(result),
                        file_name="Insight.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    )


            except Exception as e:
                st.error(f"Error: {e}")


