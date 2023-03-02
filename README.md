# ChatGPT-VUE-Chat

## Description
A simple chat interface with ChatGPT on the left and users on the right. When the 'Send' button is clicked, the prompt is sent to the backend API for processing.

Here is example:

![image](./example.png)

### Features
-  In server/app.py has `init_prompt`, which can make the model become different role before you start the official chat.
 
- need your openai.api_key from "https://platform.openai.com/account/api-keys"

## News
OPENAI released the chatGPT interface on 2023.03.02 (just today), so I put previous code which don't use chatgpt into the v1.0 branch, and I am going to give up maintaining this branch.

I use the new chatgpt interface, modified the code of the branch v1.0, removed some redundant codes, and highlighted the core functions as much as possible.I put the latest code into the main branch, hope you like it.

So I change name of the repository from `BingChatGPT-Vue-Chat` into `ChatGPT-Vue-Chat`.

If you have better suggestions, please issue.


## Run
### Client
#### Reference
https://github.com/taylorchen709/vue-chat

```shell
cd client
nvm install 18 # use node version 18 if possible
npm install
npm run serve
```

### Server 
```shell
cd server
pip3 install -r requirements.txt
python3 app.py
```
Because there are not too much packages dependencies, maybe the python version is not a ploblem.(I use python3.11).

I use openai==0.27.0, because of the new chatgpt api. You'd better make sure the version of openai package.
The package is new, so maybe you could not use 'mirror'. 
Just download it like this:
```sh
pip install -i https://pypi.python.org/simple/ openai==0.27.0
```

## Noting:
- At the beginning of this project, I did a combination of BingChatGPT backend and a Vue frontend.
- Later, BingChatGPT did not open the API interface for use.
- Then, I changed the back-end code to an API interface based on OPENAI GPT3 (because ChatGPT is not open anymore), but there is also a problem: too many people use this API, which may cause the connection to fail.(The code maybe redundant.You can modify the redundant code of server/app.py and src/components/ChatList.vue/sendMsg())
- After openai public chatgpt api at 2023.03.02. **I archive the origin code into branch v1.0.** And write new code in branch main.

## TODO:

- I want to make more chat interfaces, users can choose who to talk to in the left sidebar, such as a beautiful girl, a handsome man or Elon Musk, etc.
  - In server/app.py has `init_prompt`, which can make the model become different role.
