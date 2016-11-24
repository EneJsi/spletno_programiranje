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

function validate_polog(){
    var eur = document.forms["Form"]["polog_visina"].value;
    //var date = document.forms["Form"]["rokcilj"].value;
    
    validate_polog_euro(eur);
    //validate_datum(date)
return true;
}

function validate_strosek(){
    var eur = document.forms["Form"]["strosek_visina"].value;
    //var date = document.forms["Form"]["rokcilj"].value;
    alert("aa")
    validate_polog_euro(eur);
    //validate_datum(date)
return true;
}

function validate_polog_euro(vnos_euro){
    var isnum = /^\d+$/.test(vnos_euro);
    
    if (!isnum)
        {
        alert("Višina pologa so le številke");
        return false;
    }
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