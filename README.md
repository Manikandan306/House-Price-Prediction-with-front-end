House Price Prediction Web App
Overview
This is a beginner-level data science project that predicts house prices using a linear regression model. The project includes a static web interface hosted on GitHub Pages, allowing users to input house details (square footage, bedrooms, bathrooms) and get price predictions computed client-side using JavaScript. The model was trained in Python using scikit-learn and a small dataset, with coefficients hardcoded in the front-end for simplicity.
This project demonstrates skills in:

Data preprocessing and machine learning with Python and scikit-learn.
Web development with HTML, CSS, and JavaScript.
Deploying a static website on GitHub Pages.

Live Demo
[Link to GitHub Pages site, e.g., https://your-username.github.io/house-price-prediction\]
Project Structure
house-price-prediction/
├── index.html          # Static web interface for predictions
├── main.py            # Python script to train model and extract coefficients
├── house_prices.csv   # Dataset for training the model
├── requirements.txt   # Python dependencies for main.py
├── README.md          # Project documentation

How It Works

Model Training (Local):

The main.py script trains a linear regression model on house_prices.csv, which contains house features (square footage, bedrooms, bathrooms) and prices.
The script outputs the model’s coefficients and intercept, which are used in index.html for client-side predictions.


Web Interface:

The index.html file provides a form for users to input house details.
JavaScript computes the predicted price using the formula: price = intercept + (coef_square_feet * square_feet) + (coef_bedrooms * bedrooms) + (coef_bathrooms * bathrooms).
Input validation ensures valid and reasonable inputs, with warnings for values outside typical ranges.


Deployment:

The static index.html is hosted on GitHub Pages, making the app accessible online without a backend.



Setup Instructions (Local)

Clone the Repository:
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction


Install Python Dependencies (for training the model):
pip install -r requirements.txt


Train the Model and Extract Coefficients:

Run main.py:
python main.py


Copy the printed coefficients (e.g., coef_square_feet, coef_bedrooms, coef_bathrooms, intercept) into the JavaScript section of index.html.



Test Locally:

Open index.html in a browser to test the web interface.
Enter values (e.g., 2000 sq ft, 3 bedrooms, 2 bathrooms) and verify the prediction.



Deploying to GitHub Pages

Create a GitHub Repository:

Create a new repository (e.g., house-price-prediction) on GitHub.

Push all files to the repository:
git add .
git commit -m "Initial commit"
git push origin main




Enable GitHub Pages:

Go to the repository’s Settings tab on GitHub.
Scroll to Pages in the left panel.
Set the source to the main branch and root folder.
Save, and GitHub will provide a URL (e.g., https://your-username.github.io/house-price-prediction).


Test the Deployed Site:

Visit the GitHub Pages URL and test the prediction form.



Dataset
The house_prices.csv file contains 20 rows with columns:

square_feet: House size (1100–2200 sq ft).
bedrooms: Number of bedrooms (2–4).
bathrooms: Number of bathrooms (1–3).
price: House price in USD ($170,000–$420,000).

Predictions are most reliable for inputs within these ranges. The web interface warns users if inputs are outside typical ranges (500–5000 sq ft, 0–10 bedrooms/bathrooms).
Limitations

The linear regression model assumes a linear relationship, so predictions for extreme inputs (e.g., 100000 sq ft) may be unreliable.
The model is static (coefficients are hardcoded). To update the model, retrain main.py and update index.html with new coefficients.

Future Improvements

Add a visualization of the training data or prediction trends.
Use a more complex model (e.g., Random Forest) with ONNX.js for client-side execution.
Integrate with a backend API for dynamic model updates.

Author
[Your Name][Optional: Add GitHub/LinkedIn for resume purposes]z