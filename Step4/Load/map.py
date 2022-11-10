class Map():
    def __init__(self):
        self.location_map = {}
        
    def add_entity(self, id, entity):
        self.location_map[id] = entity
    
    def __str__(self):
        s = ''
        for key in self.location_map:
            entity = self.location_map[key]
            s=s + entity.__str__() + '\n'
            s=s + f"----west neighbour: {entity.west}\n"
            s=s + f"----east neighbour: {entity.east}\n"
            s=s + f"----north neighbour:{entity.north}\n"
            s=s + f"----south neighbour:{entity.south}\n"
        return s