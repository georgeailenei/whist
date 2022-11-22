<script setup>
import { server_client } from '../client';
const props = defineProps(['card_value']);
console.log(props.card_value);
// console.log(props.card_value);
const cards = {
    "10c": "10_of_clubs.png",
    "10d": "10_of_diamonds.png",
    "10h": "10_of_hearts.png",
    "10s": "10_of_spades.png",
    "2c": "2_of_clubs.png",
    "2d": "2_of_diamonds.png",
    "2h": "2_of_hearts.png",
    "2s": "2_of_spades.png",
    "3c": "3_of_clubs.png",
    "3d": "3_of_diamonds.png",
    "3h": "3_of_hearts.png",
    "3s": "3_of_spades.png",
    "4c": "4_of_clubs.png",
    "4d": "4_of_diamonds.png",
    "4h": "4_of_hearts.png",
    "4s": "4_of_spades.png",
    "5c": "5_of_clubs.png",
    "5d": "5_of_diamonds.png",
    "5h": "5_of_hearts.png",
    "5s": "5_of_spades.png",
    "6c": "6_of_clubs.png",
    "6d": "6_of_diamonds.png",
    "6h": "6_of_hearts.png",
    "6s": "6_of_spades.png",
    "7c": "7_of_clubs.png",
    "7d": "7_of_diamonds.png",
    "7h": "7_of_hearts.png",
    "7s": "7_of_spades.png",
    "8c": "8_of_clubs.png",
    "8d": "8_of_diamonds.png",
    "8h": "8_of_hearts.png",
    "8s": "8_of_spades.png",
    "9c": "9_of_clubs.png",
    "9d": "9_of_diamonds.png",
    "9h": "9_of_hearts.png",
    "9s": "9_of_spades.png",
    "Ac": "ace_of_clubs.png",
    "Ad": "ace_of_diamonds.png",
    "Ah": "ace_of_hearts.png",
    "As": "ace_of_spades.png",
    "Jc": "jack_of_clubs.png",
    "Jd": "jack_of_diamonds.png",
    "Jh": "jack_of_hearts.png",
    "Js": "jack_of_spades.png",
    "Kc": "king_of_clubs.png",
    "Kd": "king_of_diamonds.png",
    "Kh": "king_of_hearts.png",
    "Ks": "king_of_spades.png",
    "Qc": "queen_of_clubs.png",
    "Qd": "queen_of_diamonds.png",
    "Qh": "queen_of_hearts.png",
    "Qs": "queen_of_spades.png",
    "not_permitted": "back_of_card.png",
}

const card_url = `http://localhost:8000/static/images/cards/${cards[props.card_value]}`;

const send_played_card = (event) => {
    console.log(props.card_value);
    server_client.send_card_to_server(8, props.card_value);
}

</script>

<template>
    <div class="card" @click="send_played_card">
        <img class="card_img" :src="card_url" />
    </div>
</template>

<style scoped>

.card{
    height:70px;
	width:50px;
    display:inline-block;
    /* position:relative; */
/*     
    height: 70px;
    width: 50px;  
    border-radius: 5px;
    display: inline-block;
    position: relative; */
}
.card_img {
    width: 100%;
    height: 100%;
}


</style>