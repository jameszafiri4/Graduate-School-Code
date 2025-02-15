/* CSC3810 Databases
	Professor Minton
*/

/* This SQL script creates a new database, the MarioKArt database, and inserts some data into the database.
	This will be another example database we will be using in this course. */

-- First, lets add a database to work with, and let's use the MarioKart set of relations. We can do this with the UI, using the "Add Schema" button, or we can write the SQL

-- Its good practice to check if the database exists before adding it, especially in a database script like this one. That way, you can run it multiple times!
DROP DATABASE IF EXISTS MarioKart;

-- Create the database MarioKart. Note this is the SQL Create Statement that is written for you when you use the UI to create a new schema
-- Also note that create schema is synonomous to create database in MySql. 
-- This is not true in Sql Server. It is a decision that the database engine creators decided to make.
CREATE DATABASE MarioKart;

-- Because we are using a script, and because a script let's us execute against different databases, even in the same script, we have to tell it what database we want to use. If we want to use a different 
-- database later on, we would use another "Use" statement to indicate that. But we are going to stick to the MarioKart Database.
USE MarioKart;

-- Now, we need to create the tables, which are how SQL internally stores a relation, and all the information about that relation. Notice that these create table SQL statements are very
-- similiar to our relation's schemas. Again, its a good practice to check if a table exists before creating it. We can drop tables if they currently exist. I'll show both ways in this script. The rest of the table definition should be familiar.
-- We see out relation/table name, its attributes in a comma seperated list, the domains of each attribute, and we define a primary key
--  The domain has more information then we've seen before: it talks about if an attribute can be null.

-- When I went to create the Character relation, I noticed that our attribute Character.Name was a poor choice, as Name is a MySql keyword.
-- Also not that I could name this relation "Character", as Character was a reserved MySQL keyword, and you cannot have MySql keywords as relation names.
-- Its good practice to not use keywords as attribute or table names. Also not that we are paying attention not only to our attribute domains, but if we allow nulls.
CREATE TABLE IF NOT EXISTS NintendoCharacter (
CharacterName varchar(50)  not null,
IconFileName varchar(200) not null,
Color varchar(10),
Speed int not null,
Acceleration int not null,
Weight int not null,
Handeling int not null,
Traction int not null,
Turbo int not null,
PRIMARY KEY (CharacterName)
);

insert into NintendoCharacter (CharacterName, IconFileName, Color, Speed, Acceleration, Weight, Handeling, Traction, Turbo) values ("Daisy", "DaisyFile.txt", "Orange", 1, 2, 3, 4, 5, 6);
insert into NintendoCharacter (CharacterName, IconFileName, Color, Speed, Acceleration, Weight, Handeling, Traction, Turbo) values ("Shy Guy", "ShyGuyFile.txt", "Black", 2, 3, 4, 5, 6, 7);
insert into NintendoCharacter (CharacterName, IconFileName, Color, Speed, Acceleration, Weight, Handeling, Traction, Turbo) values ("Donkey Kong", "DKFile.txt", "Brown", 3, 4, 5, 6, 7, 8);
insert into NintendoCharacter (CharacterName, IconFileName, Color, Speed, Acceleration, Weight, Handeling, Traction, Turbo) values ("Lakitu", "LakituFile.txt", "Yellow", 4, 5, 6, 7, 8, 9);

-- Let's add the other tables we defined. We can note that these tables have a lot of similarites, and we may start to wonder if we could revise out design to take advantage
-- of all this common data. We absolutly can, and will in our BCNF lab later in the course. For now, let's leave it as is.
CREATE TABLE IF NOT EXISTS KartData (
KartName varchar(50)  not null,
IconFileName varchar(200) not null,
Color varchar(10),
SpeedModifier double not null,
AccelerationModifier double not null,
WeightModifier double not null,
HandelingModifier double not null,
TractionModifier double not null,
TurboModifier double not null,
PRIMARY KEY (KartName)
);

