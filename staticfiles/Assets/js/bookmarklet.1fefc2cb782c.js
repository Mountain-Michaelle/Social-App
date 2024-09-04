const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/Assets/scss/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;


//Load CSS
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random()*9999999999999999);
head.appendChild(link);


// Load HTML
var body = document.getElementsByTagName('body')[0];
boxHtml = 
`
<div id="bookmarklet">
 <a href="#" id="close">&times;</a> 
    <h1>Select an image to bookmark:</h1>
    <div class="images"></div
 </div>
`;
body.innerHTML += boxHtml;


function bookmarkletLaunch() {
    bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images');
    // clear images found
    imagesFound.innerHTML = '';
    // display bookmarklet
    bookmarklet.style.display = 'block';
    // close event
    bookmarklet.querySelector('#close')
    .addEventListener('click', function(){
    bookmarklet.style.display = 'none'
    });


// find images in the DOM with the minimum dimensions
images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"],img[src$=".png"]');
images.forEach(image => {
if(image.naturalWidth >= minWidth
&& image.naturalHeight >= minHeight)
{
var imageFound = document.createElement('img');
imageFound.src = image.src;
imagesFound.append(imageFound);
}
})
}
// launch the bookmkarklet
bookmarkletLaunch();