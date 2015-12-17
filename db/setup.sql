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
INSERT INTO Food_Item VALUES (0, 'Ham Sandwich');
INSERT INTO Food_Item VALUES (0, 'Donut');
INSERT INTO Food_Item VALUES (0, 'Chili');
INSERT INTO Food_Item VALUES (0, 'Graham Cracker');
INSERT INTO Food_Item VALUES (0, 'Caesar Salad');
INSERT INTO Food_Item VALUES (0, 'Yellow Cake');
INSERT INTO Food_Item VALUES (0, 'Pancakes');
INSERT INTO Food_Item VALUES (0, 'Coleslaw');
INSERT INTO Food_Item VALUES (0, 'Clam Chowder');
INSERT INTO Food_Item VALUES (0, 'Green Bean Casserole');
INSERT INTO Food_Item VALUES (0, 'Crab Cake');
INSERT INTO Food_Item VALUES (0, 'Corn on the Cob');
INSERT INTO Food_Item VALUES (0, 'Baked Potato');
INSERT INTO Food_Item VALUES (0, 'French Fries');
INSERT INTO Food_Item VALUES (0, 'Key Lime Pie');
INSERT INTO Food_Item VALUES (0, 'Fajitas');
INSERT INTO Food_Item VALUES (0, 'Sushi');
INSERT INTO Food_Item VALUES (0, 'Cioppino');
INSERT INTO Food_Item VALUES (0, 'Popcorn');
INSERT INTO Food_Item VALUES (0, 'Pork Chops');
INSERT INTO Food_Item VALUES (0, 'Nachos');

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
INSERT INTO Ingredient VALUES (0, 'Beans');
INSERT INTO Ingredient VALUES (0, 'Corn');
INSERT INTO Ingredient VALUES (0, 'Breadcrumbs');
INSERT INTO Ingredient VALUES (0, 'Cocoa Powder');
INSERT INTO Ingredient VALUES (0, 'Paprika');
INSERT INTO Ingredient VALUES (0, 'Maple Syrup');
INSERT INTO Ingredient VALUES (0, 'Peanut Butter');
INSERT INTO Ingredient VALUES (0, 'Jelly');
INSERT INTO Ingredient VALUES (0, 'Sugar');
INSERT INTO Ingredient VALUES (0, 'Honey');
INSERT INTO Ingredient VALUES (0, 'Mushroom');


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
INSERT INTO Eats VALUES (1, 1, '2015-11-15 18:46:29');
INSERT INTO Eats VALUES (1, 2, '2015-11-16 18:46:29');
INSERT INTO Eats VALUES (2, 2, '2015-11-17 18:46:29');

-- Insert into Has
INSERT INTO Has VALUES (1, 1, 'Mild', '2015-11-15 19:46:29');
INSERT INTO Has VALUES (2, 1, 'Moderate', '2015-11-16 19:46:29');
INSERT INTO Has VALUES (2, 2, 'Severe', '2015-11-17 19:46:29');

-- Insert into Contains

INSERT INTO Contains VALUES (43,1);
INSERT INTO Contains VALUES (20,1);
INSERT INTO Contains VALUES (57,1);
INSERT INTO Contains VALUES (24,1);
INSERT INTO Contains VALUES (13,1);

INSERT INTO Contains VALUES (,2);
INSERT INTO Contains VALUES (,2);
INSERT INTO Contains VALUES (,2);
INSERT INTO Contains VALUES (,2);
INSERT INTO Contains VALUES (,2);
40
 8
11
 2
 9

INSERT INTO Contains VALUES (,3);
INSERT INTO Contains VALUES (,3);
INSERT INTO Contains VALUES (,3);
INSERT INTO Contains VALUES (,3);
INSERT INTO Contains VALUES (,3);
55
56
 3
26
25

INSERT INTO Contains VALUES (,4);
INSERT INTO Contains VALUES (,4);
INSERT INTO Contains VALUES (,4);
INSERT INTO Contains VALUES (,4);
INSERT INTO Contains VALUES (,4);
29
63
31
46
36

INSERT INTO Contains VALUES (,5);
INSERT INTO Contains VALUES (,5);
INSERT INTO Contains VALUES (,5);
INSERT INTO Contains VALUES (,5);
INSERT INTO Contains VALUES (,5);
37
61
58
45
30

INSERT INTO Contains VALUES (,8);
INSERT INTO Contains VALUES (,8);
INSERT INTO Contains VALUES (,8);
INSERT INTO Contains VALUES (,8);
INSERT INTO Contains VALUES (,8);
15
 1
60
28
22

INSERT INTO Contains VALUES (,9);
INSERT INTO Contains VALUES (,9);
INSERT INTO Contains VALUES (,9);
INSERT INTO Contains VALUES (,9);
INSERT INTO Contains VALUES (,9);
21
51
23
59
64

INSERT INTO Contains VALUES (,10);
INSERT INTO Contains VALUES (,10);
INSERT INTO Contains VALUES (,10);
INSERT INTO Contains VALUES (,10);
INSERT INTO Contains VALUES (,10);
54
53
50
18
33

INSERT INTO Contains VALUES (,11);
INSERT INTO Contains VALUES (,11);
INSERT INTO Contains VALUES (,11);
INSERT INTO Contains VALUES (,11);
INSERT INTO Contains VALUES (,11);
6
47
10
35
16

INSERT INTO Contains VALUES (,12);
INSERT INTO Contains VALUES (,12);
INSERT INTO Contains VALUES (,12);
INSERT INTO Contains VALUES (,12);
INSERT INTO Contains VALUES (,12);
32
19
38
 4
48

INSERT INTO Contains VALUES (,13);
INSERT INTO Contains VALUES (,13);
INSERT INTO Contains VALUES (,13);
INSERT INTO Contains VALUES (,13);
INSERT INTO Contains VALUES (,13);
12
34
52
39
49

