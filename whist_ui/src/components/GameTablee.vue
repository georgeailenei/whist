<script setup>
import { computed } from 'vue';
import Card from './Card.vue';


import { ref } from 'vue';
import Player from './Player.vue';
import {server_client} from '../client';


const room = ref(null);
const loaded_data = ref(false);

// setInterval(() => {
    server_client.get_room_details(1)
    .then((data) => {
        console.log(data);
        room.value = data;
        loaded_data.value = true;
    })
// }, 2000);

const player_playing = 0;
const players = [
    { name: 'rivy33', bank: 100, onTable: 77, hasCards: false },
    { name: 'kattar', color: 'cyan', bank: 100, onTable: 20, hasCards: false },
    { name: 'mikelaire', color: 'lightcoral', bank: 100, onTable: 20, hasCards: false },
    { name: 'tomtom', color: 'crimson', bank: 100, onTable: 20, hasCards: false },
    // { name: 'nana', color: '#444', bank: 100, onTable: 20, hasCards: false },
    // { name: 'ionion', color: 'forestgreen', bank: 100, onTable: 20, hasCards: false },
    // { name: 'link6996', color: 'goldenrod', bank: 100, onTable: 20, hasCards: false },
    // { name: 'gossboganon', color: 'gold', bank: 100, onTable: 20, hasCards: false }
]

const values = [
    'A',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'V',
    'D',
    'K'
]

const figures = [
			's',
			'h',
			'c',
			'd'
		]


const cards = () => {
    let all = []
    let i = 0;
    for (let figure of figures) {
        for (let value of values) {
            all.push({
                f: figure,
                v: value
            })
            i +=1;
            if (i === 5) {
                return all
            }
        }
    }
    return all
}

const show = ref(true);
</script>
<template>

<button @click="show=!show">apasama</button>
<div class="vue-container" v-if="loaded_data">
	<div class="table">
		<div class="card-place">
			<div class="deck">
					
					<!-- <Card :style="{left: `${index / 4}px`}" v-for="index in 51" :key="index" class="card_in_deck" card_value="not_permitted"></Card> -->
					<Transition name="spread">
						<Card v-if="show" class="animated_card" :style="{left: `${52/4}px`}" card_value="not_permitted"></Card>
					</Transition>
	
					
			</div>
			<!-- <Card v-for="(card, index) in cards()" :card_value="`${card.v}${card.f}`"></Card> -->
		</div>
		<div class="players">
			<div :class="['player', 'player-5']">
				<div class="avatar" :style="{backgroundColor: players[0].color || 'dodgerblue'}"></div>
				<div class="name">{{players[0].name}}</div>
			</div>
			<div :class="['player', 'player-7']">
				<div class="avatar" :style="{backgroundColor: players[1].color || 'dodgerblue'}"></div>
				<div class="name">{{players[1].name}}</div>
			</div>
			<div :class="['player', 'player-6']">
				<div class="avatar" :style="{backgroundColor: players[2].color || 'dodgerblue'}"></div>
				<div class="name">{{players[2].name}}</div>
			</div>
			
			<div :class="['player', 'player-8']">
				<div class="avatar" :style="{backgroundColor: players[3].color || 'dodgerblue'}"></div>
				<div class="name">{{players[3].name}}</div>
			</div>
		</div>
	</div>
	<!-- <button class="bouton" @click="">Refresh</button> -->
</div>


</template>

<style scoped>
html, body{
	margin:0;
	padding:0;
}

.vue-container{
	width:100vw;
	height:100vh;
}

.deck {
    position: relative;
}
.card_in_deck {
    position: absolute;
}


.spead {
	transform: translateX('1000px') scale(1.2);
}

.spread-leave-from {
	transition: 1;	
}
.spread-leave_to {
	opacity: 0;
  
}

.spread-enter-active {
	transition: all 2s ease;
}


.table {
  width: 1000px;
  height: 400px;
  background-color: #4aad4a;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  border-radius: 150px;
  position: relative;
  border: 15px solid #a95555;
}
.table:before {
  content: "";
  border: 7px solid rgba(0, 0, 0, 0.1);
  display: block;
  width: 1015px;
  height: 415px;
  border-radius: 150px;
  position: absolute;
  top: -15px;
  left: -15px;
}
.table:after {
  content: "";
  border: 7px solid rgba(0, 0, 0, 0.1);
  display: block;
  width: 985px;
  height: 385px;
  border-radius: 130px;
  position: absolute;
  top: 0;
  left: 0;
}
.table .card-place {
  border: 5px solid #63c763;
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
.table .card-place .card:not(:last-child) {
  margin-right: 15px;
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
.players .player .avatar {
  width: 120px;
  height: 120px;
  background-color: lightcoral;
  border-radius: 100%;
  position: relative;
  box-shadow: 2px 10px 0px rgba(0, 0, 0, 0.4);
  z-index: 20;
}
.players .player .avatar:after {
  content: "";
  width: 70px;
  height: 70px;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.1);
  top: 50%;
  left: 50%;
  transform: translatex(-50%) translatey(-50%);
  border-radius: 100%;
  box-shadow: 0px 5px 0px rgba(0, 0, 0, 0.2);
}
.players .player .name {
  font-family: "Houschka Rounded";
  text-align: center;
  width: 100px;
  color: #96e296;
  padding: 5px 0;
  margin-left: 10px;
  box-sizing: border-box;
  border: 2px solid #96e296;
  border-radius: 5px;
  margin-top: 15px;
  text-overflow: ellipsis;
  font-size: 11px;
  overflow: hidden;
  position: relative;
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
  top: 0px;
  left: 25%;
  transform: translatex(-50%) translatey(-50%);
}
.players .player.player-6 {
  bottom: 0px;
  left: 75%;
  transform: translatex(-50%) translatey(50%) rotatez(180deg);
}
.players .player.player-6 .name {
  transform: rotatez(180deg);
}
.players .player.player-6 .bank-value {
  transform: rotatez(180deg);
}
.players .player.player-6 .mise-value {
  transform: rotatez(180deg);
}
.players .player.player-7 {
  top: 0px;
  left: 75%;
  transform: translatex(-50%) translatey(-50%);
}
.players .player.player-8 {
  bottom: 0px;
  left: 25%;
  transform: translatex(-50%) translatey(50%) rotatez(180deg);
}
.players .player.player-8 .name {
  transform: rotatez(180deg);
}
.players .player.player-8 .bank-value {
  transform: rotatez(180deg);
}
.players .player.player-8 .mise-value {
  transform: rotatez(180deg);
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