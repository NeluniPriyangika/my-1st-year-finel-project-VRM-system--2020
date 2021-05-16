import  sqlite3
import sys
import datetime
conn  =  sqlite3 . connect ( 'vehi.db' )
print("-------------------------------------- \n")
print("** Vehicle Rental management system **\n".title())
print("-------------------------------------- \n")

conn = sqlite3.connect('vehi.db')
cursor = conn.cursor()
#please uncomment following codes when you run very first time,agin comment it from second run

#cursor.execute("CREATE TABLE employee(Name char(50), Emp_id n(20), NIC char(20),Possition char(20), Joined_date char(20),Basic_salary n(20));""")
'''
cursor.execute("CREATE TABLE rented(Model char(50),"
               " Vehicle_No char(30), Customer_Name char(50), Customer_ID char(40) ,"
              "Rent_date char(50),Current_Millage char(50),Deposit_Amount char(20),"
               "Requested dates n(20),Free_km char(40),Charges_Per_Km char(20));")
               
               
cursor.execute("CREATE TABLE Lorry(Model char(50),Owner_name char(30), "
               "EngineNo n(35), ChsNo n(40) ,VehicleNo char(50),"
               "Millage char(50),Fuel char(20),Passengers n(20), Charges_per_km n(20),Fiexed_charge n(20),Free_km n(20));""")
               
               
cursor.execute("CREATE TABLE van(Model char(50), Owner_name char(30), "
               "EngineNo n(35), ChsNo n(40) ,VehicleNo char(50),"
               "Millage char(50),Fuel char(20),Passengers n(20), Charges_per_km n(20),Fiexed_charge n(20),Free_km n(20));""")
               
               
cursor.execute("CREATE TABLE Bike(Model char(50), Owner_name char(30), "
               "EngineNo n(35), ChsNo n(40) ,VehicleNo char(50),"
               "Millage char(50),Fuel char(20),Passengers n(20), Charges_per_km n(20),Fiexed_charge n(20),Free_km n(20));""")
               
               
cursor.execute("CREATE TABLE Other(Model char(50), Owner_name char(30), "
               "EngineNo n(35), ChsNo n(40) ,VehicleNo char(50),"
               "Millage char(50),Fuel char(20),Passengers n(20), Charges_per_km n(20),Fiexed_charge n(20),Free_km n(20));""")
               
               
cursor.execute("CREATE TABLE cars(Model char(50), Owner_name char(30), "
                 "EngineNo n(35), ChsNo n(40) ,VehicleNo char(50),"
                 "Millage char(50),Fuel char(20),Passengers n(20), Charges_per_km n(20),Fiexed_charge n(20),Free_km n(20));""")
                 
                 
cursor.execute("""ALTER TABLE rented ADD COLUMN fixed_charge n(20);""")
cursor.execute("""ALTER TABLE cars ADD COLUMN ac_nac chr(20);""" )'''

#This is the main function of the code. this is to take inputs from
#the user and navigate the user to the correct function
def mainhome():
    print("\nSelect the action you want to perform \n ")

    print("1.Add a new vehicle ")
    print("2.Rent a vehicle ")
    print("3.Return a vehicle ")
    print("4.Calculate rental fees  ")
    print("5.Search for a vehicle")
    print("6.Show all vehicles available")
    print("7.Create a bill for a rented vehicle")
    print("8.Employee details ")
    print("9.Help")
    print("0.Exit\n")

    userinput1 = input(">>What is your choice - ")
    if userinput1 == '1':
        selectADD()
    if userinput1 == '3':
        returnVehicle()
    if userinput1 == '4':
       calculate()
    if userinput1 == '9':
        helpfunction()
    if userinput1 == '5':
        findVehicle()
    if userinput1 == '2':
        rentvehicle()
    if userinput1 == '6':
        showall()
    if userinput1 == '8':
        employee()
    if userinput1 == '9':
        helpfunction()
    if userinput1=='7':
        createbill()
    if userinput1 == '0':
        sys.exit()

    print("\nDo you want to go to homepage")
    print("1.Yes")
    print("2.No")
    userinput2 = input(">>Your choise  :  ")

    if userinput2 == '1':
        mainhome()
    if userinput2 == '2':
        sys.exit()
#when the user is going to add a vehicle to the system this function navigates the
#the user to the exact vehicle that he wants to add
def selectADD():
    print("\nWhat do you want to add ")
    print("1.A Car")
    print("2.A Lorry")
    print("3.A Van")
    print("4.A Bike")
    print(("5.Other"))
    print("9.Return to home page \n")
    userinput7=input(">>Your choice:")
    if userinput7 == '1':
        addcar()
    if userinput7=='2':
        addLorry()
    if userinput7=='3':
        addVan()
    if userinput7=='4':
        addBike()
    if userinput7=='5':
        addAnother()
    if userinput7=='9':
        mainhome()
#funtion for adding a car
#take the inputs from the user then added in to the database
def addcar():
#taking the details from the user
  print("********************************************\n")
  s_Model = input('Enter Model:')
  s_Own = input('Enter Owner name:')
  s_Eng = input('Enter engine no :')
  s_Chs = input('Enter chasie no :')
  s_vehino=input('Enter Vehicle no :')
  s_milage=input('Enter Current Millage :')
  s_fuel=input('Enter Fuel Type :')
  s_passenger=input('Enter Passenger Capacity :')
  s_perKm=int(input("Charges per additional Km (Rs) :"))
  s_fixed=int(input("Enter the fixed charge of the vehicle (Rs) :"))
  s_freekm=int(input("Enter free Km's given to the vehicle :"))
  s_ac_nac=input("Enter AC/NAC:")
