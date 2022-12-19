class ServerClient{
    constructor() {
        this.BASE_URL = 'http://localhost:8000/';
    }

    get_room_details = async (room_id) => {
        const response = await fetch(`${this.BASE_URL}rooms/${room_id}/`);
        const data = await response.json();
    
        return data;
    }

    send_card_to_server = async (room_id, card_value) => {
        const csrf_token = this.getCookie('csrftoken');
        const response = await fetch(`${this.BASE_URL}rooms/${room_id}/`, {
            method: 'PATCH',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token,
            },
            body: JSON.stringify({
                'card': card_value
            })
        });
        return response;
    }

    // send_players_choice_to_server = async (room_id, players_choice) => {
    //     const csrf_token = this.getCookie('csrftoken');
    //     const response = await fetch(`${this.BASE_URL}rooms/${room_id}/`, {
    //         method: 'PATCH',
    //         headers: {
    //             'Accept': 'application/json',
    //             'Content-Type': 'application/json',
    //             'X-CSRFToken': csrf_token,
    //         },
    //         body: JSON.stringify({
    //             'players_choice': players_choice
    //         })
    //     });
    //     return response;
    // }

    get_user_details = async () => {
        const user_data = await fetch(`${this.BASE_URL}users/self`);
        const data = await user_data.json();

        return data;
    }

    getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}

export const server_client = new ServerClient();