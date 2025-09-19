UPDATE [NJTransit].[dbo].[2018_03]
SET [train_id] = REPLACE([train_id], 'A', '')

UPDATE [NJTransit].[dbo].[2018_03]
SET [train_id] = REPLACE([train_id], '.', '')
  