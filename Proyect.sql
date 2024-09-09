create database clientesdb;
use clientesdb;
create table usuarios(
    id int auto_increment,
    nombres varchar(40),
    apellidos varchar(40),
    partida varchar(40),
    precio varchar(40),
    fecha date,
    descripcion longtext,
    primary key (id)
);

insert into usuarios values (null, "Sebastian", "Bueno", "Comun", "100", "2024/08/29", "");
insert into usuarios values (null, "Luciano", "Ayala", "Profesional", "200", "", "Quiere que sea en 5 tandas el juego");
insert into usuarios values (null, "Sol", "Carhuapoma", "Profesional", "150", "2025/01/12", "Tiene un descuento el 25%");