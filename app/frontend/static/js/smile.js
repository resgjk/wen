var smileys = document.getElementsByClassName('smiley');
var speed = 1;

function moveSmileys() {
    for (var i = 0; i < smileys.length; i++) {
        var smiley = smileys[i];
        var currentTop = parseFloat(smiley.style.top) || 0;
        if (currentTop > window.outerHeight + 70) {
            smiley.style.top = '0px';
        } else {
            smiley.style.top = currentTop + speed + 'px';
        }
    }
}

setInterval(moveSmileys, 1000/60);