import datetime
import json


dictionary = []

vehicules = [
    {
        "pk": 1,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 1,
            "immatriculation": "AA-111-DH",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.76,
            "largeur": 1.96,
            "poids": 2.27,
            "puissance": 89,
            "id_agence": 10
        }
    },
    {
        "pk": 2,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 2,
            "immatriculation": "AB-222-DG",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.41,
            "largeur": 2.21,
            "poids": 3.21,
            "puissance": 81,
            "id_agence": 8
        }
    },
    {
        "pk": 3,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 3,
            "immatriculation": "AC-333-DF",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.82,
            "largeur": 2.12,
            "poids": 3.43,
            "puissance": 114,
            "id_agence": 3
        }
    },
    {
        "pk": 4,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 4,
            "immatriculation": "AD-444-DE",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.22,
            "largeur": 1.52,
            "poids": 3.4,
            "puissance": 114,
            "id_agence": 13
        }
    },
    {
        "pk": 5,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 5,
            "immatriculation": "AE-555-DC",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.78,
            "largeur": 2.25,
            "poids": 3.14,
            "puissance": 82,
            "id_agence": 7
        }
    },
    {
        "pk": 6,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 6,
            "immatriculation": "AF-666-DB",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.05,
            "largeur": 2.22,
            "poids": 3.44,
            "puissance": 97,
            "id_agence": 1
        }
    },
    {
        "pk": 7,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 7,
            "immatriculation": "AG-777-DA",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.03,
            "largeur": 1.69,
            "poids": 2.6,
            "puissance": 95,
            "id_agence": 14
        }
    },
    {
        "pk": 8,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 8,
            "immatriculation": "AH-888-DD",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.74,
            "largeur": 1.5,
            "poids": 3.06,
            "puissance": 85,
            "id_agence": 10
        }
    },
    {
        "pk": 9,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 9,
            "immatriculation": "AJ-999-CZ",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.36,
            "largeur": 2.39,
            "poids": 2.39,
            "puissance": 98,
            "id_agence": 4
        }
    },
    {
        "pk": 10,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 10,
            "immatriculation": "AK-123-CY",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.07,
            "largeur": 2.16,
            "poids": 3.18,
            "puissance": 89,
            "id_agence": 6
        }
    },
    {
        "pk": 11,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 11,
            "immatriculation": "AL-456-CX",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.46,
            "largeur": 1.96,
            "poids": 2.93,
            "puissance": 99,
            "id_agence": 12
        }
    },
    {
        "pk": 12,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 12,
            "immatriculation": "AM-789-CW",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.4,
            "largeur": 1.69,
            "poids": 3.31,
            "puissance": 85,
            "id_agence": 10
        }
    },
    {
        "pk": 13,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 13,
            "immatriculation": "AN-987-CV",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.16,
            "largeur": 1.67,
            "poids": 2.06,
            "puissance": 109,
            "id_agence": 5
        }
    },
    {
        "pk": 14,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 14,
            "immatriculation": "AP-654-CU",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.92,
            "largeur": 2.14,
            "poids": 3.17,
            "puissance": 113,
            "id_agence": 2
        }
    },
    {
        "pk": 15,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 15,
            "immatriculation": "AQ-321-CT",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.95,
            "largeur": 2.49,
            "poids": 2.59,
            "puissance": 106,
            "id_agence": 9
        }
    },
    {
        "pk": 16,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 16,
            "immatriculation": "AR-147-CS",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.75,
            "largeur": 2.3,
            "poids": 2.0,
            "puissance": 90,
            "id_agence": 14
        }
    },
    {
        "pk": 17,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 17,
            "immatriculation": "AS-258-CR",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.59,
            "largeur": 2.27,
            "poids": 3.38,
            "puissance": 108,
            "id_agence": 4
        }
    },
    {
        "pk": 18,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 18,
            "immatriculation": "AT-369-CQ",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.59,
            "largeur": 2.07,
            "poids": 3.44,
            "puissance": 107,
            "id_agence": 14
        }
    },
    {
        "pk": 19,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 19,
            "immatriculation": "AU-963-CP",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.97,
            "largeur": 2.2,
            "poids": 2.73,
            "puissance": 101,
            "id_agence": 11
        }
    },
    {
        "pk": 20,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 20,
            "immatriculation": "AV-852-CN",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.7,
            "largeur": 2.03,
            "poids": 2.68,
            "puissance": 99,
            "id_agence": 12
        }
    },
    {
        "pk": 21,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 21,
            "immatriculation": "AW-741-CM",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.51,
            "largeur": 1.74,
            "poids": 2.52,
            "puissance": 87,
            "id_agence": 2
        }
    },
    {
        "pk": 22,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 22,
            "immatriculation": "AX-999-CL",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.17,
            "largeur": 1.74,
            "poids": 2.93,
            "puissance": 91,
            "id_agence": 12
        }
    },
    {
        "pk": 23,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 23,
            "immatriculation": "AY-888-CK",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.8,
            "largeur": 2.46,
            "poids": 3.46,
            "puissance": 100,
            "id_agence": 14
        }
    },
    {
        "pk": 24,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 24,
            "immatriculation": "AZ-777-CJ",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.94,
            "largeur": 2.36,
            "poids": 2.05,
            "puissance": 100,
            "id_agence": 9
        }
    },
    {
        "pk": 25,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 25,
            "immatriculation": "BB-666-CH",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.73,
            "largeur": 2.38,
            "poids": 3.35,
            "puissance": 90,
            "id_agence": 9
        }
    },
    {
        "pk": 26,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 26,
            "immatriculation": "BA-555-CG",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.35,
            "largeur": 2.06,
            "poids": 3.1,
            "puissance": 101,
            "id_agence": 13
        }
    },
    {
        "pk": 27,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 27,
            "immatriculation": "BC-444-CF",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.09,
            "largeur": 2.43,
            "poids": 2.02,
            "puissance": 104,
            "id_agence": 5
        }
    },
    {
        "pk": 28,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 28,
            "immatriculation": "BD-333-CE",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.15,
            "largeur": 1.83,
            "poids": 2.15,
            "puissance": 104,
            "id_agence": 5
        }
    },
    {
        "pk": 29,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 29,
            "immatriculation": "BE-222-CD",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.53,
            "largeur": 2.16,
            "poids": 2.35,
            "puissance": 106,
            "id_agence": 1
        }
    },
    {
        "pk": 30,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 30,
            "immatriculation": "BF-111-CB",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.91,
            "largeur": 2.02,
            "poids": 3.42,
            "puissance": 94,
            "id_agence": 3
        }
    },
    {
        "pk": 31,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 31,
            "immatriculation": "BG-951-BS",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.46,
            "largeur": 2.01,
            "poids": 2.61,
            "puissance": 103,
            "id_agence": 13
        }
    },
    {
        "pk": 32,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 32,
            "immatriculation": "BH-753-BT",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.18,
            "largeur": 2.49,
            "poids": 2.75,
            "puissance": 83,
            "id_agence": 9
        }
    },
    {
        "pk": 33,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 33,
            "immatriculation": "BJ-946-BU",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.28,
            "largeur": 1.58,
            "poids": 2.69,
            "puissance": 97,
            "id_agence": 11
        }
    },
    {
        "pk": 34,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 34,
            "immatriculation": "BK-743-BV",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.09,
            "largeur": 1.72,
            "poids": 3.12,
            "puissance": 94,
            "id_agence": 5
        }
    },
    {
        "pk": 35,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 35,
            "immatriculation": "BL-186-BW",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.41,
            "largeur": 1.71,
            "poids": 2.16,
            "puissance": 87,
            "id_agence": 13
        }
    },
    {
        "pk": 36,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 36,
            "immatriculation": "BM-349-BX",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.73,
            "largeur": 2.49,
            "poids": 2.1,
            "puissance": 90,
            "id_agence": 11
        }
    },
    {
        "pk": 37,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 37,
            "immatriculation": "BN-267-BY",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.21,
            "largeur": 1.73,
            "poids": 2.82,
            "puissance": 112,
            "id_agence": 5
        }
    },
    {
        "pk": 38,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 38,
            "immatriculation": "BP-486-BZ",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.91,
            "largeur": 1.51,
            "poids": 2.35,
            "puissance": 107,
            "id_agence": 13
        }
    },
    {
        "pk": 39,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 39,
            "immatriculation": "BQ-348-CC",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.96,
            "largeur": 2.49,
            "poids": 2.61,
            "puissance": 92,
            "id_agence": 11
        }
    },
    {
        "pk": 40,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 40,
            "immatriculation": "BR-168-CA",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.24,
            "largeur": 2.39,
            "poids": 3.14,
            "puissance": 115,
            "id_agence": 10
        }
    },
    {
        "pk": 41,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 41,
            "immatriculation": "BS-123-BR",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.67,
            "largeur": 2.32,
            "poids": 2.01,
            "puissance": 99,
            "id_agence": 9
        }
    },
    {
        "pk": 42,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 42,
            "immatriculation": "BT-456-BQ",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.48,
            "largeur": 1.65,
            "poids": 3.04,
            "puissance": 90,
            "id_agence": 5
        }
    },
    {
        "pk": 43,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 43,
            "immatriculation": "BU-789-BP",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.52,
            "largeur": 2.42,
            "poids": 3.2,
            "puissance": 103,
            "id_agence": 3
        }
    },
    {
        "pk": 44,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 44,
            "immatriculation": "BV-987-BN",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.87,
            "largeur": 2.27,
            "poids": 2.62,
            "puissance": 106,
            "id_agence": 6
        }
    },
    {
        "pk": 45,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 45,
            "immatriculation": "BW-654-BM",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.82,
            "largeur": 2.13,
            "poids": 2.05,
            "puissance": 94,
            "id_agence": 13
        }
    },
    {
        "pk": 46,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 46,
            "immatriculation": "BX-321-BL",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.01,
            "largeur": 1.76,
            "poids": 3.02,
            "puissance": 107,
            "id_agence": 1
        }
    },
    {
        "pk": 47,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 47,
            "immatriculation": "BY-112-BK",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.67,
            "largeur": 2.05,
            "poids": 3.1,
            "puissance": 85,
            "id_agence": 3
        }
    },
    {
        "pk": 48,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 48,
            "immatriculation": "BZ-113-BJ",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.9,
            "largeur": 2.21,
            "poids": 3.27,
            "puissance": 91,
            "id_agence": 6
        }
    },
    {
        "pk": 49,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 49,
            "immatriculation": "CC-114-BH",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.55,
            "largeur": 1.96,
            "poids": 2.88,
            "puissance": 87,
            "id_agence": 2
        }
    },
    {
        "pk": 50,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 50,
            "immatriculation": "CA-115-BG",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.64,
            "largeur": 2.41,
            "poids": 2.95,
            "puissance": 102,
            "id_agence": 7
        }
    },
    {
        "pk": 51,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 51,
            "immatriculation": "CB-116-BF",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.09,
            "largeur": 2.42,
            "poids": 3.39,
            "puissance": 115,
            "id_agence": 2
        }
    },
    {
        "pk": 52,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 52,
            "immatriculation": "CD-117-BE",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.57,
            "largeur": 1.58,
            "poids": 2.9,
            "puissance": 96,
            "id_agence": 14
        }
    },
    {
        "pk": 53,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 53,
            "immatriculation": "CE-118-BD",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.46,
            "largeur": 2.2,
            "poids": 2.88,
            "puissance": 108,
            "id_agence": 14
        }
    },
    {
        "pk": 54,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 54,
            "immatriculation": "CF-119-BC",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.58,
            "largeur": 2.0,
            "poids": 2.78,
            "puissance": 106,
            "id_agence": 8
        }
    },
    {
        "pk": 55,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 55,
            "immatriculation": "CG-221-BA",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.73,
            "largeur": 2.36,
            "poids": 3.39,
            "puissance": 103,
            "id_agence": 1
        }
    },
    {
        "pk": 56,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 56,
            "immatriculation": "CH-223-BB",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.13,
            "largeur": 2.11,
            "poids": 2.77,
            "puissance": 110,
            "id_agence": 7
        }
    },
    {
        "pk": 57,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 57,
            "immatriculation": "CJ-224-AZ",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.65,
            "largeur": 2.26,
            "poids": 3.45,
            "puissance": 111,
            "id_agence": 4
        }
    },
    {
        "pk": 58,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 58,
            "immatriculation": "CK-225-AY",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.83,
            "largeur": 2.09,
            "poids": 2.63,
            "puissance": 98,
            "id_agence": 9
        }
    },
    {
        "pk": 59,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 59,
            "immatriculation": "CL-226-AX",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.88,
            "largeur": 2.38,
            "poids": 2.15,
            "puissance": 88,
            "id_agence": 1
        }
    },
    {
        "pk": 60,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 60,
            "immatriculation": "CM-227-AW",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.43,
            "largeur": 2.11,
            "poids": 3.38,
            "puissance": 99,
            "id_agence": 14
        }
    },
    {
        "pk": 61,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 61,
            "immatriculation": "CN-228-AV",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.63,
            "largeur": 1.74,
            "poids": 3.25,
            "puissance": 105,
            "id_agence": 8
        }
    },
    {
        "pk": 62,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 62,
            "immatriculation": "CP-229-AU",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.79,
            "largeur": 2.32,
            "poids": 2.52,
            "puissance": 87,
            "id_agence": 13
        }
    },
    {
        "pk": 63,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 63,
            "immatriculation": "CQ-331-AT",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.96,
            "largeur": 2.46,
            "poids": 2.9,
            "puissance": 95,
            "id_agence": 12
        }
    },
    {
        "pk": 64,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 64,
            "immatriculation": "CR-332-AS",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.74,
            "largeur": 1.8,
            "poids": 3.44,
            "puissance": 110,
            "id_agence": 13
        }
    },
    {
        "pk": 65,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 65,
            "immatriculation": "CS-334-AR",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.47,
            "largeur": 2.38,
            "poids": 3.43,
            "puissance": 107,
            "id_agence": 14
        }
    },
    {
        "pk": 66,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 66,
            "immatriculation": "CT-335-AQ",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.74,
            "largeur": 1.79,
            "poids": 3.22,
            "puissance": 103,
            "id_agence": 1
        }
    },
    {
        "pk": 67,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 67,
            "immatriculation": "CU-336-AP",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.91,
            "largeur": 1.74,
            "poids": 2.33,
            "puissance": 88,
            "id_agence": 4
        }
    },
    {
        "pk": 68,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 68,
            "immatriculation": "CV-337-AN",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.7,
            "largeur": 2.23,
            "poids": 2.55,
            "puissance": 118,
            "id_agence": 13
        }
    },
    {
        "pk": 69,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 69,
            "immatriculation": "CW-338-AM",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.48,
            "largeur": 2.16,
            "poids": 2.94,
            "puissance": 105,
            "id_agence": 14
        }
    },
    {
        "pk": 70,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 70,
            "immatriculation": "CX-339-AL",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.41,
            "largeur": 1.86,
            "poids": 2.56,
            "puissance": 100,
            "id_agence": 4
        }
    },
    {
        "pk": 71,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 71,
            "immatriculation": "CY-998-AK",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.43,
            "largeur": 1.72,
            "poids": 2.21,
            "puissance": 117,
            "id_agence": 11
        }
    },
    {
        "pk": 72,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 72,
            "immatriculation": "CZ-997-AJ",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.32,
            "largeur": 1.7,
            "poids": 2.09,
            "puissance": 81,
            "id_agence": 3
        }
    },
    {
        "pk": 73,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 73,
            "immatriculation": "DD-996-AH",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.22,
            "largeur": 2.16,
            "poids": 2.95,
            "puissance": 87,
            "id_agence": 14
        }
    },
    {
        "pk": 74,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 74,
            "immatriculation": "DA-995-AG",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.71,
            "largeur": 1.52,
            "poids": 2.66,
            "puissance": 93,
            "id_agence": 7
        }
    },
    {
        "pk": 75,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 75,
            "immatriculation": "DB-994-AF",
            "modele": "Ford",
            "date_fabrication": "2019-03-08",
            "hauteur": 2.07,
            "largeur": 1.67,
            "poids": 2.89,
            "puissance": 106,
            "id_agence": 11
        }
    },
    {
        "pk": 76,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 76,
            "immatriculation": "DC-993-AE",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.95,
            "largeur": 1.86,
            "poids": 3.1,
            "puissance": 104,
            "id_agence": 14
        }
    },
    {
        "pk": 77,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 77,
            "immatriculation": "DE-992-AD",
            "modele": "Renault",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.66,
            "largeur": 1.94,
            "poids": 3.11,
            "puissance": 106,
            "id_agence": 7
        }
    },
    {
        "pk": 78,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 78,
            "immatriculation": "DF-991-AC",
            "modele": "Citroen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.79,
            "largeur": 1.96,
            "poids": 2.53,
            "puissance": 89,
            "id_agence": 12
        }
    },
    {
        "pk": 79,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 79,
            "immatriculation": "DG-882-AB",
            "modele": "Volkswagen",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.89,
            "largeur": 1.91,
            "poids": 2.16,
            "puissance": 113,
            "id_agence": 10
        }
    },
    {
        "pk": 80,
        "model": "vehicule.vehicule",
        "fields": {
            "id": 80,
            "immatriculation": "DH-881-AA",
            "modele": "Peugeot",
            "date_fabrication": "2019-03-08",
            "hauteur": 1.78,
            "largeur": 2.43,
            "poids": 2.97,
            "puissance": 86,
            "id_agence": 13
        }
    }
]

i = 0
for x in range(80):
    dt = datetime.date.today()
    date = dt.strftime("%Y-%m-%d")
    new_histo = {
        "pk": x + 1,
        "model": "historique.historique",
        "fields": {
            "id": x + 1,
            "id_agence": vehicules[x]["fields"]["id_agence"],
            "id_vehicule": x + 1,
            "id_statut": 5,
            "id_agent": 1,
            "date_debut": date,
            "statut": "en cours",
            "localisation": "null"
        }
    }
    dictionary.append(new_histo)

json_object = json.dumps(dictionary, indent=4)
with open("fixtures/historique.json", "w") as outfile:
    outfile.write(json_object)
