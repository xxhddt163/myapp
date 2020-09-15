import turtle


def tree(branch_len):
    if branch_len > 5:  # 树干太短不画 递归结束条件
        t.forward(branch_len)  # 画树干
        t.right(20)  # 右倾斜20度
        tree(branch_len - 15)  # 递归调用自身画右边的小树，树干减15
        t.left(40)  # 向左边回40度，即向左边倾斜20度
        tree(branch_len - 15)  # 画左边的小树
        t.right(20)  # 回正
        t.backward(branch_len)  # 海龟返回原位置


t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(75)
t.hideturtle()
