# boucled

La librairie ne permet que de créer un bot qui postera des topics prédéfinis.

### Prérequis

* Installer python3
* Installer la librairie pandas ```python3 -m pip install pandas```
* Cloner le repository ```git clone https://github.com/ataraxient/boucled.git```

### Créer une base de donnée de topics

Pour créer un bot qui post des topics il faut d'abord des topics. Pour cela, deux options possibles :
* mettre les topics dans un fichier *.txt*, avec sur la première ligne le titre du topic, et ensuite le message du topic. Cette méthode est simple et lisible, mais devient lourde lorsque la base de donnée devient grosse (> 10.000 topics)
* pour des grosses bases de données : mettre les topics dans un fichier *.csv* avec deux colonnes : une colonne *title* et une colonne *content*, et remplir les colonne avec le contenu voulu

### Comment choisir un compte sur lequel poster

Pour poster sur jvc, le bot à besoin d'un compte jvc pour poster. Lorsque vous vous connectez sur jvc, les serveurs de webedia vous envoient un cookie *coniunctio* qui servira de preuve que vous êtes bien authentifié, et qui est stocké par votre navigateur. Ensuite à chaque fois que vous essaierez de créer un message, votre navigateur enverra le cookie *coniunctio* qui permettra au serveur de valider que c'est bien vous. Tout ce dont à besoin *boucled* pour poster depuis votre compte, c'est ce cookie. Pour trouver votre cookie *coniunctio* sur jvc : SHIFT+F9 sur Firefox ou en faisant ça sur Chrome https://fr.wikihow.com/voir-les-cookies, il suffit ensuite de regarder le champ *coniunctio*

Les cookies sont à mettre dans le fichier `cookies.txt`, au format `pseudo cookie` sur chaque ligne.

### Lancer le bot

Pour lancer le bot il suffit de lancer la commande :

```console
python3 run.py [-h] (--csv CSV | --txt TXT) delay

positional arguments:
  delay       Délai entre les topics postés

optional arguments:
  -h, --help  show this help message and exit
  --csv CSV   Chemin vers un fichier .csv
  --txt TXT   Chemin vers un dossier contenant des .txt
```

Par exemple 
```console
python3 run.py 5  --txt topics/
```
pour poster les topics du dossier `topics/` à 5 minutes d'intervalle.
