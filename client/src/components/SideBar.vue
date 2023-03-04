<template>
    <div class="sidebar">
        <h2>Bots</h2>
        <ul>
            <li v-for="(bot, index) in bots" :key="index"
                :class="{current: currentBotIndex === index}"
                @click="selectBot(index)">
                {{ bot.name }}
            </li>
        </ul>
    </div>
</template>

<script>
import util from '@/common/util'
import axios from 'axios'

export default {
    name: 'SideBar',
    computed: {
        bots () {
            return this.$store.state.bots
        },
        currentBotIndex () {
            return this.$store.state.currentBotIndex
        }
    },
    methods: {
        selectBot (index) {
            this.$store.commit('SET_CURRENT_BOT', index)
            // this.$nextTick(() => {
            //     this.$refs.messages.scrollTop = this.$refs.messages.scrollHeight
            // })
        },
    },
    // before the chat, use `bots.json` to load bot_name and init_prompt
    created () {
        this.$store.dispatch('fetchBots')
    }
}
</script>

<style scoped>
.sidebar {
    position: absolute;
    width: 20%;
    background-color: skyblue;
    top: 0;
    left: 0;
    bottom: 0;
}

.sidebar h2 {
    margin-top: 0;
}

.sidebar ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.sidebar li {
    cursor: pointer;
    padding: 10px;
    border-radius: 5px;
}

.sidebar li.current {
    background-color: #ccc;
}
</style>
