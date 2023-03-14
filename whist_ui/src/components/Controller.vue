<script setup>
import {ref, onUnmounted} from 'vue';
import { server_client } from '../client';
import _ from "lodash";
import Game from './Game.vue'
import EmptyTable from './EmptyTable.vue';


const loaded_data = ref(false);
const user_data = ref(null);
const room = ref(null);
const game_is_playing = ref(true);

const winners = ref(null);
const losers = ref(null);

const display_winners = ref(false);
const display_losers = ref(false);
const is_modal_open = ref(false);
const room_full = ref(false);
const timer = ref(0);

const update_user_data = () => {
  server_client.get_user_details()
    .then((data) => {
      user_data.value = data;
      console.log(user_data.value);

      if (user_data.value.choice === 1){
        is_modal_open.value = false;
      }
    })
}

update_user_data();

const update_room = () => {
    server_client.get_room_details(1)
      .then((data) => {
        if (!_.isEqual(data, room.value)) {
          
          room.value = data;
          loaded_data.value = true;

          console.log('updating');
          console.log(room.value);
          
          if (room.value.players.length !== 4){
            game_is_playing.value = false;
            room_full.value = false;
            server_client.send_players_choice_to_server(1, true, user_data.value.username);
          } else if (room.value.players.length === 4){
            room_full.value = true;
            game_is_playing.value = true;
          }
          
          if (room.value.stats.team_one_score === 0
            && room.value.stats.team_one_score === 0
            && room.value.stats.board.length === 0
            && room.value.players[room.value.stats.player_position].hand.length === 13) {
            timer.value = 30;
          } else if (room.value.stats.cards_in_play === 1) {
            timer.value = 30;
          } else {
            timer.value = 15;
          }

          if (room.value.stats.team_one_score === 5
            && room.value.stats.team_one_score > room.value.stats.team_two_score
            && user_data.value.choice === 0){

            is_modal_open.value = true;
            winners.value = String(room.value.players[0].username) + " & " + String(room.value.players[2].username)
            losers.value = String(room.value.players[1].username) + " & " + String(room.value.players[3].username)
            
            if (user_data.value.username === room.value.players[0].username || user_data.value.username === room.value.players[2].username){
              display_winners.value = true;
            } else if (user_data.value.username === room.value.players[1].username || user_data.value.username === room.value.players[3].username){
              display_losers.value = true;
            }

          } else if (room.value.stats.team_one_score < room.value.stats.team_two_score
          && room.value.stats.team_two_score === 5
          && user_data.value.choice === 0){
            
            is_modal_open.value = true;
            winners.value = String(room.value.players[1].username) + " & " + String(room.value.players[3].username)
            losers.value = String(room.value.players[0].username) + " & " + String(room.value.players[2].username)

            if (user_data.value.username === room.value.players[1].username || user_data.value.username === room.value.players[3].username){
              display_winners.value = true;
            } else if (user_data.value.username === room.value.players[0].username || user_data.value.username === room.value.players[2].username){
              display_losers.value = true;
            }
          }
        }
      })    
}

const play_another_game = () => {
  server_client.send_players_choice_to_server(1, true, user_data.value.username);
  location.replace("http://localhost:8000/card_rooms/1/game");
}

const quit_game = () => {
  server_client.send_players_choice_to_server(1, false, user_data.value.username);
  location.replace("http://localhost:8000/card_rooms");
}

const update_interval = setInterval(update_room, 500);

onUnmounted(() => {
  if (update_interval !== null) {
    console.log('clear interval');
    clearInterval(update_interval);
  }
})

const modal_timeleft = ref(5);
const modal_timer = setInterval(() => {
  const played_hand_time = Date.parse(room.value.stats.last_played_card);
  const current_time = Date.now();

  if (is_modal_open) {
    modal_timeleft.value = 5 - (Math.floor((current_time - played_hand_time) / 1000))
  }

  if (modal_timeleft.value < 0) {
    modal_timeleft.value = 0;
  }

}, 1000);

</script>

<template>
  
<Game v-if="(game_is_playing && loaded_data && room_full)" :room="room" :time="timer" />
<EmptyTable v-if="(loaded_data && !room_full)" :room="room"/>

<!-- Display Winners -->
<div v-if="display_winners && room_full && is_modal_open" class="modal">
  <div class="modal-content">
    <b class="winner-msg-congrats">Congratulations</b>
      {{ winners }}
    <b class="winner-msg">You win</b>
    <button class="button-play-again" @click.once="play_another_game">Play again</button>
    <button class="button-quit" @click.once="quit_game">Quit</button>
    <span class="modal_timer">{{ modal_timeleft }}</span>
  </div>
</div>

<!-- Display Losers -->
<div v-if="display_losers && room_full && is_modal_open" class="modal">
  <div class="modal-content">
    <b class="winner-msg-congrats">Try again</b>
      {{ losers }}
    <b class="losers-msg">You lose</b>
    <button class="button-play-again" @click.once="play_another_game">Play again</button>
    <button class="button-quit" @click.once="quit_game">Quit</button>
    <span class="modal_timer">{{ modal_timeleft }}</span>
  </div>
</div>

</template>

<style scoped>
.modal_timer{
  position: relative;
  top: 25px;
}
.modal{
  display: block;
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

.modal-content{
  text-align: center;
  background-color: #333333;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  color: #BBBBBB;
  padding: 35px;
  border: 1px solid #252322;
  width: 275px;
  height: 225px;
}

.winner-msg-congrats{
  color: #BBBBBB;
  font-size: larger;
  align-self: center;
}
.winner-msg{
  color: #269F37;
  font-size: medium;
}

.losers-msg{
  color: #ed4710;
  font-size: medium;
}
.button-play-again{
  width: 90px;
  height: 30px;
  position: relative;
  top: 10px;
  margin: auto;
  background-color: #252322;
  border: none;
  color: white;
  font-size: x-small;
  transition-duration: 0.4s;
}

.button-quit{
  width: 90px;
  height: 30px;
  position: relative;
  top: 15px;
  margin: auto;
  background-color: #252322;
  border: none;
  color: white;
  font-size: x-small;
  transition-duration: 0.4s;
}

.button-play-again:hover{
  background-color: #269F37;
}

.button-quit:hover{
  background-color: #ed4710;
}

</style>
