# BingChatGPT-VUE-Chat

A simple chat interface with BingChatGPT on the left and users on the right. When the 'Send' button is clicked, the
prompt is sent to the backend API for processing.

Here is example:

![image](./example.png)

## Client

### Reference

https://github.com/taylorchen709/vue-chat

### Run

```shell
cd client
npm i
npm run serve
```

## Server 

### Reference：

https://github.com/acheong08/EdgeGPT

### Run

```shell
cd server
python3 app.py
```

## Noting:
- At the beginning of this project, I did a combination of BingChatGPT backend and a Vue frontend.
- Later, BingChatGPT did not open the API interface for use.
- Then, I changed the back-end code to an API interface based on OPENAI GPT3 (because ChatGPT is not open anymore), but there is also a problem: too many people use this API, which may cause the connection to fail.

You can modify the redundant code of server/app.py and src/components/ChatList.vue/sendMsg()

## TODO:

- I want to make more chat interfaces, users can choose who to talk to in the left sidebar, such as a beautiful girl, a
  handsome man or Elon Musk, etc.
- Beautify the interface
