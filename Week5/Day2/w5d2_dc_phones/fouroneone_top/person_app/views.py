from django.shortcuts import render
from person_app.models import Person

# Create a view /persons/phonenumber that will display all the info of a person depending on his phone number
# Create a view /persons/name that will display all the info of a person depending on his name.
# If there is no result either way, inform the user on the page.

def byphone(request, phone_number):
    all_people = Person.objects.all()
    if str(phone_number) in [str(i.phone_number) for i in all_people]:
        for i in all_people:
            if str(i.phone_number) == str(phone_number):
                context = {
                    'found': True,
                    'name': i.name,
                    'email': i.email,
                    'address': i.address,
                    'phone_number': i.phone_number
                    }
    else:
        context = {}
    
    return render(request, 'byphone.html', context)

def byname(request, name):
    all_people = Person.objects.all()
    if name in [str(i.name) for i in all_people]:
        for i in all_people:
            if i.name == name:
                context = {
                    'found': True,
                    'name': i.name,
                    'email': i.email,
                    'address': i.address,
                    'phone_number': i.phone_number
                    }
    else:
        context = {}
    
    return render(request, 'byname.html', context)
