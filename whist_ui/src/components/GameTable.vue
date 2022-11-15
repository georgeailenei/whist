<script setup>
import { ref } from 'vue';
import Player from './Player.vue'
import {server_client} from '../client';

const room = ref(null);
const loaded_data = ref(false);

setInterval(() => {
    server_client.get_room_details(2)
    .then((data) => {
        room.value = data;
        loaded_data.value = true;
    })
}, 2000)

</script>

<template>

    <div v-if="loaded_data" class="container">
        <div class="team_container">
            <Player :player=room.players[0] />
            <Player :player=room.players[1] />
        </div>
        <div class="team_container">
            <Player :player=room.players[2] />
            <Player :player=room.players[3] />
        </div>
    </div>

</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.team_container {
    display: flex;
    justify-content: space-between;
}
</style>
