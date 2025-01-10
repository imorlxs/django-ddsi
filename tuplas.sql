BEGIN TRANSACTION;
INSERT INTO "home_campana" VALUES (1,'Promoción Verano','Publicidad','activa',1000.5),
 (2,'Descuento Invierno','Ofertas','pendiente',750.75),
 (3,'Promoción Otoño','Publicidad','finalizada',560.6),
 (4,'Ofertas Navidad','Descuentos','activa',950.1),
 (5,'Campaña San Valentin','Ofertas','pendiente',1250.4),
 (6,'Rebajas Junio','Publicidad','finalizada',1800.2),
 (7,'Descuento Primavera','Ofertas','activa',650.25),
 (8,'Promoción Año Nuevo','Publicidad','pendiente',700.45),
 (9,'Ofertas Semana Santa','Descuentos','activa',1600.3),
 (10,'Ofertas Black Friday','Descuentos','finalizada',1300.15);
 
INSERT INTO "home_compra" VALUES (1,'2025-01-10',12,'12345678X',1,'0012345678901'),
 (2,'2025-01-10',43,'12345678X',2,'0023456789012'),
 (3,'2025-01-10',21,'23456789Y',3,'0034567890123'),
 (4,'2025-01-10',20,'45678901W',4,'0034567890123'),
 (5,'2025-01-10',150,'56789012V',5,'0067890123456'),
 (6,'2025-01-10',40,'67890123U',6,'0101234567890'),
 (7,'2025-01-10',21,'23456789Y',7,'0045678901234'),
 (8,'2025-01-10',53,'45678901W',8,'0089012345678'),
 (9,'2025-01-10',112,'34567890Z',9,'0034567890123'),
 (11,'2025-01-10',40,'23456789Y',11,'0045678901234');
 
INSERT INTO "home_empleado" VALUES ('12345678A','Carlos','García Pérez','Gerente','654123987','carlos.garcia@example.com','Calle Mayor, 15','1985-02-14'),
 ('23456789B','Laura','Fernández Gómez','Secretario','656789432','laura.fernandez@example.com','Calle Sol, 22','1990-11-30'),
 ('34567890C','David','Ruiz Sánchez','Contable','678987234','david.ruiz@example.com','Calle Luna, 7','1988-07-22'),
 ('45678901D','Ana','Martínez López','Recepcionista','612987234','ana.martinez@example.com','Avenida de la Paz, 45','1995-09-15'),
 ('56789012E','Marta','Sanz Jiménez','Técnico','612398123','marta.sanz@example.com','Paseo del Prado, 3','1987-05-04'),
 ('67890123F','Jorge','Pérez Gutiérrez','Vendedor','678234987','jorge.perez@example.com','Calle Nueva, 17','1992-03-19'),
 ('78901234G','Sara','Romero Gil','Analista','611567432','sara.romero@example.com','Calle Norte, 9','1994-12-08'),
 ('89012345H','Pablo','Vidal Ortiz','Consultor','612789456','pablo.vidal@example.com','Avenida Central, 6','1991-06-18'),
 ('90123456I','Lucía','Castro García','Ingeniero','615123678','lucia.castro@example.com','Calle Oeste, 12','1989-10-05'),
 ('01234567J','Roberto','Blanco Muñoz','Desarrollador','614567987','roberto.blanco@example.com','Calle Sur, 34','1993-01-11');
 
INSERT INTO "home_gasto" VALUES (1,1000.5),
 (2,750.75),
 (3,560.6),
 (4,950.1),
 (5,1250.4),
 (6,1800.2),
 (7,650.25),
 (8,700.45),
 (9,1600.3),
 (10,1300.15),
 (11,47.97),
 (12,357),
 (13,180),
 (14,894.4),
 (15,63.75),
 (16,229.77),
 (17,172.5),
 (18,564.2),
 (19,22.8),
 (20,87.96);
 
INSERT INTO "home_genera" VALUES (1,'2025-01-10',1,1),
 (2,'2025-01-10',2,2),
 (3,'2025-01-10',3,3),
 (4,'2025-01-10',4,4),
 (5,'2025-01-10',5,5),
 (6,'2025-01-10',6,6),
 (7,'2025-01-10',7,7),
 (8,'2025-01-10',8,8),
 (9,'2025-01-10',9,9),
 (10,'2025-01-10',10,10);
 
