from django.db import models

# Create your models here.

class Endereco(models.Model):

    rua=models.CharField(max_length=50,null=True)
    numero=models.IntegerField(blank=True)
    cep=models.IntegerField(blank=True)
    complemento=models.CharField(max_length=50,null=True)
    bairro=models.CharField(max_length=50,null=True)
    cidade=models.CharField(max_length=50,null=True)
    estado=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.rua

class Pessoa (models.Model):

    nome=models.CharField(max_length=100,null=True)
    cpf=models.IntegerField(blank=True)
    telefonecel=models.IntegerField(blank=True)
    telefone=models.IntegerField(blank=True)
    email=models.CharField(max_length=100,null=True)
    endereco=models.ForeignKey(Endereco,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Cliente (Pessoa):
    passaporte=models.IntegerField(blank=True)

    def __str__(self):
        return self.passaporte


class Funcionario (Pessoa):
    nit=models.IntegerField()
    salario=models.IntegerField()
    dataentrada=models.DateField()
    datasaida=models.DateField()

    def __str__(self):
        return self.nit

class Piloto (Funcionario):
    breve=models.IntegerField()
    horasdevoo=models.IntegerField()

    def __str__(self):
        return self.breve

class Aeroporto (models.Model):
    nome=models.CharField(max_length=50)
    cnpj=models.IntegerField()
    endereco=models.ForeignKey(Endereco,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Aeronave(models.Model):
    modelo=models.CharField(max_length=50)
    capacidadecarga=models.IntegerField()
    autonomia=models.IntegerField()
    capacidadepassageiros=models.IntegerField()

    def __str__(self):
        return self.modelo

class Voo (models.Model):
    saida=models.ForeignKey(Aeroporto,related_name='saida',on_delete=models.CASCADE)
    chegada=models.ForeignKey(Aeroporto,related_name='chegada',on_delete=models.CASCADE)
    aeronave=models.ForeignKey(Aeronave,on_delete=models.CASCADE)
    piloto=models.ForeignKey(Piloto,on_delete=models.CASCADE)
    duracaovoo=models.IntegerField()

    def __str__(self):
        return self.saida

class Passagem (models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    voo=models.ForeignKey(Voo,on_delete=models.CASCADE)
    poltrona=models.IntegerField()
    datap=models.DateField()
    horariop=models.TimeField()

    def __str__(self):
        return self.poltrona



class InfoAeroporto(models.Model):
    nome=models.CharField(max_length=50)
    cnpj=models.IntegerField()
    rua=models.CharField(max_length=50,null=True)
    numero=models.IntegerField(blank=True)
    cep=models.IntegerField(blank=True)
    complemento=models.CharField(max_length=50,null=True)
    bairro=models.CharField(max_length=50,null=True)
    cidade=models.CharField(max_length=50,null=True)
    estado=models.CharField(max_length=50,null=True)
    class  Meta :
        abstract =  True


class InfoPiloto(models.Model):

    nome=models.CharField(max_length=100,null=True)
    id=models.IntegerField()
    breve=models.IntegerField()
    horasdevoo=models.IntegerField()
    salario=models.IntegerField()
    nit=models.IntegerField()
    class  Meta :
        abstract =  True



class InfoAeronave (models.Model):
    id=models.IntegerField()
    modelo=models.CharField(max_length=50)
    nomeAero=models.CharField(max_length=50)
    cnpj=models.IntegerField()
    vooid=models.IntegerField()
    class  Meta :
        abstract =  True


class InfoVoo (models.Model):
    aeroporto=models.CharField(max_length=50)
    nome=models.CharField(max_length=50)
    id=models.IntegerField()
    capacidadecarga=models.IntegerField()
    capacidadepassageiros=models.IntegerField()
    vooid=models.IntegerField()
    class  Meta :
        abstract =  True


class InfoPassagem (models.Model):
    nomecliente=models.CharField(max_length=50)
    nomeaeroporto=models.CharField(max_length=50)
    id=models.IntegerField()
    duracaovoo=models.IntegerField()
    poltrona=models.IntegerField()
    datap=models.DateField()
    horariop=models.TimeField()
    nomeDestino=models.CharField(max_length=50)
    class  Meta :
        abstract =  True
    
