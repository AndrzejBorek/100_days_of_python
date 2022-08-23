import prettytable as p
import random as r

table = p.PrettyTable()


table.add_column("Player ID",[1,2,3,4,5,6,7,8,9,10])
table.add_column("Team", ["Lakers","Hawks","Magic","Clippers","Spurs","Bulls","Pelicans","Mavericks","Heat","Celtics"])
table.add_column("Points", [r.randint(10,33),r.randint(10,33),r.randint(10,33),r.randint(10,33),r.randint(10,33),r.randint(10,33),r.randint(10,33),r.randint(10,33),r.randint(10,33),r.randint(10,33)])
table.add_column("Assists", [r.randint(3,10),r.randint(3,10),r.randint(3,10),r.randint(3,10),r.randint(3,10),r.randint(3,10),r.randint(3,10),r.randint(3,10),r.randint(3,10),r.randint(3,10)])

table.align = "l"


print(table)