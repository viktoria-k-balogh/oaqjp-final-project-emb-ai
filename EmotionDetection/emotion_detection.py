import requests
import json

def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj={ "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code==400:
        keys=["anger","disgust","fear","joy","sadness","dominant_emotion"]
        emotions_dict={key: None for key in keys}

    else:
        formatted_response= json.loads(response.text)

        emotions_dict=formatted_response['emotionPredictions'][0]['emotion']
        
        dominant_emotion=str(max(emotions_dict, key=emotions_dict.get))
        emotions_dict['dominant_emotion']=dominant_emotion

    return emotions_dict
        