from flask import Flask, request, jsonify
from flask_cors import CORS
import chatbot

app = Flask(__name__)
CORS(app)


@app.route("/process", methods=["POST"])
def process_input():
    data = request.json
    user_input = data["input"]
    user_location = data.get("location", None)

    # Process input with your AI model here
    response = chatbot.return_statement(user_input, user_location)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(port=5000)
