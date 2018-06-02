$('.carousel').carousel({
    interval: 2000
})


var colorWell;
var defaultColor = "#0000ff";

function Init(){
    document.getElementById("iframe_redactor").contentWindow.document.designMode = "On";
}

function doStyle(style) {
    if (style === 'foreColor'){
        colorWell = document.querySelector("#colorWell");
        document.getElementById("iframe_redactor").contentWindow.document.execCommand(style, false, colorWell.value);
    }
    else{
        document.getElementById("iframe_redactor").contentWindow.document.execCommand(style, false, null);
    }
}

function Case(cs) {
    if (cs == 'lower'){
        document.getElementById("iframe_redactor").contentWindow.document.body.innerHTML = document.getElementById("iframe_redactor").contentWindow.document.body.innerHTML.toLowerCase()
    }
    else{
        document.getElementById("iframe_redactor").contentWindow.document.body.innerHTML = document.getElementById("iframe_redactor").contentWindow.document.body.innerHTML.toUpperCase();
    }

}