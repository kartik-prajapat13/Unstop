# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load sample data (replace this with actual data from the university's system)
sample_data = pd.DataFrame({
    'StudentID': [1, 2, 3, 4, 5],
    'GPA': [3.8, 3.5, 4.0, 3.2, 3.9],
    'Credits Completed': [90, 85, 120, 60, 110],
    'Courses Enrolled': [4, 3, 5, 2, 4]
})

# Sidebar for user input (replace with actual interactive elements)
st.sidebar.title('User Input')
selected_metric = st.sidebar.selectbox('Select Metric:', ['GPA', 'Credits Completed', 'Courses Enrolled'])

# Display main content
st.title('University of South Florida - Student Analytics Dashboard')
st.write('Visualizing student data for better insights.')

# Display selected metric visualization
plt.figure(figsize=(8, 6))
plt.bar(sample_data['StudentID'], sample_data[selected_metric])
plt.xlabel('Student ID')
plt.ylabel(selected_metric)
plt.title(f'{selected_metric} Distribution Across Students')
st.pyplot(plt)

# Additional information or analysis (replace with actual insights)
st.write('Insight 1: Average GPA is 3.68')
st.write('Insight 2: Total credits completed range from 60 to 120')
st.write('Insight 3: Most students are enrolled in 4 courses')

# Code Example (replace with actual code snippets)
st.markdown('**Code Example:**')
st.code("""
# Your code snippet here
""")

# Q&A Section (replace with actual Q&A interaction)
st.title('Questions & Answers')
st.write('Open the floor for questions and discussions.')
