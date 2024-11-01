
from django.shortcuts import render, redirect
from .models import Time_Futebol
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



@login_required
def time_list(request):
    times = Time_Futebol.objects.all()
    return render(request, 'times/times_lista.html', {'times': times})

@login_required
def time_add(request):
    if request.method == 'POST':
      nome_time = request.POST.get('nome_time')
      tecnico_time = request.POST.get('tecnico_time')
      data_criacao = request.POST.get('data_criacao')
      Mascote = request.POST.get('Mascote')
        
      if nome_time:
          Time_Futebol.objects.create(
              nome_time=nome_time,
              tecnico_time =tecnico_time,
              data_criacao =data_criacao,
              Mascote =Mascote,
              
              )  
      return redirect('times_lista')
    return render(request, 'times/times_ad.html')  
    
# Create your views here.
