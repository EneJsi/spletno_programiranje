function validate_cilj(){
    var eur = document.forms["Form"]["visina_cilj"].value;
    var ime_cilja = document.forms["Form"]["ime_cilj"].value;
    //var date = document.forms["Form"]["rokcilj"].value;
    if(eur != "")
        validate_polog_euro(eur);
    if(ime_cilja != ""){
        validate_ime_cilja(ime_cilja);
    }
    
    //validate_datum(date)
return true;
}

function validate_polog_euro(vnos_euro){
    var isnum = /^\d+$/.test(vnos_euro);
    
    if (!isnum)
        {
        alert("Višina stroška so lahko le številke");
        return false;
    }
}

function validate_ime_cilja(ime_cilja){
    var alphanum = /^[a-z0-9]+$/i.test(ime_cilja);
    
    if (!alphanum)
        {
        alert("Ime cilja so lahko le alfanumerični znaki");
        return false;
    }
}