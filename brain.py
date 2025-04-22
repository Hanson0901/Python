w=input('please input your weight (kg):')
w=float(w)
h=input('please input your height (cm):')
h=float(h)
BMI=w/pow(h,2)
if int(BMI)<18.5:
    print('You are underweight')
elif  18.55<=int(BMI)<24:
    print('normal')
elif 24<=int(BMI)<27:
    print('slightly heavier')
elif 27<=int(BMI)<30:
    print('mild obesity')
elif 30<=int(BMI)<35:
    print('moderate obesity') 
else :
    print('severe obesity')
