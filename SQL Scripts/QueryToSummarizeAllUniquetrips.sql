select 
ID_DATA,
count (distinct ID_DATA) 
FROM [NJTransit].[dbo].[2018_03]
group by ID_DATA