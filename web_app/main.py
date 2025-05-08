from flask import Flask, render_template, jsonify, request
from chat_bot import ChatAgent
import mimetypes

mimetypes.add_type('application/wasm', '.wasm')


app = Flask(__name__)



OPENAI_API_KEY = "YOUR_API_KEY_HERE"


agent = ChatAgent(api_key=OPENAI_API_KEY)
agent.set_primary_directive("You are an A.I. assistant named Tomatio that wants to help users")
agent.add_context("You are a frog")
agent.add_context_document("chat_bot_knowledge.txt")


@app.route('/chat', methods=['POST'])
def chat():
    print("CHAT TRIGGERED")
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Missing 'message' in request"}), 400
    response = agent.chat(data["message"])
    return jsonify({"response": response})




@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template("index.html")


@app.route('/robot_sim', methods=['GET', 'POST'])
def robot_sim():
	return render_template("robot_sim.html")



if __name__ == '__main__':
	app.run(debug=True,  host='0.0.0.0', port = 8080)







