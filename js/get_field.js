const button = document.getElementById("graph");
button.addEventListener("click", e => {
    const fx = document.getElementById("Fx").value;
    const fy = document.getElementById("Fy").value;
    const skip = 1;
    const url = "https://vector-field.herokuapp.com/?fx=" + fx + "&fy=" + fy + "&skip=" + skip;
    document.getElementById("loading").innerHTML = "Loading ...";
    document.getElementById("img").src = url;
    document.getElementById("loading").innerHTML = "";

});
