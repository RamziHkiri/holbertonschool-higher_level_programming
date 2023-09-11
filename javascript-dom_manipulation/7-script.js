list_movies = document.getElementById("list_movies");
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    films = data.results;
    films.forEach(film => {
        new_item = document.createElement("li");
        new_item.textContent = film.title;
        list_movies.appendChild(new_item);
    });
  });