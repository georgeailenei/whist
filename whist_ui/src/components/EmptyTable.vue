<script setup>
import { ref } from 'vue';
import Player from './Player.vue';

const player_number = ref(0);
const props = defineProps([
    'room',
]);

</script>

<template>
<div class="vue-container">

<div class="table">
  <div class="board">
  </div>

  <div class="players">
    <div v-for="player, index in room.players" :class="['player', `player-${index + 1}`]">
        <Player :player="player" />
    </div>
  </div>
</div>

</div>

</template>

<style scoped>
.vue-container {
width: calc(100vw - 120px);
height: 100vh;
}

.table {
width: 776px;
height: 346px;
background-color: #456658;
left: 50%;
top: 50%;
transform: translateX(-50%) translateY(-50%);
border-radius: 200px;
position: relative;
border: 30px solid #252322;
}

.table .board {
border: 2px solid #5c8773;
height: 70px;
width: 225px;
position: absolute;
border-radius: 10px;
top: 50%;
left: 50%;
transform: translateX(-50%) translateY(-50%);
box-sizing: border-box;
}

.players {
position: relative;
width: 100%;
height: 100%;
z-index: 100;
}

.players .player {
position: absolute;
}

.players .player.player-1 {
top: -25px;
left: 25%;
transform: translatex(-50%) translatey(-50%);
}

.players .player.player-2 {
top: -25px;
left: 75%;
transform: translatex(-50%) translatey(-50%);
}

.players .player.player-3 {
bottom: -78px;
left: 75%;
transform: translatex(-50%) translatey(50%);
}

.players .player.player-4 {
bottom: -78px;
left: 25%;
transform: translatex(-50%) translatey(50%);
}

</style>