DROP DATABASE IF EXISTS HolidayParty;

CREATE DATABASE HolidayParty;

USE HolidayParty;

CREATE TABLE IF NOT EXISTS Music (
SongName varchar (40) not null,
Genre varchar (20),
Artist varchar (40),
PRIMARY KEY (SongName)
);

CREATE TABLE IF NOT EXISTS Game (
GameName varchar(40) not null,
Prize varchar(50) not null,
Rules varchar(200),
PRIMARY KEY (GameName)
);

CREATE TABLE IF NOT EXISTS Food (
MealName varchar(40) not null,
Price int,
PRIMARY KEY (MealName)
);

CREATE TABLE IF NOT EXISTS Decorator (
DecoratorName varchar(50) not null,
Contact varchar(50) not null,
PRIMARY KEY (DecoratorName)
);

CREATE TABLE IF NOT EXISTS PartyInfo (
PartyName varchar(50) not null,
PartyDate Date not null,
PartyTheme varchar(30) not null,
PartyLocation varchar(40) not null,
DecoratorName varchar(50) not null,
PRIMARY KEY (PartyName),
FOREIGN KEY (DecoratorName) REFERENCES Decorator (DecoratorName) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS Employee (
EmployeeName varchar(50) not null,
Contact varchar(50) not null,
RSVP bool not null,
PartyName varchar(50) not null,
SongName varchar (40) not null,
MealName varchar(40) not null,
GameName varchar(40) not null,
PRIMARY KEY (EmployeeName),
FOREIGN KEY (PartyName) REFERENCES PartyInfo (PartyName) on update cascade on delete cascade,
FOREIGN KEY (SongName) REFERENCES Music (SongName) on update cascade on delete cascade,
FOREIGN KEY (MealName) REFERENCES Food (MealName) on update cascade on delete cascade,
FOREIGN KEY (GameName) REFERENCES Game (GameName) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS Gift (
GiftName varchar(50) not null,
GiftType varchar(30) not null,
EmployeeName varchar(50) not null,
PRIMARY KEY (GiftName),
FOREIGN KEY (EmployeeName) REFERENCES Employee (EmployeeName) on update cascade on delete cascade
);

