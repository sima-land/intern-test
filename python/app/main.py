from fastapi import FastAPI
import emotion_analyzer
import OutFormating

app = FastAPI()

@app.post("/analyze/{text}")
def analyze_text(text: str):
    """ Принимает строку и возвращает анализ эмоций введённого сообщения """
    analysis_result = emotion_analyzer.predict_emotions(text)
    return OutFormating.decorate(analysis_result)
    
