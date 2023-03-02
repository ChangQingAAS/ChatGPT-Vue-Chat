<template>
    <div id="app">
        <Header></Header>
        <ChatList></ChatList>
    </div>
</template>

<script>
import ChatList from './components/ChatList'
import Header from '@/components/Header.vue'

export default {
    name: 'app',
    components: {
        Header,
        ChatList
    }
}
</script>

<style>
@import "../node_modules/font-awesome/css/font-awesome.min.css";

body {
    /*background-color: #324057;*/
    margin: 0;
    padding: 0;
    font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, SimSun, sans-serif;
    /*font-weight: 400;
    -webkit-font-smoothing: antialiased;*/
    overflow: hidden;
}

blockquote,
body,
button,
dd,
div,
dl,
dt,
form,
h1,
h2,
h3,
h4,
h5,
h6,
input,
li,
ol,
p,
pre,
td,
textarea,
th,
ul {
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

ul,
li {
    list-style: none;
}

a {
    color: #666;
}

/*
Define the height, width and background of the scroll bar
The height and width correspond to the size of the horizontal and vertical scroll bars
*/
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
    background-color: #F8F8F8;
}

::-webkit-scrollbar-track {
    background-color: #F8F8F8;
}

::-webkit-scrollbar-thumb {
    background-color: #e2e2e2;
}

#app {
    overflow: hidden;
}
</style>
