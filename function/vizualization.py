from import_libraries.libraries import  *

def support_resistance_chart(data, support: str = "support_100", resistance: str = "resistance_100") -> None:
    """
    Displays a candlestick chart with support and resistance lines.

    Args:
        data (pd.DataFrame): Input data.
        support (str): Name of the column representing the support line. Defaults to "support_100".
        resistance (str): Name of the column representing the resistance line. Defaults to "resistance_100".
    """
    init_notebook_mode(connected=True)
    
    fig = go.Figure(data=[go.Candlestick(x=data['datetime'],
                                         open=data['open'],
                                         high=data['high'],
                                         low=data['low'],
                                         close=data['close'])],
                    layout=go.Layout(
                        height=700,  
                        width=1000,  
                        title='Candlestick Chart with Support and Resistance Lines',
                        yaxis_title='Price',
                        xaxis_rangeslider_visible=False
                    ))
    
    fig.add_trace(go.Scatter(x=data['datetime'], y=data[support], mode='lines', name='Support Line', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=data['datetime'], y=data[resistance], mode='lines', name='Resistance Line', line=dict(dash='dash')))
    
    fig.update_layout(title='Candlestick Chart with Support and Resistance Lines',
                      yaxis_title='Price',
                      xaxis_rangeslider_visible=False)

    fig.show()