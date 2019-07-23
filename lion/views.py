from django.shortcuts import render

# Create your views here.
def pagina_inicial(request):
    context = {"nome":"Lorrany", "gatos":["Harry", "Melinha", "Max", "Bichento", "Cat"]}
    return render(request, 'index.html', context)
