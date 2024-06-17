import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    json_response = json.loads(response.text)
    if response.status_code == 200:
        emotions_dict = json_response['emotionPredictions'][0]['emotion']
        emotions_scores = list(emotions_dict.values())
        emotions_scores.sort(reverse=True)
        dominant_emotion = list(emotions_dict.keys())[list(emotions_dict.values()).index(emotions_scores[0])]
        formatted_response = {
            'anger': emotions_dict['anger'],
            'disgust': emotions_dict['disgust'],
            'fear': emotions_dict['fear'],
            'joy': emotions_dict['joy'],
            'sadness': emotions_dict['sadness'],
            'dominant_emotion': dominant_emotion
        } 
    elif response.status_code == 400:
        formatted_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    return formatted_response
    