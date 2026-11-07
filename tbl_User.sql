USE [Northwind]
GO
/****** Object:  Table [dbo].[tbl_user]    Script Date: 18/07/2025 07:10:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_user](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[username] [nvarchar](100) NULL,
	[password] [nvarchar](300) NULL,
	[email] [nvarchar](100) NULL,
	[address] [nvarchar](100) NULL,
 CONSTRAINT [PK_tbl_user] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[tbl_user] ON 
GO
INSERT [dbo].[tbl_user] ([id], [username], [password], [email], [address]) VALUES (1, N'dhgia', N'123456', N'dhgia', N'HoChiMinhCity')
GO
INSERT [dbo].[tbl_user] ([id], [username], [password], [email], [address]) VALUES (2, N'admin', N'jZae727K08KaOmKSgOaGzww/XVqGr/PKEgIMkjrcbJI=', N'admin@hce.edu.vn', N'HoChiMinh City')
GO
INSERT [dbo].[tbl_user] ([id], [username], [password], [email], [address]) VALUES (3, N'user1', N'jZae727K08KaOmKSgOaGzww/XVqGr/PKEgIMkjrcbJI=', N'user1@hce.edu.vn', N'HoChiMinh City')
GO
INSERT [dbo].[tbl_user] ([id], [username], [password], [email], [address]) VALUES (4, N'user2', N'jZae727K08KaOmKSgOaGzww/XVqGr/PKEgIMkjrcbJI=', N'user2@hce.du.vn', N'HoChiMinh City')
GO
INSERT [dbo].[tbl_user] ([id], [username], [password], [email], [address]) VALUES (5, N'user3', N'jZae727K08KaOmKSgOaGzww/XVqGr/PKEgIMkjrcbJI=', N'user2@hce.du.vn', N'HoChiMinh City')
GO
INSERT [dbo].[tbl_user] ([id], [username], [password], [email], [address]) VALUES (6, N'user4', N'jZae727K08KaOmKSgOaGzww/XVqGr/PKEgIMkjrcbJI=', N'user2@hce.du.vn', N'HoChiMinh City')
GO
INSERT [dbo].[tbl_user] ([id], [username], [password], [email], [address]) VALUES (7, N'user5', N'jZae727K08KaOmKSgOaGzww/XVqGr/PKEgIMkjrcbJI=', N'user2@hce.du.vn', N'HoChiMinh City')
GO
SET IDENTITY_INSERT [dbo].[tbl_user] OFF
GO



