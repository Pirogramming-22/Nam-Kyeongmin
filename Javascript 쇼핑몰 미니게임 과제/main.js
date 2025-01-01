// data.json에서 items 데이터를 동적으로 로드
function loadItems() {
    return fetch('data/data.json')
        .then(response => response.json())
        // 성공적으로 동적 로드(fetch) 시, json으로 변환
        .then(json => json.items);
        // json으로 변환 시, 배열 object "items"를 가져옴
}

// MAIN
loadItems()
    .then(items => {
        console.log(items);
        //displayItems(items);
        /* 로드한 items를 화면에 보여줄 수 있도록 */
        //setEventListeners(items);
    })
    .catch(console.log);