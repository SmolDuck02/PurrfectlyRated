const userIcon = document.querySelector(".fa-user");
const userPopout = document.getElementById("user-popout");
const main = document.querySelector("main");
const nav = document.querySelector("nav");

userIcon.addEventListener("click", () => {
    userPopout.style.display = "block";
    nav.classList.add("blur-background");
    main.classList.add("blur-background");

    window.addEventListener("click", (e) => {
        if (e.target !== userIcon && e.target !== userPopout) {
            userPopout.style.display = "none";
            nav.classList.remove("blur-background");
            main.classList.remove("blur-background");
        }
    });
});
