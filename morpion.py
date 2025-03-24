import tkinter
import math

def check_nul():
    '''Vérifie si la grille est pleine sans gagnant'''
    global win
    count = sum(1 for row in buttons for btn in row if btn['text'] in ('X', 'O'))
    if count == 9 and not win:
        win = True
        print("Match nul")
        screen.after(100, screen.quit)

def print_winner():
    '''Permet d'afficher le gagnant'''
    global win
    win = True
    print(f"Le joueur {current_player} a gagné.")
    screen.after(100, screen.quit)

def change_player():
    '''Alterne entre le joueur X et O'''
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

def check_win():
    '''Vérifie si un joueur a aligné 3 symboles'''
    global win
    for i in range(3):
        # Vérifie les lignes et colonnes
        if all(buttons[i][j]['text'] == current_player for j in range(3)) or \
                all(buttons[j][i]['text'] == current_player for j in range(3)):
            print_winner()
            return
    # Vérifie les diagonales
    if all(buttons[i][i]['text'] == current_player for i in range(3)) or \
            all(buttons[i][2 - i]['text'] == current_player for i in range(3)):
        print_winner()
        return
    check_nul()

def place_symbol(row, col):
    '''Place le symbole du joueur actuel sur la grille'''
    global win
    if win or buttons[row][col]['text']:
        return
    buttons[row][col].config(text=current_player)
    check_win()
    if not win:
        change_player()
        if current_player == 'O':
            screen.after(100, ai_move)  # Ajout d'un délai pour fluidifier l'affichage

def draw_grid():
    '''Dessine la grille de jeu avec des boutons'''
    for row in range(3):
        row_buttons = []
        for col in range(3):
            button = tkinter.Button(screen, font=("Arial", 50), width=5, height=2, command=lambda r=row, c=col: place_symbol(r, c))
            button.grid(row=row, column=col)
            row_buttons.append(button)
        buttons.append(row_buttons)

def minmax(is_max, alpha, beta):
    '''Application de l'algorithme Minimax avec élagage alpha-bêta'''
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return None, 1 if buttons[i][0]['text'] == 'O' else -1
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return None, 1 if buttons[0][i]['text'] == 'O' else -1
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return None, 1 if buttons[0][0]['text'] == 'O' else -1
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return None, 1 if buttons[0][2]['text'] == 'O' else -1
    if all(buttons[r][c]['text'] != "" for r in range(3) for c in range(3)):
        return None, 0 # Match nul

    best_score = -math.inf if is_max else math.inf  # Score initial selon le joueur
    best_move = None # Stocke le meilleur coup à jouer

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                buttons[row][col]['text'] = 'O' if is_max else 'X'
                _, score = minmax(not is_max, alpha, beta)
                buttons[row][col]['text'] = "" # Annule le coup après l'évaluation

                if is_max:
                    if score > best_score:
                        best_score, best_move = score, (row, col)
                    alpha = max(alpha, best_score)
                else:
                    if score < best_score:
                        best_score, best_move = score, (row, col)
                    beta = min(beta, best_score)
                if beta <= alpha:
                    break
    return best_move, best_score

def ai_move():
    '''Fait jouer l'IA en utilisant l'algorithme Minimax'''
    move, _ = minmax(True, -math.inf, math.inf)
    if move:
        place_symbol(*move)

# Définition des variables globales
buttons = []
current_player = 'X'
win = False

# Création de la fenêtre principale
screen = tkinter.Tk()
screen.title("Morpion")
screen.minsize(500, 500)

# Démarrage du jeu
draw_grid()
screen.mainloop()