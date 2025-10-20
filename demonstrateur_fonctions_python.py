"""
=============================================================================
DÉMONSTRATEUR DE FONCTIONS PYTHON - DE LA BASE À L'AVANCÉ
=============================================================================
Ce fichier vous guide à travers tous les concepts des fonctions en Python,
de la syntaxe de base aux techniques avancées.

Chaque section peut être exécutée indépendamment pour voir les résultats.
=============================================================================
"""

print("=" * 80)
print("BIENVENUE DANS LE DÉMONSTRATEUR DE FONCTIONS PYTHON")
print("=" * 80)
print()

# =============================================================================
# NIVEAU 1 : LES BASES
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 1 : LES BASES DES FONCTIONS")
print("=" * 80)

# 1.1 Fonction simple sans paramètre
def dire_bonjour():
    """Fonction la plus simple : sans paramètre, sans retour."""
    print("Bonjour le monde !")

print("\n1.1 Fonction simple sans paramètre :")
dire_bonjour()


# 1.2 Fonction avec paramètres
def saluer(nom):
    """Fonction avec un paramètre."""
    print(f"Bonjour {nom} !")

print("\n1.2 Fonction avec paramètre :")
saluer("Alice")


# 1.3 Fonction avec retour (return)
def additionner(a, b):
    """Fonction qui retourne une valeur."""
    return a + b

print("\n1.3 Fonction avec retour :")
resultat = additionner(5, 3)
print(f"5 + 3 = {resultat}")


# 1.4 Fonction avec plusieurs paramètres et retour
def calculer_rectangle(longueur, largeur):
    """Calcule l'aire et le périmètre d'un rectangle."""
    aire = longueur * largeur
    perimetre = 2 * (longueur + largeur)
    return aire, perimetre  # Retourne un tuple

print("\n1.4 Fonction retournant plusieurs valeurs :")
a, p = calculer_rectangle(5, 3)
print(f"Rectangle 5x3 : Aire = {a}, Périmètre = {p}")


# =============================================================================
# NIVEAU 2 : PARAMÈTRES AVANCÉS
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 2 : PARAMÈTRES AVANCÉS")
print("=" * 80)

# 2.1 Paramètres par défaut
def presenter(nom, age=18, ville="Paris"):
    """Fonction avec paramètres par défaut."""
    return f"{nom}, {age} ans, habite à {ville}"

print("\n2.1 Paramètres par défaut :")
print(presenter("Bob"))
print(presenter("Charlie", 25))
print(presenter("Diana", 30, "Lyon"))


# 2.2 Arguments nommés (keyword arguments)
def creer_profil(nom, age, profession, ville):
    """Démontre l'utilisation des arguments nommés."""
    return f"{nom} ({age} ans) - {profession} à {ville}"

print("\n2.2 Arguments nommés :")
print(creer_profil(nom="Emma", ville="Marseille", age=28, profession="Développeuse"))


# 2.3 *args - Nombre variable d'arguments positionnels
def calculer_somme(*nombres):
    """Accepte un nombre variable d'arguments."""
    total = sum(nombres)
    return f"Somme de {nombres} = {total}"

print("\n2.3 *args (arguments variables) :")
print(calculer_somme(1, 2, 3))
print(calculer_somme(10, 20, 30, 40, 50))


# 2.4 **kwargs - Nombre variable d'arguments nommés
def afficher_infos(**informations):
    """Accepte un nombre variable d'arguments nommés."""
    print("Informations reçues :")
    for cle, valeur in informations.items():
        print(f"  - {cle}: {valeur}")

print("\n2.4 **kwargs (arguments nommés variables) :")
afficher_infos(nom="Frank", age=35, profession="Ingénieur", pays="France")


