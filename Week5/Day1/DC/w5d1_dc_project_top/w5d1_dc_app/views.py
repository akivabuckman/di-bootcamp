from django.shortcuts import render

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def show_list(request):
    sorted_people = sorted(people, key=lambda x: x['age'])
    results = {}
    for index, value in enumerate(sorted_people):
        results[index] = value
    context = {}
    context['results'] = results
    return render(request, 'whole_list.html', context)

def show_person(request, id):
    for i in people:
        if i['id'] == int(id):
            context = i
    return render(request, 'one_person.html', context)
