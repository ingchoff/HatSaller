from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hatseller.forms import MyLoginForm
from hatseller.models import hat


@login_required
def index(request):
    hat_list = hat.objects.all()
    context = {
        'page_title': 'Hat Seller',
        'hat_list': hat_list
    }

    return render(request, 'hatseller/index.html', context=context)


def my_login(request):
    context = {}
    if request.method == 'POST':
        form = MyLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                next_url = request.POST.get('next_url')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('index')

    else:
        form = MyLoginForm()
        next_url = request.GET.get('next')
        context['form'] = form
        if next_url:
            context['next_url'] = next_url

    context['form'] = form
    return render(request, 'hatseller/login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')
