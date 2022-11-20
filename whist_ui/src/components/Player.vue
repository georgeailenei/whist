<script setup>

import Card from './Card.vue';
const props = defineProps(['player']);

</script>

<template>
    <div class="container-fluid">
        <div>
        <img 
            src="http://localhost:8000/static/images/placeholder_avatar.png"
            height="100"
            width="100"
        />
        <ul class="no-bullets">
        <li><b>{{player.username}}</b></li>
        <li><b>Tricks:{{player.tricks}}</b></li>
        </ul>
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
    display: flex;
    flex-direction: column;
    align-items: center;
}
.card-container{
    display: flex;
}
.card{
    margin-left: -80px;
}
.empty{

}

ul.no-bullets {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
</style>
