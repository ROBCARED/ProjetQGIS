import pandas as pd
import openpyxl 
import os 


"""
df = pd.read_excel('reseau_en_arbre.xlsx')


df_batiment = df[['id_batiment', 'nb_maisons']].drop_duplicates()

df_infrastructure = df[['id_batiment', 'infra_id', 'infra_type', 'longueur']]


df_batiment.to_csv('batiments2.csv', index=False)
df_infrastructure.to_csv('infrastructures2.csv', index=False)



if os.path.exists('batiments2.csv'):
    df_ancien = pd.read_csv('batiments2.csv')
else:
    df_ancien = pd.DataFrame(columns=['id_batiment', 'type_batiment', 'nb_maisons'])

df_nouveau = pd.read_csv('batiments.csv') 

print(f"Lignes avant : {len(df_ancien)}")
print(f"Lignes à traiter (Ajouts/Modifs) : {len(df_nouveau)}")


df_total = pd.concat([df_ancien, df_nouveau])


df_final = df_total.drop_duplicates(subset=['id_batiment'], keep='last')


df_final.to_csv('batiments2.csv', index=False)

print(f"Terminé ! Lignes totales après opération : {len(df_final)}")






fichier_cible = 'infrastructures2.csv'
fichier_source = 'infra.csv'


if os.path.exists(fichier_cible) and os.path.exists(fichier_source):
    

    df_cible = pd.read_csv(fichier_cible)
    df_source = pd.read_csv(fichier_source)

    
    df_cible.columns = df_cible.columns.str.strip()
    df_source.columns = df_source.columns.str.strip()

    colonne_id = 'id_infra' 
    colonne_a_ajouter = 'type_infrastru'

    if colonne_id in df_cible.columns and colonne_id in df_source.columns:
        
        df_source_clean = df_source[[colonne_id, colonne_a_ajouter]].drop_duplicates(subset=colonne_id)


        df_merged = pd.merge(df_cible, df_source_clean, on=colonne_id, how='left')

        df_merged.to_csv(fichier_cible, index=False)
        print(f" Colonne '{colonne_a_ajouter}' importée avec succès dans {fichier_cible} !")
        

        lignes_totales = len(df_merged)
        lignes_remplies = df_merged[colonne_a_ajouter].notna().sum()
        print(f" Info : {lignes_remplies}/{lignes_totales} lignes ont trouvé une correspondance.")

    else:
        print(f" Erreur : La colonne ID nommée '{colonne_id}' n'a pas été trouvée dans l'un des fichiers.")
else:
    print(" Un des fichiers n'existe pas.")


fichier = 'infrastructures2.csv'

if os.path.exists(fichier):
    df = pd.read_csv(fichier)
    

    df['etat'] = df['etat'].astype(str).str.strip()


    df_filtre = df[df['etat'] == 'a_remplacer']


    print(f"Lignes avant : {len(df)} -> Lignes après : {len(df_filtre)}")


    fichier_sortie = 'infrastructures_a_remplacer.csv'
    df_filtre.to_csv(fichier_sortie, index=False)
    print(f"Fichier créé : {fichier_sortie}")


    
else:
    print(f"Le fichier {fichier} n'existe pas.")
"""
    

dossier_data = r"C:\Users\HP\OneDrive\Documents\Work_project\ProjetQGIS\bd"

fichier_cible = os.path.join(dossier_data, 'infrastructures_a_remplacer.csv')
fichier_source = os.path.join(dossier_data, 'batiments2.csv')              

if os.path.exists(fichier_cible) and os.path.exists(fichier_source):
    

    df_infra = pd.read_csv(fichier_cible) 
    df_bat = pd.read_csv(fichier_source)


    df_infra.columns = df_infra.columns.str.strip()
    df_bat.columns = df_bat.columns.str.strip()


    colonne_id = 'id_batiment'  
    

    colonnes_a_importer = [colonne_id, 'nb_maisons', 'type_batiment'] 


    cols_valides = [colonnes for colonnes in colonnes_a_importer if colonnes in df_bat.columns]

    if len(cols_valides) > 1: 
        

        df_bat_clean = df_bat[cols_valides]
        
    
        df_bat_clean = df_bat_clean.drop_duplicates(subset=colonne_id)

    
        df_final = pd.merge(df_infra, df_bat_clean, on=colonne_id, how='left')


        df_final.to_csv(fichier_cible, index=False)
        
        print(f"Succès ! Les colonnes {cols_valides[1:]} ont été ajoutées.")
        print(f"Fichier mis à jour : {fichier_cible}")
        
    else:
        print("Attention : Aucune des colonnes demandées n'a été trouvée dans batiments2.csv (à part l'ID).")
        print(f"Colonnes disponibles dans batiments2 : {list(df_bat.columns)}")

else:
    print("Un des fichiers est introuvable.")