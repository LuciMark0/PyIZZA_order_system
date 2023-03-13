import sqlite3

createCustomerTable = """CREATE TABLE IF NOT EXISTS customer 
(personal_number TEXT PRIMARY KEY,
customer_name TEXT NOT NULL, 
password TEXT NOT NULL, 
e_mail TEXT NOT NULL UNIQUE);"""

insertCustomer = "INSERT OR IGNORE INTO customer (personal_number,customer_name, password,e_mail) VALUES (?, ?, ?, ?);"

AllCustomer = "SELECT * FROM customer;"

checkForLogin = "SELECT personal_number from customer WHERE e_mail=? AND password =? ;"

updatepassword="UPDATE customer SET password = ? WHERE personal_number = ? AND e_mail= ? ;"

updatecustomername="UPDATE customer SET customer_name = ? WHERE personal_number = ? AND e_mail= ? ;"

deletecustomer= "DELETE FROM customer WHERE personal_number= ? ;"

personalnumbercheck="SELECT personal_number FROM customer WHERE personal_number=? ;"

forget_password_check = "SELECT * FROM customer WHERE personal_number=? AND e_mail =?;"

get_customer_name = "SELECT customer_name FROM customer WHERE personal_number=? ;"
#-------------------------------------------------------------------end

class Customer_Database:
    def __init__(self) -> None:
        self.con = sqlite3.connect("a.db")
        self.cur = self.con.cursor()
        self.create_tables()

    
    def create_tables(self):
        self.cur.execute(createCustomerTable)

    
    def insert_customer(self,personal_number,customer_name, password,e_mail):
        self.cur.execute(insertCustomer, (personal_number,customer_name, password,e_mail))
        self.con.commit()


    def get_all_customer(self):
        return self.cur.execute(AllCustomer).fetchall()


    def check_login(self,e_mail,password):
        return self.cur.execute(checkForLogin,(e_mail,password)).fetchone()[0]
        # farklı bir sayfaya buradan gideceğiz yeni bir masaüstü uygulması buradan açılacak
        
    def personal_number_checked(self,personal_number):
        return self.cur.execute(personalnumbercheck,(personal_number,)).fetchone()

    def forget_password_check_func(self,  personal_number,e_mail):
        return self.cur.execute(forget_password_check,(personal_number,e_mail)).fetchone()
    
    def get_name_by_id(self, personal_numb):
        return self.cur.execute(get_customer_name,(personal_numb,)).fetchone()

    def update_password(self,password,personal_number,e_mail):
        # farklı sayfadan alınacak
        self.cur.execute(updatepassword,(password,personal_number,e_mail))
        self.con.commit()

    def update_customername(self,customername,personal_number,e_mail):
        self.cur.execute(updatecustomername,(customername,personal_number,e_mail))
        self.con.commit()
    
    
    def delete_customer(self,personal_number):
        self.cur.execute(deletecustomer, (personal_number,))
        self.con.commit()
 
#-------------------------------------------------------------------end
createpizzaTable="""CREATE TABLE IF NOT EXISTS pizza 
(pizza_name TEXT PRIMARY KEY,price TEXT NOT NULL,description TEXT NOT NULL);"""

insertpizza = "INSERT OR IGNORE INTO pizza (pizza_name, price, description) VALUES ( ?, ?, ?);"

AllPizza = "SELECT * FROM pizza;"

deletepizza= "DELETE FROM pizza WHERE pizza_name= ? ;"

updatepizzaprice="UPDATE pizza SET price = ? WHERE pizza_name = ? ;"

updatepizzadescription="UPDATE pizza SET description = ? WHERE pizza_name = ? ;"

