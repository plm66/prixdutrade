import http.client
import json

def get_token_price(symbol="BTCUSDT"):
    conn = http.client.HTTPSConnection("api.binance.com")
    endpoint = f"/api/v3/ticker/price?symbol={symbol}"

    try:
        conn.request("GET", endpoint)
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            price_info = json.loads(data)
            price = float(price_info['price'])
            return price
        else:
            print(f"Erreur HTTP : {response.status}")
            return None
    except Exception as e:
        print(f"Erreur lors de la connexion : {e}")
        return None
    finally:
        conn.close()

if __name__ == "__main__":
    price = get_token_price()
    if price is not None:
        print(f"Le prix actuel du Bitcoin (BTCUSDT) est : {price} $")
    else:
        print("Impossible de récupérer le prix du token.")
