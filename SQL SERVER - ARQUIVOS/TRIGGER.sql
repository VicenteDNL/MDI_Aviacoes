--################################################################################
--CREATE TRIGGER DeletaAeroporto
--ON Gerenciar_aeroporto
--FOR DELETE
--AS
--BEGIN
--	DECLARE
--	@CodAero int
--	SET @CodAero = (SELECT endereco_id  FROM DELETED)	

--	DELETE FROM Gerenciar_endereco where Gerenciar_endereco.id=@CodAero
--END
--################################################################################



--################################################################################
--CREATE TRIGGER DeletaPessoa
--ON Gerenciar_pessoa
--FOR DELETE
--AS
--BEGIN
--	DECLARE
--	@CodClit int
--	SET @CodClit = (SELECT endereco_id  FROM DELETED)	

--	DELETE FROM Gerenciar_endereco where Gerenciar_endereco.id=@CodClit
--END
--################################################################################