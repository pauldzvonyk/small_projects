from canvas import Canvas
from shapes import Square, Rectangle

# Get canvas input
c_height = int(input("Enter canvas height: "))
c_width = int(input("Enter canvas width: "))

# get canvas color input
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}

while True:
    c_color = input("Choose a color of the canvas (black or white): ").lower()
    if c_color in ["black", "white"]:
        canvas = Canvas(height=c_height, width=c_width, color=colors[c_color])
        break
    elif c_color == "q":
        break
    else:
        print(f"'{c_color}' is not supported color, choose between 'black' or 'white' (q to quit)")

while True:
    shape_type = input("What would you like to draw (square or rectangle)? Enter q to quit.")
    if shape_type.lower() == "square":
        # Get square input
        square_x = int(input("Enter X for the square: "))
        square_y = int(input("Enter Y for the square: "))
        square_side = int(input("Enter square side length: "))
        red = int(input("Enter red intensity of the square (from 0 to 255): "))
        green = int(input("Enter green intensity of the square (from 0 to 255): "))
        blue = int(input("Enter blue intensity of the square (from 0 to 255): "))

        s1 = Square(x=square_x, y=square_y, side=square_side, color=(red, green, blue))
        s1.draw_square(canvas)

    elif shape_type.lower() == "rectangle":
        rec_x = int(input("Enter X for the rectangle: "))
        rec_y = int(input("Enter Y for the rectangle: "))
        rec_height = int(input("Enter rectangle height: "))
        rec_width = int(input("Enter rectangle width: "))
        red = int(input("Enter red intensity of the rectangle (from 0 to 255): "))
        green = int(input("Enter green intensity of the rectangle (from 0 to 255): "))
        blue = int(input("Enter blue intensity of the rectangle (from 0 to 255): "))

        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw_rectangle(canvas)

    elif shape_type.lower() == "q":
        break

    else:
        print(f"Sorry, can not draw '{shape_type}', only square and rectangle are allowed.")

    canvas.make_canvas("files/canvas.png")
