from rectangle import Rectangle
from circle import Circle
from square import Square

def polymorphism_check():
    print("--- Polymorphism check ---")
    c1 = Circle(0, 0, 4, "Circle_1")
    c2 = Circle(0, 0, 9, "Circle_2")
    r1 = Rectangle(10, 20, "Rectangle_1")
    r2 = Rectangle(20, 30, "Rectangle_2")
    s1 = Square(10, "Square")

    shapes = [c1, c2, r1, r2, s1]
    for shp in shapes:
        print(str(shp))
    return c1, r1, s1

def getters_setters_check(c1, r1, s1):
    print("\n--- Getter/setter check")
    print(f"{c1.name} Current:  {c1.radius:g} {c1.area:.5f}")
    c1.radius *= 2
    print(f"{c1.name} Doubled:  {c1.radius:g} {c1.area:.5f}")

    print(f"\n{r1.name} Current:  {r1.length:g} {r1.width:g} {r1.area:g}")
    r1.length *= 2
    r1.width *= 2
    print(f"{r1.name} Doubled:  {r1.length:g} {r1.width:g} {r1.area:g}")

    print(f"\n{s1.name} Current:  {s1.side:g} {s1.area:g}")
    s1.side *= 2
    print(f"{s1.name} Doubled:  {s1.side:g} {s1.area:g}")

def main():
    c1, r1, s1 = polymorphism_check()
    getters_setters_check(c1, r1, s1)

if __name__ == "__main__":
    main()