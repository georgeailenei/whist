// Refresh & Countdown;
let time = 5; 
const countdown_element = document.getElementById('countdown');
const the_interval = setInterval(counter, 1000);
const reload_the_page = setInterval('window.location.reload()', 2000);

function counter () {
    if (countdown_element == null) {
        return;
    } else {
        clearInterval(reload_the_page);
        countdown_element.innerHTML = time.toString();

        if (time == -1) {
            clearInterval(the_interval);
            countdown_element.innerHTML = "Game is starting";
            const one_refresh = setTimeout(window.location.reload(), 1000);
        }
    }
    time--;
}
