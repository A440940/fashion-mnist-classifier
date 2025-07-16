# 👕 Fashion MNIST Classifier

Ce projet consiste à **réentraîner un modèle MobileNetV3 sur le jeu de données Fashion-MNIST**, puis à le déployer via une **API FastAPI**. L’objectif est de proposer une classification d’images d’articles vestimentaires en 10 catégories.

Le modèle utilise l’architecture **MobileNetV3-Small**, fine-tunée sur Fashion-MNIST (60 000 images en niveaux de gris).  
Il est ensuite mis à disposition via une API REST, pouvant recevoir une **URL d’image** en entrée et retourner la classe prédite.

---

## 🚀 Lancer le projet en local

### 1. Cloner le projet

```bash
git clone https://github.com/A440940/fashion-mnist-classifier.git
cd fashion-mnist-classifier
```

### 2. Construire l'image docker à partir du DockerFile

```bash
docker build -t fashion_classifier:1.0.0 .
```

### 3. Lancer un conteneur

```bash
docker build -t fashion_classifier:1.0.0 .
```

### 3. Accéder à l'API

```bash
http://localhost:8080/docs
```

Exemples d'URL valides (issues du jeu de test) :

- https://drive.google.com/uc?id=1jUgYj7RCd1nB9PLU4OEU1-trh1kPYigV
- https://drive.google.com/uc?id=1iUoG4387hD1njbDwt2FzA4jIt57ERPkr
- https://drive.google.com/uc?id=1rlAG3P_O2IPDLtrMDD56LwXwU5eDu7dY
- https://drive.google.com/uc?id=1KaPSHfvC9qrJsYAjjW4Yk45M7vsoqOYA
- https://drive.google.com/uc?id=1XGzI491Nti259stY_zf28Gr5-TygidZV

❌ Le modèle est peu performant sur des images prises aléatoirement sur Google Images.
En effet, le jeu d'entraînement Fashion-MNIST contient des images très normalisées :

- taille 28x28

- fond noir, objet gris/blanc centré

- pas de couleurs, pas de bruits de fond

Pour des résultats fiables, utilisez de préférence des images issues du dataset ou respectant ce format.
