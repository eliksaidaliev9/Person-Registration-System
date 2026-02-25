from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Person


def main(request):
    if request.POST:
        model = Person()
        model.first_name = request.POST.get('first_name','')
        model.last_name = request.POST.get('last_name','')
        model.company = request.POST.get('company', '')
        model.email = request.POST.get('email', '')
        model.phone = request.POST.get('area_code', '') + request.POST.get('phone', '')
        model.course_type = request.POST.get('course_type', '')
        model.subject = request.POST.get('subject', '')
        model.exist = request.POST.get('exist', '')
        model.save()
        print(request.POST)
        return redirect("persons-list")
    return render(request,'index.html')


def persons_list(request):
    persons = Person.objects.all().order_by('id')
    p_list = "<h1>Persons list:</h1><ol>"
    for p in persons:
        p_list += (
            f"<li>First_name: {p.first_name}, "
            f"Last_name: {p.last_name}, "
            f"Company: {p.company}, "
            f"Email: {p.email}, "
            f"Phone: {p.phone}, "
            f"Exist: {p.exist}</li> "
        )
    p_list += "</ol>"
    return HttpResponse(p_list, content_type="text/html")


