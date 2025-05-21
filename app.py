import streamlit as st
import pandas as pd

# Import et lecture du fichier .csv 'taxis'
link = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(link)

# Sélection des différents quartiers sous forme de liste
borough_list = df['pickup_borough'].unique()

# Duplication d'une image de taxi volant en 2
### Créer 2 colonnes côte à côte
col1, col2 = st.columns(2)

### Afficher l'image dans chaque colonne
with col1:
    st.image("https://png.pngtree.com/png-clipart/20240115/original/pngtree-flying-taxi-png-image_14120966.png", width=210)

with col2:
    st.image("https://png.pngtree.com/png-clipart/20240115/original/pngtree-flying-taxi-png-image_14120966.png", width=210)

# Afficher l'image New-York skyview
st.image("https://purepng.com/public/uploads/large/purepng.com-new-york-city-skylinecitycitiesskylineskyscrapers-251520164674syfxp.png")


# Titre principal de l'application (affiché en haut de la page)
st.title("Bienvenue sur le site web de Jordan")

# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
# 'choix' -> stocke la sélection de l'utilisateur
choix = st.selectbox("Indiquez votre région de récupération", borough_list)
st.write('___')

# Affiche une ligne de texte simple (sans mise en forme particulière)
st.text("Tu as choisi : " + str(choix))

# Création d'une condition générant le texte et l'image associés au choix de l'user
if choix == 'Manhattan':
    st.image('https://cdn.pixabay.com/photo/2014/11/21/17/23/new-york-540807_1280.jpg')
elif choix == 'Queens':
    st.image('https://media.istockphoto.com/id/974704892/fr/photo/m%C3%A9tro-approche-de-la-station-de-m%C3%A9tro-sur%C3%A9lev%C3%A9e-dans-le-queens-%C3%A0-new-york.jpg?s=1024x1024&w=is&k=20&c=KBSP-t1MvXZL6LCy0tgU6a2WdBojL1i8B1doQBiFirM=')
elif choix == 'Brooklyn':
    st.image('https://cdn.pixabay.com/photo/2020/04/04/20/43/new-york-5003804_1280.jpg')
elif choix == 'Bronx':
    st.image('https://www.nyctourism.com/_next/image/?url=https%3A%2F%2Fimages.ctfassets.net%2F1aemqu6a6t65%2FY88wCNNmL1eWKwvM05DWN%2Ff4548b97b9365d2cfa549fcc82ac46ad%2FFordham-Bronx-NYCY-Photo-Molly-Flores.jpg&w=1920&q=75')
else:
    st.image('https://static.vecteezy.com/ti/vecteur-libre/p1/6742141-cartoon-illustration-de-l-emplacement-symbole-avec-le-point-d-interrogation-vectoriel.jpg')