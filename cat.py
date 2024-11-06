from turtle import *

def draw_cat():
    speed(8)  
    bgcolor("white")
    pensize(4)
    
    # ears
    pencolor("orange")
    penup()
    goto(-85, 240)
    begin_fill()  
    fillcolor("orange")
    pendown()
    goto(-98,310)
    goto(-20,280)
    end_fill()

    penup()
    goto(85, 240)
    begin_fill()
    fillcolor("orange")
    pendown() 
    goto(98,310)
    goto(20,280)
    end_fill()
    
    pencolor("white")
    penup()
    goto(-75, 245)
    begin_fill()  
    fillcolor("white")
    pendown()
    goto(-85,295)
    goto(-40,280)
    end_fill()

    penup()
    goto(75, 245)
    begin_fill()  
    fillcolor("white")
    pendown()
    goto(85,295)
    goto(40,280)
    end_fill()

    # face
    pencolor("orange")
    penup()
    goto(0, 100)
    pendown()
    begin_fill()
    fillcolor("orange")
    circle(100)
    end_fill()
    
    # eyes
    pencolor("yellow")
    penup()
    goto(-45, 175)
    pendown()
    begin_fill()
    fillcolor("yellow")
    circle(30)
    end_fill()
    
    penup() 
    goto(45, 175)
    pendown()
    begin_fill()
    fillcolor("yellow")
    circle(30)
    end_fill()
    
    # eyes' balls
    pencolor("black")
    penup()
    goto(-45, 185)
    pendown()
    begin_fill()
    fillcolor("black")
    circle(20)
    end_fill()
    
    penup()
    goto(45, 185) 
    pendown()
    begin_fill()
    fillcolor("black")
    circle(20)
    end_fill()
    
    # nose
    penup()
    goto(0, 145)
    pendown()  
    begin_fill()
    fillcolor("black")
    circle(13)
    end_fill()
    
    # mouth
    penup()
    goto(0, 145)
    pendown()
    right(90)
    circle(12, 180)
    
    penup()
    goto(-24, 145)
    pendown()
    right(180)
    circle(12, 180)

    # whiskers
    pencolor("white")
    pensize(2)
    penup()  
    goto(-85, 170)
    pendown()
    goto(-35, 165)
    
    penup()
    goto(-90, 160)
    pendown()  
    goto(-32, 158)
    
    penup()
    goto(-86, 150)
    pendown()  
    goto(-35, 152)
    
    penup()  
    goto(85, 170)
    pendown()
    goto(35, 165)
    
    penup()
    goto(90, 160)
    pendown()  
    goto(32, 158)
    
    penup()
    goto(86, 150)
    pendown()  
    goto(35, 152)
    

    hideturtle()
    done()

draw_cat()