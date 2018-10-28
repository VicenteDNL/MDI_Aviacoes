--         /*Aeronave*/
--CREATE PROCEDURE Stored_Aeronave
--@CodAeronave int = null, 
--@CapacidadedeCarga int = null, 
--@Modelo varchar(50) = null, 
--@Autonomia int = null,
--@CapacidadePassageiros int =null,
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Gerenciar_aeronave(capacidadecarga, modelo, autonomia,capacidadepassageiros)
--	VALUES ( @CapacidadedeCarga, @Modelo, @Autonomia, @CapacidadePassageiros); 

--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Gerenciar_aeronave SET capacidadecarga = @CapacidadedeCarga, modelo = @Modelo, autonomia = @Autonomia, capacidadepassageiros = @CapacidadePassageiros WHERE id = @CodAeronave;

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Gerenciar_aeronave WHERE id = @CodAeronave;
	
--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Gerenciar_aeronave;
		
--END
--END


--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Aeronave 2,33,'Av', 20, 12,1
--PRINT (@msg)

--select * from Gerenciar_aeronave


          /*Endereco*/

--CREATE PROCEDURE Stored_Endereco
--@CodEndereco int  = null, 
--@Rua varchar(50) = null, 
--@Numero varchar(10) = null, 
--@Cep int  = null,
--@Complemento varchar(50) = null, 
--@Bairro varchar(50) = null, 
--@Estado varchar(50) = null, 
--@Cidade varchar(50) = null, 
--@Mensagem varchar(50) OUTPUT, 
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Endereco(CodEndereco, Rua, Numero, Cep, Complemento, Bairro, Estado, Cidade)
--	VALUES (@CodEndereco, @Rua, @Numero, @Cep, @Complemento, @Bairro, @Estado, @Cidade);	 
--	SET @Mensagem = 'O registro foi inserido!';
	
	
--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Endereco SET Rua = @Rua, Numero = @Numero, Cep = @Cep, Complemento = @Complemento, Bairro = @Bairro, Estado = @Estado, Cidade = @Cidade WHERE CodEndereco = @CodEndereco;
--	SET @Mensagem = 'Alterado com sucesso!' ;	
	

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Endereco WHERE CodEndereco = @CodEndereco;
--	SET @Mensagem = 'Deletado!' ;	
	

--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Endereco;
		
--END
--END

--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Endereco 1, 'mariana', '20',77270000, ' perto do cem', 'jarddim', 'to', 'palmas', @msg OUTPUT,1
--PRINT (@msg)




          /*Aeroporto*/

--CREATE PROCEDURE Stored_Aeroporto
--@CodAeroporto int  = null, 
--@NomeAeroporto varchar(50) = null, 
--@CNPJ int = null,
--@CodEndereco int = null,
--@Mensagem varchar(50) OUTPUT, 
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Aeroporto(CodAeroporto, NomeAeroporto, CNPJ, CodEndereco)
--	VALUES (@CodAeroporto, @NomeAeroporto, @CNPJ, @CodEndereco);	 
--	SET @Mensagem = 'O registro foi inserido!';
	
	
--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Aeroporto SET NomeAeroporto = @NomeAeroporto, CNPJ = @CNPJ, CodEndereco = @CodEndereco WHERE CodAeroporto = @CodAeroporto;
--	SET @Mensagem = 'Alterado com sucesso!' ;	
	

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Aeroporto WHERE CodAeroporto = @CodAeroporto;
--	SET @Mensagem = 'Deletado!' ;	
	

--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Aeroporto;
		
--END
--END

--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Aeroporto 2, 'beare', 10, 1, @msg OUTPUT,4
--PRINT (@msg)




          /*Pessoa*/

--CREATE PROCEDURE Stored_Pessoa
--@CodPessoa int  = null, 
--@NomePessoa varchar(50) = null, 
--@CPF int  = null,
--@TelefoneCel int = null, 
--@TelefoneRes int = null, 
--@CodEndereco int  = null,  
--@Mensagem varchar(50) OUTPUT, 
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Pessoa(CodPessoa, NomePessoa, CPF, TelefoneCel, TelefoneRes, CodEndereco)
--	VALUES (@CodPessoa, @NomePessoa, @CPF, @TelefoneCel, @TelefoneRes, @CodEndereco);	 
--	SET @Mensagem = 'O registro foi inserido!';
	
	
--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Pessoa SET NomePessoa = @NomePessoa, CPF = @CPF, TelefoneCel = @TelefoneCel, TelefoneRes = @TelefoneRes, CodEndereco = @CodEndereco WHERE CodPessoa = @CodPessoa;
--	SET @Mensagem = 'Alterado com sucesso!' ;	
	

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Pessoa WHERE CodPessoa = @CodPessoa;
--	SET @Mensagem = 'Deletado!' ;	
	

--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Pessoa;
		
--END
--END

--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Pessoa 2, 'maria', 333, 84510609, 84510609, 1, @msg OUTPUT,1
--PRINT (@msg)





         /*Cliente*/

--CREATE PROCEDURE Stored_Cliente
--@CodCliente int  = null, 
--@CodPessoa int  = null,  
--@Mensagem varchar(50) OUTPUT, 
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Cliente(CodCliente, CodPessoa)
--	VALUES (@CodCliente, @CodPessoa);	 
--	SET @Mensagem = 'O registro foi inserido!';
	
	
--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Cliente SET CodPessoa = @CodPessoa WHERE CodCliente = @CodCliente;
--	SET @Mensagem = 'Alterado com sucesso!' ;	
	

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Cliente WHERE CodCliente = @CodCliente;
--	SET @Mensagem = 'Deletado!' ;	
	

