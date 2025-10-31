# 🫀 Prédiction du Risque Cardiovasculaire – API FastAPI & Machine Learning

## 📌 Contexte du Projet
Les maladies cardiovasculaires représentent **la première cause de mortalité dans le monde**, avec environ **17,9 millions de décès par an**.  
Les médecins ont donc besoin d’un **outil prédictif fiable** capable d’estimer le risque de développer une maladie cardiaque à partir des données d’un patient.

---

## 🎯 Objectif Final
Développer une **API FastAPI** qui :
- Reçoit les informations cliniques d’un patient,
- Calcule le **score de risque cardiovasculaire** via un modèle de Machine Learning,
- Retourne le résultat sous forme de prédiction JSON.

---

## 🧩 Tâches à Réaliser

### 1. 🗂️ Organisation du Projet
Travail effectué **en binôme** avec une répartition claire des rôles :

| Rôle | Responsabilités principales |
|------|------------------------------|
| **Développeur Backend** | Structure FastAPI, intégration SQLite, endpoints `POST /patients` & `GET /patients` |
| **Développeur IA / Data** | Nettoyage du dataset, entraînement du modèle ML, intégration de la prédiction dans l’API |

#### 🔄 Collaboration GitHub
- Branche principale : `main`
- Branches fonctionnelles :
  - `feature/api` → Backend FastAPI
  - `feature/ml` → Modèle de Machine Learning

---

### 2. ⚙️ Développement Web & Base de Données

- Framework : **FastAPI**
- Base de données : **SQLite** (via **SQLAlchemy**)
- Validation : **Pydantic**

#### 🧠 Endpoints principaux :
| Méthode | Route | Description |
|----------|--------|-------------|
| `POST` | `/patients` | Ajouter un nouveau patient |
| `GET` | `/patients` | Lister tous les patients |
| `POST` | `/predict_risk` | Calculer le risque cardiovasculaire d’un patient |

---

### 3. 🤖 Partie Machine Learning

1. Charger et nettoyer le dataset  
2. Transformer les colonnes (catégorielles / numériques)  
3. Séparer les données en `X` et `y`  
4. Créer un **Pipeline Scikit-Learn**  
5. Entraîner et sauvegarder le modèle avec **joblib.dump**  
6. (Bonus) Utiliser **GridSearchCV** pour optimiser les hyperparamètres  
7. Intégrer le modèle dans la route `/predict_risk`

---

### 4. 🧪 Tests Unitaires

- Outil : **pytest**
- Client : **TestClient (FastAPI)**
  
Vérifier :
- Le bon fonctionnement de la route `/predict_risk`  
- Code de réponse HTTP = `200`

---

### 5. 📚 Documentation

#### 🧭 Swagger (intégré)
Une documentation interactive disponible sur : 
http://127.0.0.1:8000/docs

🧱 2. Créer et activer un environnement virtuel
python -m venv venv
venv\Scripts\activate      # Sous Windows
source venv/bin/activate   # Sous Linux/Mac

📦 3. Installer les dépendances
pip install -r requirements.txt

🚀 4. Lancer le serveur FastAPI
uvicorn app.main:app --reload
📤 Exemple de Requête /predict_risk
✅ Requête :
POST /predict_risk
{
  "age": 45,
  "gender": 1,
  "pressurehight": 14,
  "pressurelow": 9,
  "glucose": 12,
  "kcm": 1.3,
  "troponin": 1.2,
  "impluse": 7
}