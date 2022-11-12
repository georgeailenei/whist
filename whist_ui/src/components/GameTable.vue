<script setup>
import { ref } from 'vue';
import Player from './Player.vue'

const room = ref(null);
const loaded_data = ref(false);

fetch('http://localhost:8000/rooms/8/')
.then((response) => response.json())
.then((data) => {
    room.value = data; 
    loaded_data.value = true;
})
</script>

<template>
    <div v-if="loaded_data">
        <div v-for="player in room.players">
            <Player :player=player />
        </div>

    </div>
  
</template>

<style scoped>

</style>
