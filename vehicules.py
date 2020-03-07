import datetime
import decimal
import json
import random

dictionary = []
modeles = ["Renault", "Peugeot", "Citroen", "Volkswagen", "Ford"]
immatriculations = [
    "AA-111-DH", "AB-222-DG", "AC-333-DF", "AD-444-DE", "AE-555-DC", "AF-666-DB", "AG-777-DA", "AH-888-DD", "AJ-999-CZ", "AK-123-CY",
    "AL-456-CX", "AM-789-CW", "AN-987-CV", "AP-654-CU", "AQ-321-CT", "AR-147-CS", "AS-258-CR", "AT-369-CQ", "AU-963-CP", "AV-852-CN",
    "AW-741-CM", "AX-999-CL", "AY-888-CK", "AZ-777-CJ", "BB-666-CH", "BA-555-CG", "BC-444-CF", "BD-333-CE", "BE-222-CD", "BF-111-CB",
    "BG-951-BS", "BH-753-BT", "BJ-946-BU", "BK-743-BV", "BL-186-BW", "BM-349-BX", "BN-267-BY", "BP-486-BZ", "BQ-348-CC", "BR-168-CA",
    "BS-123-BR", "BT-456-BQ", "BU-789-BP", "BV-987-BN", "BW-654-BM", "BX-321-BL", "BY-112-BK", "BZ-113-BJ", "CC-114-BH", "CA-115-BG",
    "CB-116-BF", "CD-117-BE", "CE-118-BD", "CF-119-BC", "CG-221-BA", "CH-223-BB", "CJ-224-AZ", "CK-225-AY", "CL-226-AX", "CM-227-AW",
    "CN-228-AV", "CP-229-AU", "CQ-331-AT", "CR-332-AS", "CS-334-AR", "CT-335-AQ", "CU-336-AP", "CV-337-AN", "CW-338-AM", "CX-339-AL",
    "CY-998-AK", "CZ-997-AJ", "DD-996-AH", "DA-995-AG", "DB-994-AF", "DC-993-AE", "DE-992-AD", "DF-991-AC", "DG-882-AB", "DH-881-AA",
]
i = 0

for x in range(80):
    modele = random.randrange(0, len(modeles))
    dt = datetime.datetime.now() - datetime.timedelta(365)
    date = dt.strftime("%Y-%m-%d")
    ht = random.randrange(150, 250)
    hauteur = ht/100
    lg = random.randrange(150, 250)
    largeur = lg/100
    pds = random.randrange(200, 350)
    poids = pds/100
    puissance = random.randrange(80, 120)
    agence_id = random.randrange(1, 15)
    new_vehicule = {
        "pk": x + 1,
        "model": "vehicule.vehicule",
        "fields": {
            "id": x + 1,
            "immatriculation": immatriculations[i],
            "modele": modeles[modele],
            "date_fabrication": date,
            "hauteur": hauteur,
            "largeur": largeur,
            "poids": poids,
            "puissance": puissance,
            "id_agence": agence_id
        }
    }
    dictionary.append(new_vehicule)
    i += 1

json_object = json.dumps(dictionary, indent=4)
with open("fixtures/vehicule.json", "w") as outfile:
    outfile.write(json_object)
