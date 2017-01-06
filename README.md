# footPi
python, flux rss, xpath, foot, raspberry pi, coloration de la console,  (RGB led), son 

footPi permet de récupérer un flux RSS depuis le site "http://www.scorespro.com/rss2/live-soccer.xml".
Ceci pour obtenir les scores des matchs de foot en direct et pouvoir faire des traitements en fonction:
- affichage de message 
- lancement de son 
- déclenchement de LED


Dans un premier temps vous devrez installer le module feedparser qui vous permettra de traiter le flux RSS.
-> sudo apt-get install python-pip
-> sudo pip install feedparser


Le module lxml vous permettra de parser des page html et de récupérer des informations via XPATH.
-> sudo apt-get install python3-lxml


La librairie "colorlib.py" contient les différentes couleurs et méthodes pour écrire dans la console.
Pour obtenir l'ensemble des couleurs vous pouvez lancer la commande :
-> python colorlib.Py
Vous pourrez ainsi ajouter une couleur sous la forme d'un tableau [style, couleur texte, couleur de fond].


La librairie "payslib.py" contient un ensemble de pays et retourne en fonction de son trigrame le pays écrit avec les couleurs de son drapeau.
si le pays n'est pas trouvé on retourne le trigramme.
Pour obtenir l'ensemble des pays contenu dans la lib, vous pouvez lancer la commande :
-> python payslib.py


La librairie "messagelib.py" contient l'nsemble des messages du post. Vous pouvez voir les messages disponibles en lançant la commande :
-> python messagelib.py


La librairie "footParsing.py" permet de récupérer les flux et traiter les informations.
Vous pouvez voir l'ensemble des flux en tapant la commande :
-> python footParsing.py


pour chacune des informations, nous afficherons :
	- l'identifiant qui est l'url de la page html du détail du match.
	- la date
	- le pays
	- la division
	- l'équipe domicile le score et les buteurs si il y en a.
	- les cartons de l'équipe domicile le score et les buteurs si il y en a.
	- les remplacements effectués par l'équipe domicile.
	- l'équipe exterieur le score et les buteurs si il y en a.
	- les cartons de l'équipe exterieur le score et les buteurs si il y en a.
	- les remplacements effectués par l'équipe exterieur.
	- le message du post

	le programme se lance avec la commande suivante:
  -> python lanceur.py
  


