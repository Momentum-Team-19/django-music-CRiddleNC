// otheralbums.js
var otherAlbums = document.querySelectorAll('.otherAlbums');

if (otherAlbums.length === 0) {
    var otherAlbumsContainer = document.querySelector('.otherAlbumsContainer');
    if (otherAlbumsContainer) {
        otherAlbumsContainer.style.display = 'none'
    }
}