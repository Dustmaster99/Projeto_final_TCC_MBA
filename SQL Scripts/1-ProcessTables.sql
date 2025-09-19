DECLARE @Const NVARCHAR(50) = '10';
DECLARE @columnName NVARCHAR(50);
DECLARE @tableName NVARCHAR(50);

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

	DECLARE @sqlCommand nvarchar(max);
	SET @sqlCommand = 'UPDATE ' + @tableName + ' SET ' + @columnName +' =' + @columnName + '/' + @Const + ' WHERE ' + @columnName + ' IS NOT NULL;'
	EXECUTE sp_executesql @sqlCommand;

    select @idColumn = min( ID ) from @Metadata where ID > @idColumn
end


/* EXAMPLE of Query beeing done 
UPDATE [NJTransit].[dbo].[2018_03] SET stop_sequence = stop_sequence/10 WHERE stop_sequence IS NOT NULL;
*/






