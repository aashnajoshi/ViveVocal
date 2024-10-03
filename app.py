import azure.cognitiveservices.speech as speechsdk
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import streamlit as st
import pyttsx3
import os

load_dotenv()
speech_key = os.getenv("SPEECH_API_KEY")
speech_region = os.getenv("SPEECH_REGION")
text_analytics_key = os.getenv("TEXT_ANALYTICS_KEY")
text_analytics_endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")
engine = pyttsx3.init()

def speech_to_text():
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    audio_config = speechsdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    st.write("Listening...")
    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        st.write(f"Recognized: {result.text}")
        return result.text
    else:
        st.error("Speech recognition failed.")
        return None

def authenticate_client():
    credential = AzureKeyCredential(text_analytics_key)
    text_analytics_client = TextAnalyticsClient(endpoint=text_analytics_endpoint, credential=credential)
    return text_analytics_client

def analyze_sentiment(text):
    client = authenticate_client()
    documents = [text]
    response = client.analyze_sentiment(documents=documents)[0]
    
    sentiment_info = {
        "Sentiment": response.sentiment,
        "Positive score": response.confidence_scores.positive,
        "Neutral score": response.confidence_scores.neutral,
        "Negative score": response.confidence_scores.negative}
    return sentiment_info

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

st.title("Speech Sentiment Analyzer")
if st.button("Start Listening"):
    recognized_text = speech_to_text()
    if recognized_text:
        sentiment = analyze_sentiment(recognized_text)
        response_text = f"The tone detected is {sentiment['Sentiment']}."
        st.success(response_text)
        text_to_speech(response_text)
        st.write(f"Positive score: {sentiment['Positive score']:.2f}")
        st.write(f"Neutral score: {sentiment['Neutral score']:.2f}")
        st.write(f"Negative score: {sentiment['Negative score']:.2f}")
