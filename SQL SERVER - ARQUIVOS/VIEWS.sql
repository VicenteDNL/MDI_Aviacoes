
--==================================================================================================
--CREATE View View_Passagem 
--(NomeCliente,AeroportoSaida, CodPassagem,DuracaoVoo, Poltrona, DataP, HorarioP, CodChegada)
--AS
--SELECT pes.nome,aero.nome,pa.id, duracaovoo, poltrona, datap, horariop, v.chegada_id
--From Gerenciar_pessoa pes inner join Gerenciar_cliente cl on pes.id=cl.pessoa_ptr_id
--	inner join Gerenciar_passagem pa on pa.cliente_id=cl.pessoa_ptr_id
--	inner join Gerenciar_voo v on pa.voo_id=v.id 
--	inner join  Gerenciar_aeroporto aero on v.saida_id=aero.id

--==================================================================================================


--==================================================================================================
--CREATE View View_Voo
--(NomeAeroporto, NomePessoa, CodAeronave, CapacidadedeCarga, CapacidadePassageiros, ID_VOO )
--AS
--SELECT p.nome, pe.nome, n.id, capacidadecarga,capacidadepassageiros , v.id
--FROM Gerenciar_aeronave n inner join Gerenciar_voo v  on n.id=v.aeronave_id 
--     inner join Gerenciar_aeroporto p on p.id=v.chegada_id 
--	 inner join Gerenciar_passagem pa on pa.voo_id=v.id 
--	 inner join Gerenciar_cliente c on c.pessoa_ptr_id=pa.cliente_id 
--	 inner join Gerenciar_pessoa pe on pe.id=c.pessoa_ptr_id 
--==================================================================================================


--==================================================================================================
--CREATE View View_Aeronave
--(CodAeronave,Modelo, NomeAeroporto, CNPJ, voo_id)
--AS
--SELECT a.id, Modelo, aero.nome, cnpj, vo.id
--FROM Gerenciar_aeronave a inner join  Gerenciar_voo vo on a.id=vo.aeronave_id 
--inner join Gerenciar_aeroporto aero on aero.id=vo.saida_id
--==================================================================================================


--==================================================================================================
--CREATE View View_InfoPiloto
--(NomePiloto, CodPiloto, Breve,HorasdeVoo,Salario,NIT)
--AS
--SELECT p.nome, pp.funcionario_ptr_id, breve, horasdevoo,salario,nit 
--FROM Gerenciar_pessoa p inner join Gerenciar_funcionario f on f.pessoa_ptr_id=p.id 
--inner join Gerenciar_piloto pp on pp.funcionario_ptr_id=f.pessoa_ptr_id
--==================================================================================================


--==================================================================================================
--CREATE View View_InfoAeroporto
--( NomeAeroporto, CNPJ,Rua, Numero, CEP,Complemento, Bairro, Estado, Cidade)
--AS
-- SELECT  p.nome, cnpj, Rua, Numero, CEP, Complemento, Bairro, Estado, Cidade 
-- FROM Gerenciar_aeroporto p inner join Gerenciar_endereco e on e.id=p.endereco_id 
--==================================================================================================


