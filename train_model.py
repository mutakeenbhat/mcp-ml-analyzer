import os
import json
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


TRAIN_DATA_DIR = "training_data"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)


def load_csv(path):
    """Loads CSV safely."""
    return pd.read_csv(path)


def train_transport_model():
    print("\n📦 Training Transport Classifier...")

    df = load_csv(f"{TRAIN_DATA_DIR}/transport_train.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=0.3, random_state=42
    )

    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=300)
    model.fit(X_train_vec, y_train)

    preds = model.predict(X_test_vec)
    print("\nTransport Model Evaluation:")
    print(classification_report(y_test, preds))

    joblib.dump(model, f"{MODEL_DIR}/transport_model.pkl")
    joblib.dump(vectorizer, f"{MODEL_DIR}/transport_vectorizer.pkl")

    print("✅ Transport model saved.")


def train_tool_model():
    print("\n🛠 Training Tool Detector...")

    df = load_csv(f"{TRAIN_DATA_DIR}/tool_train.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=0.3, random_state=42
    )

    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = RandomForestClassifier(n_estimators=40)
    model.fit(X_train_vec, y_train)

    preds = model.predict(X_test_vec)
    print("\nTool Model Evaluation:")
    print(classification_report(y_test, preds))

    joblib.dump(model, f"{MODEL_DIR}/tool_model.pkl")
    joblib.dump(vectorizer, f"{MODEL_DIR}/tool_vectorizer.pkl")

    print("✅ Tool model saved.")


def train_schema_model():
    print("\n📄 Training Schema Detector...")

    df = load_csv(f"{TRAIN_DATA_DIR}/schema_train.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        df["json_snippet"], df["label"], test_size=0.3, random_state=42
    )

    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    preds = model.predict(X_test_vec)
    print("\nSchema Model Evaluation:")
    print(classification_report(y_test, preds))

    joblib.dump(model, f"{MODEL_DIR}/schema_model.pkl")
    joblib.dump(vectorizer, f"{MODEL_DIR}/schema_vectorizer.pkl")

    print("✅ Schema model saved.")


def main():
    print("\n🚀 Starting ML Model Training...\n")

    train_transport_model()
    train_tool_model()
    train_schema_model()

    print("\n🎉 All models trained and saved to /models folder!\n")


if __name__ == "__main__":
    main()
