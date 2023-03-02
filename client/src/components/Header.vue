<template>
    <section class="top">
        <img class="head" src="../assets/default.png"/>
        <span class="name">gpt-3.5-turbo</span>
    </section>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: 'Header',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.top {
    height: 50px;
    line-height: 50px;
    position: absolute;
    top: 0px;
    left: 0px;
    right: 0px;
    background-color: #F8F8F8;
    padding: 5px 10px;
}

.top .head {
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
