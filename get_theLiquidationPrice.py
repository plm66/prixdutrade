
"""
samedi 8 juin 2024
on a d'abord fait un tableau a imprimer pour avoir une idee des risques pour un capital de 1000
sur l'empan des leverages possibles entre 1 et 200.
c'est marrant de penser qu'avec un leverage de 2, je peux quand meme etre liquidé si le prix perd la moitie de sa valeur
donc mon capital passera à 500 et c'est la marge utilisée pour un leverage de 2
c'est ce principe que je ne comprends pas  facilement
le ratio de la marge  entre le prix d'achat et le nouveau prix en dessous
le ratio de la difference entre le capital et la ratio du leverage.( là j'ai vraiment de l'eau dans le cerveau, il faut le savoir)
pour moi faire des math c est comme vouloir regarder un film sans ecran ni projecteur dans la piece.


"""

# CALCUL DE POSITION basée sur le \capital et le \leverage



def calculate_position_size(capital, token_price, liquidation_price):
    # Calculate leverage needed to determine the position size
    leverage = 1 / (1 - (liquidation_price / token_price))
    # Calculate the position size based on leverage
    position_size = capital * leverage
    return leverage, position_size

# Given default values
default_capital = 1000
default_token_price = 70000
default_token = "BTC"

# Get user input for capital, with a default value if the input is empty
capital_input = input("Enter the exact capital (press Enter for default $1000): ")
if not capital_input.strip():
    capital = default_capital
else:
    capital = float(capital_input)

# Get user input for token price, with a default value if the input is empty
token_price_input = input("Enter the token price (press Enter for default $70,000): ")
if not token_price_input.strip():
    token_price = default_token_price
else:
    token_price = float(token_price_input)

# Get user input for token type, with a default value if the input is empty
token_input = input("Which token? (press Enter for default 'BTC'): ")
if not token_input.strip():
    token = default_token
else:
    token = token_input

# Get user input for liquidation price
liquidation_price = float(input("Enter the desired liquidation price: "))

# Calculate the position size
leverage, position_size = calculate_position_size(capital, token_price, liquidation_price)

# Calculate the amount in token units
token_units = position_size / token_price

# Display the results
print(f"Leverage: {leverage}")
print(f"Position Size: ${position_size:.2f}")
print(f"Equivalent Position in {token}: {token_units:.6f} {token}")
