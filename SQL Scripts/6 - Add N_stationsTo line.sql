drop table #TempTable
SELECT [line], COUNT(*) AS n_stationsTemp
INTO #TempTable
FROM [NJTransit].[dbo].[line_station]
GROUP BY [line] 

Alter table dbo.lines add n_stations INT

update dbo.lines 
set n_stations = #TempTable.n_stationsTemp
from dbo.lines inner join #TempTable on dbo.lines.[lineName] = #TempTable.line