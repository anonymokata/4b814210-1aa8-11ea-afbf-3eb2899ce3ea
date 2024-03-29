class Inventory:
    def __init__(self):
        self._store = {}
        
    def add(self, id, price, by_weight=False):
        self._store[id] = {
            "price": price,
            "by_weight": by_weight
        }
        return None
    
    def read(self, id):
        return self._store.get(id)
        
    def delete(self, id):
        self._store.pop(id)
    
    def modify(self, id, price, by_weight=False):
        self.delete(id)
        self.add(id, price, by_weight=False)