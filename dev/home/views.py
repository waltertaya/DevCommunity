from django.shortcuts import render
from .models import Post

posts = [
    {'author': '',
     'title': '',
     'content': '',
     'date_posted': ''
     },
    {'author': '',
     'title': '',
     'content': '',
     'date_posted': ''
     },
    {'author': '',
     'title': '',
     'content': '',
     'date_posted': ''
     },
    {'author': '',
     'title': '',
     'content': '',
     'date_posted': ''
     }
]

def home_page(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'home.html', context)
