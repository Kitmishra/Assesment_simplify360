
"""Both Alice & Bob have friends. Create a Java/Python/JS/Typescript console application to find all the friends of Alice and all the friends of Bob & common friends of Alice and Bob.
Your algorithm should be able to do the following:
Take any 2 friends and find the common friends between the 2 friends
Take any 2 friends find the nth connection - for example: connection(Alice, Janice) => 2
Alice has friend Bob and Bob has friend Janice, if the input given is Alice and Janice the output should be 2, meaning 2nd connection, that means Janice is the second connection of Alice and Bob being the 1st connection of Alice.
Likewise if input given is Alice and Bob, the output should be 1, for 1st connection
If there is no connection at all, it should return -1
Add the console applications(programs) to your Github account and share the Github links for evaluation. Make sure your code is executable and free of syntax errors. Also please explain the Time and Space complexity of your respective programs as code comments
"""

from collections import defaultdict
from collections import deque 

class friendship:
  def __init__(self):
    self.friends = defaultdict(set)    # creating graph named friends, person name as dictionary key and their as values in terms of set.

  def add_friend(self, name1, name2):
    self.friends[name1].add(name2)       # connecting friends in the friend list.
    self.friends[name2].add(name1)

  def find_friend(self, person):         # This function will return all the friends of person, it can be either bob, alice or anyone else.
    return self.friends[person]          TIME AND SPACE -> O (1)
    
  def find_common_friends(self, person1, person2):           #TIME AND SPACE -> O(MIN(LEN(person1_friends, person2_friends))
    person1_friends = self.friends[person1]                # find friend of person1.
    person2_friends = self.friends[person2]                # find friend of person2.
    return person1_friends.intersection(person2_friends)   # finding the common friends of person1 and person2.

  def nth_connection(self, person1, person2):   # This will return the nth connection distance of person2 from person1. 
    visited = set()
    queue = deque()                             # double ended queue so that insertion and deletion can be performed in constant time.
    queue.append((person1, 0))  

    while queue:                                          # BFS traversal in graph until we find the person2 or queue is empty. 
      current_person, distance = queue.popleft()
      if current_person in visited:                        #TIME  -> O(V + E)  AND SPACE ->  O(E)
        continue
      if current_person == person2:
        return distance
      visited.add(current_person)
      
      for neighbor in self.friends[current_person]:
        if neighbor not in visited:
          queue.append((neighbor, distance+1))

    return -1         # returning -1 in case if person1 and person2 are not friends.
  


