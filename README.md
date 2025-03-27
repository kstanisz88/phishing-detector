# Phishing URL Detector

## Overview
This project demonstrates how to detect phishing websites using a machine learning model trained on a dataset of URL-based features. A Random Forest Classifier is used to classify websites as either **legitimate** or **phishing**.

## Dataset
The dataset includes 11,430 samples and 88 features extracted from URLs, covering:
- URL structure (lengths, use of symbols, subdomains)
- Use of HTTPS or shortening services
- Domain registration details (age, WHOIS presence)
- JavaScript behavior (e.g., `onmouseover`, `popup_window`)
- External resources and redirections

**Target column:** `status`
- `legitimate` → 0
- `phishing` → 1

## Project Workflow
1. **Data Cleaning**
   - Removed the raw URL column
   - Encoded `status` to binary labels
2. **Modeling**
   - Train-test split (80/20)
   - Trained a Random Forest Classifier with 100 trees
3. **Evaluation**
   - Achieved **96.94% accuracy**
   - Confusion matrix and feature importance analysis confirm strong performance

## Usage
To run the model:
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python phishing_detector.py
   ```
4. Use the saved model to make predictions on new URL data

## Technologies
- Python (pandas, scikit-learn, matplotlib)
- Random Forest (ensemble method)

## Improvements
- Real-time classification using streamlit or Flask
- Integration with browser extensions
- Use NLP to analyze website content

---
Created by: Krzysztof Stanisz  
Date: January 2025
