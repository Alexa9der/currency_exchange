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


def automated_trading_from_signals(df, symbol="GER30", lot: float=0.01, deviation=10):
    """
    Executes automated trading operations based on buy and sell signals in the provided DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing buy and sell signals.
        symbol (str, optional): The trading symbol. Defaults to "GER30".
        lot (float, optional): The trading lot size. Defaults to 0.01.
        deviation (int, optional): The deviation parameter for order execution. Defaults to 10.

    This function executes automated trading operations based on buy and sell signals in the provided DataFrame.
    It opens a new position according to the latest signal and closes the previous deal if any.

    Note:
    - The function assumes that there is a connection to MetaTrader 5 established before calling it.
    - It utilizes the `connect_to_mt5` function to establish the connection.
    """

    def order(signal, symbol, lot, deviation):
        # Define the order parameters based on the given signal
        price = mt5.symbol_info_tick(symbol).ask if signal == "buy" else mt5.symbol_info_tick(symbol).bid
        trade_type = mt5.ORDER_TYPE_BUY if signal == "buy" else mt5.ORDER_TYPE_SELL
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": float(lot),
            "type": trade_type,
            "price": price,
            "deviation": deviation,
            "magic": 234000,
            "comment": f"python script open {signal}",
            "type_time": mt5.ORDER_TIME_DAY,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }
        return request

    def close_previous_deal(symbol, signal):
        # Close any existing position opposite to the current signal
        positions = mt5.positions_get(symbol)
        if positions:
            if signal == "buy":
                for position in positions:
                    if position.type == mt5.ORDER_TYPE_SELL:
                        result = mt5.position_close(position.ticket)
            if signal == "sell":
                for position in positions:
                    if position.type == mt5.ORDER_TYPE_BUY:
                        result = mt5.position_close(position.ticket)

    try:
        # Establish a connection to MetaTrader 5
        connect_to_mt5()
        # Get the latest signal from the DataFrame
        signal = df["Signal"].iloc[-1]
        # Close the previous deal if any
        close_previous_deal(symbol=symbol, signal=signal)
        # Get the current market price based on the signal
        price = mt5.symbol_info_tick(symbol).ask if signal == "buy" else mt5.symbol_info_tick(symbol).bid
        # Create an order request based on the signal and other parameters
        request = order(signal=signal, symbol=symbol, lot=lot, deviation=deviation)
        # Send the order request to execute the trade
        result = mt5.order_send(request)

        # Check the result of the order execution
        if result is not None:
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                # Print an error message if the order execution fails
                print("2. order_send failed, retcode={}".format(result.retcode))
                result_dict = result._asdict()
                for field in result_dict.keys():
                    if field == "request":
                        traderequest_dict = result_dict[field]._asdict()
                        for tradereq_filed in traderequest_dict:
                            print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
        else:
            print("Order send failed. Result is None.")

    except Exception as e:
        # Handle any exceptions that may occur during the trading process
        print(f"Exception: {e}")

    finally:
        # Shut down the MetaTrader 5 connection
        mt5.shutdown()







