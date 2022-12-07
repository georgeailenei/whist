<script setup>
import {ref, onUnmounted} from 'vue';
import { server_client } from '../client';
import _ from "lodash";
import Game from './Game.vue'


const game_is_playing = ref(true);
const round_finished = ref(false);
const is_modal_open = ref(true);
const loaded_data = ref(false);
const user_data = ref(null);
const room = ref(null);

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
  // if (!is_in_animation.value) {
    server_client.get_room_details(1)
      .then((data) => {
        if (!_.isEqual(data, room.value)) {
          console.log('updating');
          // const is_last_turn = data.stats.board.length === 0;
          // console.log(is_last_turn, room.value !== null)
          console.log(room.value);
          console.log(data);

          room.value = data;
          loaded_data.value = true;


          // if (is_last_turn && room.value !== null) {
          //   board.value = data.stats.old_board;
          // } else {
          //   board.value = data.stats.board;
          // }

          // room.value = data;
          // // console.log(room)
          // round_started.value = room.value.stats.board.length === 0 && room.value.players[room.value.stats.player_position].hand.length === 13;
          // loaded_data.value = true;
          // played_hand_time.value = Date.parse(room.value.stats.last_played_card);

          // if (data.stats.winner === data.players[0].username) {
          //   y.value = -253;
          //   x.value = -68;
          // } else if (data.stats.winner === data.players[1].username) {
          //   y.value = -253;
          //   x.value = 289;
          // } else if (data.stats.winner === data.players[2].username) {
          //   y.value = 136;
          //   x.value = 289;
          // } else if (data.stats.winner === data.players[3].username) {
          //   y.value = 136;
          //   x.value = -68;
          // }

          // if (data.stats.old_board === 4) {
          //   change_position.value = 'absolute';
          // } else {
          //   change_position.value = 'relative';
          //   sounds.slide_card.play();
          // }

          // // if (room.value.stats.team_one_score === 5){
          // //   console.log("do something");
          // // } else if (room.value.stats.team_two_score === 5){
          // //   console.log("altceva");
          // // }
        }
      })
  // }
}

// watch(round_started, async (new_round_started, old_round_started) => {
//   if (old_round_started === true && new_round_started === false) {
//     
//   }
// })

const update_interval = setInterval(update_room, 500);

onUnmounted(() => {
  if (update_interval !== null) {
    console.log('clear interval');
    clearInterval(update_interval);
  }
})

const finish_game = () => {
  game_is_playing.value = false;
}

const finish_round = () => {
  round_finished.value = true;
}
</script>

<template>
  <Game v-if="(game_is_playing && loaded_data)" :finish_round="finish_round" :finish_game='finish_game' :room="room"/>
  
    <!-- Display the winners and losers here -->
  <!-- <div v-if="is_modal_open" class="modal">
    <div class="modal-content">
      <b class="winner-msg-congrats">Congratulations</b>
        Team 1 wins
      <b class="winner-msg">You win</b>
      <button class="button-play-again">Play again</button>
    </div>
  </div> -->

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
