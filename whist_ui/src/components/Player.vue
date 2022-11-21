<script setup>

import Card from './Card.vue';
const props = defineProps(['player']);

</script>

<template>
    <div class="container">
        <div>
            <div class="points" ></div>
            <img 
                src="http://localhost:8000/static/images/placeholder_avatar.png"
                height="100"
                width="100"
            />
            <div class="no-bullets">
                <ul>
                <li><b>{{player.username}}</b></li>
                <li><b>Tricks:{{player.tricks}}</b></li>
                </ul>
            </div>
        </div>
        <div class="card-container">
            <div v-for="(card, index) in player.hand" :key="card">
                <Card :card_value="card" :class="index === 0 ? 'empty': 'card'"/>
            </div>
        </div>

    </div>
    
</template>

<style scoped>
.container{
    position: absolute;
}
.card{
    margin-left: -50px;
}
.no-bullets {
  background-color:blue;
  list-style-type: none;
}
.card-container{
    display: flex;
    position: absolute;
    top: 0%;
    left: 120px;
}

.points{
    background-color: aqua;
    position: absolute;
    top: -6%;
    left: 2%;
    height: 25px;
    width: 25px;
    border-radius: 80%;
}
</style>
