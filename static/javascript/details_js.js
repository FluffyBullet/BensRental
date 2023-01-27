// Looping through photo's on details.hmtl page

let n = 0;
var activePhoto = document.getElementsByClassName('picture')[n];
activePhoto.getElementsByClassName.display = 'block';
let photoParent = document.getElementById('images');
let nextPhoto = document.getElementById('left');
let lastPhoto = document.getElementById('right');

nextPhoto.addEventListener('click', nextImage);
function nextImage(){
    n = n + 1;
    if (n === 14){
        n = 14 - n;
    }
    activePhoto.getElementsByClassName.display='none';
    activePhoto = photoParent.children[n];
    activePhoto.style.display = 'block'; 
}

lastPhoto.addEventListener('click', lastImage);
function lastImage(){
    n = n - 1;
    if (n === 0-1){
        n = 14;
    }
    activePhoto.getElementsByClassName.display='none';
    activePhoto = photoParent.children[n];
    activePhoto.style.display = 'block'; 
}