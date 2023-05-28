from django.shortcuts import render
from django.http import HttpResponse
import json

def families(request, fam_id):
    with open('info/animal_json.json') as file:
        data = json.load(file)
    
    
    context = {}
    context['animal_list'] = []
    for animal in data['animals']:
        if animal['family'] == int(fam_id):
            context['animal_list'].append(animal['name'])
    
    return render(request, 'family.html', context)


def animals(request, animal_id):
    with open('info/animal_json.json') as file:
        data = json.load(file)
    
    for animal in data['animals']:
        if animal['id'] == int(animal_id):
            animal_info = {"Name": animal['name'],
                           "Legs": animal['legs'],
                            "Weight": animal['weight'],
                            "Height": animal['height'],
                             "Speed": animal['speed']}
    return render(request, 'animal.html', animal_info)