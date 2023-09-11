// select the red_header element by ID
toggle_header = document.getElementById("toggle_header");
// select the header element 
header = document.querySelector("header");

toggle_header.addEventListener("click", () => {
    // add the class red to the selected element header
    if (header.classList.contains("green")){
        header.classList.remove("green");
        header.classList.add("red");
    }
    else{
        header.classList.remove("red");
        header.classList.add("green");
    }
    });