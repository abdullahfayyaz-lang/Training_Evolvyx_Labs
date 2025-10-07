from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Student
from .form import ContactForm,CustomerForm,StudentForm
# Create your views here.
def index(request):
    context={#its used to extract data from models and then pass it to templates
        "variable":"Enemy is on the website"
    }
    return render(request,"index.html",context)
#   return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is aboutpage")

def services(request):
    return HttpResponse("This is servicespage")

def contact(request):
    return HttpResponse("This is contactpage")



def contact_view(request):
    submitted = False  # flag to show success message

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (you can save to DB or send email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"📩 Message from {name} ({email}): {message}")  # just printing for now

            submitted = True
            form = ContactForm()  # reset form after submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})

def customer_view(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "✅ Customer added successfully!"
            form = CustomerForm()  # clear the form
            return render(request, 'customer_form.html', {'form': form, 'success_message': success_message})

    else:
        form = CustomerForm()

    return render(request, 'customer_form.html', {'form': form})



def student_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Student added successfully!"
            form = StudentForm() 
            context={'form': form, 'success_message': success_message} 
            return render(request, 'student_form.html', context)

    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})



def edit_student(request, id):
    # Fetch the student using the custom field 'student_id'
    student = get_object_or_404(Student, student_id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit_student.html', {
                'form': form,
                'student': student,
                'success_message': '✅ Student updated successfully!'
            })
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {
        'form': form,
        'student': student
    })
