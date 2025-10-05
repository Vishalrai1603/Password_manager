create database if not exists password_manager;

use password_manager;

create table user_credential(
    id int auto_increment primary key,
    website varchar(255) not null,
    username varchar(255) not null,
    password text  not null
);