# 2.5 Combinaison de tout
def fonction_complete(arg1, arg2, *args, option1="default", **kwargs):
    """Démontre la combinaison de tous les types de paramètres."""
    print(f"Arguments positionnels obligatoires: {arg1}, {arg2}")
    print(f"Arguments positionnels supplémentaires (*args): {args}")
    print(f"Option avec défaut: {option1}")
    print(f"Arguments nommés supplémentaires (**kwargs): {kwargs}")

print("\n2.5 Combinaison de tous les types de paramètres :")
fonction_complete(1, 2, 3, 4, 5, option1="custom", extra="info", autre="donnée")


# =============================================================================
# NIVEAU 3 : FONCTIONS LAMBDA (ANONYMES)
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 3 : FONCTIONS LAMBDA")
print("=" * 80)

# 3.1 Lambda simple
carre = lambda x: x ** 2

print("\n3.1 Fonction lambda simple :")
print(f"Carré de 5 : {carre(5)}")


# 3.2 Lambda avec plusieurs paramètres
multiplier = lambda x, y: x * y

print("\n3.2 Lambda avec plusieurs paramètres :")
print(f"3 × 4 = {multiplier(3, 4)}")


# 3.3 Lambda avec map()
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x ** 2, nombres))

print("\n3.3 Lambda avec map() :")
print(f"Nombres : {nombres}")
print(f"Carrés : {carres}")


# 3.4 Lambda avec filter()
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = list(filter(lambda x: x % 2 == 0, nombres))

print("\n3.4 Lambda avec filter() :")
print(f"Nombres : {nombres}")
print(f"Nombres pairs : {pairs}")


# 3.5 Lambda avec sorted()
etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 18},
    {"nom": "Charlie", "note": 12}
]
trie_par_note = sorted(etudiants, key=lambda e: e["note"], reverse=True)

print("\n3.5 Lambda avec sorted() :")
print("Étudiants triés par note (décroissant) :")
for e in trie_par_note:
    print(f"  {e['nom']}: {e['note']}/20")


# =============================================================================
# NIVEAU 4 : PORTÉE DES VARIABLES (SCOPE)
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 4 : PORTÉE DES VARIABLES")
print("=" * 80)

# 4.1 Variables locales vs globales
x = 10  # Variable globale

def demo_scope():
    """Démontre la portée des variables."""
    x = 5  # Variable locale (masque la globale)
    print(f"  x local dans la fonction : {x}")

print("\n4.1 Variables locales vs globales :")
print(f"x global avant : {x}")
demo_scope()
print(f"x global après : {x}")


# 4.2 Mot-clé global
compteur = 0

def incrementer():
    """Modifie une variable globale."""
    global compteur
    compteur += 1
    print(f"  Compteur : {compteur}")

print("\n4.2 Utilisation du mot-clé 'global' :")
incrementer()
incrementer()
incrementer()


# 4.3 Mot-clé nonlocal (pour les fonctions imbriquées)
def fonction_externe():
    """Démontre nonlocal avec des fonctions imbriquées."""
    message = "Externe"

    def fonction_interne():
        nonlocal message
        message = "Modifié par interne"
        print(f"    Message dans interne : {message}")

    print(f"  Message avant : {message}")
    fonction_interne()
    print(f"  Message après : {message}")

print("\n4.3 Mot-clé 'nonlocal' :")
fonction_externe()


# =============================================================================
# NIVEAU 5 : FONCTIONS D'ORDRE SUPÉRIEUR
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 5 : FONCTIONS D'ORDRE SUPÉRIEUR")
print("=" * 80)

# 5.1 Fonction qui prend une fonction en paramètre
def appliquer_operation(x, y, operation):
    """Fonction qui accepte une autre fonction en paramètre."""
    return operation(x, y)

def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

print("\n5.1 Fonction prenant une fonction en paramètre :")
print(f"5 + 3 = {appliquer_operation(5, 3, addition)}")
print(f"5 × 3 = {appliquer_operation(5, 3, multiplication)}")


# 5.2 Fonction qui retourne une fonction
def creer_multiplicateur(facteur):
    """Retourne une fonction qui multiplie par un facteur."""
    def multiplicateur(x):
        return x * facteur
    return multiplicateur

