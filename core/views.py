from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def olaMundo(request):
    return HttpResponse("<h1>Olá Mundo!</h1>")

def index(request):
    context = {
        "titulo": "Faculdade Impacta"
    }
    return render(request, "index.html", context)

def premio(request):
    context = {
        "titulo": "Lista de Premios",
        "premios": [
            {
                "nome": "Graduação em Análise e Desenvolvimento de Sistemas",
                "sigla": "ADS",
                "descricao": "Nota 4 na avaliação do ENADE/MEC - 1.º melhor curso da cidade de São Paulo."
            },
            {
                "nome": "Graduação em Administração",
                "sigla": "ADM",
                "descricao": "Nota 4 na avaliação do MEC – 10.ª maior nota entre as faculdades privadas da cidade de São Paulo. 3 estrelas na avaliação realizada pelo Guia do Estudante, da Editora Abril, que seleciona os melhores cursos para os estudantes que estão se preparando para o vestibular. Destaque no portal da Revista Exame como o curso que está entre os melhores do Brasil. (06/2017)"
            },
            {
                "nome": "Graduação em Redes de Computadores",
                "sigla": "RE",
                "descricao": "Nota 3 na avaliação do ENADE/MEC - 4.º melhor curso da cidade de São Paulo. "
            },
            {
                "nome": "Graduação em Sistemas da Informação",
                "sigla": "SI",
                "descricao": "Nota 4 na avaliação do ENADE/MEC - 3.º melhor curso da cidade de São Paulo."
            }
        ]
    }
    return render(request, "premios.html", context)