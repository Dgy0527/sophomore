area=input('请输入你所在的地区(中国、美国、英国、德国、俄罗斯、澳大利亚、法国、加拿大):')
year=int(input('请输入年份:'))
month=int(input('请输入月份:'))
day=int(input('请输入哪一日:'))
hour=int(input('请输入哪个小时:'))
minute=int(input('请输入哪一分钟:'))
second=int(input('请输入哪一秒:'))

if area=="中国":
    print(f'{year}年{month}月{day}日 {hour}:{minute}:{second}')
elif area=="美国":
    print(f'{month}/{day}/{year} {hour}:{minute}{second}')
elif area =="英国":
    print(f'{day}/{month}/{year} {hour}:{minute}:{second}')
elif area=="德国":
    print(f'{day}.{month}.{year} {hour}:{minute}:{second}')
elif area=="俄罗斯":
    print(f'{day}.{month}.{year} {hour}:{minute}:{second}')
elif area=="澳大利亚":
    print(f'{day}/{month}/{year} {hour}:{minute}:{second}')
elif area=="法国":
    print(f'{day}/{month}/{year} {hour}:{minute}:{second}')
elif area=="加拿大":
    print(f'{year}-{month}-{day} {hour}:{minute}:{second}')
else:
    print('请按提示输入')


