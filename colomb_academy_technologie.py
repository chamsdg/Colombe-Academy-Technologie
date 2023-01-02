# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:10:07 2022

@author: caidara01, CHAMSEDINE AIDARA
"""
#--------------------------------------------------------------------------------------#
#                     DASHBOARD DATA & IA COLOMBE ACADEMY TECHNOLOGIE                  #
#--------------------------------------------------------------------------------------#

# importer les librairies.
import streamlit as st

# occuper tous l'ecran.
st.set_page_config(layout="wide")

# l'image à afficher.
st.image("cat.jfif", width=200)

# afficher le titre.
st.title("Master Data Science & IA dashboard")
    
# trois colonnes pour la progression et les modules
progression, niveau, module, professeur = st.columns(4)
#---------------------------------------------------------------------------------------------#
#                                    MASTER 1                                                 #
#---------------------------------------------------------------------------------------------#
# le niveau de la filiere.
with niveau:
    select_niveau = st.selectbox(
        "Merci de selectionner le niveau d'étude",
        ("Master 1 Data & IA","Master 2 Data & IA", "Licence 3 Data"),)
    if select_niveau == "Master 1 Data & IA":
        with module:
            select_module = st.selectbox(
                "Merci de selectionner le module",
                ("Machine Learning","Deep Learning", "Data Science"),)
            if  select_module == "Machine Learning":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 45.0,
                        disabled = True,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - apprentissage supervisé et non supervisé.
                        - Explication detaillée sur l'overfitting effectuée'
                        ''')
                with professeur:
                    nom_professeur = st.selectbox(
                        "Le professeur chargé du cours",
                        ("Chamsedine AIDARA",""),disabled = True,)
                        
            if  select_module == "Deep Learning":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 65.0,
                        disabled = True,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - Les applications du deep learning.
                        - Classification avec les reseaux de neurones artificielles.
                        ''')  
                with professeur:
                    nom_professeur = st.selectbox(
                        "Le professeur chargé du cours",
                        ("Djibril Diop", " "),disabled = True,)
                    
            if  select_module == "Data Science":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 25.0,
                        disabled = True,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - Bon debut dans l' ensemble.
                        - Decouvert des librairies.
                        ''') 
                with professeur:
                    nom_professeur = st.selectbox(
                        "Le professeur chargé du cours",
                        ("Moussa Diop", " "),disabled = True,)
  
    
#---------------------------------------------------------------------------------------------#
#                                    MASTER 2                                                 #
#---------------------------------------------------------------------------------------------#

    with niveau:
        if select_niveau == "Master 2 Data & IA":
            with module:
                select_module = st.selectbox(
                    "Merci de selectionner le module",
                    ("DataWarehouse","Computer Vision", "ElasticSearch"),)
                if  select_module == "DataWarehouse":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 50.0,
                            disabled = True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - Donner plus d'exercice.
                            - Plus d'explication sur les concepts.
                            ''')   
                    with professeur:
                        nom_professeur = st.selectbox(
                            "Le professeur chargé du cours",
                            ("Moustapha Mané",""),disabled = True,)
                            
                if  select_module == "Computer Vision":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 85.0,
                            disabled = True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - Travailler davantage sur les images.
                            - Reconnaissance de video.
                            ''')  
                    with professeur:
                        nom_professeur = st.selectbox(
                            "Le professeur chargé du cours",
                            ("Malick",""),disabled = True,)
                        
                if  select_module == "ElasticSearch":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 95.0,
                            disabled = True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - L'utilité de ElasticSearch.
                            - Dashboard en temps réel.
                            ''') 
                    with professeur:
                        nom_professeur = st.selectbox(
                            "Le professeur chargé du cours",
                            ("Moustapha Touré",""),disabled = True,)

#---------------------------------------------------------------------------------------------#
#                                    LICENCE 3                                                #
#---------------------------------------------------------------------------------------------#
      
    with niveau:
        if select_niveau == "Licence 3 Data":
            with module:
                select_module = st.selectbox(
                    "Merci de selectionner le module",
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
                            - La problématique de L'IA.
                            - Les limites de L'IA.
                            ''')   
                    with professeur:
                        nom_professeur = st.selectbox(
                            "Le professeur chargé du cours",
                            ("Malainy Aidara",""),disabled = True,)
                            
                if  select_module == "Web Scraping":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 95.0,
                            disabled = True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - Lister les librairies de python.
                            - load depuis wikipedia toutes les regions du senegal.
                            ''')  
                            
                    with professeur:
                        nom_professeur = st.selectbox(
                            "Le professeur chargé du cours",
                            ("Abdoulaye Sow"," "),disabled = True,)
                    
                    
                if  select_module == "Data Visualisation":
                    with progression:
                        progression_percentage = st.slider(
                            "Estimation de la progression du cours.",
                            min_value = 0.0,
                            max_value = 100.0,
                            value = 15.0,
                            disabled = True,
                            format = "%d%%")
                    with st.expander("Compte rendu du module selectionné"):
                      st.markdown('''
                            - Comprehension des concepts de power Bi.
                            - Ces differentes applications.
                            ''') 
                        
                    with professeur:
                        nom_professeur = st.selectbox(
                            "Le professeur chargé du cours",
                            ("Pape Moussa Gueye"," "),disabled = True,)



#---------------------------------------------------------------------------------------------#
#                                   DIVERS                                                    #
#---------------------------------------------------------------------------------------------#
                    
# presentation dashboard.
st.sidebar.header('A Propos du Dashboard')
st.sidebar.markdown('''
                    Ce dashboard a été realisé dans le but d'avoir un meilleur suivi des differents modules 
                    effectués par les enseignants. Il permet d' avoir une estimation sur chaque module. Chaque cours sera ponctué par 
                    un compte rendu. Le dashboard est mis à jours chaque fin de semaine.
                    ''')

st.sidebar.image("image-ia.jfif")


                    
# A propos de moi.
if st.checkbox("By"):
        st.caption("Aidara Chamsedine")
        st.caption("Consultant Chargé du programme Data Science & IA à CAT")
        st.caption("Mentor OpenClassrooms sur les Parcours Data Analyst & Data Scientist")
        st.caption("Supervisor Data Scientist Expresso Télécom")
        st.caption("c.aidara@cat.sn")
        st.caption("aidarachamsedine10@gmail.com")