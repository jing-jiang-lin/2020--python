a=input('輸入性別(M/F)')

if a=='M':
    print('公')

#(if a in ['M','m']:)
if a=='M' or a=='m':
    print('公')

elif a in ['F','f']:
    print('母')

else:
    print('404 not found')