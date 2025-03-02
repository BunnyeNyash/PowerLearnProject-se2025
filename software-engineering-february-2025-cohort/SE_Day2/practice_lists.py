"""
Questions:

Create a list called colors with at least 5 different colors. Print the second color.
Add a new color to the list.
Replace the first color with "black".
Remove the last color.
Loop through the list and print each color.

"""

colors = ["purple", "red", "white", "blue", "maroon"]

print(colors[1])                    # 1

colors.append("cyan")               # 2
print(colors)

colors[0] = "black"                 # 3
print(colors)

del colors[-1]                      # 4
print(colors)

for color in colors:                # 5
    print(color)
