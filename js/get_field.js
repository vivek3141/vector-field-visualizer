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
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("read");
  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Advanced";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Advanced";
    moreText.style.display = "inline";
  }
});