--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Cliente;
		
--END
--END

--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Cliente 2, 1, @msg OUTPUT,1
--PRINT (@msg)






           /*Funcionaro*/

--CREATE PROCEDURE Stored_Funcionario
--@CodFuncionario int  = null, 
--@Nit int = null, 
--@Salario money = null, 
--@DataSaida date  = null,
--@DataEntrada date  = null,
--@CodPessoa int  = null, 
--@Mensagem varchar(50) OUTPUT, 
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Funcionario(CodFuncionario, Nit, Salario, DataSaida, DataEntrada, CodPessoa)
--	VALUES (@CodFuncionario, @Nit, @Salario, @DataSaida, @DataEntrada, @CodPessoa);	 
--	SET @Mensagem = 'O registro foi inserido!';
	
	
--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Funcionario SET Nit = @Nit, Salario = @Salario, DataSaida = @DataSaida, DataEntrada = @DataEntrada, CodPessoa = @CodPessoa WHERE CodFuncionario = @CodFuncionario;
--	SET @Mensagem = 'Alterado com sucesso!' ;	
	

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Funcionario WHERE CodFuncionario = @CodFuncionario;
--	SET @Mensagem = 'Deletado!' ;	
	

--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Funcionario;
		
--END
--END

--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Funcionario 2, 2, 97, '03/31/1997', '03/11/1997', 2, @msg OUTPUT,4
--PRINT (@msg)





          /*Passagem*/

--CREATE PROCEDURE Stored_Passagem
--@CodPassagem int  = null, 
--@Poltrona int = null, 
--@dataP date = null, 
--@HorarioP int  = null,
--@CodCliente int = null,
--@codVoo int = null,
--@Mensagem varchar(50) OUTPUT, 
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Passagem(CodPassagem, Poltrona, dataP, HorarioP, CodCliente, codVoo)
--	VALUES (@CodPassagem, @Poltrona, @dataP, @HorarioP, @CodCliente, @codVoo);	 
--	SET @Mensagem = 'O registro foi inserido!';

	
--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Passagem SET Poltrona = @Poltrona, dataP = @dataP, HorarioP = @HorarioP, CodCliente = @CodCliente, codVoo = @codVoo WHERE CodPassagem = @CodPassagem;
--	SET @Mensagem = 'Alterado com sucesso!' ;	
	 

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Passagem WHERE CodPassagem = @CodPassagem;
--	SET @Mensagem = 'Deletado!' ;	
	

--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Passagem;
		
--END
--END

--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Passagem 2, 3, '01/11/2018', 1, 2, 2, @msg OUTPUT,1
--PRINT (@msg)




        


           /*Piloto*/

--CREATE PROCEDURE Stored_Piloto
--@CodPiloto int  = null, 
--@Breve int = null, 
--@HorasdeVoo int = null, 
--@CodFuncionario int  = null, 
--@Mensagem varchar(50) OUTPUT, 
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Piloto(CodPiloto, Breve, HorasdeVoo, CodFuncionario)
--	VALUES (@CodPiloto, @Breve, @HorasdeVoo, @CodFuncionario);	 
--	SET @Mensagem = 'O registro foi inserido!';
	
	
--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Piloto SET Breve = @Breve, HorasdeVoo = @HorasdeVoo, CodFuncionario = @CodFuncionario WHERE CodPiloto = @CodPiloto;
--	SET @Mensagem = 'Alterado com sucesso!' ;	
	 

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Piloto WHERE CodPiloto = @CodPiloto;
--	SET @Mensagem = 'Deletado!' ;	
	

--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Piloto;
		
--END
--END


--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Piloto 2, 56, 5, 2, @msg OUTPUT,1
--PRINT (@msg)





          /*Voo*/

--CREATE PROCEDURE Stored_Voo
--@CodVoo int  = null, 
--@DuracaoVoo int = null, 
--@CodChegada int  = null, 
--@CodAeronave int  = null,
--@CodPiloto int  = null, 
--@CodSaida int  = null, 
--@Mensagem varchar(50) OUTPUT, 
--@Opcao int = null

--AS
--BEGIN
--	IF (@Opcao = 1)  BEGIN
--	INSERT INTO Voo(CodVoo, DuracaoVoo, CodChegada, CodAeronave, CodPiloto,CodSaida)
--	VALUES (@CodVoo, @DuracaoVoo, @CodChegada, @CodAeronave, @CodPiloto, @CodSaida);	 
--	SET @Mensagem = 'O registro foi inserido!';
	
	
--	END
--	IF (@Opcao = 2)  BEGIN
--	UPDATE Voo SET DuracaoVoo = @DuracaoVoo, CodChegada = @CodChegada, CodAeronave = @CodAeronave, CodPiloto = @CodPiloto, CodSaida = @CodSaida WHERE CodVoo = @CodVoo;
--	SET @Mensagem = 'Alterado com sucesso!' ;	
	

--	END
--	IF (@Opcao = 3) BEGIN
--	DELETE FROM Voo WHERE CodVoo = @CodVoo;
--	SET @Mensagem = 'Deletado!' ;	
	
--	END
--	IF (@Opcao = 4) BEGIN
--	SELECT * FROM Voo;
		
--END
--END

--DECLARE 
--  @msg varchar(50)
--EXEC Stored_Voo 2, 40, 2, 2, 2, 1, @msg OUTPUT,4
--PRINT (@msg)



