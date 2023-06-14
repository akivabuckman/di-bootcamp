from django.shortcuts import render, redirect
from .forms import AdminForm
# Create your views here.

def admin_search(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')

            if phone_number:
                return redirect('person_by_phone', phone_number=phone_number)
            elif name:
                return redirect('person_by_name', name=name)
            elif email:
                return redirect('admin_app', email=email)
    else:
        form = AdminForm()

    return render(request, 'searchperson.html', {'form': form})