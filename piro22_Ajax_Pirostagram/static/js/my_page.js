const requestLike = new XMLHttpRequest();
const onClickLike = (feedID) => {
    const url = "/like_ajax/";
    requestLike.open("POST", url, true);
    requestLike.setRequestHeader(
        "Content-Type",
        "application/json"
    );
    requestLike.send(JSON.stringify({id: feedID}));
};

requestLike.onreadystatechange = () => {
    if(requestLike.readyState === XMLHttpRequest.DONE) {
        if(requestLike.status === 200) {
            const response = JSON.parse(requestLike.responseText);
            const likeCount = response.like_count;

            const likeElement = document.querySelector(".update_like_num");
            likeElement.innerHTML = `${likeCount}명이 이 게시글을 좋아합니다.`;
        }
        else {
            console.error("error exist!", requestLike.status);
        }
    }
};