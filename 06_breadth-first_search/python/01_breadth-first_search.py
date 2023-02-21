from collections import deque

def person_is_seller(name):
      return name[-1] == 'm'

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}

def search(name):
      search_queue = deque()
      search_queue += [name]
      # This is how you keep track of which people you've searched before.
      searched = set()
      while search_queue:
            person = search_queue.popleft()
            # Only search this person if you haven't already searched them.
            if person in searched:
                continue
            if person_is_seller(person):
                  print(f"{person} is a mango seller!")
                  return True
            search_queue += graph[person]
            # Marks this person as searched
            searched.add(person)
      return False

search("you")
