<script setup>


<<<<<<< HEAD
=======
const room = ref(null);
const loaded_data = ref(false);

setInterval(() => {
    server_client.get_room_details(8)
    .then((data) => {
        console.log(data);
        room.value = data;
        loaded_data.value = true;
    })
}, 2000);

>>>>>>> 9d165c79e4ce83d6d73dd2c7d62f474eb4f2912a
</script>

<template>


    
    <div v-if="loaded_data" class="container">
        <!-- <div class="row mt-5">
            <div class="col-6 text-center">
                <b>TEAM ONE POINTS: {{ room.stats.team_one_score }}</b>
                <p>{{ room.players[0].username}} , {{ room.players[2].username }}</p>
            </div>
            <div class="col-6 text-center">
                <b>TEAM TWO POINTS: {{ room.stats.team_two_score }}</b>
                <p>{{ room.players[1].username}} , {{ room.players[3].username }}</p>
            </div>
        </div> -->
                
                <div class="whist-table">

                    <div id="players-turn">{{room.players[room.stats.player_position].username}} is your turn</div>
                    <div class="player-1"><Player :player=room.players[0] /></div>
                    <div class="player-2"><Player :player=room.players[1] /></div>
                    <div class="player-3"><Player :player=room.players[2] /></div>
                    <div class="player-4"><Player :player=room.players[3] /></div>

                    
                    <div class="board">
                        <div class="board-cards" v-for="card in room.stats.board" :key="card">
                            <Card  :card_value="card" />
                        </div>
<<<<<<< HEAD

                        
                    </div>
=======
                        
                    </div>
                    <div class="deck" v-for="index in 52" :key="index">
                        <Card card_value="not_permitted"></Card>
                    </div>
>>>>>>> 9d165c79e4ce83d6d73dd2c7d62f474eb4f2912a
                    
                </div>
    </div>

</template>


<style scoped>
<<<<<<< HEAD
.deck {
    position: relative;
}
.card_in_deck {
    position: absolute;
}
=======

>>>>>>> 9d165c79e4ce83d6d73dd2c7d62f474eb4f2912a
.container{
    display: flex;
}
.whist-table {
    width: 1024px;
    height: 570px;
    background: #346751;
    border-radius: 300px;
    border-style: solid;
    border-width: 20px;
    border-color: #161616;
    flex: 1;
    flex-basis: 100%;
    transition: transform 1s;
    position:absolute;
	top: 25%;
}

.board{
    border:5px solid #63c763;
    height:118px;
    width:340px;
    position:absolute;
    border-radius:10px;
    padding:10px;
    top: 35%;
    left:33%;
}

.board-cards{
    display:inline-block;
	position: relative;
    margin-left: 5px;
    top: -3px;
    left: -8px;
}

.player-1{
    position: absolute;
    top: -28%;
    left: 20%;
}

.player-2{
    position: absolute;
    top: -28%;
    left: 65%;
}

.player-3{
    position: absolute;
    top: 106%;
    left: 20%;
}

.player-4{
    position: absolute;
    top: 106%;
    left: 65%;
}

@keyframes players-turn {
    0% {transform: scale(1.4);}
    85% {transform: scale(1.2);}
    100% {transform: scale(1);}
}


#players-turn{
    color: white;
    position: absolute;
    top: 25%;
    left: 43%;
    animation-name: players-turn;
    animation-duration: 2s;
}

</style>
