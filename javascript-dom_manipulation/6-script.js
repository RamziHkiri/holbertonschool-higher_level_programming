character = document.getElementById("character");

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    char_name = data.name;

    character.innerHTML = char_name;
  });
