SELECT distinct [from], [from_id]
INTO dbo.stations
FROM [NJTransit].[dbo].[2018_03] order by from_id 

exec sp_rename 'dbo.stations.from','stationName','COLUMN'
exec sp_rename 'dbo.stations.from_id','stationID','COLUMN'

ALTER TABLE dbo.stations
   ADD CONSTRAINT PK_StationName PRIMARY KEY CLUSTERED (stationID);


