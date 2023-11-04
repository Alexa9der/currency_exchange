from import_libraries.libraries import *

with open('data/private_data.json', 'r') as f:
    private_data = json.load(f)

account = private_data["account"]
password = private_data["password"]
server = private_data["server"]


def connect_to_mt5():
    """
    Łączy się z MetaTrader 5 i loguje przy użyciu podanych danych konta.

    Zwraca:
    bool: True, jeśli połączenie jest udane, w przeciwnym razie False.
    """
    global account, password, server

    # Inicjalizacja połączenia z MetaTrader 5
    if not mt5.initialize():
        print("Błąd inicjalizacji ()")
        mt5.shutdown()
        return None

    authorized = mt5.login(account, password=password, server=server)

    if authorized:
        print(f"Połączono z kontem")
        return True
    else:
        print("Nie udało się połączyć. Kod błędu:", mt5.last_error())
        mt5.shutdown()
        return False

def get_historical_data(timeframe=mt5.TIMEFRAME_D1, symbol="GER30", start='2012-01-01'):
    """
    Pobiera historyczne dane z MetaTrader 5.

    Argumenty:
    timeframe (int): Interwał czasowy dla danych historycznych.
    symbol (str): Symbol, dla którego mają zostać pobrane dane historyczne.
    start (str): Data rozpoczęcia pobierania danych historycznych.

    Zwraca:
    pd.DataFrame: DataFrame zawierający pobrane dane historyczne.
    """
    if not connect_to_mt5():
        return None

    start_time = pd.Timestamp(start)  # Ustaw datę rozpoczęcia pobierania danych historycznych

    count = 22734  # Ustaw liczbę świec, które chcesz pobrać
    rates = mt5.copy_rates_from(symbol, timeframe, start_time, count)

    # Sprawdź, czy pobieranie danych jest udane
    if rates is not None:
        # Konwertuje dane do DataFrame pandas
        rates_frame = pd.DataFrame(rates)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame = rates_frame.rename(columns=lambda x: x.capitalize())
        rates_frame = rates_frame.rename(columns={ "Time" : "Date" })
        
        rates_frame['Volume'] = rates_frame['High'] - rates_frame['Low']
        rates_frame['MaxPositivePriceChange'] =  rates_frame['High'] -  rates_frame['Open'] 
        rates_frame['MaxNegativePriceChange'] = rates_frame['Open'] - rates_frame['Low']
        
        rates_frame['PriceChange'] = abs(rates_frame['Close'] - rates_frame['Close'].shift(1))
        # Zamknięcie połączenia z MetaTrader 5
        mt5.shutdown()
        return rates_frame
    else:
        print("Błąd pobierania danych.")
        mt5.shutdown()
        return None









