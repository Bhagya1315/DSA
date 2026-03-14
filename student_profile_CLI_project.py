student_id = ""
name=""
age=""
course=""
while True:
    print('--------student profile menu ----')
    print('1.Add student')
    print('2.View student')
    print('3.Update student')
    print('4.Delete student')
    print('5.exit')

    choice = input('Enter Choice: ')
    if choice=='1':
        student_id=input('Enter student ID: ')
        name=input('Enter Name: ')
        age=input('Enter age: ')
        course=input('Enter course: ')
        print('Student added successfully')
    elif choice =='2':
        if student_id=='':
            print('No student found')
        else:
            print('\n Student data' )
            print('ID: ', student_id)
            print('Name:', name)
            print('Age: ',age)
            print('Course: ', course)
    elif choice=='3':
        if student_id=='':
            print('No student found to update')
        else:
            name=input('Enter name:')
            age=input('enter name:')
            course=input('Enter course: ')
            print('Student updated successfully')
    elif choice=='4':
        if student_id=='':
            print('No student found to delete')
        else:
            student_id=''
            name=''
            age=''
            course=''
            print('student deleted')
    elif choice=='5':
        print('Program Exitted')
        break
    else:
        print('Invalid choice')

