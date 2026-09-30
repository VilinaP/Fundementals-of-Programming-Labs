from tkinter import*
from tkinter import messagebox 
from random import*

tasks = []

def update_listbox():
  listbox.delete(0, END) 
  for task in tasks:
   listbox.insert(END, task)
   
    
def add_task():
  task  = ent.get()
  if task != '':
    tasks.append(task)
    update_listbox()
  else:
    messagebox.showwarning('Warning!', 'Empty string' )
  ent.delete(0,END)
def del_one():
  task = listbox.get('active')
  if task in tasks: 
    tasks.remove(task)
  update_listbox()
  
def del_all():
  yes = messagebox.askyesno('Confrim', 'Are you sure?')
  if yes:
    global tasks
    tasks = []
    update_listbox()
def sort_ask():
  tasks.sort()
  update_listbox()
  
  
def sort_desk():
  tasks.sort(reverse = True)
  update_listbox()
  
def rend_task():
  if len(tasks)>0:
   task = choice(tasks)
   lb_display['text'] = task
def amound():
  num = len(tasks)
  lb_display['text'] = 'Number:' + str(num)    

root = Tk()
root.title('Task Planner')
root.geometry('600x600')
root['bg'] = 'white'

frame = Frame(root)
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

lb_display = Label(frame)
lb_display.place(rely = 0.1, relx = 0.34)

ent = Entry(frame, width = 35)
ent.place(rely = 0.15, relx = 0.34)

btn_add = Button( frame, text = "Add", command = add_task )
btn_add.place( rely = 0.15, relwidth = 0.25)

btn_del_one = Button( frame, text = "Delete one", command = del_one)
btn_del_one.place( rely = 0.25, relwidth = 0.25)

btn_del_all = Button( frame, text = "Delete all", command = del_all )
btn_del_all.place( rely = 0.35, relwidth = 0.25)

btn_sort_ask= Button( frame, text = "Sort A - Z", command = sort_ask )
btn_sort_ask.place( rely = 0.45, relwidth = 0.25)

btn_sort_desk = Button( frame, text = "Sort Z - A", command = sort_desk )
btn_sort_desk.place( rely = 0.55, relwidth = 0.25)

btn_rend_task = Button( frame, text = "Random", command = rend_task )
btn_rend_task.place( rely = 0.65, relwidth = 0.25)

btn_amound = Button( frame, text = "Amound", command = amound )
btn_amound.place( rely = 0.75, relwidth = 0.25)

listbox = Listbox(frame)
listbox.place(relx = 0.34, rely = 0.25, relwidth=0.6,relheight=0.6)




root.mainloop()