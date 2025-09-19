DECLARE @Const NVARCHAR(50) = '10';
DECLARE @columnName NVARCHAR(50);
DECLARE @tableName NVARCHAR(50);
DECLARE @newColumn NVARCHAR(50) = 'ID_DATA' ;


Declare @Metadata table (ID INT , tableName NVARCHAR(50), columnName NVARCHAR(50))
INSERT @Metadata(ID, tableName, columnName) VALUES (0, '[NJTransit].[dbo].[2018_03]', 'stop_sequence')

/*INSERT @Metadata(ID, tableName, columnName) VALUES (1, '[NJTransit].[dbo].[2018_04]', 'stop_sequence')
INSERT @Metadata(ID, tableName, columnName) VALUES (2, '[NJTransit].[dbo].[2018_05]', 'stop_sequence')
INSERT @Metadata(ID, tableName, columnName) VALUES (3, '[NJTransit].[dbo].[2018_06]', 'stop_sequence')
INSERT @Metadata(ID, tableName, columnName) VALUES (4, '[NJTransit].[dbo].[2018_07]', 'stop_sequence')
INSERT @Metadata(ID, tableName, columnName) VALUES (5, '[NJTransit].[dbo].[2018_08]', 'stop_sequence')
INSERT @Metadata(ID, tableName, columnName) VALUES (6, '[NJTransit].[dbo].[2018_09]', 'stop_sequence')
INSERT @Metadata(ID, tableName, columnName) VALUES (7, '[NJTransit].[dbo].[2018_10]', 'stop_sequence')
*/

	
declare @idColumn int

select @idColumn = min( ID ) from @Metadata

while @idColumn is not null
begin
    SET @tableName = (SELECT tableName FROM @Metadata WHERE  ID =  @idColumn);
	SET @columnName = (SELECT columnName FROM @Metadata WHERE  ID =  @idColumn);
	
	DECLARE @sqlCommand1 nvarchar(max);
	SET @sqlCommand1 = 'ALTER TABLE ' + @tableName + ' ADD ' + @newColumn + ' NVARCHAR(50) NULL;'
	EXECUTE sp_executesql @sqlCommand1;
	
	DECLARE @sqlCommand2 nvarchar(max);
	SET @sqlCommand2 ='UPDATE ' + @tableName + ' SET ' + @newColumn + ' = CONCAT_WS(''.'', ' + @tableName + '.train_id, ' + @tableName + '.date);'
	EXECUTE sp_executesql @sqlCommand2;
    select @idColumn = min( ID ) from @Metadata where ID > @idColumn

	DECLARE @sqlCommand3 nvarchar(max);
	SET @sqlCommand3 = 'ALTER TABLE ' + @tableName + ' ADD ID int identity(1,1);'
	EXECUTE sp_executesql @sqlCommand3;

	DECLARE @sqlCommand4 nvarchar(max);
	SET @sqlCommand4 = 'ALTER TABLE ' + @tableName + ' ADD CONSTRAINT PK_DataTable PRIMARY KEY CLUSTERED (ID)'
	EXECUTE sp_executesql @sqlCommand4;

end

