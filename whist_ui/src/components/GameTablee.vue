<script setup>
import Card from './Card.vue';
import { ref, watch, onUnmounted } from 'vue';
import Player from './Player.vue';
import {server_client} from '../client';
import _ from "lodash";
let update_interval = null;


const room = ref(null);
const loaded_data = ref(false);
const round_started = ref(true);
const board = ref([]);

const cards_to_spread = ref(52);
const p1_visible_cards = ref(0);
const p2_visible_cards = ref(0);
const p3_visible_cards = ref(0);
const p4_visible_cards = ref(0);

const y = ref(null);
const x= ref(null);

const change_position = ref(null);

const update_room = () => {
      server_client.get_room_details(1)
      .then((data) => {
          if ( ! _.isEqual(data, room.value) ) {
            console.log('updating');
            const is_last_turn = data.stats.board.length === 0;

            if ( is_last_turn && room.value !== null) {
              board.value = data.stats.old_board;
            } else {
              board.value = data.stats.board;
            }
            room.value = data;
            console.log(room)
            round_started.value = room.value.stats.board.length === 0 && room.value.players[room.value.stats.player_position].hand.length === 13;
            loaded_data.value = true;
            
            if (data.stats.winner === data.players[0].username){
              y.value = -253
              x.value = -68
            } else if (data.stats.winner === data.players[1].username){
              y.value = -253
              x.value = 289
            } else if (data.stats.winner === data.players[2].username){
              y.value = 136
              x.value = 289
            } else if (data.stats.winner === data.players[3].username){
              y.value = 136
              x.value = -68
            }

            if (data.stats.old_board === 4){
              change_position.value = 'absolute';
            } else {
              change_position.value = 'relative';
            }

          }
      })
}

update_room();

watch(round_started, async (new_round_started, old_round_started) => {
  if (old_round_started === true && new_round_started === false) {
    update_interval = setInterval(update_room, 500);
  }
})

onUnmounted(() => {
  if (update_interval !== null) {
    console.log('clear interval');
    clearInterval(update_interval);
  }
})

const after_leave = (el) => {
    cards_to_spread.value -= 1;
    
    if (el.id === '1') {
    p1_visible_cards.value++;
  } else if (el.id === '2') {
    p2_visible_cards.value++;
  } else if (el.id === '3') {
    p3_visible_cards.value++;
  } else if (el.id === '4') {
    p4_visible_cards.value++;
  }
  
  if (cards_to_spread.value === 0) {
    round_started.value = false;
  }
}

setTimeout(() => {
  cards_to_spread.value -= 1;
}, 2000)


const board_after_leave = () => {
    const is_last_turn = room.value.stats.board.length === 0;
    if (is_last_turn) {
      board.value = room.value.stats.board;
    }
}

const isToggled = ref(false);

</script>
<template>
<div class="vue-container" v-if="loaded_data">

  <div class="info-bar">
    <div class="trump-card-1">ceva</div>

    <div class="team-1">
      <span>{{room.players[0].username}} : {{ room.players[2].username}}</span>
      <div class="glowing-bar-team-1"></div>
    </div>

    <Transition name="round-winner">
      <div v-if="room.stats.winner" class="winner-bar">
        <span>{{ room.stats.winner}} won</span>
        <div class="glowing-bar"></div>
      </div>
    </Transition>

    <div class="team-2">
      <span>{{room.players[1].username}} : {{ room.players[3].username}}</span>
      <div class="glowing-bar-team-2"></div>
    </div>
  </div>

  <div class="table">
      <div class="board">
        <div v-if="round_started" class="deck">
            <Transition v-for="el in 52" :key="el" :name="`spread-p${4 - ((el - 1) % 4)}`" @after-leave="after_leave">
              <Card :id="`${4 - ((el - 1) % 4)}`" v-if="el<=cards_to_spread" class="card_in_deck" card_value="not_permitted"></Card>
            </Transition>
        </div>

        <TransitionGroup name="board">
          <div class="board-cards"  v-for="card in board" :key="card">
            <Card  :card_value="card" />
          </div>
        </TransitionGroup>

      </div>

      <div class="players">
          <div :class="['player', 'player-5']">
            <div v-if="room.stats.player_position === 0" class="glow"></div>
            <Player :player-nr="1" :after_leave_animation='board_after_leave' :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p1_visible_cards" :player=room.players[0] />
          </div>
        <div :class="['player', 'player-7']">
          <div v-if="room.stats.player_position === 1" class="glow"></div>
          <Player :player-nr="2" :after_leave_animation='board_after_leave' :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p2_visible_cards" :player=room.players[1] />
        </div>
        <div :class="['player', 'player-6']">
          <div v-if="room.stats.player_position === 2" class="glow"></div>
          <Player :player-nr="3" :after_leave_animation='board_after_leave' :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p3_visible_cards" :player=room.players[2] />
        </div>
        <div :class="['player', 'player-8']">
          <div v-if="room.stats.player_position === 3" class="glow"></div>
          <Player :player-nr="4" :after_leave_animation='board_after_leave' :board="room.stats.cards_per_round" :round-started="round_started" :visible-cards="p4_visible_cards" :player=room.players[3] />
        </div>
      </div>
	</div>
