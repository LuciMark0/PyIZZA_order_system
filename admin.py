#siüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüü
from pizza_full_database import pizza_Database, addition_Metarial 
from data_analyst import (
    pizza_database_name_addmade_func, 
    pizza_database_together_addmade_func, 
    how_many_best_selling_pizzas
)

pizza_db = pizza_Database()
ingredients_db = addition_Metarial()

first_select_ui = """Select a database to take action:
1 => Pizza database
2 => Ingredients database
3 => Sales analytics
4 => Exit

Action: """

pizza_select_ui = """Select an action to perform on the Pizza database:
1 => Show Pizzas
2 => Add Pizza
3 => Delete Pizza
4 => Update Pizza
5 => Go back

Action: """

pizza_update_ui = """Select a field to update for the Pizza:
1 => Update Cost
2 => Update Description

Action: """

ingredients_select_ui = """Select an action to perform on the Ingredients database:
1 => Show Ingredients
2 => Add Ingredients
3 => Delete Ingredients
4 => Update Ingredients
5 => Go back

Action: """

ingredients_update_ui = """Select a field to update for the Ingredients:
1 => Update Cost
2 => Update Description

Action: """

analytics_select_ui = """Select an action to perform on the Sales analytics:
1 => Show sales graph for pizzas with additional ingredients
2 => Show sales graph for additional ingredients
3 => Show best-selling analytics
4 => Go back

Action: """




def admin_ui_system():
    while True:
        first_select = input(first_select_ui)
        if first_select in ["1","2","3"]:
            while True:
                if first_select == "1":
                    pizza_selected = input(pizza_select_ui)
                    if pizza_selected == "1":
                        for pizza in pizza_db.get_all_pizza():
                            print(pizza)
                        input("\nPress enter to continue\n")

                    elif pizza_selected == "2":
                        pizza_name = input("Pizza name: ")
                        pizza_cost = input("Pizza cost: ")
                        pizza_description = input("Pizza description: ")
                        pizza_db.insert_pizza(pizza_name, pizza_cost, pizza_description)
                    
                    elif pizza_selected == "3":
                        pizza_name = input("Pizza name: ")
                        pizza_db.delete_pizza(pizza_name)
                    
                    elif pizza_selected == "4":
                        while True:
                            pizza_update_selected = input(pizza_update_ui)
                            if pizza_update_selected == "1":
                                pizza_name = input("Pizza name: ")
                                pizza_cost = input("Pizza new cost: ") 
                                pizza_db.update_price_pizza(pizza_name, pizza_cost)
                                break

                            elif pizza_update_selected == "2":
                                pizza_name = input("Pizza name: ")
                                pizza_description = input("Pizza new description: ")
                                pizza_db.update__description_pizza(pizza_name, pizza_description)
                                break
                    
                    elif pizza_selected == "5":
                        break
                
                if first_select == "2":
                    ingredients_selected = input(ingredients_select_ui)
                    if ingredients_selected == "1":
                        for ingredients in ingredients_db.get_all_addmade():
                            print(ingredients)
                        input("\nPress enter to continue\n")

                    elif ingredients_selected == "2":
                        ingredients_name = input("ingredients name: ")
                        ingredients_cost = input("ingredients cost: ")
                        ingredients_description = input("ingredients description: ")
                        ingredients_db.insert_addmade(ingredients_name, ingredients_cost, ingredients_description)
                    
                    elif ingredients_selected == "3":
                        ingredients_name = input("ingredients name: ")
                        ingredients_db.delete_addmade(ingredients_name)
                    
                    elif ingredients_selected == "4":
                        while True:
                            ingredients_update_selected = input(ingredients_update_ui)
                            if ingredients_update_selected == "1":
                                ingredients_name = input("ingredients name: ")
                                ingredients_cost = input("ingredients new cost: ") 
                                ingredients_db.update_price_addmade(ingredients_name, ingredients_cost)
                                break

                            elif ingredients_update_selected == "2":
                                ingredients_name = input("ingredients name: ")
                                ingredients_description = input("ingredients new description: ")
                                ingredients_db.update__description_addmade(ingredients_name, ingredients_description)
                                break
                    
                    elif ingredients_selected == "5":
                        break

                if first_select == "3":
                    analytic_selected = input(analytics_select_ui)
                    if analytic_selected == "1":
                        pizza_database_name_addmade_func()
                    elif analytic_selected == "2":
                        pizza_database_together_addmade_func()
                    elif analytic_selected == "3":
                        how_many_best_selling_pizzas(int(input("How much analytic do you want to see: ")))
                        input("\nPress enter to continue\n")
                    elif analytic_selected == "4":
                        break

        elif first_select == "4":
            break

admin_ui_system()
