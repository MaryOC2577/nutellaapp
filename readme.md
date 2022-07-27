# **Project 8 - Create a platform for nutella lovers**

## **What does the program do ?**
The purpose of the program is to interact with the Open Food Facts public database.
The program also makes it possible to offer the user a healthier product than the product he has selected. The user can create an acount and save products as favorites.
Project monitoring is available [here](https://trello.com/b/leyj9b2n/projet-8-amateurs-de-nutella).
The repository on GitHub is availiable [here](https://github.com/MaryOC2577/nutellaapp.git).

## **Requirements**
* Visual Studio Code version : 1.69.2
* Visual Studio Code dependencies : django, selenium, pytest, heroku, gunicorn...
* Virtual environnement with venv module.
* Python version : 3.10.2

## **Setup the program**
* Step 1
    * Open the project in Visual Studio Code.
* Step 2
    1. Create a virtual environment in the project by executing the following commands in the terminal.
    2. python -m venv .venv : 
    3. . .venv.Scripts.activate 
    4. Add requirements : pip freeze > requirements.txt
* Step 3
    * In the terminal : python manage.py populate_db category_name number_of_pages number_of_products. This command allows you to populate the database, category_name indicates the category of the products, number_of_pages indicates the number of maximum pages and number_of_products indicates the maximum products.

## **How to use**
In the terminal : python manage.py runserver to launch the application. Open the link in your brower and you can use the application.
