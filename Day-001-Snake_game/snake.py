from turtle import Turtle

move_distance = 20

class Snake:

    def __init__(self):

        self.turtle_list = []
        
        x = 0 # Starting Position

        for _ in range(0,3):
            tim = Turtle()
            tim.penup()
            tim.shape("square")
            tim.color("white")
            tim.goto(x,0)
            x-=20
            self.turtle_list.append(tim)
        
        self.turtle_head = self.turtle_list[0]
    
    def move(self):

        for tur_num in range(len(self.turtle_list)-1,0,-1):
            new_x = self.turtle_list[tur_num-1].xcor()
            new_y = self.turtle_list[tur_num-1].ycor()
            self.turtle_list[tur_num].goto(new_x,new_y)

        self.turtle_head.forward(move_distance)
    
    def up(self):
        if self.turtle_head.heading() != 270:  
            self.turtle_head.setheading(90)

    def down(self):
        if self.turtle_head.heading() != 90:   
            self.turtle_head.setheading(270)

    def left(self):
        if self.turtle_head.heading() != 0:    
            self.turtle_head.setheading(180)

    def right(self):
        if self.turtle_head.heading() != 180:  
            self.turtle_head.setheading(0)

    def extend(self):
        # Get the position of the last segment
        tail = self.turtle_list[-1]
        x, y = tail.position()
        
        # Create a new segment
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x, y)

        # Add to the snake list
        self.turtle_list.append(new_segment)