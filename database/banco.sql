create database TDPListdb;
Use TDPListdb;

create table tbl_tarefas(
	id int primary key auto_increment,
    nome varchar(255) not null,
    status varchar(50) not null,
    data_criada timestamp default current_timestamp,
    atualizada_em timestamp default current_timestamp on update current_timestamp
);