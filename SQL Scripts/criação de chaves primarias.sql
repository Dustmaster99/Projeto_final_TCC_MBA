



ALTER TABLE [NJTransit].[dbo].[Year_stations]
DROP CONSTRAINT PK_StationName_Year_stations

ALTER TABLE [NJTransit].[dbo].[closseness]
DROP CONSTRAINT PK_closseness

ALTER TABLE [NJTransit].[dbo].[degree]
DROP CONSTRAINT PK_degree

ALTER TABLE [NJTransit].[dbo].[centrality]
DROP CONSTRAINT PK_centrality

ALTER TABLE [NJTransit].[dbo].[clustering_coef]
DROP CONSTRAINT PK_clustering_coef

ALTER TABLE [NJTransit].[dbo].[Lat_long]
DROP CONSTRAINT PK_Lat_long







/*
ALTER TABLE [NJTransit].[dbo].[Year_stations]
   ADD CONSTRAINT PK_StationName_Year_stations PRIMARY KEY CLUSTERED (Station,Line)

ALTER TABLE [NJTransit].[dbo].[closseness]
	ADD CONSTRAINT PK_closseness PRIMARY KEY CLUSTERED (Station)

ALTER TABLE[NJTransit].[dbo].[degree]
	ADD CONSTRAINT PK_degree PRIMARY KEY CLUSTERED (Station)

ALTER TABLE [NJTransit].[dbo].[centrality]
	ADD CONSTRAINT PK_centrality PRIMARY KEY CLUSTERED (Station)

ALTER TABLE [NJTransit].[dbo].[clustering_coef]
	ADD CONSTRAINT PK_clustering_coef PRIMARY KEY CLUSTERED (Station)

ALTER TABLE [NJTransit].[dbo].[Lat_long]
	ADD CONSTRAINT PK_Lat_long PRIMARY KEY CLUSTERED (StationName,LineName)


ALTER TABLE [NJTransit].[dbo].[Atl_City_Line_info]
	ADD CONSTRAINT PK_Atl_City_Line_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Bergen_Co_Line_info]
	ADD CONSTRAINT PK_Bergen_Co_Line_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Gladstone_Branch_info]
	ADD CONSTRAINT PK_Gladstone_Branch_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Main_Line_info]
	ADD CONSTRAINT PK_Main_Line_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Montclair_Boonton_info]
	ADD CONSTRAINT PK_Montclair_Boonton_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Morristown_Line_info]
	ADD CONSTRAINT PK_Morristown_Line_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[No_Jersey_Coast_info]
	ADD CONSTRAINT PK_No_Jersey_Coast_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Northeast_Corrd_info]
	ADD CONSTRAINT PK_Northeast_Corrd_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Pascack_Valley_info]
	ADD CONSTRAINT PK_Pascack_Valley_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Princeton_Shuttle_info]
	ADD CONSTRAINT PK_Princeton_Shuttle_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Raritan_Valley_info]
	ADD CONSTRAINT PK_Raritan_Valley_info PRIMARY KEY CLUSTERED (stop_sequence)

ALTER TABLE [NJTransit].[dbo].[Link_penst_habok]
	ADD CONSTRAINT PK_Link_penst_habok PRIMARY KEY CLUSTERED (stop_sequence)
	*/
