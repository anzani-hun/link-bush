from django.shortcuts import render

from .models import MyLink
from django.contrib.auth.models import User
# Create your views here.


#ezeket fogjuk látni
# http://localhost:8000/page/admin
# http://localhost:8000/page/TesztElek
def getPageByUser(request, username):
    try:
        user = User.objects.get(username=username)
        if user is not None:
            links = MyLink.objects.filter(user = user, visible = True)
            return render(request, 'page.html', {'links':links })
    except Exception as e:
        return render(request, 'page.html', {'msg':str(e)})

def changeLinkVisibility(request):
    if request.method == 'POST':
        try:
            link_id = request.POST['link_id']
            checked = request.POST['checked']


            link = MyLink.objects.get(id = link_id)
            link.visible = checked
            link.save()
            return JsonResponse({'message':'Success'})
        except Exception as e:
            return JsonResponse({'message':str(e)})
    return JsonResponse({'message':'Only POST allowed!'})