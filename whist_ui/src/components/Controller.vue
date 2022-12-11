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

const update_user_data = () => {
  server_client.get_user_details()
    .then((data) => {
      user_data.value = data;
      console.log(user_data.value);
    }
    )
}

update_user_data();

const update_room = () => {
    server_client.get_room_details(1)
      .then((data) => {
        if (!_.isEqual(data, room.value)) {
          console.log('updating');
          console.log(room.value);
          console.log(data);

          room.value = data;
          loaded_data.value = true;

          if (room.value.stats.team_one_score === 5 && room.value.stats.team_one_score > room.value.stats.team_two_score){
            winners.value = String(room.value.players[0].username) + " & " + String(room.value.players[2].username)
            is_modal_open.value = true;
          } else if (room.value.stats.team_one_score < room.value.stats.team_two_score && room.value.stats.team_two_score === 5){
            winners.value = String(room.value.players[1].username) + " & " + String(room.value.players[3].username)
            is_modal_open.value = true;
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

const finish_game = () => {
  return false;
}

const finish_round = () => {
  round_finished.value = true;
}

</script>

<template>
  <Game v-if="(game_is_playing && loaded_data)" :finish_round="finish_round" :finish_game='finish_game' :room="room"/>
  
<!-- Display the winners and losers here -->
<div v-if="is_modal_open" class="modal">
  <div class="modal-content">
    <b class="winner-msg-congrats">Congratulations</b>
      {{ winners }}
    <b class="winner-msg">You win</b>
    <button class="button-play-again">Play again</button>
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

.button-play-again:hover{
  background-color: #269F37;
}

</style>
