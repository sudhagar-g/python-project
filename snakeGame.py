from tkinter import *   #importing GUI library to create window,canvas,button label etc. 
import random 


 

GAME_WIDTH =  700   #game width
GAME_HEIGHT = 700   #game height
SPEED = 100    #game speed
SPACE_SIZE  = 25    #snake food size and movement step 25 px
BODY_PARTS = 3      #starting length of the snake
SNAKE_COLOR = "#00FF00"   
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


#creating class  for snake 
class Snake:
    def __init__(self):
         self.body_size = BODY_PARTS    
         self.coordinates = []        # a list storing each part of the snake
         self.squares = []              #storing rectangle shape  --> snake body part

         
     
         for i in range(0,BODY_PARTS):      # This code is initializing the snake’s body parts
              self.coordinates.append([0,0])

         for x,y in self.coordinates:        # this line create snake body part with canvas rectangle shape 
                   square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill =SNAKE_COLOR,tag = "snake")
                   self.squares.append(square)  
         
#creating class for food
class Food:

        def __init__(self):             
               x= random.randint(0,(GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE         # to initializing the food in  in random place and
               y= random.randint(0,(GAME_HEIGHT // SPACE_SIZE)-1) * SPACE_SIZE      #x ,y is coordinates for food randome location
           
                    #creating food shape
               self.coordinates=[x,y]
               canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill = FOOD_COLOR,tag = "food")
             
    
def new_turn(snake,food):

    x,y = snake.coordinates[0]

    if direction == "up":
         y -= SPACE_SIZE
    elif direction == "down":     
         y+= SPACE_SIZE
    elif direction == "left":
         x-=SPACE_SIZE
    elif direction == "right":   
         x+= SPACE_SIZE 

    snake.coordinates.insert(0,(x,y)) 

    



    square = canvas.create_rectangle(x,y,x + SPACE_SIZE, y + SPACE_SIZE,fill=SNAKE_COLOR) 

    snake.squares.insert(0,square)


    if x == food.coordinates[0] and y == food.coordinates[1]:
         global score

         score += 1
         label.config(text='score:{}'.format(score))

         canvas.delete("food")

         food = Food()

         

    else:    

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]

    if check_collisions(snake):
         game_over()   

    else: 
        window.after(SPEED,new_turn,snake,food)   



def change_direction(new_direction):
     global direction

     if new_direction == 'left':
          if direction != 'right':
               direction = new_direction
     elif new_direction == 'right':
          if direction != 'left':
               direction = new_direction           
     elif new_direction == 'up':
          if direction != 'down':
               direction = new_direction
     elif new_direction == 'down':
          if direction != 'up':
               direction = new_direction          

    
def check_collisions(snake):
    x,y = snake.coordinates[0]

    if x < 0 or  x >= GAME_WIDTH:
         return True
    elif y < 0 or  y >= GAME_HEIGHT:
         return True
    

    for body_part in snake.coordinates[1:]:
         
         if x == body_part[0] and y == body_part[1]:
              return True
    
def game_over():
    canvas.delete(ALL)

    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font = ("consolas",70),
                       text = "GAME OVER",
                       fill = 'red',
                       tag = "game over"
                       )

window = Tk()
window.title("Snake Game")
window.resizable(False,False)

score = 0
direction = 'down'

label = Label(window,text="Score:{}".format(score),font=('consolas',40))
label.pack()

canvas = Canvas(window,width=GAME_WIDTH,height=GAME_HEIGHT,bg=BACKGROUND_COLOR)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))

snake = Snake()
food = Food()

new_turn(snake,food)

window.mainloop()

      
