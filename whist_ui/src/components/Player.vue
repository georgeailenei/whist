<script setup>

import Card from './Card.vue';
const props = defineProps(['player']);

</script>

<template>
    <div class="container">
        <h1>{{player.username}}</h1>
        <h1>{{player.tricks}}</h1>
        <img 
            src="http://localhost:8000/static/images/placeholder_avatar.png"
            height="100"
            width="100"
        />
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
</style>
