from forex_python.converter import CurrencyCodes
from forex_python.converter import CurrencyRates


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    # Crea un oggetto CurrencyRates
    c = CurrencyRates()
    try:
        # Ottieni il tasso di cambio in tempo reale
        exchange_rate = c.get_rate(from_currency, to_currency)
        # Calcola l'importo convertito
        return amount * exchange_rate
    except:
        return "Errore nella conversione della valuta."


def get_currency_symbol(currency_code: str) -> str:
    # Crea un oggetto CurrencyCodes
    cc = CurrencyCodes()

    try:
        # Ottieni il simbolo della valuta
        return cc.get_symbol(currency_code)
    except:
        return ""


if __name__ == '__main__':
    # Esempio di utilizzo
    amount = 100  # L'importo da convertire
    from_currency = "USD"  # Valuta di origine
    to_currency = "EUR"  # Valuta di destinazione

    result = convert_currency(
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency
    )
    if isinstance(result, float):
        print(
            f"{amount}{get_currency_symbol(currency_code=from_currency)} "
            f"equivale a {result:.2f}{get_currency_symbol(currency_code=to_currency)}"
        )
    else:
        print(result)
