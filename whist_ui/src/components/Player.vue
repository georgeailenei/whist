<script setup>
import Card from './Card.vue';

const props = defineProps([
    'player', 
    'playerNr', 
    'visibleCards', 
    'roundStarted', 
    'board', 
    'afterLeaveAnimation',
    'beforeLeaveAnimation',
    'gameIsPlaying',
    'firstRound',
    'lastHand',
]);


</script>    
<template>  

<!--
    Display player's hand when spreading.
    There isn't any animations here. 
-->
    <div v-if="!roundStarted && gameIsPlaying" class="playing-cards">
        <div v-for="(card, index) in player.hand.slice(0, visibleCards)" :key="card">
            <Card :card_value="card" :class="index === 0 ? 'empty': 'card'"/>
        </div>
    </div>

    <!-- Player's cards && Animations -->
    <div v-if="roundStarted || firstRound" class="playing-cards">
        <TransitionGroup :name="`list-p${playerNr}`" @before-leave="beforeLeaveAnimation" @after-leave="afterLeaveAnimation">
            <div v-for="(card, index) in player.hand" :key="card">
                <Card :card_value="card" :class="index === 0 ? 'empty': 'card'"/> 
            </div>
        </TransitionGroup>
    </div>

<div class="avatar">{{ }}</div>
<div class="name">{{ player.username }}</div>
<div class="tricks">{{ player.tricks }}</div>
    
</template>

<style scoped>
.playing-cards .card:hover{
    transform: translateY(-20px);
}

.list-p1-leave-from{
    opacity: 0;
    position: absolute;
}
.list-p1-leave-to {
  transform: translate(calc(calc(55px * v-bind(board - 1)) + 73px), 253px);
  position: absolute;
}

.list-p1-leave-active,
.list-p2-leave-active,
.list-p3-leave-active,
.list-p4-leave-active {
    transition: all 0.5s ease;
}

.list-p2-leave-from{
    opacity: 0;
    position: absolute;
}
.list-p2-leave-to {
  transform: translate(calc(calc(55px * v-bind(board - 1)) + -284px) , 253px);
  position: absolute;
}

.list-p3-leave-from{
    opacity: 0;
    position: absolute;
}
.list-p3-leave-to {
  transform: translate(calc(calc(55px * v-bind(board - 1)) + -284px) ,-136px);
  position: absolute;
}

.list-p4-leave-from{
    opacity: 0;
    position: absolute;
}
.list-p4-leave-to {
  transform: translate(calc(calc(55px * v-bind(board - 1)) + 73px), -136px);
  position: absolute;
}

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
    font-family: Arial, Helvetica, sans-serif;
    font-size: small;
    text-align: center;
    width: 100px;
    color: #BBBBBB;
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
    font-family: Arial, Helvetica, sans-serif;
    font-size: small;
    text-align: center;
    width: 100px;
    color: #BBBBBB;
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
    top: -60px;
    transition: 0.5s;
}
</style>
