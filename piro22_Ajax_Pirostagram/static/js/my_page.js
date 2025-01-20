const requestLike = new XMLHttpRequest();
const onClickLike = (feedID) => {
    const likebtn = document.querySelector(".likebtn");
    const heart_fill = likebtn.getAttribute("data-heart-url");
    likebtn.innerHTML = `<img src="${heart_fill}" alt="좋아요 버튼" />`;

    const url = "/like_ajax/";
    requestLike.open("POST", url, true);
    requestLike.setRequestHeader(
        "Content-Type",
        "application/json"
    );
    requestLike.send(JSON.stringify({id: feedID}));
};

function onClickComment() {
    const inputField = document.querySelector('.comment_input');
    const inputValue = inputField.value;
    const commentParent = document.querySelector('.uploaded_comment_container');
    const newComment = document.createElement('div');
    newComment.classList.add('upload_comment');

    newComment.innerHTML = `
        <div class="commet_author">episode.nkm</div>
        <div class="comment_content">${inputValue}</div>
    `;

    commentParent.appendChild(newComment);
    inputField.value = '';
}

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