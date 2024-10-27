from django.shortcuts import render, redirect
from .models import MyData

def submit_form(request):
    if request.method == 'POST':
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')

        submitted_data=MyData.objects.create(name1=name1, name2 = name2)
        return redirect('success', data_id=submitted_data.id)
    return render(request, 'home.html')

def success(request, data_id):
    data = MyData.objects.get(id = data_id)
    return render(request, 'result.html', {'data':data})
# Create your views here.
