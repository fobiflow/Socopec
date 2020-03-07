import json
dictionary = {}

# for ()

json_object = json.dump(dictionary, indent=4)
with open("fixtures/photo.json", "w") as outfile:
    outfile.write(json_object)