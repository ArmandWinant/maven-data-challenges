from dash import Dash, html
import pandas as pd
from sodapy import Socrata

df = pd.read_csv('./data/MTA_Daily_Ridership.csv')

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Header(
            children=[
                html.H1('MTA Ridership', className='app-header-title'),
                html.P('Analysis', className='app-header-subtitle')
            ],
            className='app-header'
        ),
        html.Main(
            children=[]
        )
    ],
    className='app-container'
)

if __name__ == '__main__':
    app.run(debug=True)
