from django.shortcuts import render

def index(request):
    context = {
        'page_title': 'Hat Seller',
    }

    return render(request, 'hatseller/index.html', context=context)
