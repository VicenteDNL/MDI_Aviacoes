from django.shortcuts import render, redirect
from Gerenciar.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction


# Create your views here.

cliente=None
aeroporto=None
aeronave=None
piloto=None
voo=None
passagem=None

#---------------------LOGIN------------------------------------------------------------------------------

def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('usuario'), password=request.POST.get('senha'))
        if user is not None:
            login(request, user)
            return redirect('/area_interna')
    
    return render(request, 'login.html')        

@login_required
def area_interna(request):
    return render(request, 'base.html', context=None)

def sair(request):
    return render(request, 'login.html', context=None)
#--------------------------------------------------------------------------------------------------------

#---------------------CLIENTE----------------------------------------------------------------------------

def cliente_cadastrar(request):
    return render(request, 'criar_cliente.html', context=None)


def cliente_salvar(request):
    global cliente
    if cliente is None:
        cliente=Cliente()
        end=Endereco()
    else:
        end=Endereco.objects.get(id=cliente.id)
    cliente.nome = request.POST.get('nome_completo')
    cliente.cpf=request.POST.get('cpf')
    cliente.telefonecel=request.POST.get('telefone_cel')
    cliente.telefone=request.POST.get('telefone_res')
    cliente.email=request.POST.get('email')
    cliente.passaporte=request.POST.get('passaporte')
    
    
    end.rua=request.POST.get('rua')
    end.numero=request.POST.get('numero')
    end.cep=request.POST.get('cep')
    end.complemento=request.POST.get('complemento')
    end.bairro=request.POST.get('bairro')
    end.cidade=request.POST.get('cidade')
    end.estado=request.POST.get('estado')
    end.save()
    cliente.endereco=end
    cliente.save()
    cliente=None
    return redirect('/area_interna')

def cliente_alterar (request):
    lista_cliente=Cliente.objects.all()
    return render(request, 'buscar_cliente.html', context={'clientes':lista_cliente})

def cliente_buscar (request):
    global cliente
    clienteslc=request.POST.get('cliente_selecao')
    cliente=Cliente.objects.get(id=clienteslc)
    return render(request, 'alterar_cliente.html', context={'selecao':cliente})

def cliente_excluir(request):
    lista_cliente=Cliente.objects.all()
    return render(request, 'buscar_excluir_cliente.html', context={'clientes':lista_cliente})


def cliente_finalizarexcluxao(request):
    clienteslc=request.POST.get('cliente_selecao')
    cli=Cliente.objects.get(id=clienteslc)
    cli.delete()
    return redirect('/area_interna')
#-----------------------------------------------------------------------------------------



#--------------AEROPORTO-------------------------------------------------------------------
def aeroporto_cadastrar (request):
    return render(request, 'criar_aeroporto.html', context=None)


def aeroporto_salvar(request):
    global aeroporto
    if aeroporto is None:
        aeroporto=Aeroporto()
        end=Endereco()
    else:
        end=Endereco.objects.get(id=aeroporto.id)

    aeroporto.nome=request.POST.get('razao_social')
    aeroporto.cnpj=request.POST.get('cnpj')

    end.rua=request.POST.get('rua')
    end.numero=request.POST.get('numero')
    end.cep=request.POST.get('cep')
    end.complemento=request.POST.get('complemento')
    end.bairro=request.POST.get('bairro')
    end.cidade=request.POST.get('cidade')
    end.estado=request.POST.get('estado')
    end.save()
    aeroporto.endereco=end
    aeroporto.save()
    aeroporto=None
    return redirect('/area_interna')


def aeroporto_alterar(request):
    lista_aeroporto=Aeroporto.objects.all()
    return render(request, 'buscar_aeroporto.html', context={'aeroporto':lista_aeroporto})


def aeroporto_buscar (request):
    global aeroporto
    aeroportoslc=request.POST.get('cliente_selecao')
    aeroporto=Aeroporto.objects.get(id=aeroportoslc)
    return render(request, 'alterar_aeroporto.html', context={'selecao':aeroporto})

def aeroporto_excluir (request):
    lista_aeroporto=Aeroporto.objects.all()
    return render(request, 'buscar_excluir_aeroporto.html', context={'aeroporto':lista_aeroporto})


def aeroporto_finalizarexcluxao (request):
    aeroportoslc=request.POST.get('cliente_selecao')
    porto=Aeroporto.objects.get(id=aeroportoslc)
    porto.delete()
    return redirect('/area_interna')

def aeroporto_relatorio(request):
    lista_aeroporto=InfoAeroporto.objects.all()
    print(lista_aeroporto)
    return render(request, 'relatorio_aeroporto.html', context={'aeroporto':lista_aeroporto})

