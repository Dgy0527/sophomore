# 题目
"""
以一个正整数n为例，如果n为偶数，就将它变为n/2，如果除后变为奇数，则将它乘3加1（即3n+1）。不断重复这样的运算，经过有限步后，必然会得到1。
本实例要求编写代码，计算用户输入的数据按照以上规律经多少次运算后可变为1。
"""

def jiaogu(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

if __name__ == "__main__":
    try:
        num = int(input("请输入一个正整数："))
        if num < 0:
            print("请输入大于0的正整数")
        else:
            res = jiaogu(num)
            print(f"一共需要 {res} 次运算得到1")
    except ValueError:
        print("输入错误,请输入整数")