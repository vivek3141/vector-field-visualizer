function makeHttpObject() {
    try {
        return new XMLHttpRequest();
    } catch (error) {
    }
    try {
        return new ActiveXObject("Msxml2.XMLHTTP");
    } catch (error) {
    }
    try {
        return new ActiveXObject("Microsoft.XMLHTTP");
    } catch (error) {
    }

    throw new Error("Could not create HTTP request object.");
}

const button = document.getElementById("graph");
button.addEventListener("click", e => {
    document.getElementById("img").src = "";
    document.getElementById("img").src="./img/loading.jpg";
    const fx = document.getElementById("Fx").value;
    const fy = document.getElementById("Fy").value;
    const skip = document.getElementById("skip").value;
    const bounds = document.getElementById("bounds").value;
    const url = "http://vectorfield.pythonanywhere.com/?fx=" + encodeURIComponent(fx) + "&fy=" + encodeURIComponent(fy) + "&skip=" + skip + "&bounds=" + bounds;
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
    console.log("HI");
    const moreText = document.getElementById("more2");
    moreText.style.display = "inline";
    const x = document.getElementById("x").value;
    const y = document.getElementById("y").value;
    const fx = document.getElementById("Fx").value;
    const fy = document.getElementById("Fy").value;
    const url = "https://vectorfield.pythonanywhere.com/divcurl?fx=" + encodeURIComponent(fx) + "&fy=" + encodeURIComponent(fy) + "&x=" + x + "&y=" + y;
    console.log(url);
    let request = makeHttpObject();
    request.open("GET", url, true);
    request.send(null);
    request.onreadystatechange = function () {
        if (request.readyState == 4)
            var text = request.responseText;
        document.getElementById("div").innerHTML = text;
    };
});

