DROP TABLE IF EXISTS baseball2014 CASCADE;
DROP TABLE IF EXISTS baseball2015 CASCADE;
DROP TABLE IF EXISTS baseball2016 CASCADE;
DROP TABLE IF EXISTS baseballWS2016 CASCADE;
DROP TABLE IF EXISTS starters2014 CASCADE;
DROP TABLE IF EXISTS starters2015 CASCADE;
DROP TABLE IF EXISTS starters2016 CASCADE;
DROP TABLE IF EXISTS startersWS2016 CASCADE;
DROP TABLE IF EXISTS TEMPORARY2014 CASCADE;
DROP TABLE IF EXISTS TEMPORARY2015 CASCADE;
DROP TABLE IF EXISTS TEMPORARY2016 CASCADE;
DROP TABLE IF EXISTS TEMPORARYWS2016 CASCADE;
DROP TABLE IF EXISTS TEMPORARYS2014 CASCADE;
DROP TABLE IF EXISTS TEMPORARYS2015 CASCADE;
DROP TABLE IF EXISTS TEMPORARYS2016 CASCADE;
DROP TABLE IF EXISTS TEMPORARYSWS2016 CASCADE;
DROP TABLE IF EXISTS PitchCountStarters2014 CASCADE;
DROP TABLE IF EXISTS PitchCountStarters2015 CASCADE;
DROP TABLE IF EXISTS PitchCountStarters2016 CASCADE;
DROP TABLE IF EXISTS PitchCountStartersWS2016 CASCADE;
DROP TABLE IF EXISTS TEMPORARYPC2014 CASCADE;
DROP TABLE IF EXISTS TEMPORARYPC2015 CASCADE;
DROP TABLE IF EXISTS TEMPORARYPC2016 CASCADE;
DROP TABLE IF EXISTS TEMPORARYPCWS2016 CASCADE;



-- VARIABLES TO PLACE IN EACH TABLE:
-- Release velocity, SpinRate, SpinDir, location (px, py, pz, szt,szb)
-- Release point (x,z), axial velocity (VX0, VY0, VZ0), accel (ax, ay, az)
-- Pitch result (everything), pitchType, probCalledStrike, PaResult, battedBallType



CREATE TABLE baseball2014 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4) 
);

CREATE TABLE baseball2015 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4)
);

CREATE TABLE baseball2016 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4)
);

CREATE TABLE baseballWS2016 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4)
);

CREATE TABLE starters2014 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4) 
);

CREATE TABLE starters2015 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4) 
);

CREATE TABLE starters2016 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4) 
);

CREATE TABLE startersWS2016 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4) 
);

CREATE TABLE PitchCountStarters2014 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	side character varying(1),
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4),
	visitingTeamCurrentRuns integer,
	homeTeamCurrentRuns integer,
	manOnFirst Boolean,
	manOnSecond Boolean,
	manOnThird Boolean,
	gamePitchCount integer
);


CREATE TABLE PitchCountStarters2015 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	side character varying(1),
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4),
	visitingTeamCurrentRuns integer,
	homeTeamCurrentRuns integer,
	manOnFirst Boolean,
	manOnSecond Boolean,
	manOnThird Boolean,
	gamePitchCount integer
);


CREATE TABLE PitchCountStarters2016 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	side character varying(1),
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4),
	visitingTeamCurrentRuns integer,
	homeTeamCurrentRuns integer,
	manOnFirst Boolean,
	manOnSecond Boolean,
	manOnThird Boolean,
	gamePitchCount integer
);


