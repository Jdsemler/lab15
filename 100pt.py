#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
oval = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
 		self.button1.configure(text="Left", background= "green")
 		self.button1.grid(row=0,column=1)
		self.button1.bind("<Button-1>", self.button1Click)
 	        # Add a second button!
						
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="up", background= "yellow")
		self.button2.grid(row=0,column=2)		
		self.button2.bind("<Button-1>", self.button2Click)
			
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="down", background= "red")
		self.button3.grid(row=0,column=3)	
		self.button3.bind("<Button-1>", self.button3Click)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="right", background= "light blue")
		self.button4.grid(row=0,column=4)		
		self.button4.bind("<Button-1>", self.button4Click)
		
		#Creates the drawpad
		drawpad.pack()
		self.animate
					
		# BINDING THE BUTTONS												
	def button1Click(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
		drawpad.move(oval,-20,0)
		global oval
		global drawpad
			
 	def button2Click(self, event):   
 		# Make the oval move up!
                 # "global" makes sure that we can access our oval and our drawpad
		drawpad.move(oval,0,-20)
 		global oval
 		global drawpad
 		
        def button3Click(self, event):   
 		# Make the oval move down!
                 # "global" makes sure that we can access our oval and our drawpad
		drawpad.move(oval,0,20)
 		global oval
 		global drawpad
 		
 	def button4Click(self, event):   
 		# Make the oval move to the right!
                 # "global" makes sure that we can access our oval and our drawpad
		drawpad.move(oval,20,0)
 		global oval
 		global drawpad
 		
		
	def moveUp(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                drawpad.move(player,0,-10)
    
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)
	    # Insert the code here to make the target move, bouncing on the edges    
	        
	        
            
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)
                
                # Get the x and y co-ordinates of the circle
                x1, y1, x2, y2 = drawpad.coords(target)
                if x2 > drawpad.winfo_width(): 
                    dir1 = -6
                elif x1 < 0:
                    dir1 = 6
                #Move our oval object by the value of direction
                drawpad.move(target,dir1,0)
                
                # Wait for 1 millisecond, then recursively call our animate function
                drawpad.after(5, animate2)
            

                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)

root.mainloop()