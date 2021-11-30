import turtle



def draw_star():
    window = turtle.Screen()
    star = turtle.Turtle()
    star.color('red', 'blue')
    star.begin_fill()
    for i in range(36):
        star.forward(200)
        star.left(170)
    star.end_fill()
    turtle.done()
    window.mainloop()


def run():
    draw_star()

if __name__ == '__main__':
    run()


