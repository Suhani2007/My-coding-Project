import turtle
import cv2
import numpy as np
import os

# 1. Image path check kara
image_path = "maharaj.jpg" 

if not os.path.exists(image_path):
    print("Error: 'maharaj.jpg' sapdali nahi!")
else:
    # 2. Image Processing
    img = cv2.imread(image_path, 0)
    img = cv2.resize(img, (500, 500))
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 3. Turtle Setup
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("#FF4500") # Bhagva Background
    s.setup(width=750, height=800)
    s.tracer(100)
    
    t.speed(0)
    t.hideturtle()
    t.penup()

    # 4. Silhouette Drawing
    print("Maharajanchi drawing suru hot ahe...")
    for cnt in contours:
        if cv2.contourArea(cnt) > 100:
            t.goto(cnt[0][0][0] - 250, 250 - cnt[0][0][1])
            t.begin_fill()
            t.fillcolor("black")
            t.pencolor("black")
            for point in cnt:
                x, y = point[0]
                t.goto(x - 250, 250 - y)
                t.pendown()
            t.end_fill()
            t.penup()

    # 5. Adding "JAI SHIVRAY" Text
    t.goto(0, -320) # Screen chya khali
    t.pencolor("black")
    # 'Arial' chya jagi tumhala 'Times New Roman' kiva 'Verdana' vaparta yeil
    t.write("JAI SHIVRAY", align="center", font=("Arial", 40, "bold italic"))

    s.update()
    print("Jai Jijau, Jai Shivray!")
    turtle.done()