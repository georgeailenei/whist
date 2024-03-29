<script setup>
import Card from './Card.vue';
import { ref, watch } from 'vue';
import Player from './Player.vue';
import _ from "lodash";
import { Howl } from 'howler';
import AudioButton from './AudioButton.vue'

const props = defineProps([
  'room',
  'game_is_playing',
]);

const room = ref(null);
const round_started = ref(false);
const first_round_started = ref(false);
const board = ref([]);

const cards_to_spread = ref(52);
const cards_are_available = ref(false);
const p1_visible_cards = ref(0);
const p2_visible_cards = ref(0);
const p3_visible_cards = ref(0);
const p4_visible_cards = ref(0);

const y = ref(null);
const x = ref(null);

const change_position = ref(null);
const is_in_animation = ref(false);
const audio_sound = ref(true);

const mute_or_unmute = (event) => {
  console.log('Audio Button Clicked');

  if(audio_sound.value === true){
    audio_sound.value = false;
  } else {
    audio_sound.value = true;
  }
}

// Cards sounds effects. Create a button to turn the sound off && on.
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
};

const update_room = (new_room) => {
  room.value = new_room;

  // Round started && last turn conditions.
  const is_last_turn = new_room.stats.board.length === 0;
  round_started.value = !(new_room.stats.board.length === 0 && new_room.players[new_room.stats.player_position].hand.length === 13);

  // First round conditions.
  first_round_started.value = new_room.stats.board.length === 0 && 
  new_room.players[new_room.stats.player_position].hand.length === 13;

  // Board values.
  if (is_last_turn && room.value !== null) {
    board.value = new_room.stats.old_board;
  } else {
    board.value = new_room.stats.board;
  }

  // Board cards directions values.
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

    if (audio_sound.value === true) {
      sounds.slide_card.play();
    }
  }
};

update_room(props.room);

watch(() => props.room, async (new_room, old_room) => {
  update_room(new_room);
});

// Spreading cards.
const after_leave = (el) => {
  cards_to_spread.value -= 1;
  if (audio_sound.value === true) {
    sounds.spread_card.play();
  }

  if (el.id === '1') {
    p1_visible_cards.value++;
  } else if (el.id === '2') {
    p2_visible_cards.value++;
  } else if (el.id === '3') {
    p3_visible_cards.value++;
  } else if (el.id === '4') {
    p4_visible_cards.value++;
  }

  // Card animation conditions for first.
  if (cards_to_spread.value === 0) {
    cards_are_available.value = true;
  }
};

setTimeout(() => {
  cards_to_spread.value -= 1;
}, 2000);

// Board Animations.
const board_before_leave = () => {
  is_in_animation.value = true;
};

const board_after_leave = () => {
  const is_last_turn = room.value.stats.board.length === 0;
  if (is_last_turn) {
    board.value = room.value.stats.board;
    if (audio_sound.value === true) {
      sounds.pickup_cards.play();
    }
  } 
  is_in_animation.value = false;
};

const card_symbols = {
  "diamonds": "&diams;",
  "hearts": "&hearts;",
  "spades": "&spades;",
  "clubs": "&clubs;",
};

</script>
<template>

  <div class="vue-container">

    <!-- Mute Sound -->
    <div @click="mute_or_unmute">
      <AudioButton />
    </div>
    <!-- Table -->
    <div class="table">
      <div class="board">

        <!-- Trump Card -->
        <span class="card-symbol" v-html="card_symbols[room.stats.trump_card]"></span>

        <!-- Deck -->
        <div v-if="(!round_started || first_round_started)" class="deck">
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
        <div :class="['player', 'player-1']">
          <div v-if="room.stats.player_position === 0" class="glow"></div>
          <Player :game-is-playing="game_is_playing" :player-nr="1" :before-leave-animation='board_before_leave' :after-leave-animation='board_after_leave'
            :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p1_visible_cards"
            :first-round="cards_are_available" :player=room.players[0] />
        </div>
        <div :class="['player', 'player-2']">
          <div v-if="room.stats.player_position === 1" class="glow"></div>
          <Player :game-is-playing="game_is_playing" :player-nr="2" :before-leave-animation='board_before_leave' :after-leave-animation='board_after_leave'
            :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p2_visible_cards"
            :first-round="cards_are_available" :player=room.players[1] />
        </div>
        <div :class="['player', 'player-3']">
          <div v-if="room.stats.player_position === 2" class="glow"></div>
          <Player :game-is-playing="game_is_playing" :player-nr="3" :before-leave-animation='board_before_leave' :after-leave-animation='board_after_leave'
            :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p3_visible_cards"
            :first-round="cards_are_available" :player=room.players[2] />
        </div>
        <div :class="['player', 'player-4']">
          <div v-if="room.stats.player_position === 3" class="glow"></div>
          <Player :game-is-playing="game_is_playing" :player-nr="4" :before-leave-animation='board_before_leave' :after-leave-animation='board_after_leave'
            :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p4_visible_cards"
            :first-round="cards_are_available" :player=room.players[3] />
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

.card-symbol {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  color: #252322;
  font-size: x-large;
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
  }

  90% {
    position: absolute;
    opacity: 1;
    transform: translate(calc(1px * v-bind(x)), calc(1px * v-bind(y)));
  }

  100% {
    opacity: 0;
    position: absolute;
    transform: translate(calc(1px * v-bind(x)), calc(1px * v-bind(y)));
  }
}

.board-enter-active {
  animation: board-animation 0.5s ease;
}

.board-leave-active {
  animation: board-leaving-animation 2s ease;
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