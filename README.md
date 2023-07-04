# Real-Estate-House-Price-Predictor

The real estate price prediction website utilizes the Bangalore home prices dataset from Kaggle.com. The dataset is cleaned, outliers are detected and removed, and feature engineering techniques are applied to enhance the data. The primary model used for prediction is linear regression, implemented using the popular Scikit-learn (Sklearn) library.

The project incorporates various data science concepts, including data cleaning, feature engineering, model building, and hyperparameter tuning using techniques such as GridSearchCV. To evaluate the model's performance, K-fold cross-validation is employed.

To handle HTTP requests and provide accurate price predictions, a Python Flask server acts as the backend for the website. The Flask server utilizes the trained linear regression model to handle incoming requests and return the predicted prices.

The website's frontend is developed using HTML, CSS, and JavaScript, creating an intuitive user interface for users to input property details and obtain real estate price predictions. The project also showcases the integration of popular development tools such as Jupyter Notebook, Visual Studio Code, and PyCharm as IDEs for efficient model development and debugging.

**Installation**

Clone the repository to your local machine:

```
git clone https://github.com/your-username/real-estate-prediction-website.git
```
Navigate to the project directory:

```
cd real-estate-prediction-website
```
Create and activate a virtual environment (optional but recommended):

```
python3 -m venv env
source env/bin/activate
```

Install the required dependencies:

```
pip install -r requirements.txt
```

**Usage**

Start the Flask server:

```
python app.py
```

Open your web browser and go to http://localhost:5000 to access the Real Estate Price Prediction Website.

Enter the property details such as square footage and number of bedrooms.

Click on the "Predict" button to get the estimated price for the property.

**Project Structure**

The project structure is as follows:

app.py: Python Flask server script that handles HTTP requests and serves the website.
templates/index.html: HTML file containing the website's frontend code.
static/css/style.css: CSS file for styling the website.
static/js/script.js: JavaScript file for handling user interactions on the website.
data/bangalore_home_prices.csv: Dataset file containing Bangalore home prices.
model.pkl: Trained machine learning model saved as a pickle file.
notebooks/: Jupyter Notebook files containing the step-by-step process of building the model.

**Requirements**

To run the Real Estate Price Prediction Website, you need the following requirements:

Python 3.6 or higher
Flask 2.0.1 or higher
NumPy 1.21.0 or higher
Pandas 1.3.0 or higher
Matplotlib 3.4.2 or higher
Scikit-learn (Sklearn) 0.24.2 or higher
Jupyter Notebook (optional) for exploring the dataset and model development
Visual Studio Code, PyCharm, or any other preferred IDE for Python development
These dependencies are listed in the requirements.txt file. You can install them using the following command:
```
pip install -r requirements.txt
```

It is recommended to set up a virtual environment before installing the dependencies to keep your system environment clean. You can create a virtual environment using the following command:
```
python3 -m venv env
```

Activate the virtual environment:

For Windows:
```
env\Scripts\activate
```

For Linux/Mac:
```
source env/bin/activate
```


