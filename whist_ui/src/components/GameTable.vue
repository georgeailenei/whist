<script setup>
import Card from './Card.vue';
import { ref, watch } from 'vue';
import Player from './Player.vue';
import _ from "lodash";
import { Howl } from 'howler';

const props = defineProps([
  'finish_round',
  'finish_game',
  'room',
]);


const room = ref(null);
const round_started = ref(false);

const board = ref([]);

const cards_to_spread = ref(52);
const p1_visible_cards = ref(0);
const p2_visible_cards = ref(0);
const p3_visible_cards = ref(0);
const p4_visible_cards = ref(0);

const y = ref(null);
const x = ref(null);
const change_position = ref(null);

const is_in_animation = ref(false);

const sounds = {
  spread_card: new Howl({
    src: ['http://localhost:8000/static/audio/PlayingCards_DealFlip_03.mp3'], html5: true,
  }),
  slide_card: new Howl({
    src: ['http://localhost:8000/static/audio/PlayingCards_Slide_02.mp3'], html5: true,
  }),
  pickup_cards: new Howl({
    src: ['http://localhost:8000/static/audio/PlayingCards_Pickup_02.mp3'], html5: true,
  }),
}

const update_room = (new_room) => {
  room.value = new_room;
  const is_last_turn = new_room.stats.board.length === 0;
  
  round_started.value = !(new_room.stats.board.length === 0 && new_room.players[new_room.stats.player_position].hand.length === 13);
  if (is_last_turn && room.value !== null) {
    board.value = new_room.stats.old_board;
  } else {
    board.value = new_room.stats.board;
  }

  
  // console.log(room)

  if (new_room.stats.winner === new_room.players[0].username) {
    y.value = -253;
    x.value = -68;
  } else if (new_room.stats.winner === new_room.players[1].username) {
    y.value = -253;
    x.value = 289;
  } else if (new_room.stats.winner === new_room.players[2].username) {
    y.value = 136;
    x.value = 289;
  } else if (new_room.stats.winner === new_room.players[3].username) {
    y.value = 136;
    x.value = -68;
  }

  if (new_room.stats.old_board === 4) {
    change_position.value = 'absolute';
  } else {
    change_position.value = 'relative';
    sounds.slide_card.play();
  }

  // if (room.value.stats.team_one_score === 5){
  //   console.log("do something");
  // } else if (room.value.stats.team_two_score === 5){
  //   console.log("altceva");
  // }
}


update_room(props.room);

watch(() => props.room, async (new_room, old_room) => {
  update_room(new_room);
})


const after_leave = (el) => {
  cards_to_spread.value -= 1;
  sounds.spread_card.play();

  if (el.id === '1') {
    p1_visible_cards.value++;
  } else if (el.id === '2') {
    p2_visible_cards.value++;
  } else if (el.id === '3') {
    p3_visible_cards.value++;
  } else if (el.id === '4') {
    p4_visible_cards.value++;
  }
}

setTimeout(() => {
  cards_to_spread.value -= 1;
}, 2000)

const board_before_leave = () => {
  is_in_animation.value = true;
}

const board_after_leave = () => {
  const is_last_turn = room.value.stats.board.length === 0;
  if (is_last_turn) {
    board.value = room.value.stats.board;
    sounds.pickup_cards.play();
  }

  is_in_animation.value = false;
}


const card_symbols = {
  "diamonds": "&diams;",
  "hearts": "&hearts;",
  "spades": "&spades;",
  "clubs": "&clubs;",
};

</script>
<template>

  <div class="vue-container">


    <!-- Table -->
    <div class="table">
      <div class="board">

        <!-- Trump Card -->
        <span class="card-symbol" v-html="card_symbols[room.stats.trump_card]"></span>

        <!-- Deck -->
        <div v-if="!round_started" class="deck">
          <Transition v-for="el in 52" :key="el" :name="`spread-p${4 - ((el - 1) % 4)}`" @after-leave="after_leave">
            <Card :id="`${4 - ((el - 1) % 4)}`" v-if="el <= cards_to_spread" class="card_in_deck"
              card_value="not_permitted"></Card>
          </Transition>
        </div>

        <!-- Board -->
        <TransitionGroup name="board">
          <div v-if="round_started" class="board-cards" v-for="card in board" :key="card">
            <Card :card_value="card" />
          </div>
        </TransitionGroup>

      </div>

      <!-- Players -->
      <div class="players">
        <div :class="['player', 'player-5']">
          <div v-if="room.stats.player_position === 0" class="glow"></div>
          <Player :player-nr="1" :before_leave_animation='board_before_leave' :after_leave_animation='board_after_leave'
            :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p1_visible_cards"
            :player=room.players[0] />
        </div>
        <div :class="['player', 'player-7']">
          <div v-if="room.stats.player_position === 1" class="glow"></div>
          <Player :player-nr="2" :before_leave_animation='board_before_leave' :after_leave_animation='board_after_leave'
            :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p2_visible_cards"
            :player=room.players[1] />
        </div>
        <div :class="['player', 'player-6']">
          <div v-if="room.stats.player_position === 2" class="glow"></div>
          <Player :player-nr="3" :before_leave_animation='board_before_leave' :after_leave_animation='board_after_leave'
            :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p3_visible_cards"
            :player=room.players[2] />
        </div>
        <div :class="['player', 'player-8']">
          <div v-if="room.stats.player_position === 3" class="glow"></div>
          <Player :player-nr="4" :before_leave_animation='board_before_leave' :after_leave_animation='board_after_leave'
            :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p4_visible_cards"
            :player=room.players[3] />
        </div>
      </div>
    </div>

  </div>

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