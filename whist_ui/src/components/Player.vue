<script setup>
import Card from './Card.vue';
const props = defineProps(['player']);
const player = props.player;
player.hand = ['Ah', 'Ac', '10h', '9c'];
console.log(props.player);

</script>

<template>
    <div class="container">
        <h1>{{player.username}}</h1>
        <img 
            src="http://localhost:8000/static/images/placeholder_avatar.png"
            height="100"
            width="100"
        />
        <div class="card-container">
            <div v-for="(card, index) in player.hand">
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
