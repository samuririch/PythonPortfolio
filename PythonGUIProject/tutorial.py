import sys
import tkinter 
import random
 
root = tkinter.Tk()             
 
root.geometry('700x400')
label = tkinter.Label(root, text='', font=('Helvetica', 80))
label_two = tkinter.Label(root, text='', font=('Helvetica', 80))
label_three = tkinter.Label(root, text='hello', font=('Helvetica', 80))



def dice_roll():
	diceSides = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] #Unicode strings for die results 1 through 6
	dieOne = random.randint(1,6)
	dieTwo = random.randint(1,6)
	diceResult = dieOne + dieTwo
	secure_random = random.SystemRandom()
	d1 = secure_random.choice(diceSides)
	d2 = secure_random.choice(diceSides)
	label.configure(text=d1)
	label_two.configure(text=d2)
	
	
	label.pack()
	label_two.pack()
	
btn = tkinter.Button(root, text = 'Roll Dice!', bd = '5',
                          command = dice_roll)
 
btn.pack(side = 'top')   


root.mainloop()




