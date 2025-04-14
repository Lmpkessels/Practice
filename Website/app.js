const openBtn = document.getElementById("open-btn");
const closeBtn = document.getElementById("close-btn");
const nav = document.querySelector(".right-nav");

// Initial state
closeBtn.style.display = "none";

// Toggle function
openBtn.addEventListener("click", () => {
  nav.classList.add("show-menu");
  openBtn.style.display = "none";
  closeBtn.style.display = "block";
});

closeBtn.addEventListener("click", () => {
  nav.classList.remove("show-menu");
  openBtn.style.display = "block";
  closeBtn.style.display = "none";
});
