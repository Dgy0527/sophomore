# 题目
"""
使用函数的方法，编写程序统计用户输入分数的平均分（去掉最高分，去掉最低分，然后取平均分）
"""

def get_average(scores):
    score_list=scores.copy()
    max_score=max(score_list)
    score_list.remove(max_score)

    min_score=min(score_list)
    score_list.remove(min_score)

    avg=sum(score_list)/len(score_list)
    return avg

if __name__=="__main__":
    shuru=input("请输入多个分数,用英文逗号分开：")
    score_data=[float(i) for i in shuru.split(",")]
    result=get_average(score_data)
    print(f"去掉最高分和最低分的后的平均分是：{result:.2f}")



"""
# 满分代码
def get_average(scores):
    """计算去掉一个最高分、一个最低分后的平均分，兼容重复极值场景"""
    if len(scores) < 3:
        raise ValueError("输入分数数量不能少于3个,无法完成去高低分计算")
    sorted_scores = sorted(scores)
    trimmed = sorted_scores[1:-1]
    return sum(trimmed)/len(trimmed)

if __name__ == "__main__":
    try:
        input_str = input("请输入多个分数,用英文或中文逗号分开(范围0-100):").strip()
        if not input_str:
            print("输入不能为空,请重新运行程序输入分数")
            exit()
        # 替换中文逗号为英文逗号，同时支持两种分隔符输入
        input_str = input_str.replace("，",",")
        try:
            # 分割后去除每个元素前后的空白字符，过滤空字符串，避免空格、连续逗号导致的解析错误
            scores = [float(item.strip()) for item in input_str.split(",") if item.strip( )]
        except ValueError:
            raise ValueError("输入包含非数字内容,请输入有效的分数")
        for s in scores:
            if s<0 or s>100:
                raise ValueError("分数需要在0-100范围内")
        result = get_average(scores)
        print(f"去掉一个最高分和一个最低分之后的平均分是：{result:.2f}")
    except ValueError as e:
        print(f"输入错误:{e}")
"""
        