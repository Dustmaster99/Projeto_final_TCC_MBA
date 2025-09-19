DECLARE @min_station_age int;
DECLARE @max_station_age int;
DECLARE @mean_station_age float;



SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Atl. City Line')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Atl. City Line';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Atl. City Line')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Atl. City Line';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Atl. City Line')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Atl. City Line';





SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Bergen Co. Line')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Bergen Co. Line';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Bergen Co. Line')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Bergen Co. Line';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Bergen Co. Line')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Bergen Co. Line';




SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Gladstone Branch')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Gladstone Branch';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Gladstone Branch')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Gladstone Branch';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Gladstone Branch')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Gladstone Branch';




SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Main Line')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Main Line';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Main Line')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Main Line';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Main Line')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Main Line';



SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Montclair-Boonton')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Montclair-Boonton';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Montclair-Boonton')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Montclair-Boonton';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Montclair-Boonton')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Montclair-Boonton';



SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Morristown Line')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Morristown Line';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Morristown Line')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Morristown Line';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Morristown Line')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Morristown Line';



SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'No Jersey Coast')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'No Jersey Coast';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'No Jersey Coast')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'No Jersey Coast';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'No Jersey Coast')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'No Jersey Coast';



SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Northeast Corrdr')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Northeast Corrdr';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Northeast Corrdr')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Northeast Corrdr';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Northeast Corrdr')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Northeast Corrdr';



SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Pascack Valley')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Pascack Valley';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Pascack Valley')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Pascack Valley';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Pascack Valley')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Pascack Valley';



SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Princeton Shuttle')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Princeton Shuttle';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Princeton Shuttle')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Princeton Shuttle';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Princeton Shuttle')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Princeton Shuttle';




SET @min_station_age = (SELECT MIN(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Raritan Valley')
UPDATE [NJTransit].[dbo].[lines]
SET [min_year] =  @min_station_age
WHERE [lineName]= 'Raritan Valley';

SET @max_station_age = (SELECT MAX(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Raritan Valley')
UPDATE [NJTransit].[dbo].[lines]
SET [max_year] =  @max_station_age
WHERE [lineName]= 'Raritan Valley';

SET @mean_station_age = (SELECT AVG(year) FROM [NJTransit].[dbo].[Year_stations] where [Line] = 'Raritan Valley')
UPDATE [NJTransit].[dbo].[lines]
SET [mean_year] =  @mean_station_age
WHERE [lineName]= 'Raritan Valley';










