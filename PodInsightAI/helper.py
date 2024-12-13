import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import google.generativeai as genai
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from PodInsightAI.prompt import *


# Load environment variables
load_dotenv()

# Access API key from environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Generative AI client
genai.configure(api_key=GOOGLE_API_KEY)


# Prompt Template for Summary and Insights
prompt_template = PROMPT  # Imported

prompt = PromptTemplate(
    input_variables=['context'],
    template=prompt_template
)

# Extract transcript from YouTube video
def extract_transcript(youtube_video_url):
    try:
        if "youtu.be" in youtube_video_url:
            video_id = youtube_video_url.split("/")[-1]
        elif "youtube.com" in youtube_video_url:
            video_id = youtube_video_url.split("v=")[1].split("&")[0]
        else:
            raise ValueError("Invalid YouTube URL format.")
        
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        transcript = " ".join([item["text"] for item in transcript_data])
        return transcript
    except TranscriptsDisabled:
        st.error("Subtitles are disabled for this video. Unable to fetch the transcript.")
        return None
    except ValueError as ve:
        st.error(str(ve))
        return None
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None

# Generate Summary and Insights using Gemini Model
def generate_summary_and_insights(transcript_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        response = model.generate_content(prompt_template + "\nContext: " + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary and insights: {e}")
        return None
