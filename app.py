import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
# print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on typ

# challenge 1:
# for id, data  in enumerate(data):
#      print (id, ":", data["name"])
# challenge 2:
# lang = input("Select language: english, japanese, chinese, or french")
# for bla in data:
#     print (bla["name"][lang])
# challenge 3:
# lang = input("Select language: english, japanese, chinese, or french")
# type = input("Select pokemon type")
# print(type, "types:")
# for poke in data:
#     if type in poke["type"]:
#         print (poke["name"][lang])
#     else:
#         print("No Pokemon of that type found or invalid imput")
#         break
# challenge 4
usin = input("Type pokemon keyword here.. (Ex: Cosm for Cosmog, Cosmoem )")
lang = ["english"]
pokelist = []
for poke in data:
    if usin  in (poke["name"][lang]):
        list.insert(poke)

print(pokelist)




