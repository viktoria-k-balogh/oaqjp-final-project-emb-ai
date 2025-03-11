'''This module detects emotions in texts'''

from flask import Flask, render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''This function detects emotions in texts'''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'

    response_to_display=f"""For the given statement, the system response is 'anger':
    {response['anger']}, 'disgust':{response['disgust']}, 'fear':{response['fear']},
    'joy': {response['joy']} and 'sadness': {response['sadness']}.
    The dominant emotion is {response['dominant_emotion']}."""

    return response_to_display

@app.route("/")
def render_index_page():
    '''This function renders the index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
