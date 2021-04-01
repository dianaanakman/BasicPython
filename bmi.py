weight_in_kg = float(input('please enter your weight : \n'))
height_in_m = float(input('please enter your height in m : \n'))

bmi_formula = weight_in_kg / height_in_m ** 2

if bmi_formula < 18.5:
    print('you underweight')
elif bmi_formula >= 18.5 and bmi_formula<= 24.9:
    print('normal weight')
elif bmi_formula >=25.0 and bmi_formula <= 29.9:
    print('normal weight')
elif bmi_formula >= 30.5 and bmi_formula <= 34.9:
    print('boleh la')
elif bmi_formula >= 35.5 and bmi_formula <= 39.9:
    print('your weight status is obesity class 2')
elif bmi_formula >= 40:
    print('your weight status is obesity class 3')