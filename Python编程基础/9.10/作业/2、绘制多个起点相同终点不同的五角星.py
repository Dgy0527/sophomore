import turtle as t #导入turtle绘图库,并简写为t

def draw_five_stars(length): #定义函数 draw_five_stars，参数 length 表示五角星的边长
    count=1 #初始化计数器 count 为 1
    while count<=5: #循环 5 次，用来画五角星的 5 条边
        t.forward(length) #向前走50步
        t.right(144) #向右转144度（五角星每个外角为 144 度）
        count+=1 #计数器加 1
    length+=10 #函数内的局部变量 length 增加 10，准备下一次递归调用
    if length<=100:                     #如果增加后的 length 不超过 100，就递归调用自己，画一个更大的五角星。
        draw_five_stars(length)         #因为每次画完五角星海龟会回到起点且方向不变，所以这些五角星会以同一点为中心逐渐变大

def main(): #定义主函数
    t.penup() #抬笔，移动时不画线
    t.back(100) #海龟向后（初始方向的反方向）移动 100，让起点大致居中
    t.pendown() #落笔，准备画图
    t.pensize(2) #设置画笔粗细为 2
    t.pencolor("green") #设置画笔颜色为绿色
    segment=50 #初始边长设为 50
    draw_five_stars(segment) #调用函数，开始绘制
    t.Screen().exitonclick() #exitonclick():作用是点击窗口后退出

if __name__=='__main__':  #Python 程序入口判断，如果直接运行本文件就调用 main()
    main() 



'''
豆包给的代码:


import turtle as t

def draw_five_stars(length):
    """绘制一个边长为 length 的五角星"""
    for _ in range(5):
        t.forward(length)
        t.right(144)

def main():
    t.penup()
    t.back(100)          # 向左移动，使五角星大致居中
    t.pendown()
    t.pensize(2)
    t.pencolor("green")

    # 边长从 50 到 100,步长 10,依次绘制逐渐变大的五角星
    for length in range(50, 101, 10):
        draw_five_stars(length)

    t.Screen().exitonclick()   # 点击窗口退出

if __name__ == '__main__':
    main()
'''

'''
![优化示意图](./优化.png)
'''

