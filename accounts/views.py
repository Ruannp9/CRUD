from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registes.html', {'form': form})
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        form = UserCreationForm(request.POST)
        
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request,'registro/registes.html', {'form': form})
        if form.is_valid():
            user = form.save(commit=False)
            user.username = username
            user.email = email
            user.set_password(password1)
            user.save()
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect(reverse_lazy('login'))
        
        else:
            #Adiciona mensagens de erro se o formulário não for válido
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
        return render(request, 'registro/registes.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return render(request, 'registro/login.html')

    return render(request, 'registro/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
                    