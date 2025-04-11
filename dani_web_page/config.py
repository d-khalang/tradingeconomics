"""
Configuration settings and constants for the Economic Indicators Dashboard.
"""

# Available countries and indicators for free account
AVAILABLE_COUNTRIES = [
    'mexico', 'sweden', 'new zealand', 'thailand', 
]

AVAILABLE_INDICATORS = {
    'population': 'Population',
    'gdp': 'GDP',
    'interest rate': 'Interest Rate',
    'exports': 'Exports',
    'imports': 'Imports',
    "gdp per capita": "GDP Per Capita",
    "government spending": "Government Spending",
    "employment rate": "Employment Rate",
    "wages": "Wages",
    "population": "Population",
    "co2 emissions": "CO₂ Emissions",
    "food inflation": "Food Inflation",
    "industrial production": "Industrial Production",
    "construction output": "Construction Output",
    "capacity utilization": "Capacity Utilization",
    "consumer confidence": "Consumer Confidence",
    "business confidence": "Business Confidence"
}

FREQUENCY_CONVERSIONS = {
    'Monthly': {
        'Yearly': 12,
        'Quarterly': 3,
        'Monthly': 1
    },
    'Quarterly': {
        'Yearly': 4,
        'Quarterly': 1,
        'Monthly': 1/3
    },
    'Yearly': {
        'Yearly': 1,
        'Quarterly': 1/4,
        'Monthly': 1/12
    }
} 