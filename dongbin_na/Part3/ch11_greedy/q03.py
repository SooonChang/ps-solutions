array = input()
a = array.split('1')
b = array.split('0')
a_cnt = 0
b_cnt = 0
for i in a:
    if i != '':
        a_cnt +=1
for i in b:
    if i !='':
        b_cnt +=1
print(min(a_cnt, b_cnt))