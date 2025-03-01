import os
import ast
from datetime import datetime

def main() :

    user_name: str = None #user name set to none in case the, useful for when the user clicks option 8 later in the code and the user haven't performed any task

    #declaring status variables to be used in dictionaries to get the status of the tasks to either active, complete or deleted
    status1:str = 'Active'
    status2:str = 'completed'
    status3:str = 'deleted'

    #checking if the file that contains the users name exists and if it does read out the firstline from the text
    file_path = "name.txt"
    if os.path.exists(file_path):
        with open ("name.txt", "r") as file:
            user_name = file.readline()
        
    #creating a file that contains the users name incase the filename wasn't found upon the initialization of this code 
    if not os.path.exists(file_path):
        user_name = input("Hello, What is your firstname? ").strip()
        with open ("name.txt", "w") as file:
            file.write(user_name)
   
    def print_active_tasks(file_name: str):
                #file_name -> required
                '''a funtion that prints out of a file in the program folder '''
        
                with open (file_name, 'r') as file:
                    data = file.read()
                my_list = ast.literal_eval(data)
                for idx, item in enumerate(my_list):
                    print(f" Task ID: {idx + 1}, {item} ")
                return my_list

    def check_or_create(task_status: str) -> list :
        #task_status -> required
        '''A function that checks within my program folder if tasks files exists.  If not create new lists to store the tasks'''
       
        if not os.path.exists(task_status):
            
                return []
    #Initializing the list of tasks
    
    completed = check_or_create('completed.txt')
    active = check_or_create('active.txt')
    deleted = check_or_create('deleted.txt')

    #the whole program runs in a loop to be broken only if option 8 is picked by the user
    while True:
        print(f'''Hello {user_name}, this is your Todo List Manager. How may I help you today
              
                 Menu
                 ___________________________________
                 1. Add task
                 2. View active tasks
                 3. View completed tasks
                 4. View deleted tasks
                 5. Edit tasks name
                 6. Mark task as complete
                 7. Delete task 
                 8. Exit program 
              
              
                     ''')
         # try keyword used at every block of code in anticipation to handle errors and not exit our program, maybe user inputs not integers            
        try:

         option = int((input("Select an Option: ")).strip())
         #option for adding of new task
         if option == 1:
            
            task_name = input(f'{user_name}, please enter a new tasks:').strip()
            currentdatetime = datetime.now()
            current_datetime = currentdatetime.strftime("%Y-%m-%d %H:%M:%S")
            #checking if active file already exists, if yes read from the file and make manipulation
            if os.path.exists('active.txt'):
                with open ('active.txt', 'r') as file:
                    data = file.read()
                my_list = ast.literal_eval(data)
     
                catalogue : dict[str,str] = {'name': task_name, "status": status1, "created": current_datetime, "finished": "unfinished" }
                my_list.append(catalogue)
                with open ('active.txt','w') as file:
                    file.write(str(my_list))
            # if file name does exist, make manipulatin to the list created upon intialization of the code
            else: 
                
                
                catalogue : dict[str,str] = {'name': task_name, "status": status1, "created": current_datetime, "finished": "unfinished" }
                active.append(catalogue)

        #option to view active tasks
         elif option == 2:
            #checking if active file already exists, if yes read from the file
            if os.path.exists('active.txt'):
                print_active_tasks('active.txt')
            
            else: 
                # if file name does exist, read from the list created upon initialization
                for idx, item in enumerate(active):
                    print(f" Task ID: {idx + 1}, {item} ")
        #option to display completed tasks
         elif option == 3:
            if os.path.exists('completed.txt'):
                print_active_tasks('completed.txt')
                
            
            else: 
                for idx, item in enumerate(completed):
                    print(f" Task ID: {idx + 1}, {item} ")
        #option that displays deleted tasks
         elif option == 4:
            if os.path.exists('deleted.txt'):
                print_active_tasks('deleted.txt')
            
            else: 
               for idx, item in enumerate(deleted):
                    print(f" Task ID: {idx + 1}, {item} ")
        #option that change name of task
         elif option == 5:
            if os.path.exists('active.txt'):
                
                my_list = print_active_tasks('active.txt')
                try:

 
                   task_number = int(input('What task do you want to edit? ')) -1
                   if 0 <=  task_number < len(my_list) :
                       new_task = input('What would you like the new task name to be? ')
                       my_list[task_number]['name'] = new_task
                   else:
                    print('invalid Task number')
                except ValueError:
                    print("Please Enter a valid number")
                with open ("active.txt", "w") as file:
                    file.write(str(my_list))
                
            
            else: 
                for idx, item in enumerate(active):
                    print(f" Task ID: {idx + 1}, {item} ")
                try:

 
                   task_number = int(input('What task do you want to edit? ')) -1
                   if 0 <=  task_number < len(active) :
                       new_task = input('What would you like the new task name to be? ').strip()
                       active[task_number]['name'] = new_task
                   else:
                    print('invalid Task number')
                except ValueError:
                    print("Please Enter a valid number")
         #option that mark tasks as active and remove the tasks from active tasks, add them to completed list or completed file
         elif option == 6:
            if os.path.exists('active.txt'):
                
                my_list = print_active_tasks('active.txt')
                
                try:

 
                   task_number2 = int(input('What task do you want to mark as completed ')) -1
                   my_list[task_number2]['status'] = status2
                   my_list[task_number2]['finished'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                   if 0 <=  task_number2 < len(my_list) :
                       if os.path.exists('completed.txt'):
                          with open ('completed.txt', 'r') as file:
                               data5 = file.read()
                          my_list5 = ast.literal_eval(data5)
                          
                       
                          
                
                         
                          my_list5.append(my_list[task_number2])
                          my_list.pop(task_number2)
                          with open ('completed.txt','w') as file:
                             file.write(str(my_list5))
                       
                     
                   else:
                    print('invalid Task number')
                except ValueError:
                    print("Please Enter a valid number")
                with open ("active.txt", "w") as file:
                    file.write(str(my_list))
                
            
            else: 
                for idx, item in enumerate(active):
                    print(f" Task ID: {idx + 1}, {item} ")
                try:

 
                   task_number2 = int(input('What task do you want to mark as complete? ')) -1
                   if 0 <=  task_number2 < len(active) :
                       active[task_number2]['status'] = status2
                       active[task_number2]['finished'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                       completed.append(active[task_number2])
                       active.pop(task_number2)
                   else:
                    print('invalid Task number')
                except ValueError:
                    print("Please Enter a valid number")
        #option that deletes tasks from active file or list, and add them to deleted file or list
         elif option == 7:
            if os.path.exists('active.txt'):
                
                my_list = print_active_tasks('active.txt')
                try:

 
                   task_number3 = int(input('What task do you want to delete ')) -1
                   my_list[task_number3]['finished'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                   my_list[task_number3]['status'] = status3
                   if 0 <=  task_number3 < len(my_list) :
                       if os.path.exists('deleted.txt'):
                          with open ('deleted.txt', 'r') as file:
                               data7 = file.read()
                          my_list7 = ast.literal_eval(data7)
                          
                          
                
                         
                          my_list7.append(my_list[task_number3])
                          my_list.pop(task_number3)
                          with open ('deleted.txt','w') as file:
                             file.write(str(my_list7))
                       
                    
                   else:
                    print('invalid Task number')
                except ValueError:
                    print("Please Enter a valid number")
                with open ("active.txt", "w") as file:
                    file.write(str(my_list))
                
            
            else: 
                for idx, item in enumerate(active):
                    print(f" Task ID: {idx + 1}, {item} ")
                try:

 
                   task_number3 = int(input('What task do you want to mark as complete? ')) -1
                   if 0 <=  task_number3 < len(active) :
                       active[task_number3]['status'] = status3
                       active[task_number3]['finished'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                       deleted.append(active[task_number3])
                       active.pop(task_number3)
                   else:
                    print('invalid Task number')
                except ValueError:
                    print("Please Enter a valid number")

        # option 8 to exit the program and create the files to save task lists if the program is being ran on the system for the first time 
         elif option == 8:
            if user_name is None:
                print('You haven\'t even used the program')
            else:
                print(f"so sad to see you go {user_name}")
            if not os.path.exists("active.txt"):
        
       
                with open ("active.txt", "w") as file:
                    file.write(str(active))
            if not os.path.exists("completed.txt"):
        
       
                with open ("completed.txt", "w") as file:
                    file.write(str(completed))
                 
            if not os.path.exists("deleted.txt"):
        
       
                with open ("deleted.txt", "w") as file:
                    file.write(str(deleted))

            break

         else: 
            print(f"Please enter a valid input between 1-8")

         print("\n" + "-" * 20) 
        except ValueError:
            print("Enter a valid integer")
          
            
                    
if __name__ == "__main__":
    main()