let n = 0
var imageDisplay = document.getElementsByClassName('caravan_image')[n];

imageDisplay.style.display = "inline-block";
let previousImage = document.getElementById('left');
let nextImage = document.getElementById('right');
let imageParent = document.getElementById('host');

nextImage.addEventListener('click',nextpic);
previousImage.addEventListener('click',lastpic);

function nextpic(){
    n = n+1
    if (n === 15){
        n = 15-n;
    };
    console.log(n)
    imageDisplay.style.display="none";
    imageDisplay = imageParent.children[n];
    imageDisplay.style.display="block";
}

function lastpic(){
    n = n - 1
    if (n === 0-1){
        n = 15+n;
    };
    imageDisplay.style.display="none";
    imageDisplay = imageParent.children[n];
    imageDisplay.style.display="block";
}