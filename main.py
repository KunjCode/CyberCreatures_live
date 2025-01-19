import streamlit as st
import assemblyai as aai
from googletrans import Translator

# AssemblyAI API setup
aai.settings.api_key = "01f0788d47e74ebfb01c4e3ea1ebdf7b"
transcriber = aai.Transcriber()

# List of Indian languages (Google Translate codes)
INDIAN_LANGUAGES = {
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Tamil": "ta",
    "Kannada": "kn",
    "Telugu": "te",
    "Bengali": "bn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Odia": "or",
}

# Function to transcribe video/audio using AssemblyAI
def transcribe_video(file_path):
    with st.spinner("Transcribing video/audio..."):
        response = transcriber.transcribe(file_path)
        return response.text

# Function to translate text using googletrans
def translate_text_local(text, to_lang):
    try:
        translator = Translator()
        result = translator.translate(text, dest=to_lang)
        return result.text
    except Exception as e:
        return f"Translation failed: {e}"

# Streamlit app layout
st.set_page_config(page_title="Video Speech-to-Text and Translation", page_icon="🎬", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        .header {
            text-align: center;
            color: #4CAF50;
        }
        .file-upload {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .stTextArea textarea {
            font-size: 16px;
            color: #333;
        }
        .btn-process {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        .btn-process:hover {
            background-color: #45a049;
        }
        .translation-section {
            margin-top: 40px;
        }
        .translation-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 10px;
            width: 250px;
            text-align: center;
        }
        .translation-card h4 {
            color: #4CAF50;
            margin-bottom: 10px;
        }
        .translation-card p {
            color: #333;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and header section
st.markdown('<h1 class="header">🎬 Video Speech-to-Text and Translation</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Upload a Video or Audio File to Get Transcriptions and Translations!</p>", unsafe_allow_html=True)

# File upload section
uploaded_file = st.file_uploader("Upload a video/audio file", type=["mp4", "mp3", "wav", "m4a"], label_visibility="collapsed")

# Process file
if uploaded_file and st.button("Process", key="process", help="Click to start processing the file"):
    # Save the uploaded file temporarily
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.read())
    
    # Transcribe the audio/video file
    transcription = transcribe_video(uploaded_file.name)

    # Display transcription
    st.subheader("Transcription Result:")
    st.text_area("Transcribed Text", transcription, height=200)

    # Translate into 10 Indian languages
    if transcription:
        st.markdown("<div class='translation-section'><h2>Translations in Indian Languages:</h2></div>", unsafe_allow_html=True)
        for language, code in INDIAN_LANGUAGES.items():
            with st.spinner(f"Translating to {language}..."):
                translation = translate_text_local(transcription, code)
                st.markdown(f"""
                    <div class="translation-card">
                        <h4>{language}</h4>
                        <p>{translation}</p>
                    </div>
                """, unsafe_allow_html=True)