print("\n5.2 Fonction qui retourne une fonction :")
multiplier_par_2 = creer_multiplicateur(2)
multiplier_par_10 = creer_multiplicateur(10)
print(f"5 × 2 = {multiplier_par_2(5)}")
print(f"5 × 10 = {multiplier_par_10(5)}")


# 5.3 Closures (fermetures)
def creer_compteur():
    """Crée un compteur avec closure."""
    count = 0

    def incrementer():
        nonlocal count
        count += 1
        return count

    return incrementer

print("\n5.3 Closures :")
compteur1 = creer_compteur()
compteur2 = creer_compteur()
print(f"Compteur 1 : {compteur1()}, {compteur1()}, {compteur1()}")
print(f"Compteur 2 : {compteur2()}, {compteur2()}")


# =============================================================================
# NIVEAU 6 : DÉCORATEURS
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 6 : DÉCORATEURS")
print("=" * 80)

# 6.1 Décorateur simple
def decorateur_simple(fonction):
    """Décorateur qui ajoute un message avant et après."""
    def wrapper():
        print("  [Début]")
        fonction()
        print("  [Fin]")
    return wrapper

@decorateur_simple
def dire_hello():
    print("  Hello!")

print("\n6.1 Décorateur simple :")
dire_hello()


# 6.2 Décorateur avec arguments
def decorateur_avec_args(fonction):
    """Décorateur qui gère les arguments."""
    def wrapper(*args, **kwargs):
        print(f"  Arguments : {args}, {kwargs}")
        resultat = fonction(*args, **kwargs)
        print(f"  Résultat : {resultat}")
        return resultat
    return wrapper

@decorateur_avec_args
def multiplier_nombres(a, b):
    return a * b

print("\n6.2 Décorateur avec arguments :")
multiplier_nombres(4, 7)


# 6.3 Décorateur paramétré
def repeter(n):
    """Décorateur qui répète l'exécution n fois."""
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"  Exécution {i+1}/{n}")
                fonction(*args, **kwargs)
        return wrapper
    return decorateur

@repeter(3)
def afficher_message(msg):
    print(f"    Message : {msg}")

print("\n6.3 Décorateur paramétré :")
afficher_message("Bonjour")


# 6.4 Décorateur de timing
import time

def chronometrer(fonction):
    """Mesure le temps d'exécution."""
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print(f"  Temps d'exécution : {fin - debut:.6f} secondes")
        return resultat
    return wrapper

@chronometrer
def calcul_lent():
    total = sum(range(1000000))
    return total

print("\n6.4 Décorateur de chronométrage :")
calcul_lent()


# =============================================================================
# NIVEAU 7 : GÉNÉRATEURS
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 7 : GÉNÉRATEURS")
print("=" * 80)

# 7.1 Générateur simple avec yield
def compter_jusqu_a(n):
    """Générateur qui compte de 1 à n."""
    i = 1
    while i <= n:
        yield i
        i += 1

print("\n7.1 Générateur simple :")
for nombre in compter_jusqu_a(5):
    print(f"  {nombre}")


