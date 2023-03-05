// Import and use Vuex
import Vuex from 'vuex'
import Vue from 'vue'
import util from '@/common/util'
import axios from 'axios'

Vue.use(Vuex)

// actions in the corresponding component
const actions = {
    // before the chat, use `bots.json` to load bot_name and init_prompt
    async fetchBots (context) {
        try {
            const response = await fetch('bots.json')
            const data = await response.json()
            context.commit('INIT_BOTS', data)
        } catch (error) {
            console.error(error)
        }
    }
}

// manipulating data in `state`
const mutations = {
    SEND_MESSAGE (state, payload) {
        // console.log('SEND_MESSAGE in mutations is called.')
        // bot to user
        if (payload.receiver === 'user') {
            for (let bot of state.bots) {
                if (bot.name === payload.sender) {
                    bot.messages.push({
                        content: payload.content,
                        sender: payload.sender,
                        receiver: payload.receiver,
                        time: payload.time,
                    })
                }
            }
            return
        }

        // user to bot
        for (let bot of state.bots) {
            if (bot.name === payload.receiver) {
                bot.messages.push({
                    content: payload.content,
                    sender: payload.sender,
                    receiver: payload.receiver,
                    time: payload.time,
                })
            }
        }

    },

    SET_CURRENT_BOT (state, value) {
        // console.log('SET_CURRENT_BOT in mutation is called.')
        state.currentBotIndex = value
    },

    // before the chat, use `bots.json` to load bot_name and init_prompt
    INIT_BOTS: function (state, value) {
        for (let bot_name in value) {
            let init_prompt = value[bot_name]
            state.bots.push({
                name: bot_name,
                avatar: 'assets/' + Math.floor(Math.random() * 10) + '.png',
                init_prompt: init_prompt,
                messages: []
            })
        }
        // console.log("init bots are: ",state.bots)

        /*
        Somehow, if I write the code of sending `init_prompt` in `created()` of other components
        after initializing the data structure of bots,
        Code does not perform as expected, so I wrote the code here.
        I speculate that it is due to the asynchronous execution mechanism of js and some mechanisms of vuex.
        Fortunately, it is not a big problem to write the code here.
        If you have better suggestions, please contact me.
         */
        // before chat to the bot, send the init_prompt to the bot
        for (let bot of state.bots) {
            console.log('send init prompt to ', bot.name)

            // user send init prompts of all bots
            this.commit('SEND_MESSAGE', {
                content: bot.init_prompt,
                sender: 'user',
                receiver: bot.name,
                time: util.formatDate.format(new Date(), 'yyyy-MM-dd hh:mm:ss')
            })

            // make a request to server
            const param = {
                'bot': bot.name,
                'prompt': bot.init_prompt,
            }
            const path = `http://${window.location.hostname}:5000/get_answer`
            axios.post(path, param)
                .then((res) => {
                    this.commit('SEND_MESSAGE', {
                        content: res.data['answer'],
                        sender: bot.name,
                        receiver: 'user',
                        time: util.formatDate.format(new Date(), 'yyyy-MM-dd hh:mm:ss')
                    })
                })
                .catch((error) => {
                    this.commit('SEND_MESSAGE', {
                        content: `${bot.name} happened error: ${error}`,
                        sender: bot.name,
                        receiver: 'user',
                        time: util.formatDate.format(new Date(), 'yyyy-MM-dd hh:mm:ss')
                    })
                })
        }
    }
}

// Storing data
const state = {
    currentBotIndex: 0,
    bots: [],
}

// Create and export Store
export default new Vuex.Store({
    actions: actions,
    mutations: mutations,
    state: state
})
