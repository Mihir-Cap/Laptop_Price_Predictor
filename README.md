# Laptop Price Predictor

This is a web application built with Streamlit that predicts the price of a laptop based on its specifications. The application utilizes a machine learning pipeline trained on a dataset of laptop specifications.

## Setup

1. Clone the repository or download the code files.

2. Install the required dependencies by running the following command:

   ```
   pip install streamlit pandas scikit-learn
   ```

3. Run the script by executing the following command:

   ```
   streamlit run laptop_price_predictor.py
   ```

4. The application will launch in your default web browser.

## Usage

1. Select the brand, type, RAM, weight, touchscreen availability, IPS display, screen size, screen resolution, CPU, HDD size, SSD size, GPU, and operating system of the laptop.

2. Click on the "Predict Price" button to get the predicted price for the configured laptop.

## Model and Data

The machine learning model used for price prediction is loaded from a pickle file (`pipe.pkl`). The model has been trained on a dataset of laptop specifications and prices.

The dataset is stored in a pickle file (`df.pkl`) and contains information about various laptop features, such as brand, type, RAM, weight, display properties, CPU, storage, GPU, and operating system.

## Dependencies

- Streamlit: A Python library for building interactive web applications.
- Pandas: A data manipulation library for data analysis.
- scikit-learn: A machine learning library for building and evaluating models.

Feel free to use and modify this application for predicting laptop prices based on different features. If you have any questions or suggestions, please feel free to reach out. Enjoy predicting laptop prices!
