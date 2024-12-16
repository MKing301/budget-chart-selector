from django.shortcuts import render
import pandas as pd
from datetime import datetime
import json

def budget_chart(request):
    # Sample data - you can replace this with your actual data source
    data = {
        'date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-01-01', '2024-02-01', '2024-03-01'],
        'total': [1000, 1200, 800, 1500, 1300, 900],
        'budget': [1200, 1200, 1200, 1500, 1500, 1500],
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
    
    # Prepare data for Chart.js
    months = filtered_df['month'].tolist()
    totals = filtered_df['total'].tolist()
    budgets = filtered_df['budget'].tolist()
    
    chart_data = {
        'labels': months,
        'datasets': [
            {
                'label': 'Actual Spending',
                'data': totals,
                'backgroundColor': '#00FF00',  # Solid green
                'borderColor': '#00FF00',
                'borderWidth': 1
            },
            {
                'label': 'Budget',
                'data': budgets,
                'backgroundColor': '#0000FF',  # Solid blue
                'borderColor': '#0000FF',
                'borderWidth': 1
            }
        ]
    }
    
    # Debug print
    print("Chart Data:", json.dumps(chart_data, indent=2))
    print("Years:", years)
    print("Selected Year:", selected_year)
    
    context = {
        'chart_data': json.dumps(chart_data),
        'years': years,
        'selected_year': selected_year,
    }
    
    return render(request, 'budget.html', context)
