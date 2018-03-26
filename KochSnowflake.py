#Author: Mortyyy

from turtle import *

#Draws one side of a Koch snowflake.
def snowflake(lengthSide, m):
    if m == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, m-1)
    left(60)
    snowflake(lengthSide, m-1)
    right(120)
    snowflake(lengthSide, m-1)
    left(60)
    snowflake(lengthSide, m-1)

#Draws the full snowflace.
def fullSnowflake(lengthside, m):
    for i in range(3):
        snowflake(lengthside, m)
        right(120)
        
if __name__ == "__main__":      # Only runs if this is the main module;
    speed(0)                                # the program is not imported.
    length = 300.0
    penup()
    backward(length/2.0)
    pendown()
    fullSnowflake(length, 4)
