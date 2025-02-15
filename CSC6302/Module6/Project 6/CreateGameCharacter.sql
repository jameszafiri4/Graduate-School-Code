DROP DATABASE IF EXISTS GameCharacter;

CREATE DATABASE GameCharacter;

USE GameCharacter;

CREATE TABLE IF NOT EXISTS GameUser (
Username varchar(30) not null,
UserLevel int not null,
UserAge int,
PRIMARY KEY (Username)
);

CREATE TABLE IF NOT EXISTS PlayerCharacter (
CharacterName varchar(30) not null,
Username varchar(30) not null,
CharacterLevel int not null,
CharacterType varchar(20) not null,
PRIMARY KEY (CharacterName, Username),
FOREIGN KEY (Username) REFERENCES GameUser (Username) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS Appearance (
CharacterName varchar(30) not null,
SkinColor varchar(20) not null,
Hairstyle varchar(20) not null,
HairColor varchar(20) not null,
Clothing varchar(30) not null,
PRIMARY KEY (CharacterName),
FOREIGN KEY (CharacterName) REFERENCES PlayerCharacter (CharacterName) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS Skill (
SkillName varchar(30) not null,
SkillLevel int not null,
CharacterName varchar(30) not null,
PRIMARY KEY (SkillName, CharacterName),
FOREIGN KEY (CharacterName) REFERENCES PlayerCharacter (CharacterName) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS Equipment (
ItemName varchar(30) not null,
Quantity int not null,
CharacterName varchar(30) not null,
PRIMARY KEY (ItemName, CharacterName),
FOREIGN KEY (CharacterName) REFERENCES PlayerCharacter (CharacterName) on update cascade on delete cascade
);

