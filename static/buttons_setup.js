// PARSE THE JSON_SCRIPT
const interaction_list = JSON.parse(document.getElementById("interaction_toList").textContent);
const user_list = JSON.parse(document.getElementById("user_list").textContent);

interaction_list.map((interaction) => {
  const postId = interaction[2];

  const likeButtonId = "like-" + postId;
  const VPLikeButtonId = "VP" + likeButtonId;

  const dislikeButtonId = "dislike-" + postId;
  const VPDislikeButtonId = "VP" + dislikeButtonId;

  const favoriteButtonId = "favorite-" + postId;
  const VPFavoriteButtonId = "VP" + favoriteButtonId;

  console.log("buttons id", likeButtonId, dislikeButtonId, favoriteButtonId);

  const likeButton = document.getElementById(likeButtonId);
  const VPLikeButton = document.getElementById(VPLikeButtonId);

  const dislikeButton = document.getElementById(dislikeButtonId);
  const VPDislikeButton = document.getElementById(VPDislikeButtonId);

  const favoriteButton = document.getElementById(favoriteButtonId);
  const VPFavoriteButton = document.getElementById(VPFavoriteButtonId);

  if (interaction[4]) {
    likeButton.classList.toggle("active");
    VPLikeButton.classList.toggle("active");
  }
  if (interaction[5]) {
    dislikeButton.classList.toggle("active");
    VPDislikeButton.classList.toggle("active");
  }
  if (interaction[6]) {
    favoriteButton.classList.toggle("active");
    VPFavoriteButton.classList.toggle("active");
  }
});
