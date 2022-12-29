# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:10:07 2022

@author: caidara01
"""

# importer les librairies.
import streamlit as st
# import plotly.express as px

# occuper tous l'ecran.
st.set_page_config(layout="wide")


# l'image à afficher.
st.image("cat.jfif", width=200)


# afficher le titre.
st.title("Master Data Science & IA dashboard")
    
# deux colonnes pour la progression et les modules
progression, niveau, module = st.columns(3)
#---------------------------------------------------------------------------------------------#
#                                    MASTER 1                                                 #
#---------------------------------------------------------------------------------------------#
# le niveau de la filiere.
with niveau:
    select_niveau = st.selectbox(
        "Merci de choisir le niveau d' étude",
        ("Master DataScience1","Master DataScience2", "Licence3 Data"),)
    if select_niveau == "Master DataScience1":
        with module:
            select_module = st.selectbox(
                "Merci de choisir le module",
                ("Machine Learning","Deep Learning", "Data Science"),)
            if  select_module == "Machine Learning":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 45.0,
                        disabled=True,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - Les differentes applications du ML.
                        - Lister les metrics d'évaluation'
                        ''')   
                        
            if  select_module == "Deep Learning":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 65.0,
                        disabled=True,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - Definition du deep learning.
                        - Introduction aux reseaux de neurones
                        ''')  
            if  select_module == "Data Science":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 25.0,
                        disabled=True,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - Les conceptes clés de la data science
                        - Les differentes types de statistiques
                        ''') 
  
    
#---------------------------------------------------------------------------------------------#
#                                    MASTER 2                                                 #
#---------------------------------------------------------------------------------------------#

    with niveau:
        if select_niveau == "Master DataScience2":
            with module:
                select_module = st.selectbox(
                    "Merci de choisir le module",
                    ("DataWarehouse","Computer Vision", "ElasticSearch"),)
                if  select_module == "DataWarehouse":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 50.0,
                            disabled=True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - Donner plus d'exercice.
                            - Plus d'explication sur les concepts'
                            ''')   
                            
                if  select_module == "Computer Vision":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 85.0,
                            disabled=True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - Travailler davantage sur les images.
                            - Reconnaissance de video
                            ''')  
                if  select_module == "ElasticSearch":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 95.0,
                            disabled=True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - L'utilité de Elastic.
                            - Dashboard en temps réel 
                            ''') 

#---------------------------------------------------------------------------------------------#
#                                    LICENCE 3                                                #
#---------------------------------------------------------------------------------------------#
      
    with niveau:
        if select_niveau == "Licence3 Data":
            with module:
                select_module = st.selectbox(
                    "Merci de choisir le module",
                    ("Culture et Ethique IA","Web Scraping", "Data Visualisation"),)
                if  select_module == "Culture et Ethique IA":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 100.0,
                            disabled=True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - La problématique de L'IA
                            - Les limites de L'IA
                            ''')   
                            
                if  select_module == "Web Scraping":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 95.0,
                            disabled=True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - Lister les librairies de python.
                            - load depuis wikipedia toutes les regions du senagal
                            ''')  
                if  select_module == "Data Visualisation":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 15.0,
                            disabled=True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - Comprehension des concepts de power Bi
                            - Ces differentes applications 

                            ''') 
# presentation dashboard.
st.sidebar.header('A Propos du Dashboard')
st.sidebar.markdown('''
                    Ce dashboard a été realisé dans le but d'avoir un meilleur suivi des differents modules 
                    effectués par les enseignants. Il permet d' avoir une estimation sur chaque module. Chaque cours sera ponctué par 
                    un compte rendu. Le dashboard est mis à jours chaque fin de semaine.
                    ''')
                    
# A propos de moi.
if st.checkbox("By"):
        st.markdown("Aidara Chamsedine")
        st.markdown("Consultant Chargé du programme Data Science & IA à CAT (https://cat.sn/)")
        st.markdown("c.aidara@cat.sn")
