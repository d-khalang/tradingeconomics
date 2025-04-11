"""
Main application file for the Economic Indicators Dashboard.
"""
from flask import Flask, render_template, jsonify, request
import tradingeconomics as te
from collections import defaultdict
import os
from dotenv import load_dotenv

from config import AVAILABLE_COUNTRIES, AVAILABLE_INDICATORS
from utils import process_economic_data, determine_target_frequency

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Initialize Trading Economics with API key
te.login(os.getenv('TE_API_KEY'))

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('index.html', 
                         countries=AVAILABLE_COUNTRIES,
                         indicators=AVAILABLE_INDICATORS)

@app.route('/api/data')
def get_data():
    """API endpoint to fetch and process economic data."""
    countries = request.args.getlist('countries[]')
    indicator = request.args.get('indicator', 'population')
    target_frequency = request.args.get('frequency', 'auto')
    
    if not countries:
        return jsonify({'error': 'No countries selected'}), 400
    
    try:
        data = {}
        frequencies = defaultdict(set)
        all_frequencies = set()
        
        # First pass: collect frequencies
        for country in countries:
            country_data = te.getHistoricalData(country=country, indicator=indicator)
            for entry in country_data:
                if isinstance(entry, dict) and 'Frequency' in entry and entry['Frequency']:
                    frequencies[country].add(entry['Frequency'])
                    all_frequencies.add(entry['Frequency'])
        
        # Determine target frequency if auto
        if target_frequency == 'auto':
            target_frequency = determine_target_frequency(frequencies)
        
        # Second pass: process data
        for country in countries:
            country_data = te.getHistoricalData(country=country, indicator=indicator)
            processed_data = process_economic_data(country_data, target_frequency, indicator)
            
            if processed_data:
                data[country] = {
                    'data': processed_data,
                    'frequency': target_frequency,
                    'original_frequency': list(frequencies[country])[0] if frequencies[country] else 'Unknown'
                }
        
        # Prepare response with metadata
        response = {
            'data': data,
            'metadata': {
                'frequencies': {country: list(freqs) if freqs else ['Unknown'] 
                              for country, freqs in frequencies.items()},
                'available_frequencies': list(all_frequencies) if all_frequencies else ['Unknown'],
                'target_frequency': target_frequency
            }
        }
        
        return jsonify(response)
    
    except Exception as e:
        print(f"Error in get_data: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 