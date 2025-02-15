DROP DATABASE IF EXISTS SpookyVacation;

CREATE DATABASE SpookyVacation;

USE SpookyVacation;

CREATE TABLE IF NOT EXISTS Destination (
DestinationName varchar(30) not null,
activities varchar(30),
destination_price numeric(5,2),
PRIMARY KEY (DestinationName)
);

CREATE TABLE IF NOT EXISTS FamilyMember (
FamilyMemberName varchar(20) not null,
age int not null,
DestinationName varchar(30),
PRIMARY KEY (FamilyMemberName, age),
FOREIGN KEY (DestinationName) REFERENCES Destination (DestinationName) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS Costume (
CostumeName varchar(30) not null,
FamilyMemberName varchar(20) not null,
costume_price numeric(3,2) not null,
PRIMARY KEY (CostumeName, FamilyMemberName, costume_price),
FOREIGN KEY (FamilyMemberName) REFERENCES FamilyMember (FamilyMemberName) on update cascade on delete cascade
);

INSERT INTO Destination (DestinationName, activities, destination_price) VALUES ("Salem", "Witch Tour", 200.57)

INSERT INTO FamilyMember (FamilyMemberName, age, DestinationName) VALUES ("James", 24, "Salem")

INSERT INTO Costume (CostumeName, FamilyMemberName, costume_price) VALUES ("Sasuke", "James", 6.35)