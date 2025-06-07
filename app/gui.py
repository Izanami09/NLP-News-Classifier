import streamlit as st
import joblib
import pandas as pd

# Set page title
st.set_page_config(page_title="News Categorizer", layout="wide")

# Load the saved pipeline
try:
    pipeline = joblib.load('lr_model.joblib')
except FileNotFoundError:
    st.error("Model file 'news_classifier_pipeline.joblib' not found. Please ensure the model file is in the same directory as this script.")
    st.stop()

def predict_category(text):
    """
    Make prediction using the loaded pipeline
    """
    try:
        # Make prediction
        prediction = pipeline.predict([text])
        return prediction[0]
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        return None

# App title and description
st.title("News Category Predictor")
st.write("Enter news text to predict its category")

# Create text input
news_text = st.text_area("Enter News Text", height=200)

# Create predict button
if st.button("Predict Category"):
    if news_text.strip() != "":
        # Make prediction
        prediction = predict_category(news_text)
        
        if prediction is not None:
            # Display prediction
            st.success(f"Predicted Category: {prediction}")
            
            # Display confidence scores if available
            try:
                probabilities = pipeline.predict_proba([news_text])[0]
                categories = pipeline.classes_
                
                # Create DataFrame for displaying probabilities
                prob_df = pd.DataFrame({
                    'Category': categories,
                    'Confidence': probabilities
                })
                prob_df = prob_df.sort_values('Confidence', ascending=False)
                
                # Display top 3 categories with probabilities
                st.write("Top Categories with Confidence Scores:")
                st.dataframe(prob_df.head(3).style.format({'Confidence': '{:.2%}'}))
                
            except AttributeError:
                # If predict_proba is not available
                st.info("Confidence scores are not available for this model")
    else:
        st.warning("Please enter some text to classify")