CREATE TABLE PitchCountStartersWS2016 (
	pitcherId integer,
	pitcher text,
	gameString character varying(50),
	inning integer,
	side character varying(1),
	pitchType character varying(3),
	releaseVelocity Numeric,
	spinRate Numeric, 
	spinDir Numeric,
	px Numeric,
	pz Numeric,
	szt Numeric,
	szb Numeric,
	x0 Numeric, 
	z0 Numeric,
	vx0 Numeric,
	vy0 Numeric,
	vz0 Numeric,
	ax Numeric,
	ay Numeric,
	az Numeric,
	probCalledStrike Numeric,
	paResult character varying(15),
	pitchResult character varying(5),
	battedBallType character varying(4),
	visitingTeamCurrentRuns integer,
	homeTeamCurrentRuns integer,
	manOnFirst Boolean,
	manOnSecond Boolean,
	manOnThird Boolean,
	gamePitchCount integer
);



-- CREATES TEMPORARY TABLE SO THAT WE MAY GATHER ONLY THE NEEDED COLUMNS
CREATE TABLE TEMPORARY2014 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric,spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text
);

CREATE TABLE TEMPORARY2015 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric,spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text
);

CREATE TABLE TEMPORARY2016 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text
);

CREATE TABLE TEMPORARYWS2016 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text
);

CREATE TABLE TEMPORARYS2014 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text
);

CREATE TABLE TEMPORARYS2015 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text
);

CREATE TABLE TEMPORARYS2016 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text
);

CREATE TABLE TEMPORARYSWS2016 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text
);

CREATE TABLE TEMPORARYPC2014 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text, gamePitchCount integer
);

CREATE TABLE TEMPORARYPC2015 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text, gamePitchCount integer
);

CREATE TABLE TEMPORARYPC2016 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text, gamePitchCount integer
);

CREATE TABLE TEMPORARYPCWS2016 (
	seasonYear integer, gameString text, gameDate text, gameType text, visitor text, home text, visitingTeamFinalRuns integer, homeTeamFinalRuns	integer, inning integer, side char(2), batterId integer, batter	text, batterHand char(2), pitcherId integer, pitcher text, pitcherHand char(2), catcherId integer,catcher text,umpireId integer,umpire text, timesFaced integer,batterPosition char (3),balls integer, strikes integer, outs integer,manOnFirst text,manOnSecond text,manOnThird text,endManOnFirst text,endManOnSecond TEXT,endManOnThird text,visitingTeamCurrentRuns integer,homeTeamCurrentRuns integer, pitchResult character varying(5),pitchType character varying(3), releaseVelocity Numeric, spinRate Numeric, spinDir Numeric,px Numeric,	pz Numeric, szt Numeric, szb Numeric,x0 Numeric, y0 Numeric,z0	Numeric, vx0 Numeric, vy0 Numeric,vz0 Numeric, ax Numeric, ay Numeric, az	Numeric, probCalledStrike Numeric, paResult character varying(15),runsHome integer, battedBallType character varying(4), battedBallAngle Numeric, battedBallDistance	Numeric, atbatDesc text, gamePitchCount integer
);

COPY TEMPORARY2014 FROM '/vagrant/project/mlb-hackathon-2017/2014.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARY2015 FROM '/vagrant/project/mlb-hackathon-2017/2015.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARY2016 FROM '/vagrant/project/mlb-hackathon-2017/2016.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYWS2016 FROM '/vagrant/project/mlb-hackathon-2017-samples/2016-WS.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYS2014 FROM '/vagrant/project/startersOnly_2014.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYS2015 FROM '/vagrant/project/startersOnly_2015.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYS2016 FROM '/vagrant/project/startersOnly_2016.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYSWS2016 FROM '/vagrant/project/startersOnly_2016-WS.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYPC2014 FROM '/vagrant/project/starters_Pitch_Count_2014.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYPC2015 FROM '/vagrant/project/starters_Pitch_Count_2015.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYPC2016 FROM '/vagrant/project/starters_Pitch_Count_2016.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');
COPY TEMPORARYPCWS2016 FROM '/vagrant/project/starters_Pitch_Count_2016-WS.csv' WITH
(FORMAT csv, HEADER true, DELIMITER ',');

INSERT INTO baseball2014 (pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType)
	(select pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType
	from TEMPORARY2014);

INSERT INTO baseball2015 (pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType)
	(select pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType
	from TEMPORARY2015);

