\copy (select * from startersws2016 order by pitcherId DESC, gameString, inning ASC) To '/vagrant/project/2016WS_Starter_Order.csv' DELIMITER ',' CSV HEADER