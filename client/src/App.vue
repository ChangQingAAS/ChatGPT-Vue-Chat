<template>
    <div class="app">
        <SideBar></SideBar>
        <ChatList></ChatList>
    </div>
</template>

<script>

import SideBar from '@/components/SideBar.vue'
import ChatList from '@/components/ChatList.vue'

export default {
    name: 'app',
    components: {
        ChatList,
        SideBar,
    }
}
</script>

<style>
.app {
    display: flex;
    flex-direction: row;
    height: 100vh;
}
</style>
