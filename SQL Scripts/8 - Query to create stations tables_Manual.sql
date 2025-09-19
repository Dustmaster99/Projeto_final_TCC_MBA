--https://www.geeksforgeeks.org/how-to-eliminate-duplicate-values-based-on-only-one-column-of-the-table-in-sql/ -> reference for code to delete

--Example of what is aplied for each station
----------------------------------------------------------------------------------------------------------------------
--'Atl. City Line'
SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Atl_City_Line_info FROM [NJTransit].[dbo].[2018_03] where line = 'Atl. City Line' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence;
DELETE B1 
FROM [NJTransit].dbo.Atl_City_Line_info B1
JOIN [NJTransit].dbo.Atl_City_Line_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;
----------------------------------------------------------------------------------------------------------------------
--'Bergen Co. Line'
SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Bergen_Co_Line_info FROM [NJTransit].[dbo].[2018_03] where line = 'Bergen Co. Line' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Bergen_Co_Line_info B1
JOIN [NJTransit].dbo.Bergen_Co_Line_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;
----------------------------------------------------------------------------------------------------------------------
--'Gladstone Branch'
SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Gladstone_Branch_info FROM [NJTransit].[dbo].[2018_03] where line = 'Gladstone Branch' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Gladstone_Branch_info B1
JOIN [NJTransit].dbo.Gladstone_Branch_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;
----------------------------------------------------------------------------------------------------------------------
--'Main Line'
SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Main_Line_info FROM [NJTransit].[dbo].[2018_03] where line = 'Main Line' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Main_Line_info B1
JOIN [NJTransit].dbo.Main_Line_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;

----------------------------------------------------------------------------------------------------------------------
--'Montclair-Boonton'
SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Montclair_Boonton_info FROM [NJTransit].[dbo].[2018_03] where line = 'Montclair-Boonton' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Montclair_Boonton_info B1
JOIN [NJTransit].dbo.Montclair_Boonton_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;

----------------------------------------------------------------------------------------------------------------------
--'Morristown Line'
SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Morristown_Line_info FROM [NJTransit].[dbo].[2018_03] where line = 'Morristown Line' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Morristown_Line_info B1
JOIN [NJTransit].dbo.Morristown_Line_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;

----------------------------------------------------------------------------------------------------------------------
--'No Jersey Coast'
SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.No_Jersey_Coast_info FROM [NJTransit].[dbo].[2018_03] where line = 'No Jersey Coast' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.No_Jersey_Coast_info B1
JOIN [NJTransit].dbo.No_Jersey_Coast_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;


----------------------------------------------------------------------------------------------------------------------
--'Northeast Corrdr'

SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Northeast_Corrd_info FROM [NJTransit].[dbo].[2018_03] where line = 'Northeast Corrdr' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Northeast_Corrd_info B1
JOIN [NJTransit].dbo.Northeast_Corrd_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;

----------------------------------------------------------------------------------------------------------------------
--'Pascack Valley'

SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Pascack_Valley_info FROM [NJTransit].[dbo].[2018_03] where line = 'Pascack Valley' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Pascack_Valley_info B1
JOIN [NJTransit].dbo.Pascack_Valley_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;

----------------------------------------------------------------------------------------------------------------------
--'Princeton Shuttle'

SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Princeton_Shuttle_info FROM [NJTransit].[dbo].[2018_03] where line = 'Princeton Shuttle' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Princeton_Shuttle_info B1
JOIN [NJTransit].dbo.Princeton_Shuttle_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;


----------------------------------------------------------------------------------------------------------------------
--'Raritan Valley'

SELECT distinct [stop_sequence] ,[to] ,[to_id] ,[line] ,[type] INTO [NJTransit].dbo.Raritan_Valley_info FROM [NJTransit].[dbo].[2018_03] where line = 'Raritan Valley' and train_id IS NOT NULL and  stop_sequence IS NOT NULL and (train_id % 2) = '1' order by stop_sequence

DELETE B1 
FROM [NJTransit].dbo.Raritan_Valley_info B1
JOIN [NJTransit].dbo.Raritan_Valley_info B2
ON B1.[to] = B2.[to]
AND B2.stop_sequence > B1.stop_sequence;











