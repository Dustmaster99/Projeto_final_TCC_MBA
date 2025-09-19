DECLARE @count int;

SET @count = (select count(*) from [NJTransit].[dbo].[Atl_City_Line_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Atl. City Line';

SET @count = (select count(*) from [NJTransit].[dbo].[Bergen_Co_Line_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Bergen Co. Line';

SET @count = (select count(*) from [NJTransit].[dbo].[Gladstone_Branch_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Gladstone Branch';

SET @count = (select count(*) from [NJTransit].[dbo].[Main_Line_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Main Line';

SET @count = (select count(*) from [NJTransit].[dbo].[Montclair_Boonton_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Montclair-Boonton';

SET @count = (select count(*) from [NJTransit].[dbo].[Morristown_Line_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Morristown Line';

SET @count = (select count(*) from [NJTransit].[dbo].[No_Jersey_Coast_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'No Jersey Coast';

SET @count = (select count(*) from [NJTransit].[dbo].[Northeast_Corrd_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Northeast Corrdr';

SET @count = (select count(*) from [NJTransit].[dbo].[Pascack_Valley_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Pascack Valley';

SET @count = (select count(*) from [NJTransit].[dbo].[Princeton_Shuttle_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Princeton Shuttle';

SET @count = (select count(*) from [NJTransit].[dbo].[Raritan_Valley_info])
UPDATE [NJTransit].[dbo].[lines]
SET [n_stations] =  @count 
WHERE [lineName]= 'Raritan Valley';