#Entering the data to the database
  cursor.execute("""
  INSERT INTO cars(Model, Owner_name, EngineNo, ChsNO, VehicleNo,
   Millage, Fuel, Passengers,Charges_per_km,Fiexed_charge,Free_km,ac_nac)
  VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
  """, (s_Model, s_Own, s_Eng, s_Chs,s_vehino,s_milage,s_fuel,s_passenger,s_perKm,s_fixed,s_freekm,s_ac_nac))
#saving the entered data to the database
  conn.commit()
  print('>>Data entered successfully.<<')
#Closing the database connection



# funtion for adding a lorry
# take the inputs from the user then added in to the database
def addLorry():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    print("********************************************\n")
    s_Model = input('Enter Model:')
    s_Own = input('Enter Owner name:')
    s_Eng = input('Enter engine no :')
    s_Chs = input('Enter chasie no :')
    s_vehino = input('Enter Vehicle no :')
    s_milage = input('Enter Current Millage :')
    s_fuel = input('Enter Fuel Type :')
    s_passenger = input('Enter Passenger Capacity :')
    s_perKm = input("Charges per additional Km :")
    s_fixed = input("Enter the fixed charge of the vehicle :")
    s_freekm = input("Enter free Km's given to the vehicle :")
    #Entering the data to the database
    cursor.execute("""
     INSERT INTO Lorry(Model, Owner_name, EngineNo, ChsNO, VehicleNo,
      Millage, Fuel, Passengers,Charges_per_km,Fiexed_charge,Free_km)
     VALUES (?,?,?,?,?,?,?,?,?,?,?)
     """, (s_Model, s_Own, s_Eng, s_Chs, s_vehino, s_milage, s_fuel, s_passenger, s_perKm, s_fixed, s_freekm))
    #saving entered data to the database
    conn.commit()

    print('>>Data entered successfully.<<')



#funtion for adding a van
#take the inputs from the user then added in to the database
def addVan():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    print("********************************************\n")
    s_Model = input('Enter Model:')
    s_Own = input('Enter Owner name:')
    s_Eng = input('Enter engine no :')
    s_Chs = input('Enter chasie no :')
    s_vehino = input('Enter Vehicle no :')
    s_milage = input('Enter Current Millage :')
    s_fuel = input('Enter Fuel Type :')
    s_passenger = input('Enter Passenger Capacity :')
    s_perKm = input("Charges per additional Km :")
    s_fixed = input("Enter the fixed charge of the vehicle :")
    s_freekm = input("Enter free Km's given to the vehicle :")
    # Entering the data to the database
    cursor.execute("""
     INSERT INTO Van(Model, Owner_name, EngineNo, ChsNO, VehicleNo,
      Millage, Fuel, Passengers,Charges_per_km,Fiexed_charge,Free_km)
     VALUES (?,?,?,?,?,?,?,?,?,?,?)
     """, (s_Model, s_Own, s_Eng, s_Chs, s_vehino, s_milage, s_fuel, s_passenger, s_perKm, s_fixed, s_freekm))
    # saving entered data to the database
    conn.commit()

    print('>>Data entered successfully.<<')
    conn.close()


#funtion for adding a bike
#take the inputs from the user then added in to the database
def addBike():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    print("********************************************\n")
    s_Model = input('Enter Model:')
    s_Own = input('Enter Owner name:')
    s_Eng = input('Enter engine no :')
    s_Chs = input('Enter chasie no :')
    s_vehino = input('Enter Vehicle no :')
    s_milage = input('Enter Current Millage :')
    s_fuel = input('Enter Fuel Type :')
    s_passenger = input('Enter Passenger Capacity :')
    s_perKm = input("Charges per additional Km :")
    s_fixed = input("Enter the fixed charge of the vehicle :")
    s_freekm = input("Enter free Km's given to the vehicle :")
    # Entering the data to the database
    cursor.execute("""
     INSERT INTO Bike(Model, Owner_name, EngineNo, ChsNO, VehicleNo,
      Millage, Fuel, Passengers,Charges_per_km,Fiexed_charge,Free_km)
     VALUES (?,?,?,?,?,?,?,?,?,?,?)
     """, (s_Model, s_Own, s_Eng, s_Chs, s_vehino, s_milage, s_fuel, s_passenger, s_perKm, s_fixed, s_freekm))
    # saving entered data to the database
    conn.commit()
    print('>>Data entered successfully.<<')
    #closing the database connection
    conn.close()


#funtion for adding an another vehicle
#take the inputs from the user then added in to the database
def addAnother():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    print("********************************************\n")
    s_Model = input('Enter Model:')
    s_Own = input('Enter Owner name:')
    s_Eng = input('Enter engine no :')
    s_Chs = input('Enter chasie no :')
    s_vehino = input('Enter Vehicle no :')
    s_milage = input('Enter Current Millage :')
    s_fuel = input('Enter Fuel Type :')
    s_passenger = input('Enter Passenger Capacity :')
    s_perKm = input("Charges per additional Km :")
    s_fixed = input("Enter the fixed charge of the vehicle :")
    s_freekm = input("Enter free Km's given to the vehicle :")
    # Entering the data to the database
    cursor.execute("""
     INSERT INTO Other(Model, Owner_name, EngineNo, ChsNO, VehicleNo,
      Millage, Fuel, Passengers,Charges_per_km,Fiexed_charge,Free_km)
     VALUES (?,?,?,?,?,?,?,?,?,?,?)
     """, (s_Model, s_Own, s_Eng, s_Chs, s_vehino, s_milage, s_fuel, s_passenger, s_perKm, s_fixed, s_freekm))
    # saving entered data to the database
    conn.commit()
    print('>>Data entered successfully.<<')
    conn.close()


