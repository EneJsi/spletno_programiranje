function validate_polog(){
    var eur = document.forms["Form"]["polog_visina"].value;
    //var date = document.forms["Form"]["rokcilj"].value;

    validate_polog_euro(eur);
    //validate_datum(date)
return true;
}


function validate_polog_euro(vnos_euro){
    var isnum = /^\d+$/.test(vnos_euro);
    
    if (!isnum)
        {
        alert("Višina pologa so lahko le številke");
        return false;
    }
}