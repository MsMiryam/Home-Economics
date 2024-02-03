import streamlit as st
import pandas as pd
import random

# Load your grocery inventory data (e.g., from a CSV file or database)
# grocery_data = pd.read_csv('grocery_inventory.csv')

# Sample inventory data (replace with your data)
grocery_data = pd.DataFrame({
    'Item': ['Apples', 'Bananas', 'Carrots', 'Chicken', 'Spinach', 'Rice'],
    'Quantity': [20, 15, 10, 5, 7, 25]
})

# Function to generate a random meal plan (replace with your algorithm)
def generate_meal_plan(num_days, dietary_restrictions):
    meal_plan = []
    for day in range(num_days):
        breakfast = random.choice(grocery_data['Item'])
        lunch = random.choice(grocery_data['Item'])
        dinner = random.choice(grocery_data['Item'])
        meal_plan.append({
            'Day': day + 1,
            'Breakfast': breakfast,
            'Lunch': lunch,
            'Dinner': dinner
        })
    return pd.DataFrame(meal_plan)

# Streamlit Interface
st.title("Grocery-Based Meal Planner")

# User Input
num_days = st.slider("Select the number of days to plan for:", 1, 7, 7)
dietary_restrictions = st.multiselect("Select dietary restrictions:", ["Vegetarian", "Vegan", "Gluten-Free"])

# Generate Meal Plan Button
if st.button("Generate Meal Plan"):
    meal_plan = generate_meal_plan(num_days, dietary_restrictions)
    
    # Display the Meal Plan
    st.header("Meal Plan for the Week")
    st.table(meal_plan)

# Show Grocery Inventory
st.header("Available Grocery Inventory")
st.table(grocery_data)

# Deployment (for sharing with others)
# Deploy the app to a hosting platform of your choice
