"""
Vous devez programmer un jeu du pendu. Pour rappel, le jeu du pendu est un jeu ou l’objectif est de découvrir un mot caché en choisissant une lettre. La longueur du mot caché est connue car il est affiché sous cette forme :

	Pour le mot « Bonjour » :    _ _ _ _ _ _ _

Si le mot caché contient cette lettre, l’indice est mis à jour avec cette lettre.

	Choix de la lettre « o » : _ o _ _ o _ _

Sinon le joueur perd un essai. Si le joueur atteint un nombre prédéfini d’essais manqués, le joueur perds la partie. S’il trouve le mot avant, il gagne la partie. Le joueur possède 10 essais et le mot caché est sélectionné aléatoirement dans une liste de mots. Le mot caché se trouve dans la constante MOT mise à votre disposition.

Pour ce faire vous devrez séparer votre code en plusieurs fonctions.
    a.	La fonction affichage_mot_cache qui prends en paramètres le mot caché,
    les lettres déjà tirées et le nombre d’erreurs restant
        i.	Cette fonction affichera le mot caché et les lettres déjà
        trouvées sous la forme vu ci-dessus
        ii.	Elle affichera également le nombre d’erreurs restantes
        (voir exemple de sortie)
    b.	La fonction tirage_lettre qui prend en paramètres les lettres
    déjà tirées. Celle-ci retournera les lettres déjà tirées avec la
    nouvelle lettre venant d’être choisie
        i.	Cette fonction demandera à l’utilisateur de saisir une lettre
        et reposera la question tant que la lettre entrée a déjà été choisie
    c.	La fonction verification_mot qui prend en paramètres le mot et
    les lettres déjà tirées. Celle-ci retournera un booléen si le mot a été
    trouvé ou non
        i.	Cette fonction vérifiera si le mot a effectivement été trouvé.
    d.	La fonction diminuer_erreurs qui prend en paramètre le nombre d’erreurs restants et retourne le nombre d’erreurs restant diminué de 1.

"""
from mots_pendus import tirer_mot

#Fonctions


#Programme principal
### Déclaration et Initialisation des variables
MOT: str = tirer_mot()



### Séquence d'opérations

