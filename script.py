meme_dict = {
    "FACTO": "Algo que es totalmente cierto o con lo que estás de acuerdo",
    "FOMO": "Miedo a perderte algo interesante o importante",
    "NPC": "Persona que actúa de forma muy automática, predecible o sin personalidad",
    "DELULU": "Persona que está siendo muy ilusa o vive en su propia fantasía",
    "FARMEAR AURA": "Hacer cosas que te hacen ver más cool, interesante o con más presencia",
    "RIZZ": "Habilidad o carisma para coquetear y conquistar a alguien"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print ("La palabra no esta en el diccionario de memes :(")