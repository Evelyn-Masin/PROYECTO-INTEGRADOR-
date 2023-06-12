use bd_ejemplo_big_bread_sa;
-- Tabla productos
create table productos(
       idproductos integer primary key,
       nombre varchar(50) not null unique,
       descripcion varchar(256) null,
       stock bit default(1),
       precio_menor decimal(11,2) not null,
       precio_mayor decimal(11,2) not null);
       -- Tabla insumos 
 create table insumos(
       idinsumos integer primary key,
       idcategoria integer not null,
       codigo varchar(50) null,
       designacion varchar(256) not null unique,
       stock decimal(11,2) not null,
       estado bit (1),
       idproductos integer,
       FOREIGN KEY (idproductos) REFERENCES productos(idproductos));
       
-- Tabla produccion diaria
create table produccion_diaria(
	   idproduccion integer primary key,
       idcategoria integer not null,
       codigo varchar(50) null,
       designacion varchar(256) not null unique,
       stock decimal(11,2) not null,
       estado bit (1),
        idproductos integer,
       FOREIGN KEY (idproductos) REFERENCES productos(idproductos));
-- Tabla recetas 
create table recetas(
       idrecetas integer primary key,
       idcategoria integer not null,
       codigo varchar(50) null,
       detalle varchar(256) not null unique,
       idproductos integer,
       FOREIGN KEY (idproductos) REFERENCES productos(idproductos));
SHOW tables;

