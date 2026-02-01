# Morpion avec IA (Minimax)

Ce projet est une implémentation du jeu du Morpion (Tic-Tac-Toe) en Python avec une interface graphique réalisée en tkinter. Il inclut une intelligence artificielle utilisant l'algorithme Minimax avec élagage alpha-bêta, permettant à l'ordinateur de jouer de manière optimale.

## 🎮 Fonctionnalités

Interface graphique intuitive avec tkinter

Mode Joueur vs IA (l'IA joue en tant que 'O')

Algorithme Minimax optimisé pour des décisions stratégiques

## 📦 Installation

Assurez-vous d'avoir Python installé sur votre machine.
- **Windows** : Téléchargez Python depuis [python.org](https://www.python.org/). 
- **Linux** : Installez Python via la commande :  
     ```bash
     sudo apt install python3.10
     ```
# Clonez ce dépôt
git clone https://github.com/Adrn3/AI-Tic-Tac-Toe.git

# Exécutez le script
python morpion.py

## 🧠 Algorithme Minimax

L'algorithme Minimax analyse tous les coups possibles et attribue un score à chaque état du jeu :

+1 si l'IA gagne

-1 si le joueur gagne

0 en cas d'égalité
L'élagage alpha-bêta optimise la recherche en évitant d'explorer des branches inutiles.

## Dépendances
Bibliothèques utilisées :
Tkinter

## Licence
Adrien Ponchard

