BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "home_campana" (
	"id_campana"	integer NOT NULL,
	"nombre_campana"	varchar(20) NOT NULL,
	"tipo"	varchar(20) NOT NULL,
	"estado"	varchar(10) NOT NULL,
	"precio"	decimal NOT NULL,
	PRIMARY KEY("id_campana" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "home_compra" (
	"id"	integer NOT NULL,
	"fecha_compra"	date NOT NULL,
	"cantidad"	integer NOT NULL,
	"dnisocio_id"	varchar(9) NOT NULL,
	"id_ingreso_id"	integer NOT NULL,
	"id_producto_id"	varchar(13) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("dnisocio_id") REFERENCES "home_socio"("DNISocio") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_ingreso_id") REFERENCES "home_ingreso"("id_ingreso") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_producto_id") REFERENCES "home_producto"("ID_producto") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "home_empleado" (
	"DNIEmpleado"	varchar(9) NOT NULL,
	"nombreEmpleado"	varchar(20) NOT NULL,
	"apellidosEmpleado"	varchar(40) NOT NULL,
	"cargo"	varchar(20) NOT NULL,
	"telefonoEmpleado"	varchar(20) NOT NULL,
	"emailEmpleado"	varchar(40) NOT NULL,
	"direccionEmpleado"	varchar(40) NOT NULL,
	"fecha_nacEmpleado"	date NOT NULL,
	PRIMARY KEY("DNIEmpleado")
);
CREATE TABLE IF NOT EXISTS "home_gasto" (
	"id_gasto"	integer NOT NULL,
	"monto_gasto"	decimal NOT NULL,
	PRIMARY KEY("id_gasto" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "home_genera" (
	"id"	integer NOT NULL,
	"fecha_genera"	date NOT NULL,
	"id_campana_id"	integer NOT NULL,
	"id_gasto_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_campana_id") REFERENCES "home_campana"("id_campana") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_gasto_id") REFERENCES "home_gasto"("id_gasto") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "home_ingreso" (
	"id_ingreso"	integer NOT NULL,
	"monto_ingreso"	decimal NOT NULL,
	PRIMARY KEY("id_ingreso" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "home_ordena" (
	"id"	integer NOT NULL,
	"cantidad"	integer NOT NULL,
	"fecha_gasto"	date NOT NULL,
	"hora_gasto"	datetime NOT NULL,
	"id_empleado_id"	varchar(9) NOT NULL,
	"id_gasto_id"	integer NOT NULL,
	"id_producto_id"	varchar(13) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_empleado_id") REFERENCES "home_empleado"("DNIEmpleado") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_gasto_id") REFERENCES "home_gasto"("id_gasto") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_producto_id") REFERENCES "home_producto"("ID_producto") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "home_producto" (
	"ID_producto"	varchar(13) NOT NULL,
	"nombre_producto"	varchar(24) NOT NULL,
	"cantidad"	integer NOT NULL,
	"precio"	decimal NOT NULL,
	"tallas"	varchar(60) NOT NULL,
	"proveedor"	varchar(24) NOT NULL,
	"avisar_restock"	bool NOT NULL,
	PRIMARY KEY("ID_producto")
);
CREATE TABLE IF NOT EXISTS "home_socio" (
	"DNISocio"	varchar(9) NOT NULL,
	"nombreSocio"	varchar(24) NOT NULL,
	"apellidosSocio"	varchar(24) NOT NULL,
	"emailSocio"	varchar(40) NOT NULL,
	"telefonoSocio"	varchar(9) NOT NULL,
	"direccionSocio"	varchar(40) NOT NULL,
	"fecha_nacSocio"	date,
	PRIMARY KEY("DNISocio")
);
COMMIT;
