

from collections import defaultdict, deque

class Task:
    def __init__(self, id, duration):
      self.id = id
      self.duration = duration
      self.EST = 0                                 # Earliest Start Time
      self.EFT = 0                                 # Earliest Finish Time        
      self.LST = float('inf')                      # Latest Start Time
      self.LFT = float('inf')                      # Latest Finish Time
      self.depend = []                             # List of tasks that need to be completed before this task

def find_early_time(tasks):
                                                 # Topologically sort the tasks to find the linear ordering 
  in_degree = {task: 0 for task in tasks}
  for task in tasks:
    for dep in task.depend:        
      in_degree[dep] += 1

    queue = deque()
    for t in tasks:
      if in_degree[t] == 0:
        queue.append(t)

    while queue:
      current_task = queue.popleft()
      for dep in current_task.depend:
      dep.EST = max(dep.EST, current_task.EFT)
      dep.EFT = dep.EST + dep.duration
      in_degree[dep] -= 1
      if in_degree[dep] == 0:
        queue.append(dep)

def find_late_time(tasks, project_finish_time):
    for task in tasks:
      task.LFT = project_finish_time
      task.LST = project_finish_time - task.duration

    
    in_degree = {task: 0 for task in tasks}       # Topologically sort tasks in reverse order
    for task in tasks:
      for dep in task.depend:
        in_degree[task] += 1

    queue = deque()
    for t in tasks:
      if in_degree[t] == 0:
        queue.append(t)
        
    while queue:
      current_task = queue.popleft()
      for dep in current_task.depend:
        dep.LFT = min(dep.LFT, current_task.LST)
        dep.LST = dep.LFT - dep.duration
        in_degree[dep] -= 1
        if in_degree[dep] == 0:
          queue.append(dep)

def find_project_times(tasks):
  find_early_time(tasks)                                  # Calculate earliest time              
  project_finish_time = max(task.EFT for task in tasks)

  find_late_time(tasks, project_finish_time)              # Calculate latest times
  return project_finish_time, max(task.LFT for task in tasks)

