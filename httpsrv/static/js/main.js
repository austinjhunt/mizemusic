var superuser; 
$(document).ready(function(){
    document.getElementById("navbar_title").addEventListener("input", function() {
        if (superuser){
            $.ajax({
                type: 'POST',
                url: '/update_title/',
                data: {
                    'new_title': $("#navbar_title").html()
                },
                success: function(){
                    document.title = $("#navbar_title").html();
                }
            })
        }
        else{
            console.log(superuser);
        }
    }, false);
    
});

