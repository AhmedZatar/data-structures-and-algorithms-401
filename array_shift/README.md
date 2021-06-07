# Reverse an Array

Write a function called insertShiftArray which takes in an array and a value to be added.  return an array with the new value added at the middle index.


## Whiteboard Process

![0](./array-shift.png)

## Approach & Efficiency

Create function call insertShiftArray take an array(arr) and a value(a) as input, at first the function the array is an array, declare new empty array, check if the array length is odd or even and declare new varible(t) equal the half of the array lengeth and add to it 1 if the lengeth of array is odd, loop in range (0,t) and while looping append to the new array arr[i], append to the new array a, another loop in range (t,len(arr)) and while looping append to the new array arr[i], at the end return the newarray


Big O Time--> O(n)

Big O space--> O(n)


