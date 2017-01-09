
//==============================================

function do_canvas(pologi, stroski){
    var canvas = document.getElementById("graphec");
    var ctx = canvas.getContext("2d");
    
    var dnevi = [ "1", "2", "3", "4" , "5", "6", "7", "8", "9" , "10", "11", "12", "13", "14" , "15", "16", "17", "18", "19" , "20",
"21", "22", "23", "24" , "25", "26", "27", "28", "29" , "30", "31"];
        //850x640
    ctx.moveTo(40, 600);
    ctx.lineTo(800,600);
    ctx.stroke();
    
    ctx.moveTo(40, 600);
    ctx.lineTo(40, 50);
    ctx.stroke();
    
    var i;
    var x = 55, y = 620;
    //narisi dneve
    for(i in dnevi){
        ctx.fillText(i, x, y)
        x += 24;
    }
    x = 10, y = 550;
    //narisi eure
    for(i = 50; i <= 500; i = i + 50){
        ctx.fillText(i, x, y);
        narisi_crto(x+40, y, x+780, y, ctx)
        y = y - 50;
    }
    ctx.font="18px Georgia";
    ctx.fillText("[€]", 10, 45);
    
    ctx.font="18px Georgia";
    ctx.fillText("[Dan]", 800, 620);

    console.log(pologi)
    console.log(stroski)

    narisi_pologe(ctx, pologi)
    narisi_stroske(ctx, stroski)
}

function narisi_pologe(ctx, pologi){
    var x = 54, y = 600;
    var i;
    var visina;
    
    for(i in pologi){
        console.log(i)
        if(pologi[i] != 0){
            visina = pologi[i];
            splotaj_graf_polog(visina, x, y, ctx);
        }
        x += 24;
    }
}

function narisi_stroske(ctx, stroski){
    var x = 60, y = 600;
    var i;
    var visina;
    
    for(i in stroski){
        if(stroski[i] != 0){
            visina = stroski[i];
            splotaj_graf_strosek(visina, x, y, ctx);
        }
        x += 24;
    }
}

function splotaj_graf_polog(visina, x, y, ctx){
    ctx.beginPath();
    ctx.lineWidth = 7;
    ctx.strokeStyle = 'green';
    narisi_crto(x, y, x, y-visina, ctx);
}

function splotaj_graf_strosek(visina, x, y, ctx){
    ctx.beginPath();
    ctx.lineWidth = 7;
    ctx.strokeStyle = 'red';
    narisi_crto(x, y, x, y-visina, ctx);
}

function narisi_crto(x1, y1, x2, y2, ctx){
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}
//=========================================

function narisi_prvi_del(){
    
    var c = document.getElementById("graphec");
    var ctx = c.getContext("2d");
    ctx.moveTo(15,15);
    ctx.lineTo(15,130);
    ctx.stroke();
    ctx.moveTo(15,130);
    ctx.lineTo(270, 130);
    ctx.stroke();
}

function validate_datum(date){
    if(testDate(date)){
        alert("Zahtevan format za datum je 'DD.MM.YYYY'");
        return false;
    }
return true;
}

function testDate(date){
    var dateReg =  /^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$/;
    var t = date.match(dateReg)
    if(t===null)
        return false;   
    var d=+t[1], m=+t[2], y=+t[3];
        //za prvo silo
    if(m>=1 && m<=12 && d>=1 && d<=31){
        return true;  
     }
return false;
}