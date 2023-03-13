# PyIZZA_order_system

## Description
PyIZZA_order_system is a pizza ordering system designed with a user-friendly PyQt5 interface. The project was developed by **Göktuğ Kaan Koz** and **[Hasan Özcan](https://github.com/Hasan26ozcan)** as their final project for the Global AI Hub Akbank Python Bootcamp. This system allows customers to easily select their preferred pizza and additional ingredients, view their order in a cart, input their credit card details, and receive a receipt. The system also features an admin panel that enables menu modification and analysis of sales data through visualized data.

## Folder_Contents
The project folder contains the following files:

- **start.py**: This file contains the login screen and is the starting point of the application.
- **register.py**: This file contains the register screen where users can create a new account.
- **forgot_password.py**: This file contains the forgot password screen to reset passwords.
- **pizza_order.py**: This file contains the screen where users can select pizzas and additional ingredients for their orders.
- **pizza_cart.py**: This file contains the cart screen which displays the selected orders.
- **card_purchase.py**: This file contains the credit card input screen where users can enter their payment details.
- **receipt.py**: This file contains the receipt screen which displays the order details.
- **pizza_full_database.py**: This file contains all the databases, including customer information, pizzas, additional ingredients, credit card information, etc.
- **admin.py**: This file houses the admin control panel, where administrators can modify the menu and perform sales analysis using visualized data.

## Libraries Used
The following libraries were used in this project:

- ```PyQt5```: Used to create the graphical user interface.
- ```sqlite3```  Used to manage the databases.
- ```pandas```: Used to manipulate and analyze data.
- ```matplotlib```: Used to visualize and plot data.
- ```re```:  Used to validate user inputs.
- ```validator_collection```: Used to validate email addresses.
- ```datetime```: Used to track the purchase time.
- ```sys```: Used to safely exit the application.

## How To Use
To use the PyIZZA_order_system, ensure that the file names are the same as listed above. If you change the file names, update the references in the code. To begin the application, run the **start.py** file and use the user interface buttons to navigate through the screens. to modify the menu and perform sales analysis, use the **admin.py** file and follow the instructions on the command panel.

## Contribution
If you find any issues or want to contribute to this project, feel free to create a pull request or submit an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