#PRİCE VE DESCRİPTİON UPDATE
class pizza_Database:
    def __init__(self):
        self.con = sqlite3.connect("a.db")
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute(createpizzaTable)
    
    def insert_pizza(self,pizza_name,price,description):
        self.cur.execute(insertpizza, (pizza_name,price,description))
        self.con.commit()
    
    def get_all_pizza(self):
        return self.cur.execute(AllPizza).fetchall()
    
    def update_price_pizza(self,pizza_name,price):
        # farklı sayfadan alınacak
        self.cur.execute(updatepizzaprice,(price,pizza_name))
        self.con.commit()


    def update__description_pizza(self,pizza_name,description):
        # farklı sayfadan alınacak
        self.cur.execute(updatepizzadescription,(description,pizza_name))
        self.con.commit()


    def delete_pizza(self,pizza_name):
        self.cur.execute(deletepizza, (pizza_name,))
        self.con.commit()

#-------------------------------------------------------------------end


createaddmadeTable="""CREATE TABLE IF NOT EXISTS addmade 
(addmade_name TEXT PRIMARY KEY,price TEXT NOT NULL,description TEXT NOT NULL);"""

insertaddmade = "INSERT OR IGNORE INTO addmade (addmade_name, price, description) VALUES ( ?, ?, ?);"

AllAddmade = "SELECT * FROM addmade;"

deleteAddmade= "DELETE FROM addmade WHERE addmade_name= ? ;"

updateAddmadeprice="UPDATE addmade SET price = ? WHERE addmade_name = ? ;"

updateAddmadedescription="UPDATE addmade SET description = ? WHERE addmade_name = ? ;"
class addition_Metarial:
    def __init__(self) -> None:
        self.con = sqlite3.connect("a.db")
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute(createaddmadeTable)

    def insert_addmade(self,addmade_name,price,description):
        self.cur.execute(insertaddmade, (addmade_name,price,description))
        self.con.commit()
    
    def get_all_addmade(self):
        return self.cur.execute(AllAddmade).fetchall()
    
    def update_price_addmade(self,addmade_name,price):
        # farklı sayfadan alınacak
        self.cur.execute(updateAddmadeprice,(price,addmade_name))
        self.con.commit()

    def update__description_addmade(self,addmade_name,description):
        # farklı sayfadan alınacak
        self.cur.execute(updateAddmadedescription,(description,addmade_name))
        self.con.commit()


    def delete_addmade(self,addmade_name):
        self.cur.execute(deleteAddmade, (addmade_name,))
        self.con.commit()
#-------------------------------------------------------------------end


createcredicardTable="""CREATE TABLE IF NOT EXISTS credicard 
(personal_id TEXT PRIMARY KEY,credicardnumber TEXT NOT NULL,credicarddate TEXT NOT NULL,credicardcvv TEXT NOT NULL);"""

insertcredicard = "INSERT OR IGNORE INTO credicard (personal_id, credicardnumber, credicarddate, credicardcvv) VALUES (?, ?, ?, ?);"

Allcredicard = "SELECT * FROM credicard;"

check_credit_card = "SELECT * FROM credicard WHERE personal_id = ?"

deletecredicard= "DELETE FROM credicard WHERE personal_id= ? ;"

updatecredicardnumber="UPDATE credicard SET credicardnumber = ? , credicarddate=? , credicardcvv=? WHERE personal_id = ? ;"

class add_credi_card:
    def __init__(self) -> None:
        self.con = sqlite3.connect("a.db")
        self.cur = self.con.cursor()
        self.create_tables()
        
    def create_tables(self):
        self.cur.execute(createcredicardTable)

    def insert_credicard(self,personal_id,credicardnumber,credicarddate,credicardcvv):
        self.cur.execute(insertcredicard, (personal_id ,credicardnumber,credicarddate,credicardcvv))
        self.con.commit()

    def check_creditcard(self,personal_id):
        return self.cur.execute(check_credit_card,(personal_id,)).fetchone()
        
    def update_credicard(self,personal_id,credicardnumber,credicarddate,credicardcvv):
        self.cur.execute(updatecredicardnumber, (credicardnumber,credicarddate,credicardcvv,personal_id))
        self.con.commit()

    def delete_credicard(self,personal_id):
        self.cur.execute(deletecredicard, (personal_id,))
        self.con.commit()
        
    def all_credi_card(self):
        return self.cur.execute(Allcredicard).fetchall()
