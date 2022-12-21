<script setup>
import {ref, onUnmounted} from 'vue';
import { server_client } from '../client';
import _ from "lodash";
import Game from './Game.vue'


const game_is_playing = ref(true);
const round_finished = ref(false);
const is_modal_open = ref(false);
const loaded_data = ref(false);
const user_data = ref(null);
const room = ref(null);
const winners = ref(null);
const player_left_the_game = ref(false);
const players_choice = ref(null);


const update_user_data = () => {
  server_client.get_user_details()
    .then((data) => {
      user_data.value = data;
      console.log(user_data.value);
    })
}

update_user_data();

const play_another_game = () => {
  is_modal_open.value = false;
  server_client.send_players_choice_to_server(1, true, user_data.value.username);
}

const quit_game = () => {
  is_modal_open.value = false;
  server_client.send_players_choice_to_server(1, false, user_data.value.username);
  location.replace("http://localhost:8000/card_rooms");
}

const game_no_longer_available = () => {
  location.replace("http://localhost:8000/card_rooms");
}

const update_room = () => {
    server_client.get_room_details(1)
      .then((data) => {
        if (!_.isEqual(data, room.value)) {
          
          room.value = data;
          loaded_data.value = true;

          console.log('updating');
          console.log(room.value);

          players_choice.value = room.value.stats.players_choice
          console.log(players_choice)


          if (room.value.stats.team_one_score === 5 && room.value.stats.team_one_score > room.value.stats.team_two_score){
            winners.value = String(room.value.players[0].username) + " & " + String(room.value.players[2].username)
            is_modal_open.value = true;
          } else if (room.value.stats.team_one_score < room.value.stats.team_two_score && room.value.stats.team_two_score === 5){
            winners.value = String(room.value.players[1].username) + " & " + String(room.value.players[3].username)
            is_modal_open.value = true;
          }

          if (room.value.players.length != 4) {
            player_left_the_game.value = true;
          }

        }
      })
}

const update_interval = setInterval(update_room, 500);

onUnmounted(() => {
  if (update_interval !== null) {
    console.log('clear interval');
    clearInterval(update_interval);
  }
})


const finish_round = () => {
  round_finished.value = true;
}

</script>

<template>

<!-- Display game no longer available -->
<div v-if="player_left_the_game" class="modal">
  <div class="modal-content">
    <p>The game is no longer available</p>
    <button class="button-quit" @click="game_no_longer_available">OTHER ROOMS</button>
  </div>
</div>

<!-- The GAME -->
<Game v-if="(game_is_playing && loaded_data)" :finish_round="finish_round" :room="room"/>


<!-- Display the winners and losers here -->
<div v-if="is_modal_open && players_choice === 0" class="modal">
  <div class="modal-content">
    <b class="winner-msg-congrats">Congratulations</b>
      {{ winners }}
    <b class="winner-msg">You win</b>

    <!-- @click.once triggers the func once so replace it later 
          also do not forget to change the link  -->
    <button class="button-play-again" @click.once="play_another_game">Play again</button>
    <button class="button-quit" @click.once="quit_game">Quit</button>
  </div>
</div>


<!-- Waiting for other players -->
<div v-if="players_choice > 0" class="modal">
  <div class="modal-content">
    <p>Please wait</p>
    <p>Searching for another game</p>
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
