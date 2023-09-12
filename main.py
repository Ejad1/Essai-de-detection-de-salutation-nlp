import spacy

# Charger le modèle de langue spaCy
nlp = spacy.load("fr_core_news_sm")

# Fonction pour répondre au salut de l'utilisateur
def repondre_au_salut(salutation):
    # Utiliser spaCy pour analyser la salutation de l'utilisateur
    doc = nlp(salutation)

    # Vérifier si la salutation contient un verbe de salutation (par exemple, "salut" ou "bonjour")
    for token in doc:
        if token.lemma_ in ["salut", "bonjour", "hello", "coucou"]:
            return "Salut ! Comment puis-je t'aider aujourd'hui ?"

    # Si aucune salutation n'a été trouvée
    return "Je ne comprends pas bien. Peux-tu reformuler ta salutation ?"

# Demande à l'utilisateur de saluer
salutation_utilisateur = input("Dis-moi bonjour, salut, hello ou coucou : ")

# Obtenir la réponse appropriée
reponse = repondre_au_salut(salutation_utilisateur)

# Afficher la réponse
print(reponse)
