function validate_strosek(){
    var eur = document.forms["Form"]["strosek_visina"].value;
    //var date = document.forms["Form"]["rokcilj"].value;

    validate_polog_euro(eur);
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