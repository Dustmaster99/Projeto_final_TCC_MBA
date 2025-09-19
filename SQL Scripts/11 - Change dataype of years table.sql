 UPDATE  [NJTransit].[dbo].[Year_stations]
SET [Line] = REPLACE([Line], '"[', '')

 UPDATE  [NJTransit].[dbo].[Year_stations]
SET [Year] = REPLACE([Year], ']"', '')

ALTER TABLE [NJTransit].[dbo].[Year_stations]
ALTER COLUMN year int;

