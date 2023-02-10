from flask import Flask, jsonify, request
from flask_cors import CORS
import asyncio
from EdgeGPT import Chatbot

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
# 加载配置变量
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/answer', methods=['GET', 'POST'])
def get_answer():
    response_object = {'status': 'success'}
    if request.method == 'POST' or request.method == "GET":
        post_data = request.get_json()
        print("post_data: ", post_data)
        question = post_data["question"]
        print("question: ", question)
        result = asyncio.run(handle(question))
        response_object['answer'] = result

    return jsonify(response_object)


async def handle(prompt):
    if prompt == "!exit":
        return "聊天结束"
    elif prompt == "!help":
        print("""
        !help - Show this help message
        !exit - Exit the program
        !reset - Reset the conversation
        """)
    elif prompt == "!reset":
        await bot.reset()

    result = (await bot.ask(prompt=prompt))["item"]["messages"][1]["adaptiveCards"][0][
        "body"
    ][0]["text"]
    print("Bot： ", result)

    return result


if __name__ == '__main__':
    print("Initializing...")
    bot = Chatbot()
    app.run()
