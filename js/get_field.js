const button = document.getElementById("graph");
button.addEventListener("click", e => {
    document.getElementById("img").src = "";
    const fx = document.getElementById("Fx").value;
    const fy = document.getElementById("Fy").value;
    const skip = document.getElementById("skip").value;
    const bounds = document.getElementById("bounds").value;
    const url = "https://vector-field.herokuapp.com/?fx=" + fx + "&fy=" + fy + "&skip=" + skip + "&bounds=" + bounds;
    console.log(url);
    document.getElementById("img").src = url;
});
const button2 = document.getElementById("read");
button2.addEventListener("click", e => {
  const dots = document.getElementById("dots");
  const moreText = document.getElementById("more");
  if (dots.style.display === "none") {
    dots.style.display = "inline";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    moreText.style.display = "inline";
  }
});
const button3 = document.getElementById("calc");
button3.addEventListener("click", e => {
  const dots = document.getElementById("dots2");
  const moreText = document.getElementById("more2");
  if (dots.style.display === "none") {
    dots.style.display = "inline";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    moreText.style.display = "inline";
  }
});
