# Expense Tracker
expenses =[]
def add_expense():
    name=input('Enter expense name: ')
    amount=input('Expenses amount: ')
    expense ={
        'name':name,
        'amount':amount
    }
    expenses.append(expense)
    print('Enter added.')
def view_expenses():
    for expense in expenses:
        print(expense['name'],expense['amount'])
def show_menu():
    print('\n Expense Tracker')
    print('1,Add expense')
    print('2.view expenses')
    print('3.exit')
def main():
    while True:
        show_menu()
        choice= input('Enter choice: ')
        if choice =='1':
            add_expense()
        elif choice =='2':
            view_expenses()
        elif choice =='3':
            print('Exitting program')
            break
        else:
             print('Invalid choice.Try again')
main()
