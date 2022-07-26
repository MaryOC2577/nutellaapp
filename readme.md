# **Project 5 - Use public data from Open Food Facts**

## **What does the program do ?**
The purpose of the program is to interact with the Open Food Facts public database.
The program also makes it possible to offer the user a healthier product than the product he has selected.
Project monitoring is available [here](https://trello.com/b/DOCsE4s0/projet-5-utilisez-les-donn%C3%A9es-publiques-de-lopenfoodsfacts).
The repository on GitHub is availiable [here](https://github.com/MaryOC2577/projet_5.git).

## **Requirements**
* Visual Studio Code version : 1.53.1
* Visual Studio Code dependencies : flake8, pylint, pydocstyle, black, pylance and mypy.
* Virtual environnement with venv module.
* Python version : 3.8.2
* MySQL version : 3.5.2

## **Setup the database**
Before using the application, install MySQL version 3.5.2 in localhost.
* Step 1
    1. Create a user and set a password with root access.
    2. CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'mypassword';
*  Step 2
    1. Grant privileges to the new user.
    2. GRANT ALL PRIVILEGES ON * . * TO 'new_user'@'localhost';
* Setp 3
    * Launch mysql with the new user account.
* Step 4
    1. Execute the following instructions in SQL.
    2. CREATE DATABASE product;
    3. USE DATABASE product;

## **Setup the program**
* Step 1
    * Open the project in Visual Studio Code.
* Step 2
    1. Create a virtual environment in the project by executing the following commands in the terminal.
    2. python -m venv .venv : 
    3. . .venv.Scripts.activate 
* Step 3
    * Change user and password in file **-config.py-**, use the one created in mysql.
* Step 4
    * Launch the application with the command python **-main.py-** in Visual Studio Code.

## **How to use**
On first use of the application choose first option in the main menu
to create the database and insert data.
If you have **register user name and password in config file** when the setup is done you 
should choose second option to use the application.
