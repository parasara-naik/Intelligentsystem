import streamlit as st

# Set page configuration
st.set_page_config(
    page_title='Property Recommender System',
    page_icon="🏡",
    layout="wide",
)

# HTML styling for white box on black background
custom_html = """
<style>
  body {
    background-color: #000;
    color: #fff;
    font-family: 'Arial', sans-serif;
    padding: 20px;
  }
  h1, h2, h3 {
    color: #1E90FF; /* Header color */
  }
  .white-box {
    background-color: #fff;
    color: #000;
    padding: 20px;
    border-radius: 10px;
  }
</style>
"""

# Display HTML styling
st.markdown(custom_html, unsafe_allow_html=True)

# Main content
st.title('Property Recommender System')

st.markdown("""
## Overview

Our Recommender System is a simple two-level content-based system designed to assist you in finding the perfect property. The system takes into consideration both the nearby locations and various property features to offer personalized recommendations.

## Level 1: Nearby Location Filtering

At the first level, the system filters properties based on their proximity to your specified location. By entering your property name and estimated radius, you can quickly discover nearby properties. This initial filter simplifies your search by focusing on the geographic aspect.

## Level 2: Content-Based Recommendations

For a more refined search, our system uses advanced content-based recommendation techniques at the second level. It considers factors such as facilities, price, and nearby locations to provide tailored suggestions.

### Techniques Used:

- **Facility Matching:** Recommends properties based on similar facilities and amenities.

- **Price Comparison:** Takes into account your budget preferences.

- **Location Similarity:** Recommends properties in areas similar to your specified location.

### Methodology:

The system employs Cosine Similarity, a mathematical measure, to calculate the similarity between different properties. This ensures that the recommendations are not only relevant but also personalized to your preferences.

## How to Use

1. Click the "Search" button to initiate the recommendation process.

2. Enter your property name and specify your estimated radius for the initial location-based filtering.

3. Choose from the list of nearby properties generated.

4. For more refined suggestions, select a property, and the system will provide content-based recommendations based on facilities, price, and location similarity.

Explore the recommendations and find your dream property with ease!

Happy Property Hunting! 🏡🌟
""", unsafe_allow_html=True)
