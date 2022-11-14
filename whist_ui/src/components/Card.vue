<script setup>
import { server_client } from '../client';
const props = defineProps(['card_value']);


const cards = {
    "10c": "10_of_clubs.png",
    "10d": "10_of_diamonds.png",
    "10h": "10_of_hearts.png",
    "10s": "10_of_spades.png",
    "10c": "2_of_clubs.png",
    "2d": "2_of_diamonds.png",
    "2h": "2_of_hearts.png",
    "2s": "2_of_spades.png",
    "3c": "3_of_clubs.png",
    "3d": "3_of_diamonds.png",
    "": "3_of_hearts.png",
    "": "3_of_spades.png",
    "": "4_of_clubs.png",
    "": "4_of_diamonds.png",
    "": "4_of_hearts.png",
    "": "4_of_spades.png",
    "": "5_of_clubs.png",
    "": "5_of_diamonds.png",
    "": "5_of_hearts.png",
    "": "5_of_spades.png",
    "": "6_of_clubs.png",
    "": "6_of_diamonds.png",
    "": "6_of_hearts.png",
    "": "6_of_spades.png",
    "": "7_of_clubs.png",
    "": "7_of_diamonds.png",
    "": "7_of_hearts.png",
    "": "7_of_spades.png",
    "": "8_of_clubs.png",
    "": "8_of_diamonds.png",
    "": "8_of_hearts.png",
    "": "8_of_spades.png",
    "9c": "9_of_clubs.png",
    "": "9_of_diamonds.png",
    "": "9_of_hearts.png",
    "": "9_of_spades.png",
    "Ac": "ace_of_clubs.png",
    "": "ace_of_diamonds.png",
    "Ah": "ace_of_hearts.png",
    "": "ace_of_spades.png",
    "": "ace_of_spades2.png",
    "": "black_joker.png",
    "": "caca.txt",
    "": "jack_of_clubs.png",
    "": "jack_of_clubs2.png",
    "": "jack_of_diamonds.png",
    "": "jack_of_diamonds2.png",
    "": "jack_of_hearts.png",
    "": "jack_of_hearts2.png",
    "": "jack_of_spades.png",
    "": "jack_of_spades2.png",
    "": "king_of_clubs.png",
    "": "king_of_clubs2.png",
    "": "king_of_diamonds.png",
    "": "king_of_diamonds2.png",
    "": "king_of_hearts.png",
    "": "king_of_hearts2.png",
    "": "king_of_spades.png",
    "": "king_of_spades2.png",
    "": "queen_of_clubs.png",
    "": "queen_of_clubs2.png",
    "": "queen_of_diamonds.png",
    "": "queen_of_diamonds2.png",
    "": "queen_of_hearts.png",
    "": "queen_of_hearts2.png",
    "": "queen_of_spades.png",
    "": "queen_of_spades2.png",
    "not_permioted": "back_of_card.png",
}

const card_url = `http://localhost:8000/static/images/cards/${cards[props.card_value]}`;

const send_played_card = (event) => {
    server_client.send_card_to_server(1, props.card_value);
}
</script>

<template>
    <div @click="send_played_card">
        <img 
        :src="card_url"
        width="103"
        height="138"
        />
    </div>
</template>

<style scoped>

</style>