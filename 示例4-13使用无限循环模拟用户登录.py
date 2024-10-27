#1 初始化变量
i=0
while i<3: # 条件判断
     user_name=input('请输入您的用户名：')
     pwd=input('输入您的密码：')
      # 语句块
      # 登陆操作，if...else..
     if user_name=='jzs' and pwd== '888888':
         print('正在登陆中')
         #需要改变循环变量，目的：退出循环
         i=8   # 第三行 判断i<3,8<3 False退出while循环 # 改变变量
     else:
         if i<2:
             print('用户名或密码不正确,您还有',2-i,'次机会')
         i+=1 # 相当于i=i+1  # 改变变量

# 单分支判断
if i==3:
    print('三次均输入错误')