name=input('enter your name:')
amount=eval(input('enter amount to deposits:'))
print('------------------------------------------------------------')

a1=amount//1000
a2=amount%1000

b1=a2//500
b2=a2%500

c1=b2//200
c2=b2%200

d1=c2//100
d2=c2%100

e1=d2//50
e2=d2%50

f1=e2//20
f2=e2%20

g1=f2//10
g2=f2%10

h1=g2//5
h2=g2%5

i1=h2//1
i2=h2%1

print(f'Hi!{name} dreakdown of your deposit is:')
print(a1,'-- 1000php')
print(b1,'--- 500php')
print(c1,'--- 200php')
print(d1,'--- 100php')
print(e1,'---- 50php')
print(f1,'---- 20php')
print(g1,'---- 10php')
print(h1,'----- 5php') 
print(i1,'----- 1php')