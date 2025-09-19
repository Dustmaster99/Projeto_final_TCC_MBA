delete from [NJTransit].[dbo].[2018_03]
where [stop_sequence] is null or [delay_minutes]is null
