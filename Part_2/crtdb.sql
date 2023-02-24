--DML statements for ABC.sqlite

--Administrator
INSERT INTO Administrator (NAME, GENDER)
            VALUES ("ALDEN TRINITY", 'F'),
                   ("RANDALL URSULA", 'M'),
                   ("OAKLEY BENNETT", 'M'),
                   ("CURTIS CAMERON", 'M');

--Client
INSERT INTO Client (name, phone, address)
            VALUES ("Caleb Anabella", 304-390-5453, "1232 W Mud River Rd" ),
                   ("Nancy Sandra", 856-848-2774, "1290 Buford Way Dm"),
                   ("Reg Camellia", 714-826-5012, "8287 E Chadwick Pkwy"),
                   ("Genevieve Ralf", 252-449-8107, "110 E Meadowlark St"),
                   ("Elroy Cate", 414-377-8492, "9095 W Highland Park Ave");

--Model
INSERT INTO Model(width, height, weight, depth, screenSize)
            VALUES (3530.95, 6135.58, 4354.90, 9354.10, 3705.93),
                   (7972.95, 1403.44, 8050.46, 4941.01, 3408.53),
                   (6691.53, 3072.34, 5511.09, 3787.53, 7382.24),
                   (6374.25, 7982.34, 8957.81, 6271.60, 2371.49),
                   (7959.80, 8286.09, 5217.63, 5700.50, 2795.59);

--AdmWorkHours
INSERT INTO AdmWorkHours (day, hours)
            VALUES ('Monday', 08.00),
                   ('Tuesday', 08.00),
                   ('Wednesday', 08.00),
                   ('Thursday', 08.00),
                   ('Friday', 05.00);

--Salesman
INSERT INTO Salesman(name, gender)
            VALUES ("Willie Kayley", 'M'),
                   ("Gypsy Tessie", 'F'),
                   ("Johnnie Candyce", 'M'),
                   ("Chanelle Kayly", 'F'),
                   ("Margery Ceara", 'F');

--Site
INSERT INTO Site(type, address, phone)
            VALUES ("TYPE_1", "2891 Garrett Street", 269-203-8123),
                   ("TYPE_2", "1675 Walt Nuzum Farm Road", 585-463-1052),
                   ("TYPE_2", "4890 Blane Street", 314-608-2228),
                   ("TYPE_4", "384 Hartland Avenue", 920-378-3132),
                   ("TYPE_3", "4764 Davis Court", 618-977-5316);

--TechnicalSupport
INSERT INTO TechnicalSupport(name, gender)
            VALUES ("Rainbow Nick",'M'),
                   ("Kehlani Sophia",'F'),
                   ("Brynn Berniece",'F'),
                   ("Erik Tianna",'M'),
                   ("Jaslyn Eunice",'F');

--Video
INSERT INTO Video(videoLength)
            VALUES (25),
                   (25),
                   (40),
                   (25),
                   (40);