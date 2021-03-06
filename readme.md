# AI Driven Personalized Menu Content for the QSR Drive Thru

In 2022, the experience of going and ordering food at a drive thru is the same for every customer at every restaurant. At the start of every drive thru line you are presented with the same menu that you saw last week. It never changes to fit your tastes, never changes recommendations, and never learns. A smart menu could incorporate dietary restrictions, environmental conditions, and your past orders to provide recommendations that will fit your palate and preferences. Even though 70% of all fast food orders occur in the drive thru, the lack of personalization in the process can make this convenient process unpleasant and slow, reducing the chance that customers will return.

___

# Motivation/Project Goal
This project has been sponsored by Delphi Display Systems and was completed as part of the coursework for COMPSCI 180A/B, Capstone Project in CS at UC Irvine over the span of two academic quarters. Our main goal for the project is a proof of concept that such a system can be implemented. If our proof of concept is successful, the project could be further pursued and deployed to help make the drive thru experience faster and more personalized.
____
# How to Use
### [CSV Generator](https://github.com/GottaGitGoing/cs180_2/blob/main/SQL/csv_generator.py)
Part of the project required us to come up with dummy customer data to train and test our recommender system. Rather than manually creating complex characters and order histories, we’ve created this python script to make up customers and their order histories.

_Requirements:_
- Python
- Sklearn. TensorFlow. Pandas. Numpy. 
- an [item.csv](https://github.com/GottaGitGoing/cs180_2/blob/main/SQL/CSVs/item.csv) must be propagated and placed in the [CSV folder](https://github.com/GottaGitGoing/cs180_2/tree/main/SQL/CSVs)

_How to Run Script:_
1. Make direct changes to the csv_generator script to specify numbers of customers, orders, and customizations to create. The defaults are as follows:
```py
NUM_CUSTOMERS = 200
NUM_ORDERS = 2000
NUM_ORDER_ITEM_CUSTOMIZATIONS = 500
```
2. Navigate to SQL directory and run
```py
python csv_generator.py
```
3. Check the [CSV folder](https://github.com/GottaGitGoing/cs180_2/tree/main/SQL/CSVs) to see the newly generated csv files.

### [PostgreSQL DB](https://github.com/GottaGitGoing/cs180_2/tree/main/SQL)
The database that stores the customer and restaurant data is running on PostgreSQL 14. This database is queried to create the CSV files for the engine, and can eventually have the new order data incorporated back into it. The schema of the database is:

## NOTE to contributors: Still need to upload the images to a folder on github.
<p align="center">
  <img alt="Database Scheme" src="#">
</p>

_Requirements:_
- PostgreSQL

_How to Populate the PostgreSQL DB w/ Data:_
1. Ensure PostgreSQL is running, and enter into the CLI using
```console
psql
```
2. Create the Delphi Database and connect to it using (while in psql CLI):
```console
CREATE DATABASE delphi;
\c delphi
```
3. Change to the directory where the three .sql scripts are located (delphi.sql, reset.sql, and populate_tables.sql) using
```console
\cd <PATH_TO_DIRECTORY>
```
4. To create the schema, run
```console
\i delphi.sql
```
5. To populate the database using the CSVs created from the CSV generator, ensure the "CSVs" folder created by the generator script is in the current directory, and run
```console
\i reset.sql
```
6. The database should now be initialized and populated. You can run
```console
\dt delphi.*
```
to see a list of tables, and you can run standard SQL queries like SELECT to see the data.

### [Object-Relational Mapping (ORM)](https://github.com/GottaGitGoing/cs180_2/tree/main/ORM)
The ORM interfaces with the database and makes it easier to do SQL operations. Our script extracts columns from the tables that we use in the engine.

_Requirements:_
- Python
- SQLAlchemy

_How to Create CSVs for the Engine from the ORM:_
1. Ensure the PostgreSQL database is running and has been initialized and populated
2. Ensure that the database variables in ```delphi.py``` are correct. The default values are:
```python
db_username = 'postgres'
db_password = 'postgres'
db_hostname = 'localhost:5432'
db_database = 'delphi'
```
3. To extract the CSV's, run
```python
python extract_csvs.py
```
4. Check the [CSVs folder](https://github.com/GottaGitGoing/cs180_2/tree/main/ORM/CSVs) to see the newly generated CSV files

# Recommendation Engine:
### Overview
The Recommendations are generated by 1 or more machine learning models. Each model obtains some of the data from the databases. 
The models then train themselves to predict a user’s rating of a menu item. Each of these models will have a different basis from which it will make their recommendation, so some may use temporal data extensively and others will weigh ingredients. 
At the end these separate predictions will be averaged out in some way to make the final recommendation which will be sent to the customer.

### Functional Requirements(Based on our team interpretation of Delphi’s instructions)
- Engine must use data from the above mentioned databases as input and train Machine Learning models which can produce a ranking of items when provided with a specific user ID
	- The prominent data points of note include: 
		- The Menu of items upon which to predict with
		- The Nutritional information of each item on the menu
		- User Orders(collection of menu items ordered in a single 	transaction by a specific user)
		- Environmental Conditions when orders took place
		- User Dietary Restrictions
		- User Taste Preferences
- There must exist a way of representing the preferences of a user that is generalizable across different menus and allow cross restaurant recommendations
	- Thus, orders made from Menu A will update a user’s preferences which can be used to recommend items for that user from Menu B
- The preferences of a user should be updated when that user makes new orders and the updated preferences should be committed to the database
	- NOTE: this can be a separate system from the Recommendation Engine but it is placed here because it is closely related

### Design Thoughts
- We did not directly use dietary restrictions, might need separate filter. 
- A look into NLP for tag extraction from item description might be wise.
- Using Bayesian Personalized Ranking should be the prototype's eventual goal. 

### Current Status (June 2022):
We have completed development of two models and partially developed a third. The two working models we have both use Singular Value Decomposition to predict the unknown cells of a user-item matrix. These models count the number of times each user has ordered each item on the menu and uses that value as the score/rating metric. These models do not use time data, environmental data, or dietary restrictions whatsoever.
The third model is a neural network which was planned to use time, temperature, and a derived user score for the item to make its predictions.

**SVD 1:**
- DESCRIPTION MISSING
_Requirements:_
- Jupyter Notebook

**SVD 2:**
- This SVD takes a different approach to rating items. Every repeat item increases an item’s popularity by one fixed score. However, the baseline predictor is still the same as above.
_Requirements:_
- Jupyter Notebook. 

**Note: Google Colab will have the neccessary libraries, needed in the notebook, mentioned earlier**

# Resources:
- Kim Falk's [Practical Recommender Systems.](https://www.manning.com/books/practical-recommender-systems) Multiple resources exist to acquire the book.

# Authors
Team 2, also known as Delephantx, was brought together and had the opportunity to work together through the CS180A/B Capstone Course. The name comes from “del” - the fact that we were sponsored by Delphi Display Systems and “elephant” - we decided to use PostgreSQL and our discord server’s icon was an elephant (by chance)! 

Introducing our teammates: 
[Arian Namavar](https://github.com/GottaGitGoing) (team leader) - c/o 2022, B.S. in Computer Science
[Ezra Hammond](https://github.com/ebhammond) - c/o 2023, B.S. in Computer Science
[Ryan Sakuma](https://github.com/RSkuma) -  c/o 2022, B.S. in Computer Science
[Rieko Konishi](https://github.com/riekokonishi) - c/o 2022, B.S. in Computer Science

# Acknowledgements
We appreciate the help of our course instructors Professor Sergio Gago-Massague and our TA Hamza Errahmouni. The guidance, check-ups, and feedback we receieved from them was an invaluable part of our development process. Furthermore, We appreciate Ken Kneeld, our sponsor and CEO of Delphi Display Systems, and  Ali Malik, and Matt Nam, the lead developers whom we had weekly meetings with regarding project update and progress. 
___

#### Delephantx team.