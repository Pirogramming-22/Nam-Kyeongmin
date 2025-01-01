const submitBtn = document.getElementsByClassName("submit-button");
const number_1 = document.getElementById("number1");
const number_2 = document.getElementById("number2");
const number_3 = document.getElementById("number3");

// MAth.random(): 0~1 사이 난수 생성
let answers = [];
for (i=0; i<3; i++) {
    one_of_answer = Math.floor(Math.random() * 10);
    if ( answers.indexOf(one_of_answer) === -1 ) {
        // 랜덤 난수가 배열에 저장되어있지 않은 경우(=중복이 아닌 경우)
        answers.push(one_of_answer);
    }
    else {
        /* 
        랜덤 난수가 이미 뽑힌 경우(중복)
        다른 변수도 뽑기 위해 기회 +1*/
        i--;
    };
    console.log(answers);
}

// TODO_1: 게임 초기화
// 시도 가능 횟수 설정: 9회, input 확인할 때마다 1씩 감소
const playTime = {
    stage: 9
};

function showPlayTime(stage) {
    return `
    <div class="remaining-attempts">
        남은 횟수: <span id="attempts">${stage}</span>
    </div>`;
}
// 초기 시도 남은 횟수 보이기
document.querySelector(".remaining-attempts").innerHTML = `남은 횟수: <span id="attempts">${playTime.stage}</span>`;

// TODO_2: .submit-button의 onclick="check_numbers()" 구현
function check_numbers(left, mid, right) {
    let strike=0;
    let ball=0;

    // left.value의 s/b 비교 (.value는 문자열 형태 -> parseInt 취하기!
    if (parseInt(left.value) === answers[0]) {
        strike++;
    }
    else if (parseInt(left.value) === answers[1] 
        || parseInt(left.value) === answers[2]) {
        ball++;
    }
    // mid.value의 s/b 비교
    if (parseInt(mid.value) === answers[1]) {
        strike++;
    }
    else if (parseInt(mid.value) === answers[0] 
        || parseInt(mid.value) === answers[2]) {
        ball++;
    }
    // right.value의 s/b 비교
    if (parseInt(right.value) === answers[2]) {
        strike++;
    }
    else if (parseInt(right.value) === answers[1] 
        || parseInt(right.value) === answers[0]) {
        ball++;
    }

    // 생셩된 결과(s/b)를 바탕으로 html 업데이트
    if (strike === 0 && ball === 0) {
        // = 'out' CASE
        document.querySelector('.result-display').innerHTML
        += `
        <div class="check-result">
        <div class="left">${left.value} ${mid.value} ${right.value}</div>
        <div class="left">:</div> 
        <div class="out num-result left">O</div>
        </div>`;
    }
    else {
        document.querySelector('.result-display').innerHTML
        += `
        <div class="check-result">
        <div class="left">${left.value} ${mid.value} ${right.value}</div>
        <div class="left">:</div> 
        <div class="left">${strike}<span class="strike num-result">S</span>
        ${ball}<span class="ball num-result">B</span></div>
        </div>`;
        if(strike === 3) {
            // 정답을 맞춘 경우
            const win = 'success';
            // 게임 종료 체크(정답 맞춤)
            showImg(win);
        }
    }
};

function showImg(result) {
    // 결과 이미지 로드 + 확인하기 버튼 비활성화
    document.querySelector('.game-result').innerHTML = `<img src="./${result}.png" id="game-result-img"/>`;
    submitBtn.disabled = true;
    return;
};

// class(여러 개 가능)로 불러왔기 때문에 인덱스 지정
submitBtn[0].onclick = () => {
    if(number_1.value !== "" && number_2.value !== "" && number_3.value !== "") {
        if(playTime.stage > 1) {
            playTime.stage = playTime.stage - 1;
            document.querySelector(".remaining-attempts").innerHTML = `남은 횟수: <span id="attempts">${playTime.stage}</span>`;
            check_numbers(number_1, number_2, number_3);
        }
        else {
            // 게임 종료 체크(시도 횟수 소진)
            playTime.stage = playTime.stage - 1;
            document.querySelector(".remaining-attempts").innerHTML = `남은 횟수: <span id="attempts">${playTime.stage}</span>`;
            const lose = 'fail';
            showImg(lose);
        }
    }
    // input 3개 중 하나라도 빈 경우 -> only input 창 초기화
    number_1.value="";
    number_2.value="";
    number_3.value="";
};
