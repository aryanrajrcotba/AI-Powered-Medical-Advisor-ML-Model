# AI-Powered-Medical-Advisor-ML-Model

## Overview
AI-Powered Medical Advisor is a machine learning-based web application designed to assist users in identifying potential diseases based on their symptoms. It provides medical recommendations using a trained AI model.

## Features
- Predicts diseases based on user symptoms.
- Provides possible treatments or next steps.
- Web-based interface for user interaction.
- Utilizes a trained deep learning model for predictions.

## Installation

### Prerequisites
Ensure you have Python 3.8+ installed on your system.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/aryanrajrcotba/AI-Medical-Advisor.git
   cd AI-Medical-Advisor
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Enter symptoms and get AI-driven medical suggestions.

## Project Structure
```
medical_advisor/
│-- app.py  # Main application
│-- model.py  # Machine learning model
│-- requirements.txt  # Dependencies
│-- disease_symptoms_solutions_dataset.csv  # Dataset used for training
│-- static/  # CSS, images, and other static files
│-- templates/  # HTML files for UI
```

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Medical datasets used for training.
- Open-source ML libraries.

---
Developed by Aryan Raj

