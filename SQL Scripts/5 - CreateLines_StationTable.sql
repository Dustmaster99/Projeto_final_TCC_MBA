/*Table to show relation between Stations and lines*/

SELECT distinct [lineID],[line],[from], [from_id]
INTO dbo.line_station
FROM [NJTransit].[dbo].[2018_03] as Query
Inner join dbo.lines on query.line = dbo.lines.lineName
order by [lineID];

exec sp_rename 'dbo.line_station.from','stationName','COLUMN'
exec sp_rename 'dbo.line_station.from_id','stationID','COLUMN'

alter table dbo.line_station
add ID int identity(1,1)

ALTER TABLE dbo.line_station
   ADD CONSTRAINT PK_line_station PRIMARY KEY CLUSTERED (ID);