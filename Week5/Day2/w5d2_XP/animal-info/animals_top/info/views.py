from django.shortcuts import render
from django.http import HttpResponse
from info.models import Family, Animal

def families(request, fam_id):
    all_animals = Animal.objects.all()
    
    context = {}
    context['animal_list'] = []
    for animal in all_animals:
        if animal.family_id == int(fam_id):
            context['animal_list'].append(animal.name)
    
    return render(request, 'family.html', context)


def animal(request, animal_id):
    all_animals = Animal.objects.all()
    for animal in all_animals:
        if animal.id == int(animal_id):
            animal_info = {"Name": animal.name,
                           "Legs": animal.legs,
                            "Weight": animal.weight,
                            "Height": animal.height,
                             "Speed": animal.speed}
    return render(request, 'animal.html', animal_info)

def animals(request):
    all_animals = Animal.objects.all()
    context = {'all': all_animals}
    return render(request, 'animals.html', context)
    
