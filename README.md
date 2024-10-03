# ViveVocal
ViveVocal is an interactive web application that leverages Azure's cognitive services to convert spoken language into text, analyze the sentiment of the recognized text, and provide auditory feedback. The application combines speech recognition, sentiment analysis, and text-to-speech functionalities, making it a powerful tool for understanding emotional tone in spoken communication.

## Features
- **Speech Recognition:** Users can speak into their microphone, and the application will convert their speech into text using Azure's Speech Service.
- **Sentiment Analysis:** The recognized text is analyzed for sentiment using Azure's Text Analytics Service. The app identifies whether the sentiment is positive, neutral, or negative, and provides corresponding confidence scores.
- **Text-to-Speech Feedback:** The application verbalizes the detected sentiment back to the user, enhancing the user experience and providing immediate feedback.
- **User-Friendly Interface:** Built with Streamlit, the app features an intuitive layout that allows users to start listening and receive results seamlessly.


## Usage
### All required libraries can be installed using a single-line command:
```bash
pip install -r requirements.txt
```

### While to run the code:
#### Console-based version:
```bash
python main.py

```
#### Streamlit-based version:
```bash
streamlit run app.py
```

## Description about various files:
- **.env** Contains all the credentials and secret information.
- **app.py:** Contains a streamlit-based version of the main code. 
- **main.py:** Converts spoken language into text, analyzes the sentiment of the text, and provides auditory feedback.
- **requirements.txt:**  File containing all required Python modules.
