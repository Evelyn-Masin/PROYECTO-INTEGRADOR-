create database BD_EJEMPLO_Big_Bread_SA,
use bd_ejemplo_Big_Bread_SA,
create table BIG_Bread (productos varchar,insumos varchar,produccion diaria varchar,Recetas varchar),
-- Tabla productos
create table productos(
       idproductos integer primary key identity,
       nombre varchar(50) not null unique,
       descripcion varchar(256) null,
       stock bit default(1),
       precio_menor decimal(11,2) not null,
       precio_mayor decimal(11,2) not null,
       );
insert into producto (nombre,descripcion,stock,precio_menor,precio_mayor) values ('Cereales','');
select * from producto;
delete idproductos,
-- Tabla insumos 
 create table insumos(
       idinsumos integer primary key codigo,
       idcategoria integer not null,
       codigo varchar(50) null,
       designacion varchar(256) not null unique,
       stock integer not null(1),
       estado bit default(1),
       FOREIGN KEY (idproductos) REFERENCES categoria(idproductos),
       ); 
-- Tabla produccion diaria
create table produccion diaria(
	   idproduccion integer primary key,
       idcategoria integer not null,
       codigo varchar(50) null,
       designacion varchar(256) not null unique,
       stock integer not null(1),
       estado bit default(1),
       FOREIGN KEY (idproductos) REFERENCES categoria(idproductos),
       );
-- Tabla recetas 
create table recetas(
       idrecetas integer primary key ,
       idcategoria integer not null,
       codigo varchar(50) null,
       detalle varchar(256) not null unique,
       FOREIGN KEY (idproductos) REFERENCES categoria(idproductos),
       );       


 

