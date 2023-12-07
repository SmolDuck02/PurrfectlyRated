// LISTENS FOR CLICKS ANYWHERE IN THE DOCUMENT

const currentURL = window.location.href;

const feedContentButton = document.getElementById("feedContentButton");
const feedContentDiv = document.querySelector(".allReviewPostsParent");
feedContentButton.addEventListener("click", (event) => {
  event.stopPropagation();
  if (!currentURL.endsWith("feed")) {
    window.location.href = "/home/feed";
  }
});

const productContentButton = document.getElementById("productContentButton");
const productContentDiv = document.querySelector(".allProductPostsParent");
productContentButton.addEventListener("click", (event) => {
  event.stopPropagation();
  if (!currentURL.endsWith("product")) {
    window.location.href = "/home/product";
  }
});

const featuredDiv = document.querySelector(".featuredside");

//
if (currentURL.endsWith("/feed")) {
  document.getElementById("home-tab").classList.toggle("active");
  feedContentButton.classList.toggle("active");
  feedContentDiv.style.display = "flex";
  productContentDiv.style.display = "none";
  featuredDiv.style.display = "flex";
} else if (currentURL.endsWith("/product")) {
  document.getElementById("home-tab").classList.toggle("active");
  productContentButton.classList.toggle("active");
  feedContentDiv.style.display = "none";
  productContentDiv.style.display = "flex";
  featuredDiv.style.display = "flex";
} else if (currentURL.endsWith("/favorites/")) {
  document.getElementById("fav-tab").classList.toggle("active");
  featuredDiv.style.display = "flex";
} else if (currentURL.endsWith("/notifications/")) {
  document.getElementById("notif-tab").classList.toggle("active");
  featuredDiv.style.display = "none";
} else if (currentURL.endsWith("/about/")) {
  document.getElementById("about-tab").classList.toggle("active");
  featuredDiv.style.display = "none";
} else if (currentURL.endsWith("/team/")) {
  document.getElementById("team-tab").classList.toggle("active");
  featuredDiv.style.display = "none";
}

//
document.addEventListener("click", () => {
  if (settingsDiv.classList.contains("active")) {
    settingsDiv.classList.toggle("active");
    for (const div of divElements) {
      div.classList.toggle("active");
    }
  }

  // FOR THE VIEW POST POPOUT
  const viewPostDivs = document.querySelectorAll(`.viewPostDivBackground`);
  viewPostDivs.forEach((div) => {
    if (div.style.display != "none") {
      div.style.display = "none";
    }
  });

  // FOR THE ADD POST POPOUT
  if (makeReviewDiv.style.display != "none") {
    makeReviewDiv.style.display = "none";
  }
});
