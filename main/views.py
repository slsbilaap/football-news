from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406353364',
        'name': 'Msy Aulya Salsabila Putri',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)