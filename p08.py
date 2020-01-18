a=input('請輸入職級')
if a in ['A','a','B','b']:
    print('年終6個月')
elif a in ['C','c','D','d']:
    print('年終4個月')
elif a in ['E','e','F','f']:
    print('年終3個月')
else:
    print('年終2個月')