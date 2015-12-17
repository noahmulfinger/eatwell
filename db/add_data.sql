use eatwell;

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
INSERT INTO Ingredient VALUES (0, 'Avacado');

-- Insert into Symptoms
INSERT INTO Symptom VALUES (0, 'Headache');
INSERT INTO Symptom VALUES (0, 'Nausea');
INSERT INTO Symptom VALUES (0, 'Bloating');
INSERT INTO Symptom VALUES (0, 'Migraine');
INSERT INTO Symptom VALUES (0, 'Cough');
INSERT INTO Symptom VALUES (0, 'Stomach ache');
INSERT INTO Symptom VALUES (0, 'Hives');
INSERT INTO Symptom VALUES (0, 'Irritable Bowel');

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






