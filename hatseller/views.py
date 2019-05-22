from django.shortcuts import render, redirect

from hatseller.forms import MyLoginForm, RegisterForm

from django.contrib.auth.models import User

def index(request):
    context = {
        'page_title': 'Hat Seller',
    }

    return render(request, 'hatseller/index.html', context=context)


def my_login(request):
    context = {}
    if request.method == 'POST':
        form = MyLoginForm(request.POST)
    else:
        form = MyLoginForm()
        next_url = request.GET.get('next')
        context['form'] = form
        if next_url:
            context['next_url'] = next_url

    context['form'] = form
    return render(request, 'hatseller/login.html', context=context)

def register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.pop('password')
            user = User(**form.cleaned_data)
            user.set_password(password)
            user.save()
            return redirect('views.index', context=context)
    else:
        form = RegisterForm()
    #     next_url = request.GET.get('next')
    #     context['form'] = form
    #     if next_url:
    #         context['next_url'] = next_url

    context['form'] = form
    return render(request, 'hatseller/register.html', context=context)