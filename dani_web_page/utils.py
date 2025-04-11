"""
Utility functions for data processing and frequency conversion.
"""
from datetime import datetime
from config import FREQUENCY_CONVERSIONS

def convert_frequency(value, from_freq, to_freq, indicator=None):
    """Convert value from one frequency to another"""
    # Skip conversion for population data as it's a stock variable
    if indicator == 'population':
        return value
        
    if from_freq == to_freq:
        return value
    
    try:
        conversion_factor = FREQUENCY_CONVERSIONS[from_freq][to_freq]
        return value * conversion_factor
    except KeyError:
        return value

def process_economic_data(raw_data, target_frequency, indicator):
    """Process raw economic data and convert to target frequency."""
    processed_data = []
    
    for entry in raw_data:
        if isinstance(entry, dict) and all(k in entry for k in ['DateTime', 'Value', 'Frequency']):
            try:
                date_str = entry['DateTime'].split('.')[0]
                date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
                value = float(entry['Value'])
                original_frequency = entry['Frequency']
                
                if value > 0 and original_frequency:  # Only process positive values with valid frequency
                    converted_value = convert_frequency(value, original_frequency, target_frequency, indicator)
                    processed_data.append({
                        'date': date.strftime('%Y-%m-%d'),
                        'value': converted_value,
                        'original_frequency': original_frequency,
                        'original_value': value
                    })
            except (ValueError, TypeError) as e:
                print(f"Error processing data entry: {e}")
                continue
                
    return sorted(processed_data, key=lambda x: x['date'])

def determine_target_frequency(frequencies):
    """Determine the most common frequency from the data."""
    if not frequencies:
        return 'Yearly'
        
    frequency_counts = {}
    for country_freqs in frequencies.values():
        for freq in country_freqs:
            frequency_counts[freq] = frequency_counts.get(freq, 0) + 1
            
    return max(frequency_counts.items(), key=lambda x: x[1])[0] 