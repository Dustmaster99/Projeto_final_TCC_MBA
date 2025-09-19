Declare @Link table ([stop_sequence] INT , [to] NVARCHAR(max), [to_id] NVARCHAR(max), [line] NVARCHAR(max),[type] NVARCHAR(max))
INSERT @Link([stop_sequence], [to], [to_id],[line],[type]) VALUES (2, 'New York Penn Station', 105, 'Link','NJ Transit')
INSERT @Link([stop_sequence], [to], [to_id],[line],[type]) VALUES (1, 'Hoboken', 63, 'Link','NJ Transit')

SELECT * Into dbo.Link_penst_habok from @Link