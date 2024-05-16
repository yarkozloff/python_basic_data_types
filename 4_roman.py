a = int(input());
m=a//1000%10
c=a//100%10
l=a//10%10
i=a%10

if (m!=None):
    total0 = "M" * m
if (c!=None):
   if c==9:
    total1="CM"
   elif c==4:
    total1="CD"
   elif c>4:
    total1="D"+"C"*(c-5)
   else:
    total1="C"*c;
if (l!=None):
   if l==9:
    total2="XC"
   elif l==4:
    total2="XL"
   elif l>4:
    total2="L"+"X"*(l-5)
   else:
    total2="X"*l;
if (i!=None):
   if i==4:
    total3="IV"
   elif i>5 and i<9:
    total3="V"+(i-5)*"I"
   elif i==5:
    total3="V"
   elif i==9:
    total3="IX"
   else:
    total3="I"*i;
print(total0+total1+total2+total3);
 
 #  I - 1, V - 5, X - 10, L - 50, C - 100, D - 500, M - 1000
