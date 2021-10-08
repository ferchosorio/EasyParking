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
function expCont(e,opciones,espacio){
    let opc = document.querySelector(opciones);
    let esp = document.querySelector(espacio);
    e.style.backgroundImage = "url(../static/assets/images/SVGS/right.svg)"
    e.style.left = "0%";
    e.style.borderRadius = "15% 50% 50% 15%";
    opc.style.width = "0%";
    esp.style.width = "100%";
    e.addEventListener('click',()=>{
        if (opc.style.width == "0%"){
            e.style.backgroundImage = "url(../static/assets/images/SVGS/left.svg)"
            e.style.left = "21%";
            e.style.borderRadius = "50%";
            opc.style.width = "23%";
            esp.style.width = "77%";
        }
        else {
            e.style.backgroundImage = "url(../static/assets/images/SVGS/right.svg)"
            e.style.left = "0%";
            e.style.borderRadius = "15% 50% 50% 15%";
            opc.style.width = "0%";
            esp.style.width = "100%";
        }
    });
}
setTimeout(()=>{
    if (document.querySelector(".passed") || document.querySelector(".noPassed")){
        location.href = "/principal";
    }
},4000);
function desWarn(r) {
    document.querySelector(r).style.display = "none";
}
function salidaV(vehiculo) {
    location.href = "/salidaVehiculo/"+vehiculo;
}