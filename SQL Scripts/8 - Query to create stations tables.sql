DECLARE @lineName NVARCHAR(50);
DECLARE @tableName NVARCHAR(50);
DECLARE @rootsheet NVARCHAR(50);
Declare @Metadata table (ID INT , tableName NVARCHAR(50), lineName NVARCHAR(50), rootsheet NVARCHAR(50))
INSERT @Metadata(ID, tableName, lineName,rootsheet) VALUES (0, 'dbo.Atl_City_Line', 'Atl. City Line','[NJTransit].[dbo].[2018_03]')
INSERT @Metadata(ID, tableName, lineName,rootsheet) VALUES (1, 'dbo.Bergen_Co_Line ', 'Bergen Co. Line ','[NJTransit].[dbo].[2018_03]')



declare @idColumn int

select @idColumn = min( ID ) from @Metadata

while @idColumn is not null
begin
    SET @tableName = (SELECT tableName FROM @Metadata WHERE  ID =  @idColumn);
	print @tableName 
	SET @lineName = (SELECT lineName FROM @Metadata WHERE  ID =  @idColumn);
	print @lineName
	DECLARE @sqlCommand nvarchar(max);
	SET @sqlCommand = 'SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO ' +@tableName+ ' FROM ' +@rootsheet+ ' where line = ' + @lineName + ' and (train_id % 2) = ''1'' order by stop_sequence'
	EXECUTE sp_executesql @sqlCommand;
	

    select @idColumn = min( ID ) from @Metadata where ID > @idColumn
end

















  