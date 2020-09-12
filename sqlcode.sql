drop database if exists python2;
create database python2;
use python2;

create table if not exists customertier(
	`customername` varchar(70),
    `tier` varchar(20),
    primary key(`customerid`)
);

insert into customertier( `customername`, `tier`)
values('Animesh Nepal','Black');
insert into customertier( `customername`, `tier`)
values('David Blake','Silver');
insert into customertier( `customername`, `tier`)
values('John Grayson','Gold');
insert into customertier( `customername`, `tier`)
values('Jai Crimples','Silver');
insert into customertier( `customername`, `tier`)
values('Jack Stark','Gold');

create table if not exists supplies(
	`buns` int,
    `noodles` int,
    `flour` int, 
    `tomato` int,
    `drinks` int,
    `beef` int,
    `tissues` int
);

insert into supplies(`buns`, `noodles`, `flour`, `tomato`, `drinks`, `beef`, `tissues`)
values(13,45,24,0,148,32,679);
insert into supplies(`buns`, `noodles`, `flour`, `tomato`, `drinks`, `beef`, `tissues`)
values(123,45,24,0,148,32,679);


SELECT SUM(`buns`)
FROM supplies;
SELECT SUM(`noodles`)
FROM supplies;
SELECT SUM(`flour`)
FROM supplies;
SELECT SUM(`tomato`)
FROM supplies;
SELECT SUM(`drinks`)
FROM supplies;
SELECT SUM(`beef`)
FROM supplies;
SELECT SUM(`tissues`)
FROM supplies;


select * from customertier



