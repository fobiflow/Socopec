import json


dictionary = []
i = 0
for x in range(80):
    for y in range(4):
        i += 1
        new_photo = {
           "pk": i,
           "model": "vehicule.photo",
           "fields": {
               "id": i,
               "url": "https://picsum.photos/160/160.jpg",
               "id_vehicule": x + 1
           }
        }
        dictionary.append(new_photo)

json_object = json.dumps(dictionary, indent=4)
with open("fixtures/photo.json", "w") as outfile:
    outfile.write(json_object)
