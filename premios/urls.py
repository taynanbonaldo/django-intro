from django.urls import path
from premios.views import premios, premio

app_name = "premios"

urlpatterns = [
    path("", premios, name="lista"),
    path("<str:sigla>/", premio, name="premio")
]