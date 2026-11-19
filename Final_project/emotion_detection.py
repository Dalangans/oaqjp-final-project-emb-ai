"""Call the Skills Network Watson NLP emotion classifier."""

import requests

API_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for the given text."""
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        return {**dict.fromkeys(EMOTIONS), "dominant_emotion": None}

    response.raise_for_status()
    emotion_scores = response.json()["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(EMOTIONS, key=emotion_scores.get)
    result = {emotion: emotion_scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = dominant_emotion
    return result
