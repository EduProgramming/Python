document
  .getElementById("toggle-dark-btn")
  .addEventListener("click", ({ target }) => {
    if (document.body.classList.contains("dark-mode")) {
      document.body.classList.remove("dark-mode");
      document.body.classList.add("light-mode");
      target.src = "../static/night.svg";
    } else {
      document.body.classList.remove("light-mode");
      document.body.classList.add("dark-mode");
      target.src = "../static/light.svg";
    }
  });
