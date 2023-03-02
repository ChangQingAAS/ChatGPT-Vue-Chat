<template>
    <div>
        <section class="chatList">
            <mt-loadmore>
                <ul>
                    <div v-for="(item, index) in records" :key="index">
                        <li v-if="item.type == 1" class="chat-mine">
                            <div class="chat-user"><img src="../assets/user.png"></div>
                            <div class="time"><cite><i>{{ item.time }}</i>{{ item.name }}</cite></div>
                            <div class="chat-text" style="white-space: pre-wrap;" v-text="item.content"></div>
                            <!-- for new line： style="white-space: pre-wrap;"-->
                        </li>
                        <li v-if="item.type == 2">
                            <div class="chat-user"><img src="../assets/default.png"></div>
                            <div class="time"><cite>{{ item.name }}<i>{{ item.time }}</i></cite></div>
                            <div class="chat-text" style="white-space: pre-wrap;" v-text="item.content"></div>
                        </li>
                    </div>
                </ul>
            </mt-loadmore>
        </section>

        <section class="foot">
            <mt-field id="txtContent" v-model="content" class="con" placeholder="Please enter your prompt"></mt-field>
            <span class="btn btn-send" v-on:click="sendMsg">Send</span>
        </section>
    </div>
</template>

<script>
import util from '../common/util'
import { Toast } from 'mint-ui'
import axios from 'axios'

export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: 'ChatList',
    data() {
        return {
            content: '',
            records: [], // chat record
        }
    },
    methods: {
        sendMsg: function () {
            const _this = this

            if (this.content == '') {
                Toast('Please enter your prompt')
                return
            }

            this.records.push({
                type: 1,
                time: util.formatDate.format(new Date(), 'yyyy-MM-dd hh:mm:ss'),
                name: 'user',
                content: this.content
            })

            // make a request
            const param = {
                'prompt': this.content,
            }
            const path = `http://${window.location.hostname}:5000/get_answer`
            axios.post(path, param)
                .then((res) => {
                    _this.records.push({
                        type: 2,
                        time: util.formatDate.format(new Date(), 'yyyy-MM-dd hh:mm:ss'),
                        name: 'gpt-3.5-turbo',
                        content: res.data['answer']
                    })
                })
                .catch((error) => {
                    _this.records.push({
                        type: 2,
                        time: util.formatDate.format(new Date(), 'yyyy-MM-dd hh:mm:ss'),
                        name: 'gpt-3.5-turbo',
                        content: 'No Reply Received. Error: ' + error
                    })
                })

            this.content = ''

            this.scrollToBottom()
            this.focusTxtContent()//聚焦输入框
        },

        // focus the input box
        focusTxtContent: function () {
            document.querySelector('#txtContent input').focus()
        },

        // Scroll bar scrolls to the bottom
        scrollToBottom: function () {
            setTimeout(function () {
                const tempChatList = document.getElementsByClassName('chatList')[0]
                tempChatList.scrollTop = tempChatList.scrollHeight
            }, 100)
        },
    },
    mounted: function () {
        this.scrollToBottom()
        this.focusTxtContent()
    }
}
</script>

<style lang="css" scoped>
.chatList {
    position: absolute;
    top: 60px;
    bottom: 48px;
    left: 0px;
    right: 0px;
    overflow-y: scroll;
    overflow-x: hidden;
    padding: 10px;
}

.chatList ul {
    min-height: 300px;
}

.chatList ul .chat-mine {
    text-align: right;
    padding-left: 0;
    padding-right: 60px;
}

.chatList ul li {
    position: relative;
    /*font-size: 0;*/
    margin-bottom: 10px;
    padding-left: 60px;
    min-height: 68px;
}

.chat-mine .chat-user {
    left: auto;
    right: 3px;
}

.chat-user {
    position: absolute;
    left: 3px;
}

.chat-text,
.chat-user {
    display: inline-block;
    vertical-align: top;
    /*font-size: 14px;*/
}

.chat-user img {
    width: 40px;
    height: 40px;
    border-radius: 100%;
}

.time {
    width: 100%;
}

cite {
    left: auto;
    right: 60px;
    text-align: right;
}

cite {
    font-style: normal;
    line-height: 24px;
    font-size: 12px;
    white-space: nowrap;
    color: #999;
    text-align: left;
}

cite i {
    font-style: normal;
    padding-left: 5px;
    padding-right: 5px;
    font-size: 12px;
}

.chat-mine .chat-text {
    margin-left: 0;
    text-align: left;
    background-color: #33DF83;
    color: #fff;
}

.chat-text {
    position: relative;
    line-height: 22px;
    /*margin-top: 25px;*/
    padding: 10px 15px;
    background-color: #eee;
    border-radius: 3px;
    color: #333;
    word-break: break-all;
    max-width: 462px \9;
}

.chat-text,
.chat-user {
    display: inline-block;
    vertical-align: top;
    font-size: 14px;
}

.chat-text img {
    max-width: 100%;
    vertical-align: middle;
}

.chat-user {
    position: absolute;
    left: 3px;
}

.chat-text:after {
    content: '';
    position: absolute;
    left: -10px;
    top: 15px;
    width: 0;
    height: 0;
    border-style: solid dashed dashed;
    border-color: #eee transparent transparent;
    overflow: hidden;
    border-width: 10px;
}

.chat-mine .chat-text:after {
    left: auto;
    right: -10px;
    border-top-color: #33DF83;
}

.foot {
    width: 100%;
    min-height: 48px;
    position: fixed;
    bottom: 0px;
    left: 0px;
    background-color: #F8F8F8;
}

.foot .con {
    position: absolute;
    left: 0px;
    right: 0px;
}

.btn {
    display: inline-block;
    vertical-align: top;
    font-size: 30px;
    line-height: 48px;
    margin-left: 5px;
    padding: 0 6px;
    background-color: #33DF83;
    color: #fff;
    border-radius: 3px;
}

.btn-send {
    position: absolute;
    right: 0px;
}
</style>
