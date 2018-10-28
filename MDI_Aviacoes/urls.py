"""MDI_Aviacoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gerenciar.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #---------------LOGIN-------------------------------------------------
    path('admin/', admin.site.urls),
    path('autenticar/', do_login, name='autenticar'),
    path('area_interna/', area_interna, name='area_interna'),
    path('area_interna/sair', sair, name='sair'),
    #---------------CLIENTE---------------------------------------------------
    path('area_interna/cliente/cadastrar', cliente_cadastrar, name='cliente_cadastrar'),
    path('area_interna/cliente/salvar', cliente_salvar, name='cliente_salvar'),
    path('area_interna/cliente/alterar', cliente_alterar, name='cliente_alterar'),
    path('area_interna/cliente/buscar', cliente_buscar, name='cliente_buscar'),
    path('area_interna/cliente/excluir', cliente_excluir, name='cliente_excluir'),
    path("area_interna/cliente/finalizar_excluir",cliente_finalizarexcluxao, name='cliente_finalizar_excluir'),
   
    #---------------AEROPORTO---------------------------------------------
    path('area_interna/aeroporto/cadastrar', aeroporto_cadastrar, name='aeroporto_cadastrar'),
    path('area_interna/aeroporto/salvar', aeroporto_salvar, name='aeroporto_salvar'),
    path('area_interna/aeroporto/alterar', aeroporto_alterar, name='aeroporto_alterar'),
    path('area_interna/aeroporto/buscar', aeroporto_buscar, name='aeroporto_buscar'),
    path('area_interna/aeroporto/excluir', aeroporto_excluir, name='aeroporto_excluir'),
    path("area_interna/aeroporto/finalizar_excluir",aeroporto_finalizarexcluxao, name='aeroporto_finalizar_excluir'),
    path('area_interna/aeroporto/relatorio',aeroporto_relatorio, name='aeroporto_relatorio'),
    path('area_interna/aeroporto/relatorio', aeroporto_relatorio, name='aeroporto_relatorio'),
    #---------------AERONAVE---------------------------------------------
    path('area_interna/aeronave/cadastrar', aeronave_cadastrar, name='aeronave_cadastrar'),
    path('area_interna/aeronave/salvar', aeronave_salvar, name='aeronave_salvar'),
    path('area_interna/aeronave/alterar', aeronave_alterar, name='aeronave_alterar'),
    path('area_interna/aeronave/buscar', aeronave_buscar, name='aeronave_buscar'),
    path('area_interna/aeronave/excluir', aeronave_excluir, name='aeronave_excluir'),
    path('area_interna/aeronave/finalizar_excluir',aeronave_finalizarexcluxao, name='aeronave_finalizar_excluir'),
    path('area_interna/aeronave/relatorio', aeronave_relatorio, name='aeronave_relatorio'),
    #---------------PILOTO-----------------------------------------------
    path('area_interna/piloto/cadastrar', piloto_cadastrar, name='piloto_cadastrar'),
    path('area_interna/piloto/salvar', piloto_salvar, name='piloto_salvar'),
    path('area_interna/piloto/alterar', piloto_alterar, name='piloto_alterar'),
    path('area_interna/piloto/buscar', piloto_buscar, name='piloto_buscar'),
    path('area_interna/piloto/excluir', piloto_excluir, name='piloto_excluir'),
    path('area_interna/piloto/finalizar_excluir',piloto_finalizarexcluxao, name='piloto_finalizar_excluir'),
    path('area_interna/piloto/relatorio', piloto_relatorio, name='piloto_relatorio'),
    #---------------VOO-----------------------------------------------
    path('area_interna/voo/cadastrar', voo_cadastrar, name='voo_cadastrar'),
    path('area_interna/voo/salvar', voo_salvar, name='voo_salvar'),
    path('area_interna/voo/alterar', voo_alterar, name='voo_alterar'),
    path('area_interna/voo/buscar', voo_buscar, name='voo_buscar'),
    path('area_interna/voo/excluir', voo_excluir, name='voo_excluir'),
    path('area_interna/voo/finalizar_excluir',voo_finalizarexcluxao, name='voo_finalizar_excluir'),
    path('area_interna/voo/relatorio', voo_relatorio, name='voo_relatorio'),
    #---------------PASSAGENS-----------------------------------------------
    path('area_interna/passagen/cadastrar', passagen_cadastrar, name='passagen_cadastrar'),
    path('area_interna/passagen/salvar', passagen_salvar, name='passagen_salvar'),
    path('area_interna/passagen/alterar',passagen_alterar, name='passagen_alterar'),
    path('area_interna/passagem/buscar', passagem_buscar, name='passagem_buscar'),
    path('area_interna/passagen/excluir', passagen_excluir, name='passagen_excluir'),
    path('area_interna/passagem/finalizar_excluir',passagem_finalizarexcluxao, name='passagem_finalizar_excluir'),
     path('area_interna/passagen/relatorio', passagen_relatorio, name='passagen_relatorio'),


    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
