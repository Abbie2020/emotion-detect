import requests
import json

def emotion_detector(text_to_analyse):
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', headers=headers, json=input_json)
    response_dict = json.loads(response.text)
    anger_score = response_dict['emotionPredictions'][0]['emotion']['anger']
    disgust_score = response_dict['emotionPredictions'][0]['emotion']['disgust']
    fear_score = response_dict['emotionPredictions'][0]['emotion']['fear']
    joy_score = response_dict['emotionPredictions'][0]['emotion']['joy']
    sadness_score = response_dict['emotionPredictions'][0]['emotion']['sadness']
    score_dict = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
                }
    dominant_emotion = max(score_dict, key=score_dict.get)
    score_dict.update({'dominant_emotion': dominant_emotion})

    return score_dict