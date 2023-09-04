import os

def clear_screen():
    os.system('cls')
    
def Adding_a_task():
        Temp_list = []
        while True:
            new_entry = input("Enter a new Task: ")
            Temp_list.append(new_entry)
            print("New Task Added", Temp_list)
            
            choice = input("Do you want to add another task ? (y/n)\n")            
            if choice == "y" :
                continue
            else:
                print("To do list updated successfully")
                return Temp_list

def View_all_task():
    View_all_list = List.copy()
    print(View_all_list[:])
    
def Removing_Task():
    Removing_list = List.copy()
    print(Removing_list[:])
    index_input = input("Enter the Task that you want to delete: ")
    Removing_list.remove(index_input)
    print("Task Deleted Successfully")
    return Removing_list
    
List = []
while True:
    print("\n\tWelcome to the TO-DO list",end="\n\t------------------------\n")
    print("Main Menu\n")
    print('''
    1. Add a new Task
    2. View all Tasks
    3. Remove a Task
    4. Exit
    ''')
    inputChoice = int(input("Enter the choice number: "))
    if (inputChoice <= 4):    
        match inputChoice:
            case 1:
                print("\nAdding a new Task",end="\n------------------------\n")
                New_List = Adding_a_task()
                List.extend(New_List)
                clear_screen()
                continue
                
            case 2:
                print("\nViewing all the Tasks", end="\n------------------------\n")
                View_all_task()
                Button = input("Click F + Enter to return to Main Menu: ")
                if Button == "F" and "f":
                    clear_screen()
                    continue
            case 3:
                print("Removing a Tasks", end="\n------------------------\n")
                New_List = Removing_Task()
                List = New_List.copy()
                clear_screen()
                continue
                
            case 4:
                print("Exit the Program")
                break
    else:
        print("Invalid Input")
                    