#the calculation of the rental fees are done here
def calfuntion():
    print("\n*****Let's Calculate the rental fee*****\n")
    additional = int(input("Expected additonal Km's:"))
    perkm = int(input("Enter charge for additional Km(Rs):"))

    dep=int(input("Enter the customer deposit:"))
    fixed = int(input("Enter the fixed charge for the vehicle :"))

    adiitionalkmfee = additional * perkm
    total=adiitionalkmfee+fixed

    print("---------------------------")
    print("Total rental fee is : ", total)

    print("---------------------------")
    balance=dep-total
    print("Because customer has deposited Rs:",dep ,", His balance will be Rs.",balance)
#selecting a vehicle to calculate rental fees
def calculate():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    print("What is the vehicle you want to calculate estimated rental fees ")
    print("1.Car")
    print("2.Van")
    print("3.Bike")
    print("4.Lorry")
    print("5.Other vehicles")
    userinput4 = input(">>Your choice : ")
    if userinput4=='1':
        #to show availble models to the user
        cursor.execute("SELECT Model FROM Cars")
        print("Available car models")
        print(cursor.fetchall())

        userinput = input("\nWhat is the vehicle you want to calculate fees - ")
        cursor.execute('SELECT * FROM cars WHERE Model=(?) ', [userinput])
        cursor.execute('SELECT Charges_per_km FROM cars WHERE Model=(?) ', [userinput])
        data1=cursor.fetchone()
        print("Charges per km (Rs) :" ,data1)
        cursor.execute('SELECT Fiexed_charge FROM cars WHERE Model=(?) ', [userinput])
        data2= cursor.fetchone()
        print("Fixed charge (Rs): ", data2)
        calfuntion()


    if userinput4=='2':
        cursor.execute("SELECT Model FROM Van")
        print("Available Van models")
        print(cursor.fetchall())

        userinput = input("What is the vehicle you want to calculate fees - ")
        cursor.execute('SELECT * FROM Van WHERE Model=(?) ', [userinput])
        cursor.execute('SELECT Charges_per_km FROM Van WHERE Model=(?) ', [userinput])
        data1 = cursor.fetchone()
        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM Van WHERE Model=(?) ', [userinput])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()
    if userinput4=='3':
        cursor.execute("SELECT Model FROM Bike")
        print("Available Bike models")
        print(cursor.fetchall())

        userinput = input("What is the vehicle you want to calculate fees - ")
        cursor.execute('SELECT * FROM Bike WHERE Model=(?) ', [userinput])
        cursor.execute('SELECT Charges_per_km FROM Bike WHERE Model=(?) ', [userinput])
        data1 = cursor.fetchone()

        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM Bike WHERE Model=(?) ', [userinput])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()
    if userinput4=='4':
        cursor.execute("SELECT Model FROM Lorry")
        print("Available Lorry models")
        print(cursor.fetchall())

        userinput = input("What is the vehicle you want to calculate fees - ")
        cursor.execute('SELECT * FROM Lorry WHERE Model=(?) ', [userinput])
        cursor.execute('SELECT Charges_per_km FROM Lorry WHERE Model=(?) ', [userinput])
        data1 = cursor.fetchone()
        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM Lorry WHERE Model=(?) ', [userinput])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()
    if userinput4=='5':
        cursor.execute("SELECT Model FROM Other")
        print("Available Other Vehicle models")
        print(cursor.fetchall())

        userinput = input("What is the vehicle you want to calculate fees - ")
        cursor.execute('SELECT * FROM Other WHERE Model=(?) ', [userinput])
        cursor.execute('SELECT Charges_per_km FROM Other WHERE Model=(?) ', [userinput])
        data1 = cursor.fetchone()
        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM Other WHERE Model=(?) ', [userinput])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()

#when a customer asked for a vehicle the working crew want to search for it
#this function is for doing that
def findVehicle():
  conn = sqlite3.connect('vehi.db')
  cursor = conn.cursor()
  print("What is the vehicle are you looking for- \n")
  print("1.A Car")
  print("2.A Lorry")
  print("3.A Van")
  print("4.A Bike")
  print(("5.Other"))
  userinput=input(">>Your choice: ")
  if userinput=='1':
      userinput2=input("What is the car are you looking for  : ")
      cursor.execute("SELECT Model,VehicleNo  FROM cars WHERE Model=(?)",[userinput2])
      print("Model and the vehicle no (information will display only if the vehicle available): ")
      rows = cursor.fetchall()
      for row in rows:
          print(row)
  if userinput=='2':
      userinput3=input("What is the Lorry are you looking for  : ")
      cursor.execute("SELECT Model,VehicleNo FROM Lorry WHERE Model=(?)",[userinput3])
      print("Model and the vehicle no (information will display only if the vehicle available) : ")
      rows = cursor.fetchall()
      for row in rows:
          print(row)
  if userinput=='3':
      userinput3=input("What is the van are you looking for  : ")
      cursor.execute("SELECT Model,VehicleNo FROM Van WHERE Model=(?)",[userinput3])
      print("Model and the vehicle no  (information will display only if the vehicle available): ")
      rows = cursor.fetchall()
      for row in rows:
          print(row)
  if userinput=='4':
      userinput4=input("What is the Bike are you looking for  : ")
      cursor.execute("SELECT Model,VehicleNo FROM Bike WHERE Model=(?)",[userinput4])
      print("Model and the vehicle no (information will display only if the vehicle available) : ")
      rows = cursor.fetchall()
      for row in rows:
          print(row)
  if userinput=='5':
      userinput5=input("What is the vehicle are you looking for  : ")
      cursor.execute("SELECT Model,VehicleNo FROM Other WHERE Model=(?)",[userinput5])
      print("Model and the vehicle no (information will display only if the vehicle available): ")
      rows = cursor.fetchall()
      for row in rows:
          print(row)
