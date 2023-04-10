
HEX_COLORS = {"amethyst": "#9966cc", "babypink": "#f4c2c2", "brightlilac": "#d891ef", "brightlavender": "#bf94e4",
              "brilliantrose": "#ff55a3", "bubblegum": "#ffc1cc", "byzantine": "#bd33a4",
              "cherryblossompink": "#ffb7c5", "cottoncandy": "#ffb7c5", "darkorchid": "#9932cc"}

print(HEX_COLORS)

state_hex_color = input("Enter color name: ").lower()
while state_hex_color != "":
    try:
        print(state_hex_color, "is", HEX_COLORS[state_hex_color])
    except KeyError:
        print("Invalid color")
    state_hex_color = input("Enter color name: ").lower()