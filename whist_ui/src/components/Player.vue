<script setup>
const props = defineProps(['player']);
const player = props.player;
console.log(props.player);
</script>

<template>
    <h1>{{player.username}}</h1>
</template>

<style scoped>

</style>
