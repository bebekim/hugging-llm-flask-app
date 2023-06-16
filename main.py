from flask import Flask, request
from utils.preprocessing import load_model, chat

app = Flask(__name__)

# cold load the model and tokenizer
model, tokenizer = load_model()

# Define a route for generating responses
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Get the input message from the request
    input_message = request.json["message"]

    # Return response
    response = chat(input_message)
    return response

# Run the Flask application
if __name__ == "__main__":
    app.run()