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
    <div class="select_record">
        <input type="checkbox" class="select_circle"> 
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="circle" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="check-circle behind" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
             <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
        </svg>
    </div>
    <div class="time_for_record">${min}:${sec}<div>`;

    document.getElementById("record_list").appendChild(recordDiv);
});

reset_button.addEventListener('click', function() {
    clearInterval(interId);
    time=0;
    update(time);
});

// 상위 input의 check 구현
const select_circle = document.querySelector('.select_circle')
const circle = document.querySelector('.circle');
const check_circle = document.querySelector('.check_circle');
// 상위 input 체크 => check_circle
// 하위 input 체크 => check-circle로 구분
select_circle.addEventListener('click', function() {
    // 상위 input 체크
    circle.classList.toggle('circle');
    check_circle.classList.toggle('behind');
    // 하위 input도 동시에 체크
    const checks = document.querySelectorAll('.check-circle');
    checks.forEach((check) => {
        check.classList.toggle('behind');
    });
});

// 하위 input의 check 구현
// innerHTML로 넣은 태그에 접근 -> event로 핸들링
document.getElementById('record_list').addEventListener('click', function (event) {
    if(event.target.classList.contains('select_circle')) {
        // record를 포함하는 전체 div의 class = 'time_record'
        const prevent = event.target.closest('.time_record')
        const circle_2 = prevent.querySelector('.circle');
        const check_circle_2 = prevent.querySelector('.check-circle');

        circle_2.classList.toggle('behind');
        check_circle_2.classList.toggle('behind');
    }
});

// 삭제 버튼 구현
const delete_record = document.getElementById('delete_record');
delete_record.addEventListener('click', function() {
    const records = document.querySelectorAll('.time_record');
    records.forEach((record) => {
        const check_circle = record.querySelector('.check-circle');
        if(!check_circle.classList.contains('behind')) {
            record.remove();
        }
    });
});