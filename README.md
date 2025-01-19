# Blog Dashboard with Text and Video Input

Develop a blog dashboard that allows users to input text and video content, and enables seamless transcription, translation, and blog publishing in 10 regional Indian languages (Hindi, Marathi, Gujarati, Tamil, Kannada, Telugu, Bengali, Malayalam, Punjabi, Odia).

## Used Tools:
● Assemblyai API for Speech to text.

● googletrans for Translate text to reginal.

● Streamlit for frontend access of APIs.


---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/KunjCode/CyberCreatures_live
cd CyberCreatures_live
```

### 2. Create a Virtual Environment
Set up a Python virtual environment to manage dependencies:
```bash
python -m venv env

```
Activate the virtual environment:
On Windows:
```bash
source env/Scripts/activate
```
On Mac/Linux:
```bash
source env/bin/activate
```

### 3. Install Dependencies
Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 5. Run the Application
Start the Streamlit application:

```bash
streamlit run main.py
```

## How to Use
(1) Provide the video under 200MB.

(2) Click on the "Process" button to translate speech of the video.

View the translation result in 10 regional languages.

## Project Structure
- main.py: Main application file containing the Streamlit app logic.
- requirements.txt: List of dependencies required for the project.

## Demonstration
https://youtu.be/Ow2M2Pa-iMQ


