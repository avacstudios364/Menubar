from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Menu demonstation')

#Creating menubar
menubar = Menu(root)

#Adding file menu/commands
file = Menu(menubar, tearoff= 0)
menubar.add_cascade(label = 'File', menu = file)
file.add_command(label = 'New File', command = None)
file.add_command(label = 'Open', command = None)
file.add_command(label = 'Save', command = None)
file.add_separator() #line separates whats below and above
file.add_command(label = 'Exit', command = root.destroy)

'''tearoff command allows you to detach menu into separate menu (if set to 1)
if it is set to 0, it will not allow this funtionality'''
edit = Menu(menubar, tearoff= 0 )
menubar.add_cascade(label = 'Edit', menu = edit)
edit.add_command(label = 'Cut', command = None)
edit.add_command(label = 'Copy', command = None)
edit.add_command(label = 'Paste', command = None)
edit.add_command(label = 'Select All', command = None)
edit.add_separator()
edit.add_command(label = 'Find', command = None)

root.config(menu=menubar)
root.mainloop()
