
drop table #TempTable
SELECT [stationName], COUNT(*) AS n_lines
INTO #TempTable
FROM [NJTransit].[dbo].[line_station]
GROUP BY [stationName] 

Alter table dbo.stations add n_Lines INT

update dbo.stations 
set n_lines = #TempTable.n_lines
from dbo.stations inner join #TempTable on dbo.stations.[stationName] = #TempTable.stationName