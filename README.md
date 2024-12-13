
# Podcast Summarization and Insights

This project provides a tool to summarize YouTube podcasts and derive actionable insights, lessons, and recommendations using Google Gemini and the `youtube_transcript_api`. It leverages state-of-the-art language models to analyze podcast transcripts and present key takeaways in an organized format.

## Features
- **Transcript Extraction**: Automatically fetch transcripts from YouTube videos using `YouTubeTranscriptApi`.
- **Summary Generation**: Generate concise summaries of the podcast's key topics and points.
- **Insights and Recommendations**: Derive actionable insights, lessons, and next steps for users.
- **Streamlit Web App**: An interactive UI for users to input YouTube URLs and view results.

## How to Use
1. Clone this repository.
2. Install the required dependencies (see `requirements.txt`).
3. Set your Google Gemini API key in the environment variable `GOOGLE_API_KEY`.
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
5. Enter a YouTube video URL to extract its transcript and generate insights.

## Requirements
- Python 3.9+
- `streamlit` for the web interface.
- `youtube_transcript_api` for fetching video transcripts.
- `google.generativeai` for AI-based text generation.
- `langchain` for prompt templating and model chaining.

### Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/PriyanshuDey23/PodInsightAI.git
   cd ChatAudio
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **API Key Setup**:  
   This project uses Google's Generative AI API. You need to set up your Google API key in your environment.

   - Create a `.env` file in the project root directory.
   - Add your API key as follows:

     ```txt
     GOOGLE_API_KEY=your_api_key_here
     ```


## Example Output
1. **Transcript**: Displays the full transcript extracted from the YouTube video.
2. **Summary and Insights**: Presents a concise summary, key insights, lessons, and actionable recommendations derived from the transcript.

## License
This project is licensed under the MIT License.


