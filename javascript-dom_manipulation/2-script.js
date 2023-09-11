// select the red_header element by ID
redHeader = document.getElementById("red_header");
// select the header element 
header = document.querySelector("header");

//add event listener to the redhead element
redHeader.addEventListener("click", () => {
// add the class red to the selected element header
  header.classList.add("red");
});





