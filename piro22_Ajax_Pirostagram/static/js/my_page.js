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
    const trash_icon_url = commentParent.getAttribute('data-trash-icon');

    const newComment = document.createElement('div');
    newComment.classList.add('upload_comment');

    newComment.innerHTML = `
        <div class="commet_author">episode.nkm</div>
        <div class="comment_content">${inputValue}</div>
        <button type="submit" class="delete_comment_btn" onclick="onClickDelete(this)">
            <img src="${trash_icon_url}" alt="댓글 삭제 버튼" />
        </button>
    `;

    commentParent.appendChild(newComment);
    inputField.value = '';
}

function onClickDelete(this_comment) {
    const want_delete = this_comment.closest('.upload_comment');
    const alert = confirm("해당 댓글을 삭제하시겠습니까?");
    if (alert) {
        want_delete.remove();
    }
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