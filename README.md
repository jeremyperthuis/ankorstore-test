wget https://chromedriver.storage.googleapis.com/101.0.4951.15/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip

wget https://www.insee.fr/fr/statistiques/fichier/6011070/ensemble.zip -P ressources/
unzip -p ressources/ensemble.zip donnees_communes.csv > ressources/cities.csv
rm ressources/ensemble.zip
