#attendance tracker
student_name = ""
student_status=""
def show_menu():
    print("\n--Attendance Tracker-----------")
    print('1.Add Attendance')
    print('2.View Attendance')
    print('3.Exit')
def add_attendance():
    global student_name
    global student_status
    student_name = input('Enter student name: ')
    student_status = input('Enter status (Present/Absent):')
    print('Attendance added successfully.')
def view_attendance():
    if student_name == '':
        print('No attendance record found.')
    else:
        print('\n---Attendance Record ---')
        print(student_name, '-' ,student_status)
def main():
    while True:
        show_menu()
        choice=input('Enter your choice :')
        if choice == '1':
            add_attendance()
        elif choice == '2':
            view_attendance()
        elif choice =='3':
            print('Exitting the program')
            break
        else:
            print('Invalod choice. Try again')
main()
