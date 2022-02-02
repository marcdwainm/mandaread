$(document).ready(function(){
    hidden = true;

    $("#logout-btn").on("click", function(){
        if(hidden){
            $("#logout-dropdown").removeClass("d-none").addClass("d-flex");
            hidden = false
        }
        else{
            $("#logout-dropdown").removeClass("d-flex").addClass("d-none");
            hidden = true
        }
    })


    $("#cancel-logout").on('click', function(){
        $("#logout-dropdown").removeClass("d-flex").addClass("d-none");
        hidden = true
    })
})