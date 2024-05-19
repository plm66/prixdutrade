def calculer_position(capital=2000, risque=2, stop_loss_ratio=0.35):
    # Calcul du montant de capital à risquer
    montant_risque = capital * (risque / 100)
    
    # Demande à l'utilisateur de changer le ratio de stop loss, avec possibilité de laisser vide
    stop_loss_input = input(f"Le ratio de stop loss actuel est {stop_loss_ratio}%. Appuyez sur Entrée pour utiliser le ratio par défaut, ou entrez un nouveau ratio (en pourcentage, par exemple 0.25 pour 0.25%): ").strip()
    
    if stop_loss_input:
        try:
            stop_loss_ratio = float(stop_loss_input)
        except ValueError:
            print("Entrée invalide. Utilisation du ratio de stop loss par défaut.")
    
    # Conversion du pourcentage en ratio décimal
    stop_loss_decimal = stop_loss_ratio / 100
    
    # Calcul de la taille de la position
    taille_position = montant_risque / stop_loss_decimal
    
    # Affichage des résultats
    print(f"Montant de capital à risquer : {montant_risque} $")
    print(f"Ratio de stop loss : {stop_loss_ratio}%")
    print(f"Taille de la position : {taille_position:.2f} $")
    
    return montant_risque, stop_loss_ratio, taille_position, stop_loss_decimal, None
