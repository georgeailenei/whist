<script setup>
import { computed } from 'vue';
import Card from './Card.vue';


import { ref } from 'vue';
import Player from './Player.vue';
import {server_client} from '../client';


const room = ref(null);
const loaded_data = ref(false);

const player1_see_cards = ref(0);
const player2_see_cards = ref(0);
const player3_see_cards = ref(0);
const player4_see_cards = ref(0);

// setInterval(() => {
    server_client.get_room_details(1)
    .then((data) => {
        console.log(data);
        room.value = data;
        loaded_data.value = true;
    })
// }, 2000);

const show = ref(true);
const cards_to_spread = ref(52);

setTimeout(() => {
  cards_to_spread.value -= 1;
}, 1000)

const after_leave = (el) => {
  cards_to_spread.value -= 1;
  
  if (el.id === '1') {
    player1_see_cards.value += 1;
  } else if (el.id === '2') {
    player2_see_cards.value += 1;
  } else if (el.id === '3') {
    player3_see_cards.value += 1;
  } else if (el.id === '4') {
    player4_see_cards.value += 1;
  }
}

</script>
<template>
<div class="vue-container" v-if="loaded_data">
<button @click="show=!show">apasama</button>

	<div class="table">
		<div class="board">
			<div class="deck">
					<Transition
           v-for="el in 52" 
           :key="el"
           :name="`spread-p${4 - ((el - 1) % 4)}`"
           @after-leave="after_leave"
           >
            <Card :id="`${4 - ((el - 1) % 4)}`" v-if="el<=cards_to_spread" class="card_in_deck" :style="{left: `${52/4}px`}" card_value="not_permitted"></Card>
					</Transition>
			</div>

      <div class="board-cards" v-for="card in room.stats.board" :key="card">
        <Card  :card_value="card" />
      </div>       
		</div>
		<div class="players">
      <div :class="['player', 'player-5']">
        <Player :can_see_no_of_cards="player1_see_cards" :player="room.players[0]" />
      </div>
			<div :class="['player', 'player-7']">
				<Player :can_see_no_of_cards="player2_see_cards" :player=room.players[1] />
			</div>
			<div :class="['player', 'player-6']">
				<Player :can_see_no_of_cards="player3_see_cards" :player=room.players[2] />
			</div>
			<div :class="['player', 'player-8']">
        <Player :can_see_no_of_cards="player4_see_cards" :player=room.players[3] />
			</div>
		</div>
	</div>
</div>


</template>

<style scoped>

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
    left: 100px;
}


.spread-p1-leave-active,
.spread-p2-leave-active,
.spread-p3-leave-active,
.spread-p4-leave-active 
 {
  transition: all 0.09s ease;
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





.table {
  width: 775px;
  height: 345px;
  background-color: #456658;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  border-radius: 200px;
  position: relative;
  border: 30px solid #252322;
}
.table .board {
  /* border: 2px solid #5c8773; */
  height: 100px;
  width: 340px;
  position: absolute;
  border-radius: 10px;
  padding: 10px;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  box-sizing: border-box;
}

.board-cards{
  display:inline-block;
  position: relative;
  margin-left: 5px;
  left: 80px;
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

.bouton {
  background-color: #515260;
  color: white;
  text-transform: uppercase;
  border: none;
  outline: none;
  padding: 5px 10px;
}



</style>