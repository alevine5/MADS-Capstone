import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import Image, display

def generate_historical_viz(df, start=1709, end=2010, past_years=50, country_name="Name", duration=500):
    
    # Handle potential errors
    assert start < end, "Start year must be before end year."
    assert past_years <= 50, "Maximum past years is 50."
    assert start >= -1800, "Minimum start year is -1800."
    assert end <= 2010, "Maximum end year is 2010."
    assert country_name in ["Name", "ISO-3"], "Only two options for country_name: 'Name' or 'ISO-3'."
    
    # Choose column for country name
    if country_name == "Name":
        name_col = "Country_Name"
    else:
        name_col = "Country"  
    
    # Filter the DataFrame
    df = df.loc[(df['Year']>=start) & (df['Year']<=end) & (df['Years_Since_Outbreak']<=past_years)]
    
    # Extract unique years
    years = df['Year'].unique()

    # Create a template for hover data
    hover_temp = 'Country: %{customdata[0]}<br>Outbreak Year: %{customdata[1]}<br>Years\
    Since Outbreak: %{customdata[2]}<br><br>Description:<br>%{customdata[3]}\
    <extra></extra>'

    # Create a list to store frames
    frames = []

    # Create frames for each year
    for year in years:
        filtered_df = df[df['Year'] == year]
        frame = go.Frame(data=[
            go.Choropleth(
                locations=filtered_df['Country'],
                locationmode='ISO-3',
                z=filtered_df['Years_Since_Outbreak'], # z is used to determine color in Plotly
                colorscale = px.colors.sequential.Reds_r,
                colorbar_title='Years Since<br>Outbreak',
                customdata = filtered_df[[name_col, 'Outbreak_Year', 'Years_Since_Outbreak', 'Text']],
                hovertemplate=hover_temp,
                zmin=0, # set the range for z
                zmax=past_years, # allow range to change depending on function inputs
                colorbar = dict(
                    bgcolor='white',
                    x=.03,
                    y=.1,
                    xanchor='left',
                    yanchor='bottom',
                    len=.45,
                    bordercolor='black',
                    borderwidth=1,    
                ), 
            )
        ],
            name=f'Frame {year}'
        )
        frames.append(frame)

    # Create the initial choropleth map
    fig = go.Figure(data=[
        go.Choropleth(
            locations=df.loc[df['Year']==df['Year'].min()]['Country'],
            locationmode='ISO-3',
            z=df['Years_Since_Outbreak'],
            colorscale=px.colors.sequential.Reds_r,
            colorbar_title='Years Since<br>Outbreak',
            customdata = df[[name_col, 'Outbreak_Year', 'Years_Since_Outbreak', 'Text']],
            hovertemplate=hover_temp,
            zmin=0, 
            zmax=past_years, 
            colorbar = dict(
                    bgcolor='white',
                    x=.03,
                    y=.1,
                    xanchor='left',
                    yanchor='bottom',
                    len=.45,
                    bordercolor='black',
                    borderwidth=1,
                    outlinewidth=.5,
                    outlinecolor='black',
                    nticks=10,
                    ticks='outside',
                ), 
        )
    ])

    # Add frames to the figure
    fig.frames = frames

    # Select map version
    fig.update_geos(
        showcountries=True,
        countrywidth=.3,
        landcolor='#B8E7FF',
    )

    # Update layout properties
    fig.update_layout(
        title_text=f"Countries Experiencing Zoonotic Outbreaks by Year: {start} - {end}",
        title_font_size=24,
        title_x=.5,
        title_y=.89,
        height=600,
        width=1000,

        # Add buttons to interact with
        updatemenus=[{
            'type': 'buttons',
            'x': .08,
            'y': -.025,
            'showactive': True,
            'buttons': [{
                'label': 'Play',
                'method': 'animate',
                'args': [None, {
                    'fromcurrent': True,
                    'frame': {'duration': duration, 'redraw': True}, # allow for custom duration
                    'transition': {'duration': 300, 'easing': 'quadratic-in-out'}
                }]
            }, {
                'label': 'Pause',
                'method': 'animate',
                'args': [[None], {
                    'frame': {'duration': 0, 'redraw': True},
                    'mode': 'immediate',
                    'transition': {'duration': 0}
                }]
            }]
        }],

        # Add the year slider
        sliders=[{
            'active': 0,
            'yanchor': 'top',
            'xanchor': 'left',
            'currentvalue': {
                'font': {'size': 20},
                'prefix': 'Current Year:',
                'visible': True,
                'xanchor': 'right'
            },
            'transition': {'duration': 300, 'easing': 'cubic-in-out'},
            'pad': {'b': 0, 't': 0},
            'len': 0.9,
            'x': 0.1,
            'y': 0.00,
            'steps': [{
                'args': [[f'Frame {year}'], {
                    'frame': {'duration': 300, 'redraw': True},
                    'mode': 'immediate',
                    'transition': {'duration': 300}
                }],
                'label': f' {year}',
                'method': 'animate'
            } for year in years]
        }],
        
    )
    
    # Add a hyperlink containing source of the data
    source_text = 'Source: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7120709/">\
    Hubálek and Rudolf, National Library of Medicine, 2010</a>'
    fig.add_annotation(
        text=source_text,
        showarrow=False,
        xref='paper', # 'paper' sets the value of x to a fraction of the plotting area rather than a coordinate
        yref='paper', # do the same for y
        x=0.9, 
        y=0.02,  
        font=dict(size=10, color='gray'),
    )

    return fig