INSERT INTO Contains VALUES (,14);
INSERT INTO Contains VALUES (,14);
INSERT INTO Contains VALUES (,14);
INSERT INTO Contains VALUES (,14);
INSERT INTO Contains VALUES (,14);
14
27
17
 7
41

INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
 5
62
59
30
22

INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
36
52
17
39
31

INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
INSERT INTO Contains VALUES (,15);
56
26
28
12
 2

INSERT INTO Contains VALUES (,16);
INSERT INTO Contains VALUES (,16);
INSERT INTO Contains VALUES (,16);
INSERT INTO Contains VALUES (,16);
INSERT INTO Contains VALUES (,16);
35
61
19
 1
54

INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);

INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);

INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);
INSERT INTO Contains VALUES (,17);

INSERT INTO Contains VALUES (,18);
INSERT INTO Contains VALUES (,18);
INSERT INTO Contains VALUES (,18);
INSERT INTO Contains VALUES (,18);
INSERT INTO Contains VALUES (,18);

INSERT INTO Contains VALUES (,19);
INSERT INTO Contains VALUES (,19);
INSERT INTO Contains VALUES (,19);
INSERT INTO Contains VALUES (,19);
INSERT INTO Contains VALUES (,19);

INSERT INTO Contains VALUES (,20);
INSERT INTO Contains VALUES (,20);
INSERT INTO Contains VALUES (,20);
INSERT INTO Contains VALUES (,20);
INSERT INTO Contains VALUES (,20);

INSERT INTO Contains VALUES (,21);
INSERT INTO Contains VALUES (,21);
INSERT INTO Contains VALUES (,21);
INSERT INTO Contains VALUES (,21);
INSERT INTO Contains VALUES (,21);

INSERT INTO Contains VALUES (,22);
INSERT INTO Contains VALUES (,22);
INSERT INTO Contains VALUES (,22);
INSERT INTO Contains VALUES (,22);
INSERT INTO Contains VALUES (,22);

INSERT INTO Contains VALUES (,23);
INSERT INTO Contains VALUES (,23);
INSERT INTO Contains VALUES (,23);
INSERT INTO Contains VALUES (,23);
INSERT INTO Contains VALUES (,23);

INSERT INTO Contains VALUES (,24);
INSERT INTO Contains VALUES (,24);
INSERT INTO Contains VALUES (,24);
INSERT INTO Contains VALUES (,24);
INSERT INTO Contains VALUES (,24);

INSERT INTO Contains VALUES (,25);
INSERT INTO Contains VALUES (,25);
INSERT INTO Contains VALUES (,25);
INSERT INTO Contains VALUES (,25);
INSERT INTO Contains VALUES (,25);

INSERT INTO Contains VALUES (,26);
INSERT INTO Contains VALUES (,26);
INSERT INTO Contains VALUES (,26);
INSERT INTO Contains VALUES (,26);
INSERT INTO Contains VALUES (,26);

INSERT INTO Contains VALUES (,27);
INSERT INTO Contains VALUES (,27);
INSERT INTO Contains VALUES (,27);
INSERT INTO Contains VALUES (,27);
INSERT INTO Contains VALUES (,27);

INSERT INTO Contains VALUES (,28);
INSERT INTO Contains VALUES (,28);
INSERT INTO Contains VALUES (,28);
INSERT INTO Contains VALUES (,28);
INSERT INTO Contains VALUES (,28);

INSERT INTO Contains VALUES (,29);
INSERT INTO Contains VALUES (,29);
INSERT INTO Contains VALUES (,29);
INSERT INTO Contains VALUES (,29);
INSERT INTO Contains VALUES (,29);

INSERT INTO Contains VALUES (,30);
INSERT INTO Contains VALUES (,30);
INSERT INTO Contains VALUES (,30);
INSERT INTO Contains VALUES (,30);
INSERT INTO Contains VALUES (,30);

INSERT INTO Contains VALUES (,31);
INSERT INTO Contains VALUES (,31);
INSERT INTO Contains VALUES (,31);
INSERT INTO Contains VALUES (,31);
INSERT INTO Contains VALUES (,31);
INSERT INTO Contains VALUES (,31);

INSERT INTO Contains VALUES (,32);
INSERT INTO Contains VALUES (,32);
INSERT INTO Contains VALUES (,32);
INSERT INTO Contains VALUES (,32);
INSERT INTO Contains VALUES (,32);
INSERT INTO Contains VALUES (,32);

INSERT INTO Contains VALUES (,33);
INSERT INTO Contains VALUES (,33);
INSERT INTO Contains VALUES (,33);
INSERT INTO Contains VALUES (,33);
INSERT INTO Contains VALUES (,33);
INSERT INTO Contains VALUES (,33);

INSERT INTO Contains VALUES (,34);
INSERT INTO Contains VALUES (,34);
INSERT INTO Contains VALUES (,34);
INSERT INTO Contains VALUES (,34);
INSERT INTO Contains VALUES (,34);

INSERT INTO Contains VALUES (,35);
INSERT INTO Contains VALUES (,35);
INSERT INTO Contains VALUES (,35);
INSERT INTO Contains VALUES (,35);
INSERT INTO Contains VALUES (,35);

INSERT INTO Contains VALUES (,36);
INSERT INTO Contains VALUES (,36);
INSERT INTO Contains VALUES (,36);
INSERT INTO Contains VALUES (,36);
INSERT INTO Contains VALUES (,36);


-- Insert into Tagged_With
INSERT INTO Tagged_With VALUES (2, 1);
INSERT INTO Tagged_With VALUES (2, 2);
INSERT INTO Tagged_With VALUES (1, 2);
