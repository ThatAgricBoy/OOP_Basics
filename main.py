import another_module
from prettytable import PrettyTable


from turtle import Turtle, Screen
print(another_module.another_variable)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
timmy.right(25)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"
table.header = True
table.border = True
print(table)