INSERT INTO "home_ingreso" VALUES (1,191.88),
 (2,1096.5),
 (3,945),
 (4,900),
 (5,1498.5),
 (6,879.6),
 (7,1173.9),
 (8,964.6),
 (9,5040),
 (11,2236);
 
INSERT INTO "home_ordena" VALUES (1,3,'2025-01-10','2025-01-10 05:20:38.237579','12345678A',11,'0012345678901'),
 (2,14,'2025-01-10','2025-01-10 05:20:44.748721','23456789B',12,'0023456789012'),
 (3,4,'2025-01-10','2025-01-10 05:20:52.552845','34567890C',13,'0034567890123'),
 (4,16,'2025-01-10','2025-01-10 05:21:00.075932','56789012E',14,'0045678901234'),
 (5,5,'2025-01-10','2025-01-10 05:21:07.670691','23456789B',15,'0056789012345'),
 (6,23,'2025-01-10','2025-01-10 05:21:23.653486','45678901D',16,'0067890123456'),
 (7,23,'2025-01-10','2025-01-10 05:21:29.961583','34567890C',17,'0078901234567'),
 (8,31,'2025-01-10','2025-01-10 05:21:39.135079','56789012E',18,'0089012345678'),
 (9,2,'2025-01-10','2025-01-10 05:21:45.170872','34567890C',19,'0090123456789'),
 (10,4,'2025-01-10','2025-01-10 05:21:50.089160','23456789B',20,'0101234567890');
 
INSERT INTO "home_producto" VALUES ('0012345678901','Camiseta',91,15.99,'S,M,L,XL','Proveedor1',0),
 ('0023456789012','Pantalones',171,25.5,'M,L,XL','Proveedor2',0),
 ('0034567890123','Zapatos',-99,45,'39,40,41,42,43','Proveedor3',1),
 ('0045678901234','Chaqueta',25,55.9,'M,L','Proveedor4',1),
 ('0056789012345','Sombrero',35,12.75,'Única','Proveedor5',0),
 ('0067890123456','Guantes',23,9.99,'S,M,L','Proveedor1',0),
 ('0078901234567','Bufanda',83,7.5,'Única','Proveedor3',0),
 ('0089012345678','Corbata',-2,18.2,'Única','Proveedor2',1),
 ('0090123456789','Gorra',82,11.4,'Única','Proveedor4',0),
 ('0101234567890','Cinturón',4,21.99,'M,L','Proveedor5',1);
 
INSERT INTO "home_socio" VALUES ('12345678X','Alberto','López Díaz','alberto.lopez@example.com','612345678','Calle del Sol, 23','1990-05-12'),
 ('23456789Y','Beatriz','Moreno García','beatriz.moreno@example.com','622345678','Avenida de Europa, 45','1985-08-20'),
 ('34567890Z','Cristina','Rodríguez Torres','cristina.rodriguez@example.com','632345678','Calle de las Flores, 8','1992-02-28'),
 ('45678901W','Daniel','Martín López','daniel.martin@example.com','642345678','Calle del Río, 12','1988-11-11'),
 ('56789012V','Elena','Gómez Pérez','elena.gomez@example.com','652345678','Calle de los Árboles, 22','1987-06-25'),
 ('67890123U','Fernando','Herrera Ruiz','fernando.herrera@example.com','662345678','Avenida del Mar, 4','1991-09-10'),
 ('78901234T','Gloria','Ramos García','gloria.ramos@example.com','672345678','Calle del Sol, 15','1984-01-17'),
 ('89012345S','Héctor','Gutiérrez Sánchez','hector.gutierrez@example.com','682345678','Paseo de la Estación, 29','1989-04-14'),
 ('90123456R','Irene','Fernández Gómez','irene.fernandez@example.com','692345678','Calle del Parque, 30','1993-07-07'),
 ('01234567Q','Javier','Jiménez López','javier.jimenez@example.com','602345678','Calle de la Paz, 9','1994-03-09');
COMMIT;
