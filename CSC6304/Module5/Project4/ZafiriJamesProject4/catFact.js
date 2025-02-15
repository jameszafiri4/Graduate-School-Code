/* I received the free API from the website in the slides. Please see link below:
https://apilist.fun/api/cat-facts

Documentation links also below:
https://alexwohlbruck.github.io/cat-facts/docs/
https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html

PLEASE NOTE:
You may have to click the button a few times to receive an actual good fact. Some
people have entered bad facts.
For example:
One click may get you a good fact like this: "Cats and kittens should be acquired in
pairs whenever possible as cat families interact best in pairs." or "The Egyptian Mau
is the oldest breed of cat, and is the fastest pedigreed cat."
While another can get you: "Cat is lazy." or "La al aldklofslc,nsksls."
*/

document.getElementById('get-fact').addEventListener('click', getCatFact);

function getCatFact() {
    fetch('https://cat-fact.herokuapp.com/facts/random')
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            displayCatFact(data);
        })
        .catch(function(error) {
            console.log(error);
        });
}

function displayCatFact(data) {
    var factInfo = document.getElementById('fact-info');
    factInfo.innerHTML = '';
    
    if (data && data.text) {
        var fact = data.text;
        var factHtml = '<p>' + fact + '</p>';
        factInfo.innerHTML = factHtml;

        var imageUrl = 'cat_image.jpg';
        var imageHtml = '<img id="cat-image" src="' + imageUrl + '" alt="Cat Image">';
        factInfo.insertAdjacentHTML('beforeend', imageHtml);

    } else {
        factInfo.innerHTML = '<p>Failed to retrieve cat fact.</p>';
    }
}