</div>


</template>

<style scoped>
.trump-card-1{
  position: absolute;
  left: 25px;
}

.trump-card-2{
  position: absolute;
  left: 10px;
}

.glowing-bar-team-1{
  position: relative;
  top: 6px;
  border-bottom: 1px solid #ef3730;
  box-shadow: 1px 1px 6px #ef3730;
}

.glowing-bar-team-2{
  position: relative;
  top: 6px;
  border-bottom: 1px solid #2eafeb;
  box-shadow: 1px 1px 6px #2eafeb;
}

@keyframes winner{
  0% {opacity: 1;}
  25% {opacity: 0;}
  50% {opacity: 1;}
  75% {opacity: 0;}
  100%{opacity: 1;}
}

@keyframes winner-leave{
  0% {opacity: 1;}
  100%{opacity: 0;}
}
.round-winner-enter-active{
  animation: winner 1s ease-in;
}

.round-winner-leave-active{
  animation: winner-leave 1s ease-in;
}

.info-bar{
  display: flex;
  justify-content: space-evenly;
  border-bottom: 1px solid rgb(101, 101, 101);
  position: relative;
  color: rgb(139, 139, 139);
  font-family: sans-serif;
  font-size: small;
  padding: 5px;
  margin-bottom: 20px;
}

.glowing-bar{
  position: relative;
  top: 6px;
  border-bottom: 1px solid #75ec7b;
  box-shadow: 1px 1px 6px #75ec7b;
}

.winner-bar{
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

@keyframes board-animation{
  0% {opacity: 0;}
  99% {opacity: 0;}
  100% {opacity: 1;}
}

@keyframes board-leaving-animation {
  0% {opacity: 1;}
  10% {
    position: absolute;
    transition: ease-in;
    }
  90% {
    position: absolute;
    opacity: 1;
    transform: translate(calc(1px * v-bind(x)),calc(1px * v-bind(y)))
  }
  100% {
    opacity: 0;
    position: absolute;
    transform: translate(calc(1px * v-bind(x)),calc(1px * v-bind(y)))
  }
}
.board-enter-active{
  animation: board-animation 0.5s ease;
}

.board-leave-active{
  animation: board-leaving-animation 1s ease;
}

.text {
  color: white;
}
.vue-container{
	width: 100vw;
	height: 100vh;
  background-color: #3b3b3b;
}

.deck {
    position: relative;
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

.board-cards{
  display:inline-block;
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
.spread-p4-leave-active 
 {
  transition: all 0.1s ease;
}

.spread-p1-leave-to {
  transform: translate(0, -150px);
}


.spread-p2-leave-to {
  transform: translate(150px ,-150px);
}


.spread-p3-leave-to {
  transform: translate(280px, 100px);
}

.spread-p4-leave-to {
  transform: translate(0, 110px);
}


</style>