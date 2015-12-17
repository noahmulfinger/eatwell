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

-- Insert users
INSERT INTO User VALUES (0,'Noah','noah.mulfinger@gmail.com','pbkdf2:sha1:1000$iwazD2Qu$3f67f37871586b05d666bb47060a26349097c009');
INSERT INTO User VALUES (0,'Shinjini','sjvnunna@gmail.com','pbkdf2:sha1:1000$XWpiv2I1$aa4328aa681b396bd4180dd0893d152742d1a65c');


-- Insert food items
INSERT INTO Food_Item VALUES (0, 'Hamburger');
INSERT INTO Food_Item VALUES (0, 'Chicken Pasta');
INSERT INTO Food_Item VALUES (0, 'Apple Pie');
INSERT INTO Food_Item VALUES (0, 'French Toast');
INSERT INTO Food_Item VALUES (0, 'Chicken Piccata');
INSERT INTO Food_Item VALUES (0, 'Chicken Tacos');
INSERT INTO Food_Item VALUES (0, 'Chicken Pasta');
INSERT INTO Food_Item VALUES (0, 'Roast Beef');
INSERT INTO Food_Item VALUES (0, 'Lasagna');
INSERT INTO Food_Item VALUES (0, 'Quesadillas');
INSERT INTO Food_Item VALUES (0, 'Chocolate Chip Cookie');
INSERT INTO Food_Item VALUES (0, 'Cheesecake');
INSERT INTO Food_Item VALUES (0, 'Eggs Benedict');
INSERT INTO Food_Item VALUES (0, 'Chocolate Walnut Fudge');
INSERT INTO Food_Item VALUES (0, 'Tilapia');
INSERT INTO Food_Item VALUES (0, 'Pork Chops');

-- Insert into ingredients
INSERT INTO Ingredient VALUES (0, 'Lettuce');
INSERT INTO Ingredient VALUES (0, 'Tomato');
INSERT INTO Ingredient VALUES (0, 'Onion');
INSERT INTO Ingredient VALUES (0, 'Swiss Cheese');
INSERT INTO Ingredient VALUES (0, 'Beef');
INSERT INTO Ingredient VALUES (0, 'Mustard');
INSERT INTO Ingredient VALUES (0, 'Mayonaisse');
INSERT INTO Ingredient VALUES (0, 'Pasta');
INSERT INTO Ingredient VALUES (0, 'Red Onion');
INSERT INTO Ingredient VALUES (0, 'Olive Oil');
INSERT INTO Ingredient VALUES (0, 'Garlic');
INSERT INTO Ingredient VALUES (0, 'Chicken');
INSERT INTO Ingredient VALUES (0, 'Feta Cheese');
INSERT INTO Ingredient VALUES (0, 'Parsley');
INSERT INTO Ingredient VALUES (0, 'Salt');
INSERT INTO Ingredient VALUES (0, 'Pepper');
INSERT INTO Ingredient VALUES (0, 'Egg');
INSERT INTO Ingredient VALUES (0, 'Cheese');
INSERT INTO Ingredient VALUES (0, 'Milk');
INSERT INTO Ingredient VALUES (0, 'Apple');
INSERT INTO Ingredient VALUES (0, 'Strawberries');
INSERT INTO Ingredient VALUES (0, 'Tomatoes');
INSERT INTO Ingredient VALUES (0, 'Chocolate');
INSERT INTO Ingredient VALUES (0, 'Wine');
INSERT INTO Ingredient VALUES (0, 'Bananas');
INSERT INTO Ingredient VALUES (0, 'Avocado');
INSERT INTO Ingredient VALUES (0, 'Ginger');
INSERT INTO Ingredient VALUES (0, 'Red Pepper');
INSERT INTO Ingredient VALUES (0, 'Apple Juice');
INSERT INTO Ingredient VALUES (0, 'Brown Sugar');
INSERT INTO Ingredient VALUES (0, 'Ketchup');
INSERT INTO Ingredient VALUES (0, 'Vinegar');
INSERT INTO Ingredient VALUES (0, 'Water');
INSERT INTO Ingredient VALUES (0, 'Soy Sauce');
INSERT INTO Ingredient VALUES (0, 'Rosemary');
INSERT INTO Ingredient VALUES (0, 'Black Pepper');
INSERT INTO Ingredient VALUES (0, 'Flour');
INSERT INTO Ingredient VALUES (0, 'Baking Soda');
INSERT INTO Ingredient VALUES (0, 'Butter');
INSERT INTO Ingredient VALUES (0, 'Vanilla');
INSERT INTO Ingredient VALUES (0, 'Pasta');
INSERT INTO Ingredient VALUES (0, 'Bread');
INSERT INTO Ingredient VALUES (0, 'Carrots');
INSERT INTO Ingredient VALUES (0, 'Celery');
INSERT INTO Ingredient VALUES (0, 'Tortilla');
INSERT INTO Ingredient VALUES (0, 'Potatoes');
INSERT INTO Ingredient VALUES (0, 'Sausage');
INSERT INTO Ingredient VALUES (0, 'Bacon');
INSERT INTO Ingredient VALUES (0, 'Whipped Cream');
INSERT INTO Ingredient VALUES (0, 'Cumin');
INSERT INTO Ingredient VALUES (0, 'Margarine');
INSERT INTO Ingredient VALUES (0, 'Broccoli');
INSERT INTO Ingredient VALUES (0, 'Cauliflower');



