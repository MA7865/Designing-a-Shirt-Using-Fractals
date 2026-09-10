import turtle
import colorsys

def generate_sequence(iterations):
    sequence = "FX"
    for _ in range(iterations):
        next_seq = ""
        for ch in sequence:
            if ch == "X":
                next_seq += "X+YF+"
            elif ch == "Y":
                next_seq += "-FX-Y"
            else:
                next_seq += ch
        sequence = next_seq
    return sequence

def hsb_to_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb((h % 360) / 360, s, v)
    return (r, g, b)

def draw_arm(t, sequence, length, heading_offset, total_f):
    t.penup()
    t.goto(0, 0)
    t.setheading(heading_offset)
    t.pendown()

    hue_start = 195
    hue_end = 165
    f_count = 0
    for ch in sequence:
        if ch == "F":
            progress = f_count / total_f
            hue = hue_start + progress * (hue_end - hue_start)
            sat = 0.7 - 0.15 * progress
            bright = 0.45 + 0.5 * progress
            t.pencolor(hsb_to_rgb(hue, sat, bright))
            t.forward(length)
            f_count += 1
        elif ch == "+":
            t.right(90)
        elif ch == "-":
            t.left(90)

def main():
    screen = turtle.Screen()

    win_w, win_h = 900, 900

    # force true centering instead of relying on OS/turtle defaults
    root = screen.getcanvas().winfo_toplevel()
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    startx = (screen_w - win_w) // 2
    starty = (screen_h - win_h) // 2

    screen.setup(width=win_w, height=win_h, startx=startx, starty=starty)
    screen.bgcolor("#031419")
    screen.title("Dragon Curve Fractal - Sea Mandala")
    screen.colormode(1.0)
    screen.tracer(60, 0)

    iterations = 12
    sequence = generate_sequence(iterations)
    total_f = sequence.count("F")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2.4)

    for arm in range(4):
        draw_arm(t, sequence, length=5, heading_offset=arm * 90, total_f=total_f)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()