from django.shortcuts import render, redirect 
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
from .forms import ContactForm 
from .forms import CVForm 
from .models import CV 

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")
        employed = request.POST.get("employed", "")
        if employed == 'on':
            employed = True
        else:
            employed = False
        profile = Profile(name=name, phone=phone, email=email, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills, employed=employed)
        profile.save()
    return render(request, 'pdf/accept.html')

def resume(request, id):
    user_profile= Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})
    options = {'page-size': 'Letter',
               'encoding': 'UTF-8',
               }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename ="resume_test.pdf"
    return response
    
def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles':profiles})

"""
def contact_view(request):
    if request.method == "POST": 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email'] 
            message = form.cleaned_data['message'] 
            # You can process the form data (e.g., save to DB, send an email) 
            return render(request, 'success.html', {'name': name}) 
    else: 
        form = ContactForm() 
    return render(request, 'contact.html', {'form': form}) 
"""
def contact_view(request): 
    if request.method == "POST": 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            form.save()  # Saves directly to the database 
            return redirect('success_page') 
    else: 
        form = ContactForm() 
    return render(request, 'pdf/contact.html', {'form': form}) 


def create_cv(request): 
    if request.method == "POST": 
        form = CVForm(request.POST, request.FILES)  # Handle file uploads 
        if form.is_valid(): 
            form.save() 
            #return redirect('cv_list')  # Redirect to CV listing page 
            return render(request, 'pdf/cv_list.html', {'cv_list': cv_list})
    else: 
        form = CVForm() 
    return render(request, 'pdf/cv_form.html', {'form': form}) 