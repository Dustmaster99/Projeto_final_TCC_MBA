 UPDATE  [NJTransit].[dbo].[Lat_long]
SET [LineName] = REPLACE([LineName], '"[', '')

 UPDATE  [NJTransit].[dbo].[Lat_long]
SET [Longitude] = REPLACE([Longitude], ']"', '')

ALTER TABLE [NJTransit].[dbo].[Lat_long]
ALTER COLUMN Longitude float;

ALTER TABLE [NJTransit].[dbo].[Lat_long]
ALTER COLUMN Latitude float;