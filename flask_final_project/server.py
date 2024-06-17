''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed
    on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using the emotion_detector()
        function. The output returned shows the scores of each emotion
        and the dominant one (being the one with the highest score).
    '''
    input_text = request.args.get('textToAnalyze')
    output = emotion_detector(input_text)
    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f'''For the given statement, the system response is 'anger': {output['anger']}, 'disgust': {output['disgust']}, 'fear': {output['fear']}, 'joy': {output['joy']} and 'sadness': {output['sadness']}. The dominant emotion is {output['dominant_emotion']}'''

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
