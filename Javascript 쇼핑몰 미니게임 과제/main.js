// data.json에서 items 데이터를 동적으로 로드
function loadItems() {
    return fetch('data/data.json')
        .then(response => response.json())
        // 성공적으로 동적 로드(fetch) 시, json으로 변환
        .then(json => json.items);
        // json으로 변환 시, 배열 object "items"를 가져옴
}

// 로드한 items를 화면에 보여줄 수 있도록 html 태그화
function displayItems(items) {
    const container = document.querySelector('.items');
    /*
    map().join('')의 원리 파악하기!
    const HTML = items.map(item => createHTMLString(item)).join('');
    console.log(HTML);
    */
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
    // innerHTML의 이름을 item으로 지정해줄 수 있음
}

// 불러온 데이터의 key들을 html 태그로 직접 변환하는 함수
function createHTMLString(item) {
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />            
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

// button 클릭(event) 감지
function onButtonClick(event, items) {
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if(key==null || value==null) {
        return;
        /* key or value 없을 때 함수 종료 */
    }
    /*
    filter 작동 확인용
    const filter = items.filter(item => item[key] === value);
    console.log(filter);
    */
    displayItems(items.filter(item => item[key] === value));  
}

function setEventListeners(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click', event => onButtonClick(event, items));
}

// MAIN
loadItems()
    .then(items => {
        displayItems(items);
        setEventListeners(items);
    })
    .catch(console.log);