from django.shortcuts import render

books = [
    {   'title': 'Crime and Punishment',
        'author': 'Dostoyevskiy',
        'genre': 'Psychological romance',
        'publishing_year': '1201'
    },
    {
        'title': 'Три мушкетера',
        'author': 'Дюма',
        'genre': 'Приключенческий роман',
        'publishing_year': '1301'
    }
]

def home(request):
    context = {
        'books': books
    }
    return render(request, 'bookCatalog/home.html', context)

def about(request):
    return render(request, 'bookCatalog/about.html')


