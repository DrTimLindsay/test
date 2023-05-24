from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
# import datetime
import plotly.io as pio


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0'}]
           )
server = app.server

methods = ['Horwill 4', 'Horwill 5', 'Canova', '% WR']


# width={'size': 6, 'offset': 0, 'order': 1}
# className='text-center text-primary mb4'


# App layout


app.layout = dbc.Container([
    html.H2('Race Performances', className='text-center text-primary mt-2'),
    html.P('Input any and all race performances that represent your current fitness.', className='text-center mb4'),
    dbc.Row([
        dbc.Col(html.P('800 m', className='text-end m-0'), width=2),
        dbc.Col(dbc.Input(id='t8', placeholder='hh:mm:ss', type='text'), width=2)
    ],
        justify='center', align='center', className='mb-2'),
    dbc.Row([
        dbc.Col(html.P('1500 m', className='text-end m-0'), width=2),
        dbc.Col(dbc.Input(id='t15', placeholder='hh:mm:ss', type='text'), width=2)
    ],
        justify = 'center', align = 'center', className = 'mb-2'),
    dbc.Row([
        dbc.Col(html.P('3000 m', className='text-end m-0'), width=2),
        dbc.Col(dbc.Input(id='t3', placeholder='hh:mm:ss', type='text'), width=2)
    ],
        justify='center', align='center', className='mb-2'),
    dbc.Row([
        dbc.Col(html.P('5000 m', className='text-end m-0'), width=2),
        dbc.Col(dbc.Input(id='t5', placeholder='hh:mm:ss', type='text'), width=2)
    ],
        justify='center', align='center', className='mb-2'),
    dbc.Row([
        dbc.Col(html.P('10,000 m', className='text-end m-0'), width=2),
        dbc.Col(dbc.Input(id='t10', placeholder='hh:mm:ss', type='text'), width=2)
    ],
        justify='center', align='center', className='mb-2'),
    dbc.Row([
        dbc.Col(html.P('half marathon', className='text-end m-0'), width=2),
        dbc.Col(dbc.Input(id='tHalf', placeholder='hh:mm:ss', type='text'), width=2)
    ],
        justify='center', align='center', className='mb-2'),
    dbc.Row([
        dbc.Col(html.P('marathon', className='text-end m-0'), width=2),
        dbc.Col(dbc.Input(id='tFull', placeholder='hh:mm:ss', type='text'), width=2)
    ],
        justify='center', align='center', className='mb-5'),
    html.H2('Pace Chart', className='text-center text-primary'),
    dbc.Row(
        dbc.Col(dcc.Dropdown(id='method', multi=False, value='choose method', options=methods), width=2),
        justify='center', align='center', className='mb-2'),
    html.Div(id='output'),
])


@app.callback(
    Output(component_id='output', component_property='children'),
    Input(component_id='t8', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == "__main__":
    app.run_server(debug=True)
