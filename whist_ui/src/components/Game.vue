<script setup>
import { ref } from 'vue';
import GameTable from './GameTable.vue'

const props = defineProps([
  'finish_round',
  'finish_game',
  'room',
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

const timeleft = ref(10);
const timer = setInterval(() => {
  const played_hand_time = Date.parse(props.room.stats.last_played_card);
  const current_time = Date.now();
  timeleft.value = 10 - (Math.floor((current_time - played_hand_time) / 1000));
  if (timeleft.value < 0) {
    timeleft.value = 0;
  }
}, 1000);

</script>

<template>

<div class="container">
<div class="info-bar">
  <!-- timer -->
  <Transition name="timer">
    <div :class="[timeleft < 4 ? 'countdown_warning' : 'countdown']"><span>{{ timeleft }} seconds remaining</span>
    </div>
  </Transition>

  <div class="team-1">
    <span>{{ room.players[0].username }} & {{ room.players[2].username }} : </span>
    <span :class="[is_team_one_winning() ? 'winner-score' : 'neutral-score']">{{ room.stats.team_one_score }}</span>
    <div class="glowing-bar-team"></div>
  </div>

  <Transition name="round-winner">
    <div v-if="room.stats.winner" class="winner">
      <span>{{ room.stats.winner }} won</span>
      <div class="winner-bar"></div>
    </div>
  </Transition>

  <div class="team-2">
    <span>{{ room.players[1].username }} & {{ room.players[3].username }} : </span>
    <span :class="[is_team_two_winning() ? 'winner-score' : 'neutral-score']">{{ room.stats.team_two_score }}</span>
    <div class="glowing-bar-team"></div>
  </div>
</div>
</div>
  <GameTable :key="(room.stats.team_one_score + room.stats.team_two_score)" :room="room" />

</template>

<style scoped>

.countdown_warning {
  position: absolute;
  right: 25px;
  color: #ed4710;
}

.countdown {
  position: absolute;
  right: 25px;
  color: #269F37;
}

.card-symbol {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  color: #252322;
  font-size: larger;
}

.winner-score {
  color: #269F37;
}

.neutral-score {
  color: #ed4710;
}

@keyframes winner {
  0% {
    opacity: 1;
  }

  25% {
    opacity: 0;
  }

  50% {
    opacity: 1;
  }

  75% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes winner-leave {
  0% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

.round-winner-enter-active {
  animation: winner 2s ease-in;
}

.round-winner-leave-active {
  animation: winner-leave 1s ease-in;
}

.info-bar {
  display: flex;
  justify-content: space-evenly;
  border-bottom: 1px solid #252322;
  position: relative;
  color: #BBBBBB;
  font-family: Arial, Helvetica, sans-serif;
  font-size: x-small;
  padding: 5px;
  margin-bottom: 20px;
}

.winner-bar {
  position: relative;
  top: 5px;
  border-bottom: 1px solid #ed4710;
}

.winner {
  position: absolute;
}

.glow {
  position: absolute;
  width: 62px;
  height: 62px;
  line-height: 62px;
  border-radius: 50%;
  color: white;
  box-shadow: 0 0 2px #fff, 0 0 12px #ffffff, 0 0 5px #ffffff, 0 0 10px #d8d8d8,
    0 0 40px #9f9f9f, 0 0 20px #4b4b4b;
}


@keyframes board-animation {
  0% {
    opacity: 0;
  }

  99% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes board-leaving-animation {
  0% {
    opacity: 1;
  }

  10% {
    position: absolute;
    transition: ease-in;
  }

  90% {
    position: absolute;
    opacity: 1;
    transform: translate(calc(1px * v-bind(x)), calc(1px * v-bind(y)))
  }

  100% {
    opacity: 0;
    position: absolute;
    transform: translate(calc(1px * v-bind(x)), calc(1px * v-bind(y)))
  }
}

.board-enter-active {
  animation: board-animation 0.5s ease;
}

.board-leave-active {
  animation: board-leaving-animation 1s ease;
}

.text {
  color: white;
}

.vue-container {
  width: 100vw;
  height: 100vh;
  background-color: #333333;
}

.deck {
  position: relative;
  left: 40%;
}

.card_in_deck {
  position: absolute;
}

.spread {
  transform: translateX('1000px') scale(1.2);
}

.spread-leave-from {
  transition: 0;
}

.spread-leave-to {
  opacity: 1;
}

.spread-enter-active {
  transition: all 2s ease;
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

.board-cards {
  display: inline-block;
  margin-left: 5px;
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

.players .player.playing:before {
  content: "...";
  color: white;
  font-size: 20px;
  position: absolute;
  background-color: #76daff;
  display: inline-block;
  line-height: 0px;
  height: 10px;
  padding: 5px 10px;
  border-radius: 5px;
  z-index: 100;
}

.players .player.player-1 {
  top: 0px;
  left: 50%;
  transform: translatex(-50%) translatey(-50%);
}

.players .player.player-2 {
  bottom: 0px;
  left: 50%;
  transform: translatex(-50%) translatey(50%) rotatez(180deg);
}

.players .player.player-2 .name {
  transform: rotatez(180deg);
}

.players .player.player-2 .bank-value {
  transform: rotatez(180deg);
}

.players .player.player-2 .mise-value {
  transform: rotatez(180deg);
}

.players .player.player-3 {
  top: 50%;
  left: 0px;
  transform: translatex(-50%) translatey(-50%) rotatez(-90deg);
}

.players .player.player-3 .name {
  transform: rotatez(0deg);
}

.players .player.player-4 {
  top: 50%;
  right: 0px;
  transform: translatex(50%) translatey(-50%) rotatez(90deg);
}

.players .player.player-4 .name {
  transform: rotatez(0deg);
}

.players .player.player-5 {
  top: -25px;
  left: 25%;
  transform: translatex(-50%) translatey(-50%);
}

.players .player.player-6 {
  bottom: -78px;
  left: 75%;
  transform: translatex(-50%) translatey(50%);
}

.players .player.player-7 {
  top: -25px;
  left: 75%;
  transform: translatex(-50%) translatey(-50%);
}

.players .player.player-8 {
  bottom: -78px;
  left: 25%;
  transform: translatex(-50%) translatey(50%);
}

.spread-p1-leave-active,
.spread-p2-leave-active,
.spread-p3-leave-active,
.spread-p4-leave-active {
  transition: all 0.1s ease;
}

.spread-p1-leave-to {
  transform: translate(0, -150px);
}


.spread-p2-leave-to {
  transform: translate(150px, -150px);
}


.spread-p3-leave-to {
  transform: translate(280px, 100px);
}

.spread-p4-leave-to {
  transform: translate(0, 110px);
}
</style>