-- Insert into Symptoms
INSERT INTO Symptom VALUES (0, 'Headache');
INSERT INTO Symptom VALUES (0, 'Nausea');
INSERT INTO Symptom VALUES (0, 'Bloating');
INSERT INTO Symptom VALUES (0, 'Migraine');
INSERT INTO Symptom VALUES (0, 'Cough');
INSERT INTO Symptom VALUES (0, 'Stomach ache');
INSERT INTO Symptom VALUES (0, 'Hives');
INSERT INTO Symptom VALUES (0, 'Irritable bowel');

-- Insert into Badges
INSERT INTO Badge VALUES (0, 'Gluten');
INSERT INTO Badge VALUES (0, 'Lactose');
INSERT INTO Badge VALUES (0, 'Fructose');
INSERT INTO Badge VALUES (0, 'Salicylates');
INSERT INTO Badge VALUES (0, 'Amines');
-- Insert into Eats

-- Insert into Eats
INSERT INTO Eats VALUES (1, 1, '2015-11-15 18:46:29');
INSERT INTO Eats VALUES (1, 2, '2015-11-16 18:46:29');
INSERT INTO Eats VALUES (2, 2, '2015-11-17 18:46:29');

-- Insert into Has
INSERT INTO Has VALUES (1, 1, 'Mild', '2015-11-15 19:46:29');
INSERT INTO Has VALUES (2, 1, 'Moderate', '2015-11-16 19:46:29');
INSERT INTO Has VALUES (2, 2, 'Severe', '2015-11-17 19:46:29');

-- Insert into Contains
INSERT INTO Contains VALUES (1, 1);
INSERT INTO Contains VALUES (2, 1);
INSERT INTO Contains VALUES (3, 1);
INSERT INTO Contains VALUES (4, 1);
INSERT INTO Contains VALUES (5, 1);
INSERT INTO Contains VALUES (6, 1);
INSERT INTO Contains VALUES (7, 1);
INSERT INTO Contains VALUES (8, 1);
INSERT INTO Contains VALUES (9, 2);
INSERT INTO Contains VALUES (10, 2);
INSERT INTO Contains VALUES (11, 2);
INSERT INTO Contains VALUES (12, 2);
INSERT INTO Contains VALUES (13, 2);
INSERT INTO Contains VALUES (14, 2);
INSERT INTO Contains VALUES (15, 2);
INSERT INTO Contains VALUES (16, 2);

-- Insert into Tagged_With
INSERT INTO Tagged_With VALUES (2, 1);
INSERT INTO Tagged_With VALUES (2, 2);
INSERT INTO Tagged_With VALUES (1, 2);
