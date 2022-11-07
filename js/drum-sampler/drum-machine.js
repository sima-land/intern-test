var btnA = document.getElementById('btnA')
var btnS = document.getElementById('btnS')
var btnD = document.getElementById('btnD')
var btnF = document.getElementById('btnF')
var btnG = document.getElementById('btnG')
var btnH = document.getElementById('btnH')
var btnJ = document.getElementById('btnJ')
var btnK = document.getElementById('btnK')
var btnL = document.getElementById('btnL')
var audioA = document.getElementById('audioA')
var audioS = document.getElementById('audioS')
var audioD = document.getElementById('audioD')
var audioF = document.getElementById('audioF')
var audioG = document.getElementById('audioG')
var audioH = document.getElementById('audioH')
var audioJ = document.getElementById('audioJ')
var audioK = document.getElementById('audioK')
var audioL = document.getElementById('audioL')

window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyA') {
        audioA.currentTime = 0;
        audioA.play();
        btnA.classList.add('playing')
    }
});

window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyS') {
        audioS.currentTime = 0;
        audioS.play();
        btnS.classList.add('playing')
    }
});
window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyD') {
        audioD.currentTime = 0;
        audioD.play();
        btnD.classList.add('playing')
    }
});
window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyF') {
        audioF.currentTime = 0;
        audioF.play();
        btnF.classList.add('playing')
    }
});
window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyG') {
        audioG.currentTime = 0;
        audioG.play();
        btnG.classList.add('playing')
    }
});
window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyH') {
        audioH.currentTime = 0;
        audioH.play();
        btnH.classList.add('playing')
    }
});
window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyJ') {
        audioJ.currentTime = 0;
        audioJ.play();
        btnJ.classList.add('playing')
    }
});
window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyK') {
        audioK.currentTime = 0;
        audioK.play();
        btnK.classList.add('playing')
    }
});
window.addEventListener("keydown", function(event) {
    if(event.code == 'KeyL') {
        audioL.currentTime = 0;
        audioL.play();
        btnL.classList.add('playing')
    }
});

window.addEventListener('keyup', function(){
    btnA.classList.remove('playing')
    btnS.classList.remove('playing')
    btnD.classList.remove('playing')
    btnF.classList.remove('playing')
    btnG.classList.remove('playing')
    btnH.classList.remove('playing')
    btnJ.classList.remove('playing')
    btnK.classList.remove('playing')
    btnL.classList.remove('playing')
})
