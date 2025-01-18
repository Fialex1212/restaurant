const popup = document.getElementById("popup");
const openPopupBtn = document.getElementById("openPopupBtn");
const closePopupBtn = document.getElementById("closePopupBtn");

// open popup
openPopupBtn.addEventListener("click", () => {
    popup.style.display = "block";
});

// click by cross
closePopupBtn.addEventListener("click", () => {
    popup.style.display = "none";
});

// close outside click
window.addEventListener("click", (event) => {
    if (event.target === popup) {
        popup.style.display = "none";
    }
});
