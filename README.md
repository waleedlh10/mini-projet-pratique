# Candidates_Manager 🚀

**Candidates_Manager** est une application web qui permet de gérer les candidats d’un processus de recrutement.  
Elle offre des fonctionnalités pour **ajouter ✏️ et consulter 📄 les informations des candidats**, facilitant ainsi le suivi des candidatures.

## 🏗️ Architecture du Projet

Le projet **Candidates_Manager** est organisé de manière modulaire pour faciliter la maintenance et l'évolution :

- **backend/** : Contient toute la logique serveur et la communication avec les données.
- **candidates_manager/** : Module central qui gère les opérations sur les candidats.
- **frontend/** : Interface web permettant d’interagir avec l’application.
- **manage.py** : Script principal pour exécuter et gérer l’application.
- **requirements.txt** : Fichier listant toutes les dépendances nécessaires pour faire tour

## ✅ Prérequis

Avant d’installer et de lancer l’application, assurez-vous d’avoir installé sur votre machine :

- [Python 3.11+](https://www.python.org/downloads/) 🐍
- [pip](https://pip.pypa.io/en/stable/installation/) pour gérer les packages Python 📦

## 🚀 Installation et Démarrage

Suivez ces étapes pour installer et lancer l'application **Candidates_Manager** sur votre machine :

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/waleedlh10/mini-projet-pratique.git
   cd mini-projet-pratique
   ```

2. **Créer un environnement virtuel** (optionnel mais recommandé) :

   ```bash
   python -m venv env
   # Sur macOS/Linux
   source env/bin/activate
   # Sur Windows
   env\Scripts\activate
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l’application :**

   ```bash
   python manage.py runserver
   ```

5. **Ouvrir l’application dans votre navigateur :**
   Accédez à [http://localhost:8000](http://localhost:8000) 🌐

## 📜 Documentation de l’API

L’API de **Candidates_Manager** est documentée avec **Swagger** pour faciliter la compréhension et les tests des différentes routes.

- Vous pouvez accéder à l’interface Swagger après avoir lancé l’application à l’adresse suivante :  
  [http://localhost:8000/swagger](http://localhost:8000/swagger) 🛠️
- Swagger permet de visualiser toutes les routes disponibles, leurs paramètres et leurs réponses.
- Il facilite également les tests directs depuis le navigateur sans besoin d’outils externes.
