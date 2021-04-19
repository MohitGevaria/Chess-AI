import copy 
class something:
    def __init__(self):
        self.kirtan = "Nice"

d= [1,2,3,4,5,6,7]
e=copy.deepcopy(d)
print(d)
d.pop(1)
print(d)