SELECT distinct [line]
INTO dbo.lines
FROM [NJTransit].[dbo].[2018_03] order by line

exec sp_rename 'dbo.lines.line','lineName','COLUMN'

alter table dbo.lines
add lineID int identity(1,1)


ALTER TABLE dbo.lines
   ADD CONSTRAINT PK_LineName PRIMARY KEY CLUSTERED (lineID);