INSERT INTO baseball2016 (pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType)
	(select pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType
	from TEMPORARY2016);

INSERT INTO baseballWS2016 (pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType)
	(select pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType
	from TEMPORARYWS2016);

INSERT INTO startersWS2016 (pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType)
	(select pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType
	from TEMPORARYSWS2016);

INSERT INTO starters2014 (pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType)
	(select pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType
	from TEMPORARYS2014);

INSERT INTO starters2015 (pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType)
	(select pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType
	from TEMPORARYS2015);

INSERT INTO starters2016 (pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType)
	(select pitcherId, pitcher, gameString, inning, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType
	from TEMPORARYS2016);

INSERT INTO PitchCountStarters2014 (pitcherId, pitcher, gameString, inning, side, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType, visitingTeamCurrentRuns, homeTeamCurrentRuns, manOnFirst, manOnSecond, manOnThird, gamePitchCount)
	(select pitcherId, pitcher, gameString, inning, side, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType, visitingTeamCurrentRuns, homeTeamCurrentRuns, manOnFirst, manOnSecond, manOnThird, gamePitchCount
	from TEMPORARYPC2014);

INSERT INTO PitchCountStarters2015 (pitcherId, pitcher, gameString, inning, side, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType, visitingTeamCurrentRuns, homeTeamCurrentRuns, manOnFirst, manOnSecond, manOnThird, gamePitchCount)
	(select pitcherId, pitcher, gameString, inning, side, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType, visitingTeamCurrentRuns, homeTeamCurrentRuns, manOnFirst, manOnSecond, manOnThird, gamePitchCount
	from TEMPORARYPC2015);
	
INSERT INTO PitchCountStarters2016 (pitcherId, pitcher, gameString, inning, side, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType, visitingTeamCurrentRuns, homeTeamCurrentRuns, manOnFirst, manOnSecond, manOnThird, gamePitchCount)
	(select pitcherId, pitcher, gameString, inning, side, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType, visitingTeamCurrentRuns, homeTeamCurrentRuns, manOnFirst, manOnSecond, manOnThird, gamePitchCount
	from TEMPORARYPC2016);

INSERT INTO PitchCountStartersWS2016 (pitcherId, pitcher, gameString, inning, side, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType, visitingTeamCurrentRuns, homeTeamCurrentRuns, manOnFirst, manOnSecond, manOnThird, gamePitchCount)
	(select pitcherId, pitcher, gameString, inning, side, pitchType, releaseVelocity, spinRate, spinDir, px, pz, szt, szb , x0, z0, vx0, vy0, vz0, ax, ay, az, probCalledStrike, paResult, pitchResult, battedBallType, visitingTeamCurrentRuns, homeTeamCurrentRuns, manOnFirst, manOnSecond, manOnThird, gamePitchCount
	from TEMPORARYPCWS2016);


-- ALTER TABLE ONLY baseball2014
--     ADD CONSTRAINT baseball2014_pkey PRIMARY KEY (pitcherId);

-- ALTER TABLE ONLY baseball2015
--     ADD CONSTRAINT baseball2015_pkey PRIMARY KEY (pitcherId);

-- ALTER TABLE ONLY baseball2016
--     ADD CONSTRAINT baseball2016_pkey PRIMARY KEY (pitcherId);

DROP TABLE TEMPORARYWS2016;
DROP TABLE TEMPORARYSWS2016;
DROP TABLE TEMPORARYS2014;
DROP TABLE TEMPORARYS2015;
DROP TABLE TEMPORARYS2016;
DROP TABLE TEMPORARY2014;
DROP TABLE TEMPORARY2015;
DROP TABLE TEMPORARY2016;
DROP TABLE TEMPORARYPC2014;
DROP TABLE TEMPORARYPC2015;
DROP TABLE TEMPORARYPC2016;
DROP TABLE TEMPORARYPCWS2016;
