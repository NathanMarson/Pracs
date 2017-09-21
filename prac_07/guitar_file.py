from prac_07.guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    name = input("Name:")
    year = input("Year:")
    cost = input("Cost:")
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


    print("These are my guitars:")
    i = 0
    for guitar in guitars:
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
        i+=1

main()