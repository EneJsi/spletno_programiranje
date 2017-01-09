function validate_racun(){
    var eur = document.forms["Form"]["stanje"].value;
    var ime_racuna = document.forms["Form"]["ime_racuna"].value;
    //var date = document.forms["Form"]["rokcilj"].value;
    
    validate_ime_cilja(ime_racuna)
    validate_polog_euro(eur);
    //validate_datum(date)
return true;
}

function validate_polog_euro(vnos_euro){
    var isnum = /^\d+$/.test(vnos_euro);
    
    if (!isnum)
        {
        alert("Višina stanja na računu so lahko le številke");
        return false;
    }
}

function validate_ime_cilja(ime_racuna){
    var alphanum = /^[a-z0-9]+$/i.test(ime_racuna);
    
    if (!alphanum)
        {
        alert("Ime računa so lahko le alfanumerični znaki");
        return false;
    }
}