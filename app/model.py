import joblib

def load_model():
    return joblib.load("app/spam_detector.pkl")

def predict_message(model, message: str) -> str:
    pred = model.predict([message])[0]
    return "spam" if pred == 1 else "ham"
