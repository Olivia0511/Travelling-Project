Project Objective
- The objective is to find the most efficient route for a politician to travel to every state capital once, starting in Iowa, and ending in Washington, DC.  

Solution Approach
1. import the math function
2. make a dictionary about every capitals' location(altitude, longitude)
3. Define the Haversine Formula and use it to calculate the distance between two points on the Earth's surface by giving their latitude and longitude.
4. Build a distance matrix: calculate the distances between each pair of state capitals and then stores them in a dictionary
5. Find the distance and find the nearest city:
   -Create a set of unvisited cities, remove the starting city
   - current city is starting city and total distance at first is 0.
Then repeating select the nearest unvisited city
   - add the distance from the last visited city to the end city
