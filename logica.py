# Verifică dacă un utilizator poate adăuga taskuri

def poate_adauga_task(utilizator):
    if utilizator["activ"] == True:
        print("Acces permis — poti adauga taskuri")
    else:
        print("Acces refuzat — contul este inactiv")

utilizator = {"nume": "Darius", "activ": True}
poate_adauga_task(utilizator)