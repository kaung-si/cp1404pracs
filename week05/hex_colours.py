COLOR_TO_CODE = {"ABSOLUTEZERO": "#0048ba", "ACIDGREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff",
                 "ALIZARINCRIMSON": "#e32636", "AMARANTH": "#e52b50", "AMBER": "#ffbf00",
                 "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7", "APRICOT": "#fbceb1",
                 "AQUA": "#00ffff", "ARMYGREEN": "#4b5320"}


def main():
    color_name = input("Enter color name: ")
    formatted_color_name = color_name.strip().upper()
    while color_name != "":
        if formatted_color_name in COLOR_TO_CODE:
            print("Color code of {} is {}".format(color_name, COLOR_TO_CODE[formatted_color_name]))
        else:
            print("The color name is not in memory.")
        color_name = input("Enter color name: ").strip().upper()


main()
