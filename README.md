# EatWell
A Flask web app for a Databases class project. Allows users to keep a log of and view all foods they eat
and all allergy-related symptoms they may have.

### Setup
After pulling the code, call `pip install -r requirements.txt` to install the necessary packages.

Next, you will need to create a file called *config.py* in the top level of the directory structure,
and populate it with the following information:

```
MYSQL_DATABASE_USER = 'yourusername'
MYSQL_DATABASE_PASSWORD = 'yourpassword'
MYSQL_DATABASE_DB = 'yourdatabasename'
MYSQL_DATABASE_HOST = 'localhost' 
```

Then just run `python run.py` and open localhost:5000. 
