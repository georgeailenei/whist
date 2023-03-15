<script setup>
import { ref } from 'vue';
import GameTable from './GameTable.vue'

const props = defineProps([
  'room',
  'time',
  'game_is_playing',
]);

const is_team_one_winning = () => {
  if (props.room.stats.team_one_score > props.room.stats.team_two_score) {
    return true;
  } else { return false }
}

const is_team_two_winning = () => {
  if (props.room.stats.team_two_score > props.room.stats.team_one_score) {
    return true;
  } else { return false }
}

const timeleft = ref(props.time);
const timer = setInterval(() => {
  const played_hand_time = Date.parse(props.room.stats.last_played_card);
  const current_time = Date.now();

  if (props.room.stats.team_one_score === 0
    && props.room.stats.team_one_score === 0
    && props.room.stats.board.length === 0
    && props.room.players[props.room.stats.player_position].hand.length === 13) {
    timeleft.value = 30 - (Math.floor((current_time - played_hand_time) / 1000)); 
  } else if (props.time === 30) {
    timeleft.value = 30 - (Math.floor((current_time - played_hand_time) / 1000));
  } else if (props.time === 15) {
    timeleft.value = 15 - (Math.floor((current_time - played_hand_time) / 1000));
  } 

  if (timeleft.value < 0) {
    timeleft.value = 0;
  }
}, 1000);

</script>

<template>

<div class="info-bar">

  <!-- Team 1 -->
  <div>
    <span>{{ room.players[0].username }} & {{ room.players[2].username }} : </span>
    <span :class="[is_team_one_winning() ? 'winner-score' : 'neutral-score']">{{ room.stats.team_one_score }}</span>
  </div>

  <!-- Winner -->
  <Transition name="round-winner">
    <div v-if="room.stats.winner" class="winner">
      <span>{{ room.stats.winner }} won</span>
      <div class="winner-bar"></div>
    </div>
  </Transition>

  <!-- Team 2 -->
  <div>
    <span>{{ room.players[1].username }} & {{ room.players[3].username }} : </span>
    <span :class="[is_team_two_winning() ? 'winner-score' : 'neutral-score']">{{ room.stats.team_two_score }}</span>
  </div>
</div>

<div class="timer-bar">
      <!-- Timer -->
  <Transition name="timer">
    <div>
      <span :class="[timeleft < 4 ? 'countdown_warning' : 'countdown']">{{ timeleft }}</span>
    </div>
  </Transition>
</div>

<GameTable :key="(room.stats.team_one_score + room.stats.team_two_score)" :room="room" :game_is_playing="game_is_playing" />

</template>

<style scoped>

.timer-bar {
  display: flex;
  justify-content: center;
  border-bottom: 1px solid #252322;
  position: relative;
  color: #BBBBBB;
  font-family: Arial, Helvetica, sans-serif;
  padding: 4px;
  margin-bottom: 20px;
}

.countdown_warning {
  font-size: large;
  color: #ed4710;
}

.countdown {
  font-size: large;
  color: #BBBBBB;
}

.info-bar {
  display: flex;
  justify-content: space-evenly;
  border-bottom: 1px solid #252322;
  position: relative;
  color: #BBBBBB;
  font-family: Arial, Helvetica, sans-serif;
  font-size: x-small;
  padding: 10px;
  margin-bottom: 5px;
}

.winner-bar {
  position: relative;
  top: 10px;
  border-bottom: 1px solid #ed4710;
}

.winner {
  position: absolute;
}

.winner-score {
  color: #269F37;
}

.neutral-score {
  color: #ed4710;
}

@keyframes winner {
  0% {opacity: 1;}
  25% {opacity: 0;}
  50% {opacity: 1;}
  75% {opacity: 0;}
  100% {opacity: 1;}
}

@keyframes winner-leave {
  0% {opacity: 1;}
  100% {opacity: 0;}
}

.round-winner-enter-active {
  animation: winner 2s ease-in;
}

.round-winner-leave-active {
  animation: winner-leave 1s ease-in;
}


</style>