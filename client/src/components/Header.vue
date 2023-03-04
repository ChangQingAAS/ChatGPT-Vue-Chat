<template>
    <section class="top">
        <img :src="avatar">
        <h2 class="name">{{ bots[currentBotIndex].name }}</h2>
    </section>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: 'Header',
    computed: {
        bots () {
            return this.$store.state.bots
        },
        currentBotIndex () {
            return this.$store.state.currentBotIndex
        },
        avatar () {
            return  this.$store.state.bots[this.$store.state.currentBotIndex].avatar
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.top {
    position: absolute;
    top: 0;
    right: 0px;
    left: 20%;

    background-color: #33DF83;
    display: flex;
    flex-direction: row;
    align-items: center;
}

.top img {
    width: 50px;
    height: 50px;
    float: left;
    border-radius: 100%;
}

.top .name {
    font-size: 18px;
    color: #444;
    margin-left: 10px;
}
</style>
