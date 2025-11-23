import os
import joblib

MODEL_DIR = "models"

class MCPMLModels:
    def __init__(self):
        self.transport_model = joblib.load(os.path.join(MODEL_DIR, "transport_model.pkl"))
        self.transport_vectorizer = joblib.load(os.path.join(MODEL_DIR, "transport_vectorizer.pkl"))

        self.tool_model = joblib.load(os.path.join(MODEL_DIR, "tool_model.pkl"))
        self.tool_vectorizer = joblib.load(os.path.join(MODEL_DIR, "tool_vectorizer.pkl"))

        self.schema_model = joblib.load(os.path.join(MODEL_DIR, "schema_model.pkl"))
        self.schema_vectorizer = joblib.load(os.path.join(MODEL_DIR, "schema_vectorizer.pkl"))

    def predict_transport(self, text: str):
        X = self.transport_vectorizer.transform([text])
        return self.transport_model.predict(X)[0]

    def predict_tool(self, text: str):
        X = self.tool_vectorizer.transform([text])
        return self.tool_model.predict(X)[0]

    def predict_schema(self, text: str):
        X = self.schema_vectorizer.transform([text])
        return self.schema_model.predict(X)[0]
