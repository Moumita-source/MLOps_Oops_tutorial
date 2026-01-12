class chatbook:

    __user_id = 0

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = 'Default User'
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id

    @staticmethod
    def set_id(id):
        chatbook.__user_id = id    

    def get_name(self):
        return self.__name   

    def set_name(self, name):
        self.__name = name 

    def menu(self):
        user_input = input('''
                            Welcome to Chatbook !!! 
                            How would you like to proceed?
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit
                           

                           ''')   
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()



    def signup(self):
        email = input("Enter your email here -> ")
        password = input("Setup your password here -> ") 
        self.username = email
        self.password = password
        print(f"You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please sign up first by pressing 1 in the main menu")
        else:
            uname = input("Enter your username/email here -> ")
            pwd = input("Enter your password here -> ")
            if self.username == uname and self.password == pwd :
                print("You have signed in successfully")
                self.loggedin = True
            else:
                print("Please enter correct credentials") 

        print("\n")
        self.menu() 

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print(f"You need to signin first to post something")

        print("\n")
        self.menu()  

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the message ? ")
            print(f"Your {txt} message has been sent to your {frnd}")  
        else:
            print(f"You need to signin first to post something")

        print("\n")
        self.menu()          





# obj = chatbook()            





           