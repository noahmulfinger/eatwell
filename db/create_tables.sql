use eatwell;

CREATE TABLE User(
 	user_id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	password VARCHAR(255) NOT NULL,
    UNIQUE KEY (email),
	PRIMARY KEY (user_id)
);

CREATE TABLE Food_Item(
	item_id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	PRIMARY KEY (item_id)
);

CREATE TABLE Symptom(
	symptom_id INT NOT NULL AUTO_INCREMENT,
	description VARCHAR(300) NOT NULL,
	PRIMARY KEY (symptom_id)
);

CREATE TABLE Badge(
	badge_id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	PRIMARY KEY (badge_id)
);

CREATE TABLE Ingredient(
   ingredient_id INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(100) NOT NULL,
   PRIMARY KEY (ingredient_id)
);

CREATE TABLE Eats(
	user_id INT NOT NULL,
	item_id INT NOT NULL,
	time DATETIME,
	PRIMARY KEY (user_id, item_id, time),
	FOREIGN KEY (user_id) REFERENCES User(user_id),
	FOREIGN KEY (item_id) REFERENCES Food_Item(item_id)
);

CREATE TABLE Has(
	symptom_id INT NOT NULL,
	user_id INT NOT NULL,
	rating VARCHAR(9),
	time DATETIME,
	PRIMARY KEY (symptom_id, user_id, time),
	FOREIGN KEY (symptom_id) REFERENCES Symptom(symptom_id),
	FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Tagged_With(
	badge_id INT NOT NULL,
   	item_id INT NOT NULL,
	PRIMARY KEY (badge_id, item_id),
   	FOREIGN KEY (badge_id) REFERENCES Badge(badge_id),
   	FOREIGN KEY (item_id) REFERENCES Food_Item(item_id)
);

CREATE TABLE Contains(
   	ingredient_id INT NOT NULL,
   	item_id INT NOT NULL,
	PRIMARY KEY (ingredient_id, item_id),
   	FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id),
   	FOREIGN KEY (item_id) REFERENCES Food_Item(item_id)
);

CREATE TABLE Caused_By(
	symptom_id INT NOT NULL,
	badge_id INT NOT NULL,
	PRIMARY KEY (symptom_id, badge_id),
	FOREIGN KEY (badge_id) REFERENCES Badge(badge_id),
   	FOREIGN KEY (symptom_id) REFERENCES Symptom(symptom_id)
);