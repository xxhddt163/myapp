import turtle  # python用来作图的模板

t = turtle.Turtle()


def recur_image(line):
    """通过调用turtle模板绘制递归正方形"""
    if line > 0:
        t.forward(line)  # 画一条长度为line的直线
        t.right(90)  # 向右转动90度
        return recur_image(line - 3)


recur_image(500)
