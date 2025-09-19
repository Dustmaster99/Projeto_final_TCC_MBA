/* Changing dataype for delay_minutes */
ALTER TABLE dbo.[2018_04]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2018_05]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2018_06]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2018_07]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2018_08]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2018_09]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2018_10]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2018_11]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2018_12]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2019_01]
ALTER COLUMN [delay_minutes] float; 

ALTER TABLE dbo.[2019_02]
ALTER COLUMN [delay_minutes] float; 

/* Delete data where properties are null:  */


delete from dbo.[2018_04]
where [delay_minutes] is null

delete from dbo.[2018_05]
where [delay_minutes] is null

delete from dbo.[2018_06]
where [delay_minutes] is null

delete from dbo.[2018_07]
where [delay_minutes] is null

delete from dbo.[2018_09]
where [delay_minutes] is null

delete from dbo.[2018_08]
where [delay_minutes] is null

delete from dbo.[2018_10]
where [delay_minutes] is null

delete from dbo.[2018_11]
where [delay_minutes] is null

delete from dbo.[2018_12]
where [delay_minutes] is null

delete from dbo.[2019_01]
where [delay_minutes] is null

delete from dbo.[2019_02]
where [delay_minutes] is null


