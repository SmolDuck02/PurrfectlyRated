const user = JSON.parse(user_list);

const likeButtons = document.querySelectorAll(".fa-solid.fa-arrow-up.fa-lg");
likeButtons.forEach((button) => {
  button.addEventListener("click", (event) => {
    event.stopPropagation();
    button.classList.toggle("active");

    console.log("anon", event.target.id, button.classList, button.id);

    const postId = event.target.id.split("-")[1];

    // dislike button
    if (event.target.classList[2] === "fa-rotate-180") {
      document.getElementById(`VPdislike-${postId}`).classList.toggle("active");

      const dislikesSpan = document.querySelector(`#dislikes-count-${postId}`);
      const VPdislikeCountSpan = document.querySelector(`#VPdislike-count-${postId}`);
      const csrftoken = getCookie("csrftoken");

      fetch(`/dislike_interaction/${user.id}/${postId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          dislikesSpan.textContent = data.total_dislikes === 0 ? "" : data.total_dislikes;
          VPdislikeCountSpan.textContent = data.total_dislikes === 0 ? "" : data.total_dislikes;
          console.log("dissslikeeeess", data, dislikesSpan);
        })
        .catch((error) => {
          console.error("Error updating like count:", error);
        });

      // like button
    } else if (event.target.classList[2] === "fa-lg") {
      console.log("hayss");

      document.getElementById(`VPlike-${postId}`).classList.toggle("active");

      const likeCountSpan = document.querySelector(`#like-count-${postId}`);
      const VPlikeCountSpan = document.querySelector(`#VPlike-count-${postId}`);
      const csrftoken = getCookie("csrftoken");

      fetch(`/like_interaction/${user.id}/${postId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          likeCountSpan.textContent = data.total_likes === 0 ? "" : data.total_likes;
          VPlikeCountSpan.textContent = data.total_likes === 0 ? "" : data.total_likes;
          console.log("ababaabab", data, likeCountSpan);
        })
        .catch((error) => {
          console.error("Error updating like count:", error);
        });
    }
  });
});

const heartButtons = document.querySelectorAll(".fa-solid.fa-heart.fa-lg");
heartButtons.forEach((button) => {
  button.addEventListener("click", (event) => {
    event.stopPropagation();
    button.classList.toggle("active");
    const postId = event.target.id.split("-")[1];

    document.getElementById(`VPfavorite-${postId}`).classList.toggle("active");

    const favoriteCountSpan = document.querySelector(`#favorite-count-${postId}`);
    const VPfavoriteCountSpan = document.querySelector(`#VPfavorite-count-${postId}`);

    const csrftoken = getCookie("csrftoken");

    fetch(`/heart_interaction/${user.id}/${postId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrftoken,
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data, "lo");
        favoriteCountSpan.textContent = data.total_favorites === 0 ? "" : data.total_favorites;
        VPfavoriteCountSpan.textContent = data.total_favorites === 0 ? "" : data.total_favorites;
      })
      .catch((error) => {
        console.error("Error updating like count:", error);
      });
  });
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
