from prix_du_trade import calculer_position
from prix_token import get_token_price

def initier_trade():
    # Demande à l'utilisateur s'il veut récupérer le prix actuel du token
    choix = input("Voulez-vous récupérer le prix actuel du Bitcoin depuis Binance ? (O/N): ").strip().upper()
    
    if choix == 'O':
        prix_token = get_token_price()
        if prix_token is None:
            print("Impossible de récupérer le prix du token. Annulation du trade.")
            return
    else:
        prix_token = input("Entrez le prix du token (par défaut Bitcoin): ").strip()
        if not prix_token:
            prix_token = 30000  # Prix par défaut du Bitcoin si aucune entrée n'est fournie
        else:
            try:
                prix_token = float(prix_token)
            except ValueError:
                print("Entrée invalide. Utilisation du prix par défaut de Bitcoin.")
                prix_token = 30000

    # Appeler la fonction pour calculer la position
    montant_risque, stop_loss_ratio, taille_position, _, _ = calculer_position()

    # Calculer le nombre de tokens avec le prix récupéré ou fourni
    nombre_tokens = taille_position / prix_token

    # Afficher ou traiter les données récupérées
    print("Données récupérées du fichier 'prix_du_trade.py':")
    print(f"Montant de capital à risquer : {montant_risque} $")
    print(f"Ratio de stop loss : {stop_loss_ratio}%")
    print(f"Taille de la position : {taille_position:.2f} $")
    print(f"Prix du token : {prix_token} $")
    print(f"Nombre de tokens à acheter : {nombre_tokens:.6f}")

# Exécution de la fonction
initier_trade()