const url = "http://localhost:5000";
const routes = ["/users", "/likes"];

console.log(url + routes[0]);

axios
  .get(url + routes[0])
  .then((res) => {
    const main = document.getElementById("main");

    res.data.map((data) => {
      div = document.createElement("div");
      div.classList.add("name");
      div.innerText = data.name;
      main.appendChild(div);
    });
  })
  .catch((err) => {
    console.error(err);
  });