def aeroporto_relatorio(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM View_InfoAeroporto")
    result = []
    for row in cursor.fetchall():
        p=InfoAeroporto()
        p.nome=row[0]
        p.cnpj=row[1]
        p.rua=row[2]
        p.numero=row[3]
        p.cep=row[4]
        p.complemento=row[5]
        p.bairro=row[6]
        p.cidade=row[7]
        p.estado=row[8]
        result.append(p)
    return render(request, 'relatorio_aeroporto.html', context={'tudo':result})


#------------------------------------------------------------------------------------------


#--------------AERONAVE-------------------------------------------------------------------

def aeronave_cadastrar (request):
    return render(request, 'criar_aeronave.html', context=None)


def aeronave_salvar (request):
    cursor = connection.cursor()
    global aeronave
    if aeronave is None:
        modelo=request.POST.get('modelos')
        capacidadecarga=request.POST.get('capacidade_carga')
        autonomia=request.POST.get('autonomia')
        capacidadepassageiros=request.POST.get('capacidade_passageiros')
        cursor.execute("EXEC Stored_Aeronave 1,{},'{}',{},{},1".format(capacidadecarga, modelo, autonomia,capacidadepassageiros))
        

    aeronave=None
    return redirect('/area_interna')


def aeronave_alterar (request):
    lista_aeronave=Aeronave.objects.all()
    return render(request, 'buscar_aeronave.html', context={'aeronave':lista_aeronave})



def aeronave_buscar (request):
    global aeronave
    aeronaveslc=request.POST.get('cliente_selecao')
    aeronave=Aeronave.objects.get(id=aeronaveslc)
    return render(request, 'alterar_aeronave.html', context={'selecao':aeronave})

def aeronave_excluir(request):
    lista_aeronave=Aeronave.objects.all()
    return render(request, 'buscar_excluir_aeronave.html', context={'aeronave':lista_aeronave})


def aeronave_finalizarexcluxao (request):
    aeronaveslc=request.POST.get('cliente_selecao')
    nave=Aeronave.objects.get(id=aeronaveslc)
    nave.delete()
    return redirect('/area_interna')

def aeronave_relatorio (request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM View_Aeronave")
    result = []
    for row in cursor.fetchall():
        p=InfoAeronave()
        p.id=row[0]
        p.modelo=row[1]
        p.nomeAero=row[2]
        p.cnpj=row[3]
        p.vooid=row[4]
        result.append(p)
    return render(request, 'relatorio_aeronave.html', context={'tudo':result})


#------------------------------------------------------------------------------------------


#--------------PILOTOS---------------------------------------------------------------------

def piloto_cadastrar (request):
    return render(request, 'criar_piloto.html', context=None)

def piloto_salvar (request):
    global piloto
    if piloto is None:
        piloto=Piloto()
        end=Endereco()
    else:
        end=Endereco.objects.get(id=piloto.id)


    piloto.nome = request.POST.get('nome_completo')
    piloto.cpf=request.POST.get('cpf')
    piloto.nit= request.POST.get('nit')
    piloto.salario= request.POST.get('salario')
    piloto.dataentrada= request.POST.get('data_entrada')
    piloto.datasaida= request.POST.get('data_saida')
    piloto.breve= request.POST.get('breve')
    piloto.horasdevoo= request.POST.get('horas_voo')
    piloto.telefonecel=request.POST.get('telefone_cel')
    piloto.telefone=request.POST.get('telefone_res')
    piloto.email=request.POST.get('email')
    
    end.rua=request.POST.get('rua')
    end.numero=request.POST.get('numero')
    end.cep=request.POST.get('cep')
    end.complemento=request.POST.get('complemento')
    end.bairro=request.POST.get('bairro')
    end.cidade=request.POST.get('cidade')
    end.estado=request.POST.get('estado')
    end.save()
    piloto.endereco=end
    piloto.save()
    piloto=None
    return redirect('/area_interna')


def piloto_alterar (request): 
    lista_Piloto=Piloto.objects.all()
    return render(request, 'buscar_piloto.html', context={'piloto':lista_Piloto})


def piloto_buscar (request):
    global piloto
    pilotoslc=request.POST.get('cliente_selecao')
    piloto=Piloto.objects.get(id=pilotoslc)
    return render(request, 'alterar_piloto.html', context={'selecao':piloto})

def piloto_excluir (request):
    lista_piloto=Piloto.objects.all()
    return render(request, 'buscar_excluir_piloto.html', context={'piloto':lista_piloto})


def piloto_finalizarexcluxao(request):
    pilotoslc=request.POST.get('cliente_selecao')
    piloto=Piloto.objects.get(id=pilotoslc)
    piloto.delete()
    return redirect('/area_interna')

def piloto_relatorio (request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM View_InfoPiloto")
    result = []
    for row in cursor.fetchall():
        p=InfoPiloto()
        p.nome=row[0]
        p.id=row[1]
        p.breve=row[2]
        p.horasdevoo=row[3]
        p.salario=row[4]
        p.nit=row[5]
        result.append(p)
    return render(request, 'relatorio_piloto.html', context={'tudo':result})


#--------------VOO---------------------------------------------------------------------


def voo_cadastrar (request):
    lista_aeroporto=Aeroporto.objects.all()
    lista_piloto=Piloto.objects.all()
    lista_aeronave=Aeronave.objects.all()
    return render(request, 'criar_voo.html', context={'aeronave':lista_aeronave,'piloto':lista_piloto, 'local':lista_aeroporto})


def voo_salvar (request):
    global voo
    if voo is None:
        voo=Voo()

    saidaslc=request.POST.get('saida_selecao')
    saida=Aeroporto.objects.get(id=saidaslc)
    voo.saida=saida

    chegadaslc=request.POST.get('chegada_selecao')
    chegada=Aeroporto.objects.get(id=chegadaslc)
    voo.chegada=chegada

    aeronaveslc=request.POST.get('aeronave_selecao')
    getaeronave=Aeronave.objects.get(id=aeronaveslc)
    voo.aeronave=getaeronave

    pilotoslc=request.POST.get('piloto_selecao')
    getpiloto=Piloto.objects.get(id=pilotoslc)
    voo.piloto=getpiloto

    voo.duracaovoo=request.POST.get('duracao')
    voo.save()
    voo=None
    return redirect('/area_interna')

def voo_alterar (request):
    lista_voo=Voo.objects.all()
    return render(request, 'buscar_voo.html', context={'voo':lista_voo})


def voo_buscar (request):
    global voo
    lista_aeroporto=Aeroporto.objects.all()
    lista_piloto=Piloto.objects.all()
    lista_aeronave=Aeronave.objects.all()
    vooslc=request.POST.get('voo_selecao')
    voo=Voo.objects.get(id=vooslc)
    return render(request, 'alterar_voo.html',  context={'aeronave':lista_aeronave,'piloto':lista_piloto, 'local':lista_aeroporto})

def voo_excluir (request):
    lista_voo=Voo.objects.all()
    return render(request, 'buscar_excluir_voo.html', context={'voo':lista_voo})



def voo_finalizarexcluxao (request):
    vooslc=request.POST.get('voo_selecao')
    voo=Voo.objects.get(id=vooslc)
    voo.delete()
    return redirect('/area_interna')


def voo_relatorio (request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM View_Voo")
    result = []
    for row in cursor.fetchall():
        p=InfoVoo()
        p.aeroporto=row[0]
        p.nome=row[1]
        p.id=row[2]
        p.capacidadecarga=row[3]
        p.capacidadepassageiros=row[4]
        p.vooid=row[5]
        result.append(p)
    return render(request, 'relatorio_voo.html', context={'tudo':result})



#--------------PASSAGENS---------------------------------------------------------------------

def passagen_cadastrar (request):
    lista_voo=Voo.objects.all()
    lista_cliente=Cliente.objects.all()
    return render(request, 'criar_passagen.html', context={'cliente':lista_cliente,'voo':lista_voo})


def passagen_salvar(request):
    global passagem
    if passagem is None:
        passagem=Passagem()

    clienteslc=request.POST.get('cliente_selecao')
    cliente=Cliente.objects.get(id=clienteslc)
    passagem.cliente=cliente


    vooslc=request.POST.get('voo_selecao')
    voo=Voo.objects.get(id=vooslc)
    passagem.voo=voo

    passagem.poltrona=request.POST.get('poltrona')
    passagem.datap=request.POST.get('data_p')
    passagem.horariop=request.POST.get('hora_p')
    passagem.save()
    passagem=None
    return redirect('/area_interna')

def passagen_alterar (request):
    lista_passagem=Passagem.objects.all()
    return render(request, 'buscar_passagem.html', context={'passagem':lista_passagem})


def passagem_buscar(request):
    global passagem
    lista_voo=Voo.objects.all()
    lista_cliente=Cliente.objects.all()
    passagemslc=request.POST.get('passagem_selecao')
    passagem=Passagem.objects.get(id=passagemslc)
    return render(request, 'alterar_passagem.html', context={'cliente':lista_cliente,'voo':lista_voo, 'selecao':passagem})

def passagen_excluir (request):
    lista_passagem=Passagem.objects.all()
    return render(request, 'buscar_excluir_passagem.html', context={'passagem':lista_passagem})

def passagem_finalizarexcluxao (request):
    passagemslc=request.POST.get('passagem_selecao')
    passagem=Passagem.objects.get(id=passagemslc)
    passagem.delete()
    return redirect('/area_interna')


def passagen_relatorio (request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM View_Passagem")
    result = []
    for row in cursor.fetchall():
        p=InfoPassagem()
        p.nomecliente=row[0]
        p.nomeaeroporto=row[1]  
        p.id=row[2]
        p.duracaovoo=row[3]
        p.poltrona=row[4]
        p.datap=row[5]
        p.horariop=row[6]

        idchegada=row[7]
        lista_aeroporto=Aeroporto.objects.get(id=idchegada)
        
        p.nomeDestino=lista_aeroporto.nome


        result.append(p)
    return render(request, 'relatorio_passagem.html', context={'tudo':result})








     