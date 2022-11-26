<script setup>
import Card from './Card.vue';

const props = defineProps(['player', 'visibleCards', 'roundStarted', 'board']);



</script>    
<template>  

<div v-if="props.roundStarted" class="playing-cards">
        <div v-for="(card, index) in player.hand.slice(0, props.visibleCards)" :key="card">
            <Card :card_value="card" :class="index === 0 ? 'empty': 'card'"/>
        </div>
</div>


<div v-if="props.roundStarted == false" class="playing-cards">
    <TransitionGroup :name="`list-p${player.id}`">
        <div v-for="(card, index) in player.hand" :key="card">
            <Card :card_value="card" :class="index === 0 ? 'empty': 'card'"/>
        </div>
    </TransitionGroup>
</div>

<div class="avatar"></div>
<div class="name">{{player.username}}</div>
<div class="tricks">{{player.tricks}}</div>
    
</template>

<style scoped>

.list-p1-leave-to {
  transform: translate(calc(calc(55px * v-bind(props.board - 1)) + 70px), 253px);
  position: absolute;
}

.list-p1-leave-active{
    transition: all 0.2s ease;
}

.list-p2-leave-to {
  transform: translate(calc(calc(55px * v-bind(props.board - 1)) + -285px) , 253px);
  position: absolute;
}

.list-p2-leave-active{
    transition: all 0.2s ease;
}

.list-p3-leave-to {
  transform: translate(calc(calc(55px * v-bind(props.board - 1)) + -285px) ,-136px);
  position: absolute;
}

.list-p3-leave-active{
    transition: all 0.2s ease;
}


.list-p4-leave-to {
  transform: translate(calc(calc(55px * v-bind(props.board - 1)) + 70px), -136px);
  position: absolute;
}

.list-p4-leave-active{
    transition: all 0.2s ease;
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
    top: -60px;
    transition: 0.5s;
}

/* .playing-cards .card:hover{
    transform: translate(70px , 136px);
} */
</style>


