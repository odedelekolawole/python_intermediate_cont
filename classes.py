# class Planet:

#     shape = "round"

#     def __init__(self, name, radius, gravity, system):
#         self.name = name
#         self.radius = radius
#         self.gravity = gravity
#         self.system = system

#     def orbit(self):
#         return f"{self.name} is orbiting in the {self.system}"
    
#     @classmethod
#     def commons(cls):
#         return f"All planet are {cls.shape} because of gravity"
    
#     @staticmethod
#     def spin(speed = "2000 miles per hour"):
#         return f"The planet spins and spins at {speed}"


# hoth = Planet("Hoth", 200000, 5.5, "Hoth System")

# print(f"Name is: {hoth.name}")
# print(f"Radius is: {hoth.radius}")
# print(f"This gravity is: {hoth.gravity}")
# print(hoth.orbit())

# naboo = Planet("Naboo", 300000, 8, "Naboo System")

# print(f"Name is: {naboo.name}")
# print(f"Radius is: {naboo.radius}")
# print(f"Gravity is: {naboo.gravity}")
# print(naboo.orbit())
# print(Planet.shape)
# print(hoth.shape)
# print(naboo.shape)
# print(Planet.commons())
# print(naboo.commons())
# print(Planet.spin("a very high speed"))
# print(naboo.spin("a very high speed"))