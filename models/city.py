class City:
    
    def __init__(self, name, sight, country, visited = False,  id = None ):
        self.name = name
        self.sight = sight
        self.country = country
        self.visited = visited
        self.id = id
        
    def set_as_visited(self):
        self.visited = True