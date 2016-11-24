narisi_prvi_del();

function narisi_prvi_del(){
    var c = document.getElementById("canv");
    var ctx = c.getContext("2d");
    ctx.moveTo(15,15);
    ctx.lineTo(15,130);
    ctx.stroke();
    ctx.moveTo(15,130);
    ctx.lineTo(270, 130);
    ctx.stroke();
}