# 7.2 Générateur Fibonacci
def fibonacci(n):
    """Génère les n premiers nombres de Fibonacci."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("\n7.2 Générateur Fibonacci :")
print(f"  Les 10 premiers nombres de Fibonacci : {list(fibonacci(10))}")


# 7.3 Expression génératrice
print("\n7.3 Expression génératrice :")
carres_gen = (x**2 for x in range(10))
print(f"  Carrés de 0 à 9 : {list(carres_gen)}")


# 7.4 Générateur avec send()
def generateur_interactif():
    """Générateur qui peut recevoir des valeurs."""
    total = 0
    while True:
        valeur = yield total
        if valeur is not None:
            total += valeur

print("\n7.4 Générateur interactif (avec send) :")
gen = generateur_interactif()
next(gen)  # Initialisation
print(f"  Après ajout de 5 : {gen.send(5)}")
print(f"  Après ajout de 10 : {gen.send(10)}")
print(f"  Après ajout de 3 : {gen.send(3)}")


# =============================================================================
# NIVEAU 8 : RÉCURSIVITÉ
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 8 : RÉCURSIVITÉ")
print("=" * 80)

# 8.1 Factorielle récursive
def factorielle(n):
    """Calcule la factorielle de n de manière récursive."""
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

print("\n8.1 Factorielle récursive :")
print(f"  5! = {factorielle(5)}")
print(f"  7! = {factorielle(7)}")


# 8.2 Fibonacci récursif (avec mémoïzation)
def fibonacci_recursif(n, memo={}):
    """Fibonacci récursif optimisé avec mémoïzation."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_recursif(n-1, memo) + fibonacci_recursif(n-2, memo)
    return memo[n]

print("\n8.2 Fibonacci récursif avec mémoïzation :")
print(f"  F(10) = {fibonacci_recursif(10)}")
print(f"  F(20) = {fibonacci_recursif(20)}")


# 8.3 Parcours d'arbre récursif
def parcourir_structure(structure, niveau=0):
    """Parcourt récursivement une structure imbriquée."""
    indent = "  " * niveau
    if isinstance(structure, dict):
        for cle, valeur in structure.items():
            print(f"{indent}{cle}:")
            parcourir_structure(valeur, niveau + 1)
    elif isinstance(structure, list):
        for item in structure:
            parcourir_structure(item, niveau)
    else:
        print(f"{indent}- {structure}")

print("\n8.3 Parcours récursif de structure :")
data = {
    "entreprise": "TechCorp",
    "departements": {
        "IT": ["Alice", "Bob"],
        "RH": ["Charlie", "Diana"]
    }
}
parcourir_structure(data)


# =============================================================================
# NIVEAU 9 : ANNOTATIONS DE TYPE (TYPE HINTS)
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 9 : ANNOTATIONS DE TYPE")
print("=" * 80)

from typing import List, Dict, Tuple, Optional, Union, Callable

# 9.1 Annotations simples
def additionner_typage(a: int, b: int) -> int:
    """Fonction avec annotations de type."""
    return a + b

print("\n9.1 Annotations de type simples :")
print(f"  3 + 5 = {additionner_typage(3, 5)}")


# 9.2 Types complexes
def traiter_liste(nombres: List[int]) -> Dict[str, int]:
    """Traite une liste et retourne un dictionnaire."""
    return {
        "total": sum(nombres),
        "moyenne": sum(nombres) // len(nombres) if nombres else 0,
        "max": max(nombres) if nombres else 0
    }

print("\n9.2 Types complexes (List, Dict) :")
stats = traiter_liste([10, 20, 30, 40, 50])
print(f"  Stats : {stats}")


# 9.3 Type Optional
def saluer_optionnel(nom: Optional[str] = None) -> str:
    """Paramètre optionnel avec type hint."""
    if nom is None:
        return "Bonjour !"
    return f"Bonjour {nom} !"

print("\n9.3 Type Optional :")
print(f"  {saluer_optionnel()}")
print(f"  {saluer_optionnel('Alice')}")


# 9.4 Union de types
def traiter_donnee(valeur: Union[int, str]) -> str:
    """Accepte soit un int soit un str."""
    if isinstance(valeur, int):
        return f"Nombre : {valeur * 2}"
    return f"Texte : {valeur.upper()}"

print("\n9.4 Union de types :")
print(f"  {traiter_donnee(42)}")
print(f"  {traiter_donnee('hello')}")


# 9.5 Type Callable
def executer_fonction(func: Callable[[int, int], int], a: int, b: int) -> int:
    """Accepte une fonction comme paramètre avec type hint."""
    return func(a, b)

print("\n9.5 Type Callable :")
print(f"  {executer_fonction(lambda x, y: x + y, 10, 5)}")


