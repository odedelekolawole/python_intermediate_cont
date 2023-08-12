from space.planet import Planet
from space.calc import planet_mass, planet_volume


naboo = Planet("Naboo", 300000, 8, "Naboo System")

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_volume = planet_volume(naboo.radius)

print(f"{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_volume}")