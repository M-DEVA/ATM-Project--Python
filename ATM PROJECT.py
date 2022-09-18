import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="12345",
    database="atm"
)

print("\n*************** Welcome to ATM ***************") 

print("\nPlease insert your card")

card=input("\nEnter your card :")

if card=="verified":
    print("\nYour card is verified")
       

    print(" 0 For LOGIN")
    print(" 1 For WITHDRAWL")
    print(" 2 For DEPOSIT")


    n = int(input("\npress 0 for login & 1 for Withdrawl & 2 for Deposit :"))
    password = ""
    myname = ""
    depo = ""
    id = ""
    withdrawl=""

    if n==0:
        name = input("\nEnter your Name :")
        
        accn = int(input("\nEnter account number :"))
        
        pw = input("\nSet your password :")

        myname = name
        password = pw
        
        id = accn

        val = (myname,password,depo,id,withdrawl)

        sql = "INSERT INTO data(my_name, pass_word,de_po,i_d,with_drawl ) VALUES (%s, %s, %s, %s, %s)"
        mycursor = connection.cursor()

        mycursor.execute(sql,val)
        connection.commit()
    


    if n==1:
        name = input("\nEnter your Name :")
    
        accn = int(input("\nEnter Account number :"))

        def withdrawl(amount):

            if amount<=50000:

                print("\nWithdrawl sucssfully")
                print("\n****Collect Your Cash****")

            else:
                print("\nOnly less then 50000 to withdrawal")

                if amount==input("\nEnter Less <=50000 :"):
                    print("\nWithdrawl sucssfully")
                    print("\n****Collect Your Cash****")
                else:
                    print("Withdrawl Cancelled")

        print("\nSelect Your option ")

        print("1.Withdrawal")

        print("2.Deposit ")         

        print("3.Exit")   

        user=int(input("\nEnter your Number:"))
        
        if user==1:
            
            amount=int(input("\nEnter your Withdrawl amount:"))
        
            pin = input("\nEnter your PIN :")
        
            withdrawl(amount)
        
        myname = name
        password = pin
        
        id = accn
        withdrawl = amount
        val = (myname,password,depo,id,withdrawl)

        sql = "INSERT INTO data(my_name, pass_word,de_po,i_d, with_drawl ) VALUES (%s, %s, %s, %s, %s)"
        mycursor = connection.cursor()

        mycursor.execute(sql,val)
        connection.commit()        

    if n==2:
        
        name = input("\nEnter your Name :")
        
        accn = int(input("\nEnter account number :"))
        
        def deposit(deposit_amount):

            if deposit_amount<=100000:

                print("\nDeposite sucssfully")
                print("\n****Take your Recepit****")

            else:
                print("\nOnly less then 100000 to Deposit")

                if deposit_amount==input("\nEnter Less < 100000 :"):
                    print("\nDeposite sucssfully")
                    print("\n****Take your Recepit****")
                else:
                    print("\nDeposit Cancelled") 

        print("\nSelect Your option ")

        print("1.Withdrawal")

        print("2.Deposit ")

        print("3.Cancel")

        user=int(input("\nEnter your Number:"))
        
        if user==2:
        
            deposit_amount = int(input("\nEnter Your Deposit Amount :"))
        
            pin = input("\nEnter your PIN :")
        
            deposit(deposit_amount)
            
        myname = name
        password = pin
        depo = deposit_amount
        id = accn

        val = (myname,password,depo,id)

        sql = "INSERT INTO data(my_name, pass_word,de_po,i_d ) VALUES (%s, %s, %s, %s)"
        mycursor = connection.cursor()

        mycursor.execute(sql,val)
        connection.commit()    

        if user==3:
            print("cancel")
        
    connection.commit()     

else:

    print("\nYour card is not verified")
        
    
    print("\n**********************Thanking You********************************") 


    print("*********************************************************************")
        