insert into KartData (KartName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Yoshi Bike", "YoshiBikeFile.txt", 1, 2, 3, 4, 5, 6);
insert into KartData (KartName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Sport Bike", "SportBikeFile.txt", 2, 3, 4, 5, 6, 7);
insert into KartData (KartName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Biddy Buggy", "BiddyBuddyFile.txt", 3, 4, 5, 6, 7, 8);
insert into KartData (KartName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Cat Cruiser", "SportBikeFile.txt", 4, 5, 6, 7, 8, 9);

CREATE TABLE IF NOT EXISTS WheelData (
WheelName varchar(50)  not null,
IconFileName varchar(200) not null,
Color varchar(10),
SpeedModifier double not null,
AccelerationModifier double not null,
WeightModifier double not null,
HandelingModifier double not null,
TractionModifier double not null,
TurboModifier double not null,
PRIMARY KEY (WheelName)
);

insert into WheelData (WheelName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Slick", "SlickFile.txt", 4, 5, 6, 7, 8, 9);
insert into WheelData (WheelName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Button", "ButtonFile.txt", 5, 6, 7, 8, 9, 10);
insert into WheelData (WheelName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Sponge", "SpongeFile.txt", 3, 4, 5, 6, 7, 8);
insert into WheelData (WheelName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Wood", "WoodFile.txt", 2, 5, 10, 7, 8, 9);


CREATE TABLE IF NOT EXISTS GliderData (
GliderName varchar(50)  not null,
IconFileName varchar(200) not null,
Color varchar(10),
SpeedModifier double not null,
AccelerationModifier double not null,
WeightModifier double not null,
HandelingModifier double not null,
TractionModifier double not null,
TurboModifier double not null,
PRIMARY KEY (GliderName)
);

insert into GliderData (GliderName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Flower Glider", "FlowerFile.txt", 4, 5, 6, 7, 8, 9);
insert into GliderData (GliderName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Cloud", "CloudFile.txt", 5, 6, 7, 8, 9, 10);
insert into GliderData (GliderName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Jet Plane", "SpongeFile.txt", 3, 4, 5, 6, 7, 8);
insert into GliderData (GliderName, IconFileName, SpeedModifier, AccelerationModifier, WeightModifier, HandelingModifier, TractionModifier, TurboModifier) values ("Waddle Wing", "WaddleWingFile.txt", 2, 5, 10, 7, 8, 9);


CREATE TABLE IF NOT EXISTS PlayerCustomOptions (
PlayerId int not null,
TransmissionType varchar(10) not null,
StayOnTrack bool not null,
ControllerSettings varchar(20) not null,
GyroscopeEnabled bool not null,
PRIMARY KEY (PlayerId)
);

insert into PlayerCustomOptions (PlayerId, TransmissionType, StayOnTrack, ControllerSettings, GyroscopeEnabled) values (1, "auto", false, "standard", true);
insert into PlayerCustomOptions (PlayerId, TransmissionType, StayOnTrack, ControllerSettings, GyroscopeEnabled) values (2, "auto", false, "tilt", true);
insert into PlayerCustomOptions (PlayerId, TransmissionType, StayOnTrack, ControllerSettings, GyroscopeEnabled) values (3, "auto", false, "standard", false);
insert into PlayerCustomOptions (PlayerId, TransmissionType, StayOnTrack, ControllerSettings, GyroscopeEnabled) values (4, "auto", false, "tilt", true);

CREATE TABLE IF NOT EXISTS TrackData (
Id int not null,
TrackName varchar(100) not null,
OriginalPlatform varchar(100) not null,
PRIMARY KEY(Id)
);

insert into TrackData (Id, TrackName, OriginalPlatform) values (1, "Moo Moo Meadows", "Wii");
insert into TrackData (Id, TrackName, OriginalPlatform) values (2, "Boo Lake", "Switch");

CREATE TABLE IF NOT EXISTS CupData (
Id int not null auto_increment,
PlatformName varchar(100) not null,
CupName varchar(100) not null,
PRIMARY KEY (Id)
);

insert into CupData (Id, CupName, PlatformName) values (1, "Mushroom Cup", "Super Nintendo");
insert into CupData (Id, CupName, PlatformName) values (2, "Flower Cup", "Super Nintendo");



CREATE TABLE IF NOT EXISTS CupTracks (
Id int not null auto_increment,
TrackId int not null,
CupId int not null,
PRIMARY KEY (Id),
FOREIGN KEY (TrackId) REFERENCES TrackData (Id) on update cascade on delete cascade,
FOREIGN KEY (CupId) REFERENCES CupData (Id) on update cascade on delete cascade
);

insert into CupTracks (TrackId, CupId) values (1, 1);
insert into CupTracks (TrackId, CupId) values (1, 2);
insert into CupTracks (TrackId, CupId) values (2, 1);
insert into CupTracks (TrackId, CupId) values (2, 2);


-- This is the first example we have in our schema of a Mapping Table. The sole purpose of this table is gather all the high level information about a race. We can then join
-- to the other tables, using the foreign key relationships, to get more information about a Player, a Character, a Kart, a Wheel or a Glider. 
-- I added some information about a race we didn't have in class: ranking and Time.
-- For now, track name is just a value, but we could absolutly add a Track relation to store more information about tracks. Maybe we will come back to this.
CREATE TABLE IF NOT EXISTS RacerData (
RaceId int not null,
PlayerId int not null,
CharacterName varchar(50) not null,
KartName varchar(50) not null,
WheelName varchar(50) not null,
GliderName varchar(50) not null,
Ranking int not null,
RaceTime Time not null,
CupTrackId int not null,
PRIMARY KEY (RaceId),
FOREIGN KEY (PlayerId) REFERENCES PlayerCustomOptions (PlayerId) on update cascade on delete cascade,
FOREIGN KEY (CharacterName) REFERENCES NintendoCharacter (CharacterName) on update cascade on delete cascade,
FOREIGN KEY (KartName) REFERENCES KartData (KartName) on update cascade on delete cascade,
FOREIGN KEY (WheelName) REFERENCES WheelData (WheelName) on update cascade on delete cascade,
FOREIGN KEY (GliderName) REFERENCES GliderData (GliderName) on update cascade on delete cascade,
FOREIGN KEY (CupTrackId) REFERENCES CupTracks (Id) on update cascade on delete cascade
);

insert into RacerData(RaceId, PlayerId, CharacterName, KartName, WheelName, GliderName, Ranking, RaceTime, CupTrackId) values (1, 1, "Daisy", "Yoshi Bike", "Slick", "Flower Glider", 3, CURRENT_TIMESTAMP, 1);
insert into RacerData(RaceId, PlayerId, CharacterName, KartName, WheelName, GliderName, Ranking, RaceTime, CupTrackId) values (2, 2, "Shy Guy", "Sport Bike", "Button", "Cloud", 1, CURRENT_TIMESTAMP, 1);
insert into RacerData(RaceId, PlayerId, CharacterName, KartName, WheelName, GliderName, Ranking, RaceTime, CupTrackId) values (3, 3, "Donkey Kong", "Biddy Buggy", "Sponge", "Waddle Wing", 4, CURRENT_TIMESTAMP, 1);
insert into RacerData(RaceId, PlayerId, CharacterName, KartName, WheelName, GliderName, Ranking, RaceTime, CupTrackId) values (4, 1, "Lakitu", "Cat Cruiser", "Wood", "Jet Plane", 2, CURRENT_TIMESTAMP, 1);

