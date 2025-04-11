# Indicators Dashboard

A web application that visualizes economic indicators for different countries using data from Trading Economics.

## Features

- Compare economic indicators across multiple countries
- Support for various indicators (GDP, Population, Exports, etc.)
- Automatic frequency conversion with special handling for stock variables
- Interactive charts with original and converted values
- Responsive design

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root with your Trading Economics API key:
   ```
   TE_API_KEY=your_api_key_here
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Project Structure

- `app.py`: Main application file with Flask routes
- `config.py`: Configuration settings and constants
- `utils.py`: Utility functions for data processing
- `templates/`: HTML templates
- `.env`: Environment variables (not tracked in git)

## Dependencies

- Flask
- Trading Economics API
- Chart.js
- Bootstrap
- python-dotenv

## Notes

- Free Trading Economics account limited to Mexico, New Zealand, Sweden, and Thailand
- Population data is treated as a stock variable (no frequency conversion)
- Other indicators are treated as flow variables and converted based on frequency 