function accion(source) {
    location.href = source;
}
function lab(e,label) {
    let lab = document.querySelector(label);
    e.placeholder = "";
    lab.style.opacity = "1";
    e.addEventListener('focusout',()=>{
        if (e.value != "") {
            e.placeholder = "";
            lab.style.opacity = "1";
        }
        else {
            e.placeholder = lab.innerText;
            lab.style.opacity = "0";
        }
    });
}
function show_password(e,inp) {
    let entrada = document.querySelector(inp);
    if (entrada.type == "password") {
        e.src = "../static/assets/images/SVGS/eye2.svg";
        entrada.type = "text";
    }
    else {
        e.src = "../static/assets/images/SVGS/eye1.svg";
        entrada.type = "password";
    }
}
function embed(e,ventana,curso){
    document.querySelector(ventana).src = curso;
}
function chk(e){
    if (e.checked){
        e.value = "SI"
    }
    else {
        e.value = "NO"
    }
}