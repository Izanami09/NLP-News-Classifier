# News Classification NLP Project

This project involves a Natural Language Processing (NLP) model for classifying news articles into different categories such as sports, business, etc. The model is trained and serialized using joblib, and the project is designed to be deployed using Streamlit.

## Features

- Classifies news articles into predefined categories.
- Utilizes a Logistic Regression model for classification.
- Serialized model file (`lr_model.gz`) for easy loading and prediction.
- Streamlit app for interactive news classification.

## Installation

To get started with this project, you'll need to have Python installed on your computer. It's recommended to use a virtual environment to manage dependencies.

1. Clone the repository:

   ```bash
   git clone https://github.com/Izanami09/NLP-News-Classifier.git
   cd <your-repository-directory>

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv

3. Activate the virtual environment:
    - On macOs and Linux:

    ```bash
    source venv/bin/activate 

    - On windows

    ```bash
    .\venv\Scripts\activate

4. Install the required packages

    ```bash
    pip install -r requirement.txt

## 3 🎮 Usage

### Run the Streamlit App
   streamlit run app.py
- Then open the URL provided in your terminal (usually http://localhost:8501) to access the app in your browser.

## 📂 Project Structure

    nlp-news-classifier/
    │
    ├── app/gui.py                                      
    ├── model/lr_model.gz                               
    ├── notebooks/news.ipynb, nltk.ipynb                
    ├── requirements.txt
    |-- lr_model.joblib
    └── README.md                                       

## 🧪 Tech Stack

* Python 3.9+
* Streamlit
* Scikit-learn
* NLTK
* Pandas
* NumPy
* Matplotlib

## 📈 Screenshots


## 🤝 Contributing

Fork this repo 🍴
- Create a branch:
    ```bash
    git checkout -b feature-name
    Make changes and commit:
    git commit -m "Added feature"
    Push to GitHub:
    git push origin feature-name
    Open a Pull Request 🚀

## 📜 License

This project is licensed under the MIT License.

## 📬 Contact

* Rohan Shah
* 📧 rohan123.rs8@gmail.com
* 🌐 LinkedIn
* 🐙 GitHub

* Made with ❤️ using Streamlit & Machine Learning

