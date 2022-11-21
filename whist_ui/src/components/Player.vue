<script setup>

import Card from './Card.vue';
const props = defineProps(['player']);

</script>

<template>
    <div class="container">
                <div id="avatar-1"><img 
                    src="http://localhost:8000/static/images/placeholder_avatar.png"
                    height="100"
                    width="100"
                />
                <div class="display-name"><p id="name"><b>{{player.username}}</b></p></div>
                <div class="points"><p id="points-text"><b>{{player.tricks}}</b></p></div>
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
  list-style-type: none;
}
.card-container{
    display: flex;
    position: absolute;
    left: 170px;
}

#points-text{
    color: white;
    text-align: center;
}


#avatar-1{
    position: absolute;
}

.points{
    background-color: #674747;
    position: absolute;
    top: -10px;
    left: -10px;
    height: 25px;
    width: 25px;
    border-radius: 80%;
}

.display-name{
    background-color: #674747;
    position: absolute;
    height: 25px;
    width: 100px;
}

#name{
    color: white;
    text-align: center;
}
</style>
