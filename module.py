import tkinter as tk

global e

def dialog():
    root =tk.Tk()
    root.title('Name')
    st = 'Agile Software Development is based on:'
    tk.Label(root, text=st).grid(row=0)
    tk.Label(root,text='a. Incremental Development').grid(row=1)
    tk.Label(root,text='b.  Iterative Development').grid(row=2)
    tk.Label(root,text='c. Linear Development').grid(row=3)
    tk.Label(root,text='d. Both Incremental and Iterative Development').grid(row=4)
 
    e = tk.Entry(root)
  
    e.grid(row=5, column=0)
 
    def printtext():
    	stri = e.get()
    	if stri=='d':
    		#root.destroy()
    		print( "accepted")
    		root.quit()
    		root.destroy()
    	else:
    		print ("not accepted")
    		root.destroy()

    
    tk.Button(root,text='okay',command=printtext).grid(row=6,column=0, sticky=tk.W,pady=4)
    
    root.mainloop()
    
