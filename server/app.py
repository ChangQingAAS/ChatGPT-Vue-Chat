from flask import Flask, request
from flask_cors import CORS
from loguru import logger
import openai

# flask configuration--------------------------------------------------------------
DEBUG = True

# instantiate the app
app = Flask(__name__)
# Load configuration variables
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# flask configuration--------------------------------------------------------------


# openai chatGPT configuration--------------------------------------------------------------
openai.api_key = "https://platform.openai.com/account/api-keys"
init_prompt = ""  # it can make chatGPT be some different role, for example: beautiful girl.

messages = []  # By global `messages`, we can use it easily


# openai chatGPT configuration--------------------------------------------------------------


def chat_init():
    """
    1.input init prompt to model
    2.add the two message into the complete messages for chatting

    during this, log something for DEBUG in the future
    """
    completion = openai.ChatCompletion.create(
        # model name
        # choose other model from: https://platform.openai.com/docs/models/overview
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo-0301"
        # chat history, make the model aware of the current context
        messages=[{
            "role": "user",
            "content": init_prompt
        }],
        # The parameters below maybe could not be used
        # Control the randomness of the result, 0.0 means the result is fixed, and the randomness can be set to 0.9.
        # temperate=0.5,

        # The maximum number of words returned (including questions and answers), usually Chinese characters occupy
        # two tokens. Assuming it is set to 100, if there are 40 Chinese characters in the prompt question,
        # then the returned result will include at most 10 Chinese characters. The maximum number of tokens allowed
        # by the ChatGPT API is 4096, that is, the max_tokens maximum setting is 4096 minus the number of tokens in
        # question.
        # max_tokens=1000,

        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0
    )
    logger.info("user: " + init_prompt)

    message = completion["choices"][0]["message"]
    messages.append(message)
    logger.info("chatGPT: " + message['content'])


def get_answer_from_model(prompt):
    """
    1.prepare the input message
    2.input the complete messages into model, to get the answer

    during this, log something for DEBUG in the future
    """
    messages.append({
        "role": "user",
        "content": prompt
    })
    logger.info("user: " + prompt)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    message = completion["choices"][0]["message"]
    messages.append(message)
    logger.info("chatGPT: " + message['content'])

    return message['content']


@app.route('/get_answer', methods=['GET', 'POST'])
def get_answer():
    # 传入参数需要text
    post_data = request.get_json()
    logger.info("post_data: " + str(post_data))
    prompt = post_data["prompt"]

    return {
        'status': 'success',
        "answer": get_answer_from_model(prompt)
    }


if __name__ == '__main__':
    logger.add(
        "./log/run.log",
        encoding="utf-8",
        format="{level} | {time:YYYY-MM-DD HH:mm:ss} | {file} | {line} | {message}",
        retention="30 days",
        rotation="500 MB"
    )
    logger.info("System initializing.")

    # Before officially using the model, initialize the model by giving it `init_prompt`
    chat_init()

    # Bind to all network interfaces
    app.run(host='0.0.0.0', port=5000)
