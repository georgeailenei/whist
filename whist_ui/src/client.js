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
        const response = await fetch(`${this.BASE_URL}rooms/${room_id}/`, {
            method: 'PATCH',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'card': card_value
            })
        });
        return response;
    }

    get_user_details = async () => {
        const user_data = await fetch(`${this.BASE_URL}users/self`);
        const data = await user_data.json();

        return data;
    }
}

export const server_client = new ServerClient();
