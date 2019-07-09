###Amortized time###<br>

example: dynamic resizing array/ ArrayList<br>
double the capacity when the size of the array is power of 2: create a new array of size 2*2^n 
and then copy the 2^n elements to the new array, the majority of the insertion will be O(1)
for X insertions, the runtime is<br> 
          '''sum(X + X/2 + X/4 + ... + 1) which is roughly O(2X)'''
then the amortized tiem of each insertion is O(1)



