// select the div element by ID
update_header = document.getElementById("update_header");
// select the header element 
header = document.querySelector("header");

update_header.addEventListener("click", () => {
    header.textContent = "New Header!!!";
});
