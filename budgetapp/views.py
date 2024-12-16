from django.shortcuts import render
import pandas as pd
import plotly.express as px
from datetime import datetime
import json

def budget_chart(request):
    # Sample data - you can replace this with your actual data source
    data = {
        'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01'],
        'total': [700, 1000, 900, 1000, 1200, 800, 1500, 1300],
        'budget': [700, 1000, 900, 1000, 1200, 800, 1500, 1300],
    }
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.strftime('%B')
    
    # Get unique years for dropdown
    years = sorted(df['year'].unique())
    selected_year = request.GET.get('year', str(years[-1]))  # Default to latest year
    
    # Filter data for selected year
    filtered_df = df[df['year'] == int(selected_year)]
    
    # Create the bar chart
    fig = px.bar(filtered_df, x='month', y=['total', 'budget'],
                 title=f'Budget vs Actual Spending {selected_year}',
                 labels={'value': 'Amount ($)', 'variable': 'Type'},
                 barmode='group')
    
    chart_json = fig.to_json()
    
    context = {
        'chart': chart_json,
        'years': years,
        'selected_year': selected_year,
    }
    
    return render(request, 'budget.html', context)
