from flask import Flask, request, jsonify
from flask_cors import CORS
from document_loader import load_documents, create_vector_store
from langchain_pipeline import create_pipeline
from nvidia_gen_ai import nvidia_api_query

app = Flask(__name__)
CORS(app)  # Allow frontend to access the backend

# Load and process documents
documents = load_documents("data/documents")
vector_store = create_vector_store(documents)
pipeline = create_pipeline(vector_store)

# NVIDIA API Key (add your key here or use dotenv)
NVIDIA_API_KEY = "your_nvidia_api_key"

@app.route("/chat", methods=["POST"])
def chat_with_bot():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "Question not provided"}), 400

    # Use LangChain pipeline to get response
    langchain_response = pipeline.run({"input": question})
    # Optionally call NVIDIA GenAI API for further generation
    nvidia_response = nvidia_api_query(langchain_response, NVIDIA_API_KEY)
    return jsonify({"response": nvidia_response.get("output", "No response")})

@app.route("/upload", methods=["POST"])
def upload_pdf():
    uploaded_file = request.files.get("file")
    if uploaded_file:
        filepath = f"data/documents/{uploaded_file.filename}"
        uploaded_file.save(filepath)
        # Reload vector store with the new document
        documents = load_documents("data/documents")
        vector_store = create_vector_store(documents)
        return jsonify({"status": "File uploaded and processed"})
    return jsonify({"error": "No file uploaded"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