#to show all the vehicles available in the system
def showall():
  conn = sqlite3.connect('vehi.db')
  cursor = conn.cursor()
  cursor.execute("SELECT Model FROM Cars")
  print("Available car models")
  print(cursor.fetchall())
  cursor.execute("SELECT Model FROM Lorry")
  print("Available Lorry models")
  print(cursor.fetchall())
  cursor.execute("SELECT Model FROM Van")
  print("Available Van models")
  print(cursor.fetchall())
  cursor.execute("SELECT Model FROM Bike")
  print("Available Bike models")
  print(cursor.fetchall())
  cursor.execute("SELECT Model FROM Other")
  print("Available Other Vehicle models")
  print(cursor.fetchall())

def rentvehicle2():

    v_Model = input("Enter model :")
    v_no = input("Enter vehicle no :")
    v_cus = input("Enter customer name:")
    v_id = input("Enter customer ID no:")
    v_date = datetime.datetime.now()
    v_currentmil = input("Enter current millage: ")
    v_deposit = input("Enter deposited amount (Rs) :")
    v_reqdates = input("Enter requested dates :")
    v_freekm = input("Enter free Km's : ")
    v_perkm = input("Enter the charges per km :")
    v_fix=input("Enter fixed charge : ")
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("""
 INSERT INTO rented(Model, Vehicle_No, Customer_Name, Customer_ID, Rent_date, Current_Millage,
  Deposit_Amount, Requested,Free_km,Charges_Per_Km,fixed_charge)
 VALUES (?,?,?,?,?,?,?,?,?,?,?)
 """, (v_Model, v_no,v_cus,v_id,v_date,v_currentmil,v_deposit,v_reqdates, v_freekm, v_perkm,v_fix))

    print('***Data entered successfully *** \n.')
    print("***Now you can handover the keys to the customer***")
    cursor.execute('DELETE FROM cars WHERE VehicleNo=(?) ', [v_no])
    print("Vehicle removed from available vehicles list \n")
    conn.commit()


#when a customer want to rent a vehicle the working staff use the rent a vehicle option
#this function is for selecting a vehicle for rent
def rentvehicle():
   print(" \nWhat do you want to rent -\n")
   print("1.Car")
   print("2.Van")
   print("3.Bike")
   print("4.Lorry")
   print("5.Other vehicles")
   userinput4=input(">>Your choice : ")
   if userinput4=='1':
       rentcar()
   if userinput4=='2':
       rentvan()
   if userinput4=='3':
       rentbike()
   if userinput4=='4':
       rentlorry()
   if userinput4=='5':
       rentother()


#show the features of selected vehicle for rent
def rentother():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Model FROM Other")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print(cursor.fetchall())
    userinput5 = input("What do you want to rent ?  : ")

    print("****These are the features of your requested Vehicle**** \n ")
    cursor.execute('SELECT Model FROM Other WHERE Model=(?) ', [userinput5])
    print("Model :",cursor.fetchone())
    cursor.execute('SELECT Owner_name FROM Other WHERE Model=(?) ', [userinput5])
    print("Owner :",cursor.fetchone()),
    cursor.execute('SELECT EngineNo FROM Other WHERE Model=(?) ', [userinput5])
    print("Engine Number :",cursor.fetchone())
    cursor.execute('SELECT ChsNo FROM Other WHERE Model=(?) ', [userinput5])
    print("Chassie No :",cursor.fetchone())
    cursor.execute('SELECT VehicleNo FROM Other WHERE Model=(?) ', [userinput5])
    print("Vehicle Number :",cursor.fetchone())
    cursor.execute('SELECT Fuel FROM Other WHERE Model=(?) ', [userinput5])
    print("Fuel type :",cursor.fetchone())
    cursor.execute('SELECT Passengers FROM Other WHERE Model=(?) ', [userinput5])
    print("Passengers count:",cursor.fetchone())
    cursor.execute('SELECT Charges_per_km FROM Other WHERE Model=(?) ', [userinput5])
    print("Charges per Aditional Km :",cursor.fetchone())
    print("What do you want to do ")
    print("1.Rent this vehicle")
    print("2.Calculate rental fees ")
    userinput6 = input(">>your choice \n")
    if userinput6 == '1':
        rentother2()
    #this will alow the user to calculate fees for the slected vehicle
    if userinput6=='2':
        cursor.execute('SELECT Charges_per_km FROM Other WHERE Model=(?) ', [userinput5])
        data1 = cursor.fetchone()
        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM Other WHERE Model=(?) ', [userinput5])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()

