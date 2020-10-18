from django.shortcuts import render
from premios.models import Premio

# Create your views here.
def premios(request):
    context = {
        "titulo": "Lista de Premios",
        "premios": Premio.objects.all()
    }
    return render(request, "premios.html", context)


def premio(request, sigla):
    premio = Premio.objects.get(sigla = sigla)

    context = {
        "premio":premio
    }
    return render(request, "premio.html", context)