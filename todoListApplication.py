import tkinter
import tkinter.messagebox
import pickle
window = tkinter. Tk()
window.title("To Do List")
        #function for adding a task
def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END , todo)
        task_add.delete(0 , tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention!!" , message="To add a task , please enter some task!!")    
        
        #function for removing a task
def task_removing():
    try:
        index_todo = list_frame.curselection()[0]
        list_frame.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention!!" , message="To delete a task, you must select a task!!")       


        #function for loading a task
def task_loading():
    try:
        todo_list = pickle.load(open("tasks.dat" , "rb"))
        list_frame.delete(0,  tkinter, END)
        for todo in tasks:
            list_frame.inset(tkinter.END , todo)
    except:
        tkinter.messagebox.showwarning( title="Attention" , message="Cannot find task.dat")        

            #function for saving a task
def task_save():
    todo_list = list_frame.get(0 , list_frame.size())
    pickle.dump(todo_list, open("task.dat" , "wb"))
list_frame = tkinter.Frame(window)
list_frame.pack()

todo_box = tkinter.Listbox(list_frame , height=20 , width=50 )
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT , fill=tkinter.Y)

todo_box.config(yscrollcommand = scroller.set)
# scroller.config(command=list_frame.yview)


task_add = tkinter.Entry(window , width=70)
task_add.pack()

         #Add Button
add_task_button = tkinter.Button(window , text = "Click to add task" , font = ("arial" , 20 , "bold") ,  background="purple" , width=40 , command = task_adding)
add_task_button.pack()

          #Remove Button
remove_task_button = tkinter.Button(window , text ="Click to delete task" , font=("arial" , 20 , "bold") , background="pink" , width=40 , command = task_removing)
remove_task_button.pack()

           #Load Button
load_task_button = tkinter.Button(window , text ="Click to load task" , font=("arial" , 20 , "bold") , background="cyan" , width=40 , command = task_loading)
load_task_button.pack()

            #Save Button
save_task_button = tkinter.Button(window , text ="Click to save task" , font=("arial" , 20 , "bold") , background="brown" , width=40 , command=task_save )
save_task_button.pack()

window.mainloop()