#to take the inputs of the vehicle  from the user
#then added into the database
def rentother2():
    v_Model = input("Enter model :")
    v_no = input("Enter vehicle no :")
    v_cus = input("Enter customer name:")
    v_id = input("Enter customer ID no:")
    v_date = datetime.datetime.now()
    v_currentmil = input("Enter current millage: ")
    v_deposit = input("Enter deposited amount (Rs) :")
    v_reqdates = input("Enter requested dates :")
    v_freekm = input("Enter free Km's : ")
    v_perkm = input("Enter the charges per km")
    v_fix=input("Enter fixed charge")
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("""
               INSERT INTO rented(Model, Vehicle_No, Customer_Name, Customer_ID, Rent_date, Current_Millage,
                Deposit_Amount, Requested,Free_km,Charges_Per_Km,fixed_charge)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)
               """, (v_Model, v_no, v_cus, v_id, v_date, v_currentmil, v_deposit, v_reqdates, v_freekm, v_perkm,v_fix))
    conn.commit()
    print('>>Data entered successfully.<<\n')
    cursor.execute('DELETE FROM Other WHERE VehicleNo=(?) ', [v_no])
    print("Vehicle removed from available vehicles list \n")
    conn.commit()
#show the features of selected vehicle for rent
def rentlorry():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Model FROM Lorry")
    print("Available Lorry models")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    userinput5 = input("What do you want to rent ?  : ")

    print("****These are the features of your requested Lorry**** \n ")
    cursor.execute('SELECT Model FROM Lorry WHERE Model=(?) ', [userinput5])
    print("Model :", cursor.fetchone())
    cursor.execute('SELECT Owner_name FROM Lorry WHERE Model=(?) ', [userinput5])
    print("Owner :", cursor.fetchone()),
    cursor.execute('SELECT EngineNo FROM Lorry WHERE Model=(?) ', [userinput5])
    print("Engine Number :", cursor.fetchone())
    cursor.execute('SELECT ChsNo FROM Lorry WHERE Model=(?) ', [userinput5])
    print("Chassie No :", cursor.fetchone())
    cursor.execute('SELECT VehicleNo FROM Lorry WHERE Model=(?) ', [userinput5])
    print("Vehicle Number :", cursor.fetchone())
    cursor.execute('SELECT Fuel FROM Lorry WHERE Model=(?) ', [userinput5])
    print("Fuel type :", cursor.fetchone())
    cursor.execute('SELECT Passengers FROM Lorry WHERE Model=(?) ', [userinput5])
    print("Passengers count:", cursor.fetchone())
    cursor.execute('SELECT Charges_per_km FROM Lorry WHERE Model=(?) ', [userinput5])
    print("Charges per Aditional Km :", cursor.fetchone())
    print("What do you want to do ")
    print("1.Rent this vehicle")
    print("2.Calculate rental fees ")
    userinput6 = input(">>your choice \n")
    if userinput6 == '1':
        rentlorry2()
    if userinput6 =='2':
        cursor.execute('SELECT Charges_per_km FROM Lorry WHERE Model=(?) ', [userinput5])
        data1 = cursor.fetchone()
        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM Lorry WHERE Model=(?) ', [userinput5])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()

#to take the inputs of the vehicle  from the user
#then added into the database
def rentlorry2():
    v_Model = input("Enter model :")
    v_no = input("Enter vehicle no :")
    v_cus = input("Enter customer name:")
    v_id = input("Enter customer ID no:")
    v_date = datetime.datetime.now()
    v_currentmil = input("Enter current millage: ")
    v_deposit = input("Enter deposited amount (Rs) :")
    v_reqdates = input("Enter requested dates :")
    v_freekm = input("Enter free Km's : ")
    v_perkm = input("Enter the charges per km :")
    v_fix=input("Enter fixed charge :")
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("""
           INSERT INTO rented(Model, Vehicle_No, Customer_Name, Customer_ID, Rent_date, Current_Millage,
            Deposit_Amount, Requested,Free_km,Charges_Per_Km,fixed_charge)
           VALUES (?,?,?,?,?,?,?,?,?,?,?)
           """, (v_Model, v_no, v_cus, v_id, v_date, v_currentmil, v_deposit, v_reqdates, v_freekm, v_perkm,v_fix))
    conn.commit()
    print('>>Data entered successfully.<< \n')
    cursor.execute('DELETE FROM Lorry WHERE VehicleNo=(?) ', [v_no])
    conn.commit()
    print("Vehicle removed from available vehicles list \n")
