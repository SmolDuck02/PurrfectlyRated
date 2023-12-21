// LISTENS FOR CLICKS ANYWHERE IN THE DOCUMENT

const currentURL = window.location.href;

const feedContentButton = document.getElementById("feedContentButton");
const feedContentDiv = document.querySelector(".allReviewPostsParent");

const productContentButton = document.getElementById("productContentButton");
const productContentDiv = document.querySelector(".allProductPostsParent");

function hideModal(id) {
  document.getElementById(id).style.display = "none";
  if (id == "addProductModal") {
    document.getElementById("addCategory").selectedIndex = 0;
  }
}
function confirmFromModal(id) {
  document.getElementById(id).style.display = "none";
}

function handleImagePicker(div) {
  const changeImageInput = div.querySelector('input[type="file"]');
  changeImageInput.click();

  changeImageInput.addEventListener("change", function () {
    const selectedFile = this.files[0];
    if (selectedFile) {
      const imageURL = URL.createObjectURL(selectedFile);
      div.style.backgroundImage = `url(${imageURL})`;
    }
  });
}


if (currentURL.endsWith("/feed/")) {
  document.getElementById("home-tab").classList.toggle("active");
  feedContentButton.classList.toggle("active");
  feedContentDiv.style.display = "flex";
  document.querySelector(".searchBarContainer").style.display = "flex";
} else if (currentURL.includes("product")) {
  document.getElementById("home-tab").classList.toggle("active");
  productContentButton.classList.toggle("active");
  productContentDiv.style.display = "flex";
  document.getElementById("productFiltersDiv").style.display = "flex";
  document.getElementById("addProductButton").style.display = "flex";
} else {
  feedContentDiv.style.display = "flex";
}
//
document.addEventListener("click", (event) => {
  // if (settingsDiv.classList.contains("active")) {
  //   settingsDiv.classList.toggle("active");
  //   for (const div of divElements) {
  //     div.classList.toggle("active");
  //   }
  // }

  // FOR THE VIEW POST POPOUT
  const viewPostParentDiv = document.querySelector(`.viewPostParentDiv`);
  if (viewPostParentDiv && !viewPostParentDiv.contains(event.target)) {
    viewPostParentDiv.parentElement.style.display = "none";
  }

  // FOR THE ADD REVIEW POST POPOUT
  const makeReviewForm = document.querySelector(".makeReviewForm");
  if (makeReviewForm && !makeReviewForm.contains(event.target)) {
    makeReviewDiv.style.display = "none";
  }
});
