from django.shortcuts import render

from hatseller.forms import MyLoginForm


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