#show the features of selected vehicle for rent
def rentbike():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Model FROM Bike")
    print("Available Bike models")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    userinput5 = input("What do you want to rent ?  : ")

    print("****These are the features of your requested car**** \n ")
    cursor.execute('SELECT Model FROM Bike WHERE Model=(?) ', [userinput5])
    print("Model :", cursor.fetchone())
    cursor.execute('SELECT Owner_name FROM Bike WHERE Model=(?) ', [userinput5])
    print("Owner :", cursor.fetchone()),
    cursor.execute('SELECT EngineNo FROM Bike WHERE Model=(?) ', [userinput5])
    print("Engine Number :", cursor.fetchone())
    cursor.execute('SELECT ChsNo FROM Bike WHERE Model=(?) ', [userinput5])
    print("Chassie No :", cursor.fetchone())
    cursor.execute('SELECT VehicleNo FROM Bike WHERE Model=(?) ', [userinput5])
    print("Vehicle Number :", cursor.fetchone())
    cursor.execute('SELECT Fuel FROM Bike WHERE Model=(?) ', [userinput5])
    print("Fuel type :", cursor.fetchone())
    cursor.execute('SELECT Passengers FROM Bike WHERE Model=(?) ', [userinput5])
    print("Passengers count:", cursor.fetchone())
    cursor.execute('SELECT Charges_per_km FROM Bike WHERE Model=(?) ', [userinput5])
    print("Charges per Aditional Km :", cursor.fetchone())
    print("What do you want to do ")
    print("1.Rent this vehicle")
    print("2.Calculate rental fees ")
    userinput6 = input(">>your choice \n")
    if userinput6 == '1':
        rentbike2()
    if userinput6 =='2':
        cursor.execute('SELECT Charges_per_km FROM Bike WHERE Model=(?) ', [userinput5])
        data1 = cursor.fetchone()
        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM Bike WHERE Model=(?) ', [userinput5])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()


#to take the inputs of the vehicle  from the user
#then added into the database
def rentbike2():
    v_Model = input("Enter model :")
    v_no = input("Enter vehicle no :")
    v_cus = input("Enter customer name:")
    v_id = input("Enter customer ID no:")
    v_date = datetime.datetime.now()
    v_currentmil = input("Enter current millage: ")
    v_deposit = input("Enter deposited amount (Rs) :")
    v_reqdates = input("Enter requested dates :")
    v_freekm = input("Enter free Km's : ")
    v_perkm = input("Enter the charges per km :")
    v_fix=input("Enter fiexed charge :")
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("""
       INSERT INTO rented(Model, Vehicle_No, Customer_Name, Customer_ID, Rent_date, Current_Millage,
        Deposit_Amount, Requested,Free_km,Charges_Per_Km,fixed_charge)
       VALUES (?,?,?,?,?,?,?,?,?,?,?)
       """, (v_Model, v_no, v_cus, v_id, v_date, v_currentmil, v_deposit, v_reqdates, v_freekm, v_perkm,v_fix))
    conn.commit()
    print('>>Data entered successfully.<< \n')
    cursor.execute('DELETE FROM Bike WHERE VehicleNo=(?) ', [v_no])
    conn.commit()
    print("Vehicle removed from available vehicles list \n")
#show the features of selected vehicle for rent
def rentvan():
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Model FROM Van")
    print("Available Van models")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    userinput5 = input("What do you want to rent ?  : ")

    print("****These are the features of your requested car**** \n ")
    cursor.execute('SELECT Model FROM Van WHERE Model=(?) ', [userinput5])
    print("Model :", cursor.fetchone())
    cursor.execute('SELECT Owner_name FROM Van WHERE Model=(?) ', [userinput5])
    print("Owner :", cursor.fetchone()),
    cursor.execute('SELECT EngineNo FROM Van WHERE Model=(?) ', [userinput5])
    print("Engine Number :", cursor.fetchone())
    cursor.execute('SELECT ChsNo FROM Van WHERE Model=(?) ', [userinput5])
    print("Chassie No :", cursor.fetchone())
    cursor.execute('SELECT VehicleNo FROM Van WHERE Model=(?) ', [userinput5])
    print("Vehicle Number :", cursor.fetchone())
    cursor.execute('SELECT Fuel FROM Van WHERE Model=(?) ', [userinput5])
    print("Fuel type :", cursor.fetchone())
    cursor.execute('SELECT Passengers FROM Van WHERE Model=(?) ', [userinput5])
    print("Passengers count:", cursor.fetchone())
    cursor.execute('SELECT Charges_per_km FROM Van WHERE Model=(?) ', [userinput5])
    print("Charges per Aditional Km :", cursor.fetchone())
    print("What do you want to do ")
    print("1.Rent this vehicle")
    print("2.Calculate rental fees ")
    userinput6 = input(">>your choice \n")
    if userinput6 == '1':
        rentvan2()
    if userinput6 =='2':
        cursor.execute('SELECT Charges_per_km FROM Van WHERE Model=(?) ', [userinput5])
        data1 = cursor.fetchone()
        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM Van WHERE Model=(?) ', [userinput5])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()


#to take the inputs of the vehicle  from the user
#then added into the database
def rentvan2():
    v_Model = input("Enter model :")
    v_no = input("Enter vehicle no :")
    v_cus = input("Enter customer name:")
    v_id = input("Enter customer ID no:")
    v_date = datetime.datetime.now()
    v_currentmil = input("Enter current millage: ")
    v_deposit = input("Enter deposited amount (Rs) :")
    v_reqdates = input("Enter requested dates :")
    v_freekm = input("Enter free Km's : ")
    v_perkm = input("Enter the charges per km :")
    v_fix=input("Enter fixed charge :")
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO rented(Model, Vehicle_No, Customer_Name, Customer_ID, Rent_date, Current_Millage,
     Deposit_Amount, Requested,Free_km,Charges_Per_Km,fixed_charge)
    VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, (v_Model, v_no, v_cus, v_id, v_date, v_currentmil, v_deposit, v_reqdates, v_freekm, v_perkm,v_fix))
    conn.commit()
    print('Data entered successfully \n.')
    cursor.execute('DELETE FROM Van WHERE VehicleNo=(?) ', [v_no])
    conn.commit()
    print("Vehicle removed from available vehicles list \n")

