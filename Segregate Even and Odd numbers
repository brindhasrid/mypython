class Solution:

	def segregateEvenOdd(self,arr):
		
       evens = sorted([num for num in arr if num % 2 == 0])  # Collect even numbers and sort
       odds = sorted([num for num in arr if num % 2 != 0])   # Collect odd numbers and sort
    
       arr[:len(evens)] = evens  # Place sorted evens in original array
       arr[len(evens):] = odds   # Place sorted odds in original array