#-------------------------------------------------------------------end

createcartpizza="""CREATE TABLE IF NOT EXISTS pizza_ceart 
(id INTEGER PRIMARY KEY, pizza_name TEXT NOT NULL,pizza_add_name TEXT NOT NULL);"""

insertcartpizza = "INSERT OR IGNORE INTO pizza_ceart (pizza_name,pizza_add_name) VALUES (?, ?);"

Allcartpizza = "SELECT * FROM pizza_ceart;"

deletecartpizza= "DELETE FROM pizza_ceart WHERE id= ? ;"

deleteallcart = "DELETE FROM pizza_ceart"

class incoming_pizza_order_database:
    def __init__(self) -> None:
        self.con = sqlite3.connect("a.db")
        self.cur = self.con.cursor()
        self.create_tables()
    def create_tables(self):
        self.cur.execute(createcartpizza)

    def insert_cart(self,pizza_name,pizza_add_name):
        self.cur.execute(insertcartpizza,(pizza_name,pizza_add_name))
        self.con.commit()
    def delete_cart(self,id):
        self.cur.execute(deletecartpizza,(id,))
        self.con.commit()
    
    def all_cart_pizza(self):
        return self.cur.execute(Allcartpizza).fetchall()
    
    def all_order_database_delete(self):
        self.cur.execute(deleteallcart)
        self.con.commit()
        
#-------------------------------------------------------------------end

createreceiptpizzatable="""CREATE TABLE IF NOT EXISTS receipt_database 
(id INTEGER PRIMARY KEY,personal_id  TEXT KEY,  order_pizza_pizza_name_add_made TEXT NOT NULL,order_details_pizza_name TEXT NOT NULL, order_details_pizza_add_name TEXT NOT NULL, order_date TEXT NOT NULL,total TEXT NOT NULL);"""

insertreceiptdata = "INSERT OR IGNORE INTO receipt_Database (personal_id,order_pizza_pizza_name_add_made,order_details_pizza_name,order_details_pizza_add_name,order_date,total) VALUES (?, ?, ?, ? ,? ,?);"

Allreceiptpizza = "SELECT order_pizza_pizza_name_add_made FROM receipt_database;"

Allreceiptpizzaname = "SELECT order_details_pizza_name FROM receipt_database;"

Allreceiptpizzaaddmade = "SELECT order_details_pizza_add_name FROM receipt_database;"

Allreceiptpizzatotal = "SELECT total FROM receipt_database;"

deletereceiptpizza= "DELETE FROM receipt_database WHERE id= ? ;"

class receipt_pizza_addmade_database:
    def __init__(self) -> None:
        self.con = sqlite3.connect("a.db")
        self.cur = self.con.cursor()
        self.create_tables()
    def create_tables(self):
        self.cur.execute(createreceiptpizzatable)

    def insert_receipt_pizza(self,personal_id,order_pizza_pizza_name_add_made,order_details_pizza_name,order_details_pizza_add_name,order_date,total):
        self.cur.execute(insertreceiptdata,(personal_id,order_pizza_pizza_name_add_made,order_details_pizza_name,order_details_pizza_add_name,order_date,total))
        self.con.commit()
    
    def all_receipt_pizza_name(self):
        return self.cur.execute(Allreceiptpizzaname).fetchall()
    
    def all_receipt_pizza_name(self):
        return self.cur.execute(Allreceiptpizzaname).fetchall()
    
    def all_receipt_pizza_addmade(self):
        return self.cur.execute(Allreceiptpizzaaddmade).fetchall()
        
    def all_receipt_pizza_total(self):
        return self.cur.execute(Allreceiptpizzatotal).fetchall()
        

    def all_receipt_pizza(self):
        return self.cur.execute(Allreceiptpizza).fetchall()
    
    def del_pizza_table(self,id):
        self.cur.execute(deletereceiptpizza,(id,))
        self.con.commit()