#show the features of selected vehicle for rent
def rentcar():
    cursor.execute("SELECT Model FROM Cars")
    print("\n Available car models")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    userinput5 = input("What do you want to rent ?  : ")

    print("\n****These are the features of your requested car**** \n ")

    cursor.execute('SELECT Owner_name FROM cars WHERE Model=(?) ', [userinput5])
    print("Owner :", cursor.fetchone()),
    cursor.execute('SELECT EngineNo FROM cars WHERE Model=(?) ', [userinput5])
    print("Engine Number :", cursor.fetchone())
    cursor.execute('SELECT ChsNo FROM cars WHERE Model=(?) ', [userinput5])
    print("Chassie No :", cursor.fetchone())
    cursor.execute('SELECT VehicleNo FROM cars WHERE Model=(?) ', [userinput5])
    print("Vehicle Number :", cursor.fetchone())
    cursor.execute('SELECT Fuel FROM cars WHERE Model=(?) ', [userinput5])
    print("Fuel type :", cursor.fetchone())
    cursor.execute('SELECT Passengers FROM cars WHERE Model=(?) ', [userinput5])
    print("Passengers count:", cursor.fetchone())
    cursor.execute('SELECT Charges_per_km FROM cars WHERE Model=(?) ', [userinput5])
    print("Charges per Aditional Km :", cursor.fetchone())
    print("_____________________________________________")
    print("What do you want to do \n ")
    print("1.Rent this vehicle")
    print("2.Calculate rental fees \n ")
    userinput6 = input(">>your choice -")
    if userinput6 == '1':
        rentvehicle2()
    if userinput6 =='2':
        cursor.execute('SELECT Charges_per_km FROM cars WHERE Model=(?) ', [userinput5])
        data1 = cursor.fetchone()
        print("Charges per km (Rs) :", data1)
        cursor.execute('SELECT Fiexed_charge FROM cars WHERE Model=(?) ', [userinput5])
        data2 = cursor.fetchone()
        print("Fiexed charge (Rs): ", data2)
        calfuntion()




#when a vehicle is rented it ia automatically removed from
#the available vehicles list
#so that when returning a vehicle again this fuction does the adding process of vehicles
#to the system and, after adding the vehicle also in the available vehicles list
def returnVehicle():
    print("\nWhat is the vehicle that you want to return ")
    print("1.A Car")
    print("2.A Lorry")
    print("3.A Van")
    print("4.A Bike")
    print(("5.Other"))
    print("9.Return to home page \n")
    userinput7 = input(">>Your choice:")
    if userinput7 == '1':
        print("*****You are going to return a vehicle*****")
        print("*****This will added to availble vehicles list ***** \n")
        addcar()
    if userinput7 == '2':
        print("*****You are going to return a vehicle*****")
        print("*****This will added to availble vehicles list ***** \n")
        addLorry()
    if userinput7 == '3':
        print("*****You are going to return a vehicle*****")
        print("*****This will added to availble vehicles list ***** \n")
        addVan()
    if userinput7 == '4':
        print("*****You are going to return a vehicle*****")
        print("*****This will added to availble vehicles list ***** \n")
        addBike()
    if userinput7 == '5':
        print("*****You are going to return a vehicle*****")
        print("*****This will added to availble vehicles list ***** \n")
        addAnother()
    if userinput7 == '9':
        mainhome()
