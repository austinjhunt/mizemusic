from .models import * 
def authenticated_context(request): 
    #Meta.objects.all().delete()
    #Meta(site_title="Mize Music",navbar_title="Mize Music",footer_left="Jerry W. Mize is here to bring a little jazz into your life",
    #    column_left_color="bg-yankeesblue",column_mid_color="bg-upmaroon",column_right_color="bg-brownorange").save()
    site_title = Meta.objects.all()[0].site_title
    navbar_title = Meta.objects.all()[0].navbar_title
    footer_left = Meta.objects.all()[0].footer_left
    column_left_color = Meta.objects.all()[0].column_left_color
    column_mid_color = Meta.objects.all()[0].column_mid_color
    column_right_color = Meta.objects.all()[0].column_right_color
    

 
    return {
        'authenticated': request.user.is_authenticated,
        'site_title': site_title,
        'navbar_title':navbar_title,
        'footer_left': footer_left,
        'column_left_color': column_left_color,
        'column_mid_color': column_mid_color,
        'column_right_color': column_right_color,
        'superuser': request.user.is_superuser,
    }