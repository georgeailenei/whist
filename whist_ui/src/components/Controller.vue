<script setup>
import {ref, onUnmounted} from 'vue';
import { server_client } from '../client';
import _ from "lodash";
import Game from './Game.vue'


const game_is_playing = ref(true);
const loaded_data = ref(false);
const user_data = ref(null);
const room = ref(null);
const winners = ref(null);
const losers = ref(null);
const p_choice = ref(false);
const room_full = ref(false);
const display_winners = ref(false);
const display_losers = ref(false);
const is_modal_open = ref(false);
const timer = ref(0);

const update_user_data = () => {
  server_client.get_user_details()
    .then((data) => {
      user_data.value = data;
      console.log(user_data.value);

      if (user_data.value.choice === 1){
        p_choice.value = true;
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
            document.getElementById("game_finished").click();
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
  location.replace("http://localhost:8000/card_rooms/1");
  server_client.send_players_choice_to_server(1, true, user_data.value.username);
}

const back_to_room = () => {
  location.replace("http://localhost:8000/card_rooms/1");
}

const quit_game = () => {
  server_client.send_players_choice_to_server(1, false, user_data.value.username);
  location.replace("http://localhost:8000/card_rooms");
}

const game_no_longer_available = () => {
  let time = 1;
  const the_interval = setInterval(redirect_player, 1000);

  function redirect_player() {
    if(time === 0){
      clearInterval(the_interval);
      window.location.replace("http://localhost:8000/card_rooms/1");
    } else {
      time--;
    }
  }
}

const update_interval = setInterval(update_room, 500);

onUnmounted(() => {
  if (update_interval !== null) {
    console.log('clear interval');
    clearInterval(update_interval);
  }
})

</script>

<template>

<!-- The GAME -->
<Game v-if="(game_is_playing && loaded_data && room_full)" :room="room" :time="timer" />

<!-- Display game no longer available -->
<div v-if="!game_is_playing" class="modal">
  <div class="modal-content">
    <p>A player left.</p>
      <p>This game is no longer available</p>
    <button id="game_finished" class="button-quit" @click="game_no_longer_available">OTHER ROOMS</button>
  </div>
</div>

<!-- Display waiting on other players -->
<div v-if="room_full && p_choice != 0" class="modal">
  <div class="modal-content">
    <p>Waiting for players to act</p>
    <p>...</p>
    <button id="game_finished" class="button-quit" @click="back_to_room">Room</button>
  </div>
</div>

<!-- Display Winners -->
<div v-if="display_winners && room_full" class="modal">
  <div class="modal-content">
    <b class="winner-msg-congrats">Congratulations</b>
      {{ winners }}
    <b class="winner-msg">You win</b>
    <button class="button-play-again" @click.once="play_another_game">Play again</button>
    <button class="button-quit" @click.once="quit_game">Quit</button>
  </div>
</div>

<!-- Display Losers -->
<div v-if="display_losers && room_full" class="modal">
  <div class="modal-content">
    <b class="winner-msg-congrats">Try again</b>
      {{ losers }}
    <b class="losers-msg">You lose</b>
    <button class="button-play-again" @click.once="play_another_game">Play again</button>
    <button class="button-quit" @click.once="quit_game">Quit</button>
  </div>
</div>

</template>

<style scoped>

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
  top: 10px;
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
