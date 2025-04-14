from queue import Queue

q = Queue()
q.put("Data structure")
q.put("Database")
q.put("Javascript")
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())