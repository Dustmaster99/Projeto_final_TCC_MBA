
Declare @Bergen_Co_Line_A table ([stop_sequence] INT , [to] NVARCHAR(max), [to_id] NVARCHAR(max), [line] NVARCHAR(max),[type] NVARCHAR(max))
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (25, 'Port Jervis', 123, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (24, 'Otisville', 113, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (23, 'Middletown NY', 86, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (22, 'Campbell Hall', 26, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (21, 'Salisbury Mills-Cornwall', 135, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (20, 'Harriman', 57, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (19, 'Tuxedo', 149, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (18, 'Sloatsburg', 137, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (17, 'Suffern', 144, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (16, 'Mahwah', 78, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (15, 'Ramsey Route 17', 38417, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (14, 'Ramsey Main St', 128, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (13, 'Allendale', 3, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (12, 'Waldwick',151, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (11, 'Ho-Ho-Kus', 64, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (10, 'Ridgewood', 131, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (9, 'Glen Rock Boro Hall',  51, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (8, 'Radburn Fair Lawn', 126, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (7, 'Broadway Fair Lawn', 25, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (6, 'Plauderville', 121, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (5, 'Garfield', 46, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (4, 'Wesmont', 43599, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (3, 'Rutherford', 134, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (2, 'Secaucus Lower Lvl', 38174, 'Bergen Co. Line','NJ Transit')
INSERT @Bergen_Co_Line_A([stop_sequence], [to], [to_id],[line],[type]) VALUES (1, 'Hoboken', 63, 'Bergen Co. Line','NJ Transit')
 
 
 
 

SELECT * Into dbo.Bergen_Co_Line_A from @Bergen_Co_Line_A



