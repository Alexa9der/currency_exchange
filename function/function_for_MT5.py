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
        print("Initialization error")
        mt5.shutdown()
        return None

    authorized = mt5.login(account, password=password, server=server)

    if authorized:
        print(f"Connected to your account: {account}")
        return True
    else:
        print("Failed to connect. Error code:", mt5.last_error())
        mt5.shutdown()
        return False


def get_all_symbols():
    """
     Gets a list of all available symbols in MetaTrader 5.

     Returns:
     list: List of characters.
     """
    # It is assumed that connect_to_mt5 is a function that connects to MetaTrader 5
    if not connect_to_mt5():
        print("Error connecting to MetaTrader 5.")
        return None

    try:
        # Getting a list of symbols
        symbols_info = mt5.symbols_get()

        # Get the names of each symbol
        symbols = [symbol.name for symbol in symbols_info]

        return symbols
    except Exception as e:
        print(f"Error when retrieving a list of symbols:{e}")
        mt5.shutdown()
        return None


def get_historical_data( symbol="GER30", timeframe=mt5.TIMEFRAME_D1, count=30_000):
    """
     Retrieves historical data from MetaTrader 5.

     Arguments:
     timeframe (int): Time frame for historical data.
     symbol (str): The symbol for which you want to get historical data.
     count (int): Number of candles requested.

     Returns:
     pd.DataFrame: DataFrame containing the received historical data.
     """
    if not connect_to_mt5():
        print("Error connecting to MetaTrader 5.")
        return None

    try:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
    except Exception as e:
        print("initialize() failed, error code =",mt5.last_error())
        print(f"Error while receiving data: {e}")
        mt5.shutdown()
        return None

    # Check the success of receiving data
    if rates is not None:
        # Convert data to pandas DataFrame
        rates_frame = pd.DataFrame(rates)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame = rates_frame.rename(columns=lambda x: x.capitalize())
        rates_frame = rates_frame.rename(columns={"Time": "Date"})

        
        rates_frame['Volume'] = rates_frame['High'] - rates_frame['Low']
        rates_frame['MaxPositivePriceChange'] = rates_frame['High'] - rates_frame['Open']
        rates_frame['MaxNegativePriceChange'] = rates_frame['Open'] - rates_frame['Low']

        rates_frame['PriceChange'] = abs(rates_frame['Close'] - rates_frame['Close'].shift(1))
        rates_frame = rates_frame.dropna()
        # Close the connection to MetaTrader 5
        # mt5.shutdown()
        return rates_frame
    else:
        print("Error while receiving data.")
        mt5.shutdown()
        return None


# Orders f
def automated_trading_from_signals(df, symbol="GER30", lot = None, deviation=10):
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
            "volume": float(1), 
            "type": trade_type,
            "price": price,
            "deviation": deviation,
            "magic": 234000,
            "comment": f"python script open {signal}",
            "type_time": mt5.ORDER_TIME_DAY,
            "type_filling": mt5.TRADE_ACTION_DEAL,
            "request_actions": mt5.TRADE_ACTION_DEAL
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

        lot = lot if lot else get_min_volume(symbol)
        # Create an order request based on the signal and other parameters
        request = order(signal=signal, symbol=symbol, lot=lot, deviation=deviation)
        # Send the order request to execute the trade
        result = mt5.order_send(request)

        symbol_info = mt5.symbol_info(symbol)
 
        # Check the result of the order execution
        if result is not None:
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                # Print an error message if the order execution fails
                print(f"2. order_send failed, retcode={result.retcode}, comment={result.comment}")
                result_dict = result._asdict()
                for field in result_dict.keys():
                    if field == "request":
                        traderequest_dict = result_dict[field]._asdict()
                        for tradereq_field in traderequest_dict:
                            print(f"   traderequest: {tradereq_field}={traderequest_dict[tradereq_field]}")
            else:
                print("Order executed successfully.")
        else:
            print("Order send failed. Result is None.")

    except Exception as e:
        # Handle any exceptions that may occur during the trading process
        print(f"Exception: {e}")

    finally:
        # Shut down the MetaTrader 5 connection
        mt5.shutdown()


def get_min_volume(symbol):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is not None:
        return symbol_info.volume_min
    else:
        print("get_min_volume:")
        print(f"Information about symbol {symbol} not found.")
        return None








