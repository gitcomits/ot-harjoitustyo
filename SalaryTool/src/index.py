from formatting.format import Format
from ui.ui import UI




def main():

    u_x = UI()

    reformat = Format(u_x)

    reformat.re_format()

    print(u_x.tax_percentage)

if __name__ == "__main__":

    main()
