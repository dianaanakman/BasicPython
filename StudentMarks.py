student_marks = int(input('please enter your marks\n'))

if student_marks >= 80 and student_marks <= 100:
    print('You got A!')
elif student_marks >= 60 and student_marks < 80:
    print('You got B!')
elif student_marks >= 40 and student_marks < 60:
    print('You got C!')
elif student_marks >= 0 and student_marks < 40:
    print('You failed!')
else:
    print('You have input invalid marks')
