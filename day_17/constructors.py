from matplotlib.style import use

#How constructor works:
# class User:
#     def __init__(self) -> None:
#         print("new user is")


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Andrzejborek98"

# print(user_1)
# print(user_1.id)
# print(user_1.username)

#How to create new object with parameters:
#Its simple example of creating account of new user of instagram 
class User:
    def __init__(self, id, username) -> None: # I dont have to declare that followers in parentheses
        self.id = id
        self.username = username
        self.followers = 0  #Because new user will always have 0 followers at start
        self.following = 0 #People who are followed by our object user 

    def add_follower(self):
        self.followers += 1
    
    def subtract_follower(self):
        if self.followers > 0:
            self.followers -= 1
        else: 
            pass

    def follow(self,user):
        user.add_follower()
        self.following += 1



user_1 = User("001","Andrzejborek98")
user_2 = User("002","OlafMorawski223")

# users = []
# users.append(user_1)
# users.append(user_2)

# for user in users:
#     print (f"Id : {user.id}, login : {user.username}, followers: {user.followers}")

# print(user_1.followers) #Checking if followers are equal to 0 

# user_1.add_follower()

# print(user_1.followers) #Checking if follower is added

# user_1.subtract_follower()

# print(user_1.followers) #Checking if follower is subtracted

# user_1.subtract_follower()

# print(user_1.followers) #Checking if condition to not being less than 0 in method subtract followers works

#Checking method follow
user_1.follow(user_2)

print(user_2.followers)

print(user_1.following)

