<script setup>
import Card from './Card.vue';

const props = defineProps(['player', 'can_see_no_of_cards']);
const cevaX = '500px'
const cevaY = '220px'

document.documentElement.style.setProperty('--position-1', cevaX)
document.documentElement.style.setProperty('--position-2', cevaY)

</script>    
<template>  

<div class="playing-cards">
    <TransitionGroup name="move">
        <div v-for="(card, index) in player.hand.slice(0, props.can_see_no_of_cards)" :key="card">
            <Card :card_value="card" :class="index === 0 ? 'empty': 'card'"/>
        </div>
    </TransitionGroup>
</div>
            
<div class="avatar"></div>
<div class="name">{{player.username}}</div>
<div class="tricks">{{player.tricks}}</div>
    
</template>

<style scoped>
:root{
    --position-1: 0px;
    --position-2: 0px;
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

/* transitions */

/* .move-enter-from{
    opacity: 0;
    transform: scale(0.6);
}
.move-enter-to{
    opacity: 1;
    transform: scale(1);
}
.move-active{
    transition: all 0.4s ease;
} */
.move-leave-from{
    opacity: 1;
    transform: scale(1);
}

.move-leave-to{
    opacity: 0;
    transform: scale(0.5) translate(var(--position-1), var(--position-2));
}

.move-leave-active{
    transition: all 1s ease;
}

</style>
