from flask import Flask, jsonify, request
from flask_cors import CORS
import asyncio
from EdgechatGPT import Chatbot as BingChatBot
from loguru import logger
import uuid
from chatGPT import ChatBot
from pydantic import BaseModel
from conf import conf_reader

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
# 加载配置变量
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def getAnswer(uid, text):
    logger.info(f"ASK: {text}")
    try:
        bot = chatBots[uid]
    except Exception as e:
        return "校验失败，请刷新页面后重试. Error: " + e
    response = bot.ask_stream(text)
    return response


@app.route('/get_bot', methods=['GET'])
def get_bot():
    uid = str(uuid.uuid1())
    bot = ChatBot(api_key=conf_reader())
    chatBots[uid] = bot
    return uid


@app.route('/get_chatbots_answer', methods=['GET', 'POST'])
def get_chatbots_answer():
    # 传入参数需要uid,text
    post_data = request.get_json()
    logger.info("post_data: " + str(post_data))
    res = getAnswer(post_data["uid"], post_data["text"])
    response = ""
    for word in res:
        response += word
    logger.info("response: " + response)
    result = response.replace("<|im_end|>", "").strip()
    logger.info(f"ANSWER: {result}")
    return {
        'status': 'success',
        "answer": result
    }


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


async def handle(prompt):
    if prompt == "!exit":
        return "聊天结束"
    elif prompt == "!help":
        logger.info("""
        !help - Show this help message
        !exit - Exit the program
        !reset - Reset the conversation
        """)
    elif prompt == "!reset":
        await bot.reset()

    result = (await bot.ask(prompt=prompt))["item"]["messages"][1]["adaptiveCards"][0][
        "body"
    ][0]["text"]
    logger.info("Bot： ", str(result))

    return result


@app.route('/get_bing_answer', methods=['GET', 'POST'])
def get_bing_answer():
    post_data = request.get_json()
    logger.info("post_data: ", str(post_data))
    question = post_data["question"]
    logger.info("question: ", str(question))
    result = asyncio.run(handle(question))
    logger.info(f"ANSWER: {result}")
    return {
        'status': 'success',
        "answer": result
    }


if __name__ == '__main__':
    logger.add(
        "./log/run.log",
        encoding="utf-8",
        format="{level} | {time:YYYY-MM-DD HH:mm:ss} | {file} | {line} | {message}",
        retention="30 days",
        rotation="500 MB"
    )
    logger.info("System initializing...")
    try:
        # 使用bing的chatbot
        bot = BingChatBot()
    except Exception as e:
        logger.error("错误： " + str(e))
    try:
        # 一组openAi的chatbot,用进行索引
        chatBots = {str: ChatBot}
    except Exception as e:
        logger.error("错误： " + str(e))
    app.run(host='0.0.0.0')
