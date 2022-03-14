def calcul_score(tableau_des, tableau_position_score, tableau_score):
    for i in range(0, len(tableau_position_score)):
        somme = 0
        if tableau_position_score[i] == 0:
            # La somme de 1
            if i == 0:
                tableau_score[i] = tableau_des.count(1)
            # La somme des 2
            elif i == 1:
                tableau_score[i] = tableau_des.count(2) * 2
            # La somme des 3
            elif i == 2:
                tableau_score[i] = tableau_des.count(3) * 3
            # La somme des 4
            elif i == 3:
                tableau_score[i] = tableau_des.count(4) * 4
            # La somme des 5
            elif i == 4:
                tableau_score[i] = tableau_des.count(5) * 5
            # La somme des 6
            elif i == 5:
                tableau_score[i] = tableau_des.count(6) * 6
            # Le brelan -> somme dés
            elif i == 6:
                print("Le Brelan")
                tableau_score[i] = 0
                nombre_pareil1 = tableau_des[0]
                nombre_pareil2 = tableau_des[1]
                nombre_pareil3 = tableau_des[2]
                if tableau_des.count(nombre_pareil1) >= 3 or tableau_des.count(
                        nombre_pareil2) >= 3 or tableau_des.count(nombre_pareil3) >= 3:
                    somme = 0
                    for j in tableau_des:
                        somme += j
                    tableau_score[i] = somme
            # Le carré -> somme dés
            elif i == 7:
                tableau_score[i] = 0
                nombre_pareil1 = tableau_des[0]
                nombre_pareil2 = tableau_des[1]
                if tableau_des.count(nombre_pareil1) >= 4 or tableau_des.count(nombre_pareil2) >= 4:
                    somme = 0
                    for j in tableau_des:
                        somme += j
                    tableau_score[i] = somme
            # Le full -> 25 points
            elif i == 8:
                print("full")
                tableau_score[i] = 0
                nombre_pareil1 = tableau_des[0]
                nombre_pareil2 = tableau_des[1]
                nombre_pareil3 = tableau_des[2]
                tableau_full = tableau_des.copy()
                print(tableau_full)
                if tableau_full.count(nombre_pareil1) == 3:
                    for j in range(3):
                        tableau_full.remove(nombre_pareil1)
                elif tableau_full.count(nombre_pareil2) == 3:
                    for j in range(3):
                        tableau_full.remove(nombre_pareil2)
                elif tableau_full.count(nombre_pareil3) == 3:
                    for j in range(3):
                        tableau_full.remove(nombre_pareil3)
                print(tableau_full)
                if len(tableau_des) != len(tableau_full) and tableau_full[0] == tableau_full[1]:
                    tableau_score[i] = 25

            # La petite suite -> 30 points
            elif i == 9:
                print("petite suite")
                tableau_score[i] = 0
                nombre_suite = 1
                tableau_non_trie = tableau_des.copy()
                print(tableau_des)
                tableau_des_trie = bubble_sort(tableau_non_trie)
                tableau_des_trie = list(set(tableau_des_trie))
                print(tableau_des_trie)
                for j in range(0, len(tableau_des_trie) - 1):
                    if tableau_des_trie[j] + 1 == tableau_des_trie[j + 1]:
                        nombre_suite += 1
                if nombre_suite == 4 or nombre_suite == 5:
                    print(tableau_des_trie)

                    tableau_score[i] = 30

            # La grande suite -> 40 points
            elif i == 10:
                tableau_score[i] = 0
                tableau_non_trie = tableau_des.copy()
                tableau_des_trie = bubble_sort(tableau_non_trie)
                if tableau_des_trie == [1, 2, 3, 4, 5] or tableau_des_trie == [2, 3, 4, 5, 6]:
                    tableau_score[i] = 40
            # Le Yamso -> 50 points
            elif i == 11:
                tableau_score[i] = 0
                nombre_pareil = tableau_des[0]
                if tableau_des.count(nombre_pareil) == 5:
                    tableau_score[i] = 50
            # La chance
            elif i == 12:
                somme = 0
                for j in tableau_des:
                    somme += j
                tableau_score[i] = somme

    return tableau_score


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


def calculer_score_final(tableau_score):
    somme_1er_tableau = 0
    somme_2eme_tableau = 0
    for i in range(0, 6):
        somme_1er_tableau += tableau_score[i]

    if somme_1er_tableau > 62:
        bonus = 35
    else:
        bonus = 0
    for i in range(6, 13):
        somme_2eme_tableau += tableau_score[i]

    somme_finale = somme_1er_tableau + somme_2eme_tableau
    resultat=[somme_1er_tableau,bonus,somme_1er_tableau+bonus,somme_2eme_tableau,somme_finale]
    return  resultat