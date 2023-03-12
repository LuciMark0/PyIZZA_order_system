#siüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüüü
from pizza_full_database import pizza_Database,addition_Metarial 
pizza_db = pizza_Database()
component_db = addition_Metarial()

first_select_ui = """
Select a database to take action:
1 => Pizza database
2 => Component database
3 => Exit

Action: """

pizza_select_ui = """
Select to take action:
1 => Show Pizzas
2 => Add Pizza
3 => Delete Pizza
4 => Update a pizza
5 => Go back

Action: """

pizza_update_ui = """
Select to take action:
1 => Update Cost
2 => Update Description

Action: """

component_select_ui = """
Select to take action:
1 => Show components
2 => Add component
3 => Delete component
4 => Update a component
5 => Go back

Action: """

component_update_ui = """
Select to take action:
1 => Update Cost
2 => Update Description

Action: """

def admin_ui_system():
    while True:
        first_select = input(first_select_ui)
        if first_select in ["1","2"]:
            while True:
                if first_select == "1":
                    pizza_selected = input(pizza_select_ui)
                    if pizza_selected == "1":
                        for pizza in pizza_db.get_all_pizza():
                            print(pizza)

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
                    component_selected = input(component_select_ui)
                    if component_selected == "1":
                        for component in component_db.get_all_addmade():
                            print(component)

                    elif component_selected == "2":
                        component_name = input("component name: ")
                        component_cost = input("component cost: ")
                        component_description = input("component description: ")
                        component_db.insert_addmade(component_name, component_cost, component_description)
                    
                    elif component_selected == "3":
                        component_name = input("component name: ")
                        component_db.delete_addmade(component_name)
                    
                    elif component_selected == "4":
                        while True:
                            component_update_selected = input(component_update_ui)
                            if component_update_selected == "1":
                                component_name = input("component name: ")
                                component_cost = input("component new cost: ") 
                                component_db.update_price_addmade(component_name, component_cost)
                                break

                            elif component_update_selected == "2":
                                component_name = input("component name: ")
                                component_description = input("component new description: ")
                                component_db.update__description_addmade(component_name, component_description)
                                break
                    
                    elif component_selected == "5":
                        break

        elif first_select == "3":
            break

admin_ui_system()