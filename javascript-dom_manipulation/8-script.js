
fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    hello_element = document.getElementById("hello");
    
    char_name = data.hello;

    hello_element.innerHTML = char_name;

  });