# =============================================================================
# NIVEAU 10 : TECHNIQUES AVANCÉES
# =============================================================================

print("\n" + "=" * 80)
print("NIVEAU 10 : TECHNIQUES AVANCÉES")
print("=" * 80)

# 10.1 Fonction partielle (functools.partial)
from functools import partial

def puissance(base, exposant):
    return base ** exposant

carre_partial = partial(puissance, exposant=2)
cube_partial = partial(puissance, exposant=3)

print("\n10.1 Fonctions partielles :")
print(f"  5² = {carre_partial(5)}")
print(f"  5³ = {cube_partial(5)}")


# 10.2 Décorateur avec functools.wraps
from functools import wraps

def mon_decorateur(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper qui préserve les métadonnées."""
        return func(*args, **kwargs)
    return wrapper

@mon_decorateur
def fonction_avec_doc():
    """Cette documentation est préservée."""
    pass

print("\n10.2 Préservation des métadonnées :")
print(f"  Nom : {fonction_avec_doc.__name__}")
print(f"  Doc : {fonction_avec_doc.__doc__}")


# 10.3 Cache avec lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cache(n):
    """Fibonacci ultra-rapide avec cache."""
    if n <= 1:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)

print("\n10.3 Cache avec lru_cache :")
import time
debut = time.time()
resultat = fibonacci_cache(100)
fin = time.time()
print(f"  F(100) calculé en {fin-debut:.6f}s : {resultat}")


# 10.4 Décorateur de classe
class CompteurAppels:
    """Décorateur qui compte les appels à une fonction."""
    def __init__(self, func):
        self.func = func
        self.appels = 0

    def __call__(self, *args, **kwargs):
        self.appels += 1
        print(f"  Appel #{self.appels} à {self.func.__name__}")
        return self.func(*args, **kwargs)

@CompteurAppels
def fonction_comptee():
    return "Résultat"

print("\n10.4 Décorateur de classe :")
fonction_comptee()
fonction_comptee()
fonction_comptee()


# 10.5 Context manager avec fonction
from contextlib import contextmanager

@contextmanager
def timer_context(nom):
    """Context manager pour mesurer le temps."""
    print(f"  Début de {nom}")
    debut = time.time()
    yield
    fin = time.time()
    print(f"  Fin de {nom} : {fin-debut:.6f}s")

print("\n10.5 Context manager :")
with timer_context("opération"):
    sum(range(1000000))


# 10.6 Décorateur empilé
def gras(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italique(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@gras
@italique
def texte():
    return "Bonjour"

print("\n10.6 Décorateurs empilés :")
print(f"  {texte()}")


# =============================================================================
# EXERCICES PRATIQUES
# =============================================================================

print("\n" + "=" * 80)
print("EXERCICES PRATIQUES - À VOUS DE JOUER !")
print("=" * 80)

print("""
Voici quelques exercices pour pratiquer :

1. Créez une fonction qui prend une liste et retourne un dictionnaire
   avec le nombre d'occurrences de chaque élément.

2. Créez un décorateur qui log tous les arguments et le résultat
   d'une fonction dans un fichier.

3. Créez un générateur qui produit tous les nombres premiers.

4. Créez une fonction récursive qui inverse une chaîne de caractères.

5. Créez un décorateur qui limite le nombre d'appels à une fonction
   (rate limiting).

6. Créez une fonction d'ordre supérieur qui compose plusieurs fonctions.

7. Créez un générateur qui parcourt un fichier ligne par ligne
   en filtrant les lignes vides.

8. Créez une classe avec des méthodes qui utilisent des décorateurs
   @property, @staticmethod et @classmethod.
""")

print("\n" + "=" * 80)
print("FIN DU DÉMONSTRATEUR")
print("=" * 80)
print("\nContinuez à pratiquer et à expérimenter !")
print("La maîtrise vient avec la pratique régulière.")
print("Bon apprentissage ! 🐍")
