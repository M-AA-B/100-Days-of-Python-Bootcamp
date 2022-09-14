# Exercise 3 - Treasure Map

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))
y = int(position / 10)
x = position - y*10
map[x-1][y-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
