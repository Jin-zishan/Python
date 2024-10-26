#coding=utf-8
answer=input('请问你喝酒吗？')
if answer=='y':  # answer的值为y表示喝酒了
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('不构成酒驾。')
    elif proof<80: # 20<=proof<80
        print('已经构成酒驾,请不要开车')
    else:
        print('已经达到了醉驾标准，请千万不要开车！')
else:
    print('你走吧')
