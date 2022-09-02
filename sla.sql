create database bdsla;
use bdsla;

create table menu
(
id int unsigned not null auto_increment,
musica varchar(20),
artista  varchar(20),
album  varchar(20),
PRIMARY KEY (id)

);

select * from menu;