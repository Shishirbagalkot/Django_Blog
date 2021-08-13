from django.shortcuts import render

posts = [
    {
        'author': 'Shishir B',
        'title': 'Blog post 1',
        'content': 'First hardcoded post',
        'date_posted': 'Aug 12, 2021'
    },
    {
        'author': 'Shishir B',
        'title': 'Blog post 2',
        'content': 'Second hardcoded post',
        'date_posted': 'Aug 13, 2021'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': "Home"
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'blog/about.html', context)
