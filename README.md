# EatWell
A Flask web app for a Databases class project. Allows users to keep a log of and view all foods they eat and all allergy-related symptoms they may have.

### Setup
After pulling the code, call `pip install -r requirements.txt` to install the necessary packages.

Next, you will need to create a file called *config.py* in the top level of the directory structure, and populate it with the following information:

```
MYSQL_DATABASE_USER = 'yourusername'
MYSQL_DATABASE_PASSWORD = 'yourpassword'
MYSQL_DATABASE_DB = 'eatwell'
MYSQL_DATABASE_HOST = 'localhost' 
```

Next, start mysql and run `use eatwell;` or create the eatwell database if it doesn't exist. Run `source setup.sql;` (You may need to add full path in front of file name). This will create all necessary tables and add some fake data.

Then just run `python run.py` and open localhost:5000.