# #SCOPE A variable is only available from inside the region it is created.

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function {enemies}")

# increase_enemies()

# print(f"enemies outside function {enemies}")

# .....................

# Local scope


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

# print(potion_strength) won't work, potion_strength is not visible

# .....................

# Global scope 

# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()
# print(player_health)

# ...............

# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()

# drink_potion() # again potion won't be visible

# game()

# print(player_health)

# There is no block scope

# if 30 > 10:
#     a = 20

# print(a) #It works fine

# ................

# game_level = 3
# enemies = ["Zombie","Skeleton","Alien"]
# if game_level <5 :
#     new_enemy = enemies[0]

# print(new_enemy) #Works fine

# ................

# game_level = 3
# def create_enemy():
#     enemies = ["Zombie","Skeleton","Alien"]
#     if game_level <5 :
#         new_enemy = enemies[0]

# print(new_enemy) #Now if its closed in function it won't work

#Modyfing Global Scope:
# def game():
#     enemies = 1

#     def increase_enemies():
#         enemies #it is considered to be bad approach because of easy missing what variable i am modifying
#         enemies += 1
#         print(f"Enemies inside function {enemies}")

#     increase_enemies()
# game()
# print(f"enemies outside function {enemies}")

#One of correct approaches might be returning value which i want to get


# enemies = 1

# def increase_enemies():
#     print(f"Enemies inside function {enemies}")
#     return (enemies + 1)
    

# enemies = increase_enemies()

# print(f"enemies outside function {enemies}")

#....................

#Global constants

# PI = 3.14159 #In python there is no const values, but we write it with uppercase so other programmers know that this value shouldn't be changed

# PI = 23

# print(PI)

#..............

