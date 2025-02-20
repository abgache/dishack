import requests

u = input("Write down the webhook : ")
res = requests.delete(u)

#Is in french bcs i am french
if str(res.status_code)[0] == "2":
    print("Ressource supprimée avec succès !")
elif res.status_code == 404:
    print("Le webhook discord n'existe pas/plus, erreur 404 !")
if str(res.status_code)[0] == "5":
    print(f"Erreur avec les serveurs de discord : {res.status_code} - {res.text}")
else:
    print(f"Échec de la suppression : {res.status_code} - {res.text}")
