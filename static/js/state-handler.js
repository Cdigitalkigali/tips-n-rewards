var states = document.getElementsByClassName("state")

function switchState(from, to){
    states[from].style.display = "none"
    states[to].style.display = "block"
}
function loaderDisplay(){
    var loader = document.getElementById("loading-screen");
    loader.style.display = "block"
    const myTimeout = setTimeout(showPage(0), 5000);
    function showPage(page){
        loader.style.display = "none"
        states[page].style.display = "block";
    }
}