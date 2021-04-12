import tkinter as tk

root = tk.Tk()     
root.title('CalCuPy')      
 
root.geometry("600x400")

passw_var=tk.StringVar()


calcInput=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'))
calcInput.grid(row=0,column=0)

def oneEntry():
	calcInput.insert(0, '1')


btn_1 = tk.Button(root, text = '1', bd = '5', command = oneEntry())
btn_1.grid(row=1,column=1)                   

btn_2 = tk.Button(root, text = '1', bd = '5')
btn_2.grid(row=1,column=2)  

btn_3 = tk.Button(root, text = '1', bd = '5')
btn_3.grid(row=1,column=3)  

btn_4 = tk.Button(root, text = '1', bd = '5')
btn_4.grid(row=2,column=1)  

btn_5 = tk.Button(root, text = '1', bd = '5')
btn_5.grid(row=2,column=2)  

btn_6 = tk.Button(root, text = '1', bd = '5')
btn_6.grid(row=2,column=3)  

btn_7 = tk.Button(root, text = '1', bd = '5')
btn_7.grid(row=3,column=1)  

btn_8 = tk.Button(root, text = '1', bd = '5')
btn_8.grid(row=3,column=2)  

btn_9 = tk.Button(root, text = '1', bd = '5')
btn_9.grid(row=3,column=3) 


	
	
  

root.mainloop()


 







