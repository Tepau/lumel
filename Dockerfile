# Utilisez une image de base Python
FROM python:3.10

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt et installez les dépendances
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copiez le reste de votre application
COPY . .

# Exécutez votre application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
