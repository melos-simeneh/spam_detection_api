# Spam Detection API with FastAPI

This project is a simple API that detects whether a given SMS message is **spam** or **ham** (not spam) using a machine learning model trained on the SMS Spam Collection Dataset.

## 🚀 Features

- Train a Naive Bayes model to classify SMS messages
- REST API built with FastAPI for real-time spam detection
- Easy to extend and deploy

## 🔧 Technologies

- `Python 3.8+`
- `FastAPI`
- `scikit-learn`
- `pandas`
- `Uvicorn`

## 📁 Project Structure

```bash
spam_detection_api/
├── app/
│ ├── main.py # FastAPI app
│ ├── model.py # Model loading and prediction logic
│ ├── schemas.py # Request data models
│ ├── train_model.py # Train and save ML model
│ └── spam_detector.pkl # Saved ML model
├── data/
│ └── spam.csv # SMS Spam dataset
├── requirements.txt # Python dependencies
└── README.md # This file
```

## ⚙️ Setup & Run

1. **Clone the repo**

    ```bash
    git clone https://github.com/melos-simeneh/spam_detection_api.git
    cd spam_detection_api
    ```

2. **Create and activate virtual environment (optional but recommended)**

    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Train the ML model**

    ```bash
    python app/train_model.py
    ```

5. **Start the FastAPI server**

    ```bash
    uvicorn app.main:app --reload
    ```

    Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API interactively.

## 📝 API Endpoints

- `GET /` - Welcome message

- `POST /predict` - Predict if a message is spam or ham

    **Request body:**

    ```json
    {
        "text": "Your SMS message here"
    }
    ```

    **Response:**

    ```json
    {
        "prediction": "spam"
    }
    ```

## 📬 Contact

Feel free to reach out for questions, collaborations, or feedback. 👉 📧 [melos.simeneh@gmail.com](mailto:melos.simeneh@gmail.com)

**Happy Coding!** 🚀
