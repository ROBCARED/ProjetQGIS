import pandas as pd

from models.infrastructures import Infra
from models.batiments import Batiment


df = pd.read_csv('bd/infrastructures_a_remplacer.csv') 

liste_batiments = []

for id_bat, group in df.groupby('id_batiment'):
    infras_du_bat = []
    for _, row in group.iterrows():
        nouvelle_infra = Infra(
            infra_id=row['id_infra'],
            length=row['longueur'],
            infra_type=row['type_infrastru'],
            etat=row['etat']
        )
        infras_du_bat.append(nouvelle_infra)
    

    nouveau_bat = Batiment(id_bat, infras_du_bat)
    liste_batiments.append(nouveau_bat)

liste_batiments.sort(reverse=True)

print("Exportation des données vers 'resultats_pour_qgis.csv'...")


donnees_export = []

for bat in liste_batiments:
    donnees_export.append({
        'id_batiment': bat.id_building,       
        'score_difficulte': bat.get_building_difficulty(),
        'nombre_infras': len(bat.list_infras)
    })


df_export = pd.DataFrame(donnees_export)


df_export.to_csv('bd/resultats_pour_qgis.csv', index=False)

print("Terminé ! Le fichier 'resultats_pour_qgis.csv' a été créé.")