#all employee related process are done by this
def employee():
    print("\n**** What do you want to do ****")
    print("1.Add new eployee")
    print("2.Remove an eployee")
    print("3.See all emloyees \n")
    userinput=input(">>What is your choise :")
    if userinput=='1':
        e_name=input("Enter employee name:")
        e_id=input("Enter emloyee ID:")
        e_nic=input("Enter employee's NIC no:")
        e_pos=input("Enter employee possition:")
        e_date=datetime.datetime.now()
        e_salary=input("Enter employee basic salary(Rs) :")
        conn = sqlite3.connect('vehi.db')
        cursor = conn.cursor()
        cursor.execute("""
         INSERT INTO employee(Name, Emp_id, NIC, Possition, Joined_date, Basic_salary)
         VALUES (?,?,?,?,?,?)
         """, (e_name, e_id, e_nic, e_pos, e_date, e_salary))
        print('\n >>Data entered successfully.<< \n')
        conn.commit()
    if userinput=='3':
        conn = sqlite3.connect('vehi.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Name,Emp_id FROM employee")
        print("\n **** All employees names and Employee ID's **** \n")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        userinput9=input("\nTo see all details enter employee id - ")
        cursor.execute("SELECT Name FROM employee WHERE Emp_id=(?) ", [userinput9])
        print("Employee Name = ", cursor.fetchone())
        cursor.execute("SELECT Emp_id FROM employee WHERE Emp_id=(?) ", [userinput9])
        print("Employee ID = ",cursor.fetchone())
        cursor.execute("SELECT NIC FROM employee WHERE Emp_id=(?) ", [userinput9])
        print("Employee NIC number = ", cursor.fetchone())
        cursor.execute("SELECT Possition FROM employee WHERE Emp_id=(?) ", [userinput9])
        print("Employee Possition = ", cursor.fetchone())
        cursor.execute("SELECT Joined_date FROM employee WHERE Emp_id=(?) ", [userinput9])
        print("Employee Joined date = ", cursor.fetchone())
        cursor.execute("SELECT Basic_salary FROM employee WHERE Emp_id=(?) ", [userinput9])
        print("Employee Basic salary (Rs)  = ", cursor.fetchone())
    if userinput=='2':
        print("\n *** Select a employee to remove ****")
        conn = sqlite3.connect('vehi.db')
        cursor = conn.cursor()
        print("Here are the available employee's names and ID's ")
        print("---------------------------------------")
        cursor.execute("SELECT Name,Emp_id FROM employee")
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        print("--------------------------------------")
        print("Who do you want to remove ? ")
        input1=input("Employee id of the employee :")
        cursor.execute('DELETE FROM employee WHERE Emp_id=(?) ', [input1])
        conn.commit()
        print("\n ***** Employee removed ***** ")

def createbill():
    print("\n***** These are the rented vehicles***** \n")
    conn = sqlite3.connect('vehi.db')
    cursor = conn.cursor()
    print("Rented vehicle models and vehicle numbers")
    cursor.execute("SELECT Model,Vehicle_No FROM rented")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    print("*For what do you want to make the bill ? \n")
    userinput=input("Enter Vehicle Number -")
    cursor.execute('SELECT Charges_per_km FROM rented WHERE Vehicle_no=(?) ', [userinput])
    data1 = cursor.fetchone()
    print("Charges per km (Rs) :", data1)
    cursor.execute('SELECT fixed_charge FROM rented WHERE Vehicle_no=(?) ', [userinput])
    data2 = cursor.fetchone()
    print("Fixed Charge (Rs) :", data2)
    cursor.execute('SELECT Deposit_Amount FROM rented WHERE Vehicle_no=(?) ', [userinput])
    data3 = cursor.fetchone()
    print("Deposited Amount (Rs): ", data3)
    print("\n***** Let's Calculate the Bill *****\n")
    print("*****Enter following details - If there are any changes from above details "
          "you can include them here***** \n")
    dep = int(input("Enter customer security deposit (Rs):"))
    fixed = int(input("Enter Fixed charge (Rs):"))
    perkm = int(input("Enter charge for additional Km(Rs):"))
    additional = int(input("Driven additonal Km's:"))
    data4=perkm*additional
    rentalfee=fixed+data4
    print("The rental fee of the customer (Rs) :",rentalfee)
    print("The customer has deposited Rs.",dep," when he rent the vehicle")
    bal=dep-rentalfee
    print("The balance of the customer (Rs) : ",bal)
def helpfunction():

    print("********For what do you want to help? *********** \n")
    print("1.How to add a vehicle")
    print("2.How to return a vehicle")
    print("3.What will happen after renting")
    print("4.How the calculation of rental fees happens ")
    print("5.instructions for the first use \n")
    userinputt=input(">>Your choise : ")
    if userinputt=='1':
        print("\n *******How to add a new vehicle to the system**** \n")
        print("* Go to add new vehicle option")
        print("* Select your vehicle model")
        print("* Enter the requesting details \n")
        ui=input("***To go back press 1 or To exit press 9 :")
        if ui=='1':
            helpfunction()
        if ui=='9':
            sys.exit()
    if userinputt=='2':
        print("\n *******How to return a vehicle **** \n")
        print("* Go to return vehicle option and enter the vehicle no")
        print("* Enter requesting details")
        ui = input("***To go back press 1 or To exit press 9 :")
        if ui == '1':
            helpfunction()
        if ui == '9':
            sys.exit()
    if userinputt=='3':
        print("\n *******What will happen after renting **** \n")
        print("* After you renting a vehilce it will remove from the available vehicle list")
        print("* Then it will be added to rented vehicle table")
        print("* You can use the listing of rented vehicle when you making a bill")
        ui = input("***To go back press 1 or To exit press 9 :")
        if ui == '1':
            helpfunction()
        if ui == '9':
            sys.exit()
    if userinputt=='4':
        print("\n *******How the calculation of rental fees happens  **** \n")
        print("* Then it will be added to rented vehicle table")
        print("* First you will be asked to choose a vehicle type")
        print("* Then you can see the availble models of your requested type ")
        print("* Then enter the model that you want from list to calculate")
        print("* Then you can see the  normal fixed charge of that car and the charges per one Km")
        print("* Then enter how much the customer deposit as a security ")
        print("* Now enter the fixed charge of the vehicle(include if there are any changes)")
        print("* Enter all other details")
        print("* Then you can see the total rental fee and subtotal with the deposit")
        print("* The deposit will be given to the customer when he returns it")
        ui = input("***To go back press 1 or To exit press 9 :")
        if ui == '1':
            helpfunction()
        if ui == '9':
            sys.exit()
    if userinputt=='5':
        print("****Instructions for the first use ****")
        print("* uncommet all database codes wne you are running first time ")
        print("* Always consider about use of uppercase and lowercase letters ")
        print("* This sysytem is case sensitive ")
        print("* Dont add unwanted spaces between inputs")
        print("* Form the second time you want to make database code agin as comments.")
        print("* You want to follow these steps only if you dont have the database files ")
        ui = input("***To go back press 1 or To exit press 9 :")
        if ui == '1':
            helpfunction()
        if ui == '9':
            sys.exit()

#the mainhome function is the first and only function executed in the very begining
#this function redirects the user to all other functions

mainhome()
