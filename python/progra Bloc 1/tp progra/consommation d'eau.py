cvd = 2.16
cva = 2.35
R = 20* cvd + 30* cva
q = float(input("add your consomation :"))

if 0<q<30:
    p = 0.5*q*cvd
elif q < 5000:
    p = q*cvd + q*cva
elif  q > 5000:
    p = 0.9*q*cvd + q *cva
f = R + p
print("you need to pay ",f )