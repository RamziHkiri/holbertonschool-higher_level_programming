// select the div element by ID
add_item = document.getElementById("add_item");
// select the header element 
my_list = document.querySelector(".my_list");

add_item.addEventListener("click", () => {
    new_item = document.createElement("li");
    new_item.textContent = "Item";
    my_list.appendChild(new_item);
});