## Parent class
class Avenger:
    company = "Avengers"
    name = ""
    email = ""
    password = ""
    department = ""
    # a function for the parent class for a mission statement to be displaid with each successful login
    def foundation(self):
        msg = "Protecting the future: {}\n".format(self.company)
        return msg

## Child class used for a user (like a customer)
class User(Avenger):
    name = "Captain America"
    email = "cap@gmail.com"
    password = "IronManSucks@5914"
    # a function for the child class login input
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        # A welcome back statement display if login successful
        if (entry_email == self.email and entry_password == self.password):
            print("\nWelcome back, {}".format(entry_name))
            company = User()
            print(company.foundation())
        # A incoreect statement display if login unsuccessful
        else:
            print("The password or email is incorrect.")
            customer = User()
            customer.getLoginInfo()
    
        
## child class used for an employee log in.
class Employee(Avenger):
    name = "Stephen Strange"
    email = "drstrange@gmail.com"
    title = "Sorcerer Supreme"
    department = "Time"
    pin_number = "1130"
    # a function for the child class login input
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        # A welcome back statement display if login successful
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("\nWelcome back, {}".format(entry_name))
            company = User()
            print(company.foundation())
        # A incoreect statement display if login unsuccessful
        else:
            print("The pin or email is incorrect.")            
            manager = Employee()
            manager.getLoginInfo()
            

## child class used for a cleaning person login (Janitorial)
class Janitorial(Avenger):
    name = "Thor"
    email = "heavyhammer@gmail.com"
    title = "Janitor"
    tools = "Mop"
    pin_number = "7941"
    # a function for the child class login input
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        # A welcome back statement display if login successful
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("\nWelcome back, {}".format(entry_name))
            company = User()
            print(company.foundation())
        # A incoreect statement display if login unsuccessful
        else:
            print("The pin or email is incorrect.")            
            janitor = Janitorial()
            janitor.getLoginInfo()

        

# calls to each class for login input and display message if successful or unsuccessful login.
if __name__ == "__main__":
    customer = User()
    customer.getLoginInfo()
    manager = Employee()
    manager.getLoginInfo()
    janitor = Janitorial()
    janitor.getLoginInfo()
        
    
    
    
