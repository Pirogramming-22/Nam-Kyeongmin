const start_button = document.getElementById("start")
const stop_button = document.getElementById("stop")
const reset_button = document.getElementById("reset")

let interId;
let time=0;
let min = "00";
let sec = "00";

function update(time) {
    min = String(Math.floor((time%3600)/60)).padStart(2,"0");
    sec = String(time%60).padStart(2,"0");

    document.getElementById("time").innerText= `${min}:${sec}`;
}

start_button.addEventListener('click', function() {
    interId = setInterval(() => {
        time++;
        update(time);
    }, 10);
});

stop_button.addEventListener('click', function() {
    clearInterval(interId);

    const recordDiv = document.createElement("div");
    recordDiv.classList.add("time_record");

    recordDiv.innerHTML= `
    <div class="select_record"><input type="radio">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-circle" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
        </svg>
    </div>
    <div class="time_for_record">${min}:${sec}</div>`;

    document.getElementById("record_list").appendChild(recordDiv);
});

reset_button.addEventListener('click', function() {
    clearInterval(interId);
    time=0;
    update(time);
});