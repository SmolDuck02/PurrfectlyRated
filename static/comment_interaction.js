const commentButtons = document.querySelectorAll(".fa-solid.fa-comment.fa-lg");
commentButtons.forEach((button) => {
  button.addEventListener("click", (event) => {
    event.stopPropagation();
    const clickedId = event.target.id;
    const postId = clickedId.split("-")[1];

    //another approach - tedious
    // const post = document.getElementById(`reviewPostContainer-${postId}`).getAttribute("data");

    //if there is ID, then proceed
    if (clickedId) {
      const divvy = document.getElementById(`viewPostDivBackground-${postId}`);
      divvy.style.display = "flex";
      console.log(divvy);
      // document.querySelector(".viewPostDivBackground").style.display = "flex";
    }
  });
});

const submitCommentButtons = document.querySelectorAll(".submit-comment-button");
submitCommentButtons.forEach((button) => {
  button.addEventListener("click", (event) => {
    event.stopPropagation();
    const csrftoken = getCookie("csrftoken");
    const postId = button.id.split("-")[3];

    console.log(`/add_comment/{{ user.id }}/${postId}/`, event.target.id);

    const commentElement = document.getElementById(`commentInput-${postId}`);
    const commentValue = commentElement.value;

    console.log(commentElement, commentValue);

    if (commentValue != "") {
      console.log("yolo");

      fetch(`/add_comment/{{ user.id }}/${postId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ comment_text: commentValue }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("the data", data);

          // Append the new comment to the comments section
          const originalCommentDiv = document.querySelector(".commentContain");
          const clonedCommentDiv = originalCommentDiv.cloneNode(true);
          clonedCommentDiv.id = "clonedParent"; // Change the ID to avoid duplicates

          const pChildElements = clonedCommentDiv.getElementsByTagName("p");
          const buttonChildElements = clonedCommentDiv.getElementsByTagName("button");
          const inputChildElements = clonedCommentDiv.getElementsByTagName("input");

          pChildElements[0].innerText = data.comment_username;
          //pChildElements[1] does not need to change

          pChildElements[2].innerText = data.datetime_now;

          buttonChildElements[0].id = `reply-comment-${data.new_comment.id}`;
          buttonChildElements[1].id = `edit-comment-${data.new_comment.id}`;
          buttonChildElements[2].id = `delete-comment-${data.new_comment.id}`;

          inputChildElements[0].id = `userCommentInput-${data.new_comment.id}`;
          inputChildElements[0].attributes[6].textContent = `${data.new_comment.comment_description}`;

          const container = document.getElementById(
            `actualCommentsContainer-${data.new_comment.post}`
          );
          console.log("kis", container);
          container.appendChild(clonedCommentDiv);

          assignReplyFunction();
          assignEditFunction();
          assignDeleteFunction();

          //scroll to the bottom of div
          container.scrollTo(0, container.scrollHeight);
        })
        .catch((error) => {
          console.error("Error adding comment ( :< ) :", error);
        });

      commentElement.value = "";
    }
  });
});

function assignReplyFunction() {
  const replyCommentButtons = document.querySelectorAll(".reply-comment");
  replyCommentButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      event.stopPropagation();
      const clickedId = event.target.id;
      const replyId = clickedId.split("-")[2];

      console.log(replyId, "reply");

      // alert("Reply saved! AHAHAHAHAHH");

      // Append the new comment to the comments section
      const originalCommentDiv = document.querySelector(".commentContain");
      const clonedCommentDiv = originalCommentDiv.cloneNode(true);
      clonedCommentDiv.id = "clonedParent"; // Change the ID to avoid duplicates

      const pChildElements = clonedCommentDiv.getElementsByTagName("p");

      const commentsDetailsDiv = clonedCommentDiv.querySelector(".detailsDiv");

      console.log("this is comments", commentsDetailsDiv);
      const buttonChildElements = clonedCommentDiv.getElementsByTagName("button");
      const inputChildElements = clonedCommentDiv.getElementsByTagName("input");

      const replyDetailsDiv = commentsDetailsDiv.cloneNode(true);

      pChildElements[0].innerText = user_list[0][1];

      // reset the replyDetailsDiv since it's a copy of commentsDetailsDiv
      for (let i = replyDetailsDiv.childElementCount - 1; i >= 0; i--) {
        replyDetailsDiv.removeChild(replyDetailsDiv.children[i]);
      }

      let saveReplyButton = buttonChildElements[0].cloneNode(true);
      saveReplyButton.id = `save-reply-${replyId}`;
      saveReplyButton.innerText = "Save";

      let cancelReplyButton = buttonChildElements[0].cloneNode(true);
      cancelReplyButton.id = `cancel-reply-${replyId}`;
      cancelReplyButton.innerText = "Cancel";

      replyDetailsDiv.appendChild(saveReplyButton);
      replyDetailsDiv.appendChild(cancelReplyButton);

      inputChildElements[0].id = `userReplyInput-${replyId}`;
      inputChildElements[0].attributes[6].value = "";
      inputChildElements[0].placeholder = "Reply to {{ user.username|title}}...";
      inputChildElements[0].removeAttribute("disabled");

      clonedCommentDiv.appendChild(replyDetailsDiv);
      clonedCommentDiv.removeChild(commentsDetailsDiv);

      let childElement = button;

      while (
        childElement.parentElement &&
        !childElement.parentElement.classList.contains("commentsParentDiv")
      ) {
        console.log(childElement.parentElement.classList);
        childElement = childElement.parentElement;
      }
      console.log("child", pChildElements, childElement, user_list);

      childElement.appendChild(clonedCommentDiv);

      // FUNCTIONS
      document.getElementById(`userReplyInput-${replyId}`).focus();
      document.getElementById(`save-reply-${replyId}`).addEventListener("click", (event) => {
        event.stopPropagation();

        const replyInput = document.getElementById(`userReplyInput-${replyId}`);

        const csrftoken = getCookie("csrftoken");

        if (replyInput.value) {
          fetch(`/add_reply/{{ user.id}}/${replyId}/`, {
            method: "POST",
            headers: {
              "X-CSRFToken": csrftoken,
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ reply_content: replyInput.value }),
          })
            .then((response) => response.json())
            .then((data) => {
              console.log("Reply saved!", data);
            })
            .catch((error) => {
              console.error("Error updating like count:", error);
            });

          replyInput.disabled = true;

          clonedCommentDiv.removeChild(replyDetailsDiv);

          let editReplyButton = document.getElementById(`edit-comment-${replyId}`);
          editReplyButton.id = `edit-reply-${replyId}`;
          editReplyButton.innerText = "Edit";

          let deleteReplyButton = document.getElementById(`delete-comment-${replyId}`);
          deleteReplyButton.id = `delete-reply-${replyId}`;
          deleteReplyButton.innerText = "Delete";

          commentsDetailsDiv.appendChild(editReplyButton);
          commentsDetailsDiv.appendChild(deleteReplyButton);

          clonedCommentDiv.appendChild(commentsDetailsDiv);
          console.log(commentsDetailsDiv);
        } else {
          alert("wow");
        }
      });

      document.getElementById(`cancel-reply-${replyId}`).addEventListener("click", (event) => {
        event.stopPropagation();
        childElement.removeChild(clonedCommentDiv);
      });
    });
  });
}
assignReplyFunction();

function assignEditFunction() {
  const editCommentButtons = document.querySelectorAll(".edit-comment");
  editCommentButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      event.stopPropagation();
      const clickedId = event.target.id;
      const commentId = clickedId.split("-")[2];

      console.log(commentId, "edittt");

      const commentDescriptionInput = document.getElementById(`userCommentInput-${commentId}`);

      if (button.textContent.trim() == "Edit") {
        commentDescriptionInput.removeAttribute("disabled");
        commentDescriptionInput.focus();
        button.textContent = "Save";
        console.log(button.textContent);
      } else if (button.textContent.trim() == "Save") {
        commentDescriptionInput.disabled = true;
        button.textContent = "Edit";
        console.log(button.textContent, commentDescriptionInput.value);

        const csrftoken = getCookie("csrftoken");

        fetch(`/edit_comment/${commentId}/`, {
          method: "POST",
          headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ newCommentDescription: commentDescriptionInput.value }),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("gregrgrgr", commentValue, data);
          })
          .catch((error) => {
            console.error("Error updating like count:", error);
          });
      }
    });
  });
}
assignEditFunction();

function assignDeleteFunction() {
  const deleteCommentButtons = document.querySelectorAll(".delete-comment");
  deleteCommentButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      event.stopPropagation();
      const clickedId = event.target.id;
      const commentId = clickedId.split("-")[2];

      const csrftoken = getCookie("csrftoken");

      fetch(`/delete_comment/${commentId}/`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": csrftoken,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("gregrgrgr", data);
        })
        .catch((error) => {
          console.error("Error updating like count:", error);
        });

      let childElement = document.getElementById(`userCommentInput-${commentId}`);
      let repliesContainer = button.parentElement.parentElement.parentElement.parentElement;
      let repliesElement = button.parentElement.parentElement.parentElement;

      const parentElement = childElement.parentElement.parentElement.parentElement;
      while (
        childElement.parentElement &&
        !childElement.parentElement.classList.contains("commentsParentDiv")
      ) {
        console.log(childElement.parentElement.classList);
        childElement = childElement.parentElement;
      }
      console.log("child", childElement, parentElement);

      console.log(commentId, repliesContainer, repliesElement, "bbababbb");
      if (repliesContainer) {
        repliesContainer.removeChild(repliesElement);
      } else {
        childElement.removeChild(parentElement);
      }
    });
  });
}
assignDeleteFunction();
