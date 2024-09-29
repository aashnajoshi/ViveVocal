import azure.cognitiveservices.speech as speechsdk
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import pyttsx3
import os

#Basic Setup
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

    print("Listening...")
    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {result.text}")
        return result.text
    else:
        return None

def authenticate_client():
    credential = AzureKeyCredential(text_analytics_key)
    text_analytics_client = TextAnalyticsClient(endpoint=text_analytics_endpoint, credential=credential)
    return text_analytics_client

def analyze_sentiment(text):
    client = authenticate_client()
    documents = [text]
    response = client.analyze_sentiment(documents=documents)[0]
    print(f"Sentiment: {response.sentiment}")
    print(f"Positive score: {response.confidence_scores.positive}")
    print(f"Neutral score: {response.confidence_scores.neutral}")
    print(f"Negative score: {response.confidence_scores.negative}")
    return response.sentiment

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    recognized_text = speech_to_text()
    if recognized_text:
        sentiment = analyze_sentiment(recognized_text)
        response_text = f"The tone detected is {sentiment}."
        text_to_speech(response_text)