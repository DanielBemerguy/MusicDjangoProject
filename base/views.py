from django.shortcuts import render
from .models import Author
# Create your views here.

# author = [
#     {'id':1, 'name': 'Music Home Page'},
#     {'id':2, 'name': 'Author information and discution'},
#     {'id':3, 'name': 'Title information and discution'},
#     {'id':4, 'name': 'Playlists'},
# ]


def home(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'base/home.html', context)

def author(request, pk):
    author = Author.objects.get(id=pk)
    context = {'author' : author}

    return render(request, "base/author.html", context)