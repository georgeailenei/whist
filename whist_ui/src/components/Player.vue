<script setup>

import Card from './Card.vue';
const props = defineProps(['player']);

</script>    
<template>  

<div class="playing-cards">
    <div v-for="(card, index) in player.hand" :key="card">
        <Card :card_value="card" :class="index === 0 ? 'empty': 'card'"/>
    </div>
</div>
            
<div class="avatar"></div>
<div class="name">{{player.username}}</div>
<div class="tricks">{{player.tricks}}</div>
    
</template>

<style scoped>
.avatar {
    width: 62px;
    height: 62px;
    background-color: rgb(235, 235, 235);
    border-radius: 100%;
    position: relative;
    box-shadow: 2px 10px 0px rgba(0, 0, 0, 0.4);
    z-index: 20;
}

.name {
    font-family: "Calibri";
    text-align: center;
    width: 100px;
    color:white;
    padding: 1px 0;
    margin-left: 10px;
    box-sizing: border-box;
    border-top: 1px solid white;
    border-radius: 5px;
    margin-top: 15px;
    text-overflow: ellipsis;
    font-size: 11px;
    overflow: hidden;
    position: relative;
    top: -65px;
    left: 40px;
}

.tricks {
    font-family: "Calibri";
    text-align: center;
    width: 100px;
    color: white;
    padding: 1px 0;
    margin-left: 10px;
    box-sizing: border-box;
    border-bottom: 1px solid #232323;
    border-radius: 5px;
    text-overflow: ellipsis;
    font-size: 11px;
    overflow: hidden;
    position: relative;
    top: -65px;
    left: 40px;
}

.playing-cards{
    position: absolute;
    display: flex;
}

.playing-cards .card{
    position: relative;
    margin-left: -40px;
    left: 95px;
    top: -64px;
    transition: 0.5s;
}

.playing-cards .card:hover{
    transform: translateY(-15px) scale(1.3);
}
</style>
