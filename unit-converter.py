import streamlit as st

# Title of the app
st.title("Unit Converter App")

# Create a sidebar for selection of the unit
option = st.sidebar.selectbox(
    "Select the type of conversion:",
    ["Length", "Weight", "Temperature"]
)

# For Length Conversion
if option == "Length":
    st.header("Length Converter")
    
    length_units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards"]
    
    # Get user input for length
    value = st.number_input("Enter value:", min_value=0.0, step=0.1)
    from_unit = st.selectbox("From unit:", length_units)
    to_unit = st.selectbox("To unit:", length_units)
    
    # Convert length units
    if from_unit == "meters":
        conversion_factors = {
            "meters": 1,
            "kilometers": 0.001,
            "centimeters": 100,
            "millimeters": 1000,
            "miles": 0.000621371,
            "yards": 1.09361
        }
    elif from_unit == "kilometers":
        conversion_factors = {
            "meters": 1000,
            "kilometers": 1,
            "centimeters": 100000,
            "millimeters": 1000000,
            "miles": 0.621371,
            "yards": 1093.61
        }
    # Add conversions for other units similarly...
    
    result = value * conversion_factors[to_unit]
    st.write(f"{value} {from_unit} is equal to {result} {to_unit}.")

# For Weight Conversion
elif option == "Weight":
    st.header("Weight Converter")
    
    weight_units = ["grams", "kilograms", "pounds", "ounces"]
    
    # Get user input for weight
    value = st.number_input("Enter value:", min_value=0.0, step=0.1)
    from_unit = st.selectbox("From unit:", weight_units)
    to_unit = st.selectbox("To unit:", weight_units)
    
    # Convert weight units
    if from_unit == "grams":
        conversion_factors = {
            "grams": 1,
            "kilograms": 0.001,
            "pounds": 0.00220462,
            "ounces": 0.035274
        }
    elif from_unit == "kilograms":
        conversion_factors = {
            "grams": 1000,
            "kilograms": 1,
            "pounds": 2.20462,
            "ounces": 35.274
        }
    # Add conversions for other units similarly...
    
    result = value * conversion_factors[to_unit]
    st.write(f"{value} {from_unit} is equal to {result} {to_unit}.")

# For Temperature Conversion
elif option == "Temperature":
    st.header("Temperature Converter")
    
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    
    # Get user input for temperature
    value = st.number_input("Enter value:", min_value=-273.15, step=0.1)
    from_unit = st.selectbox("From unit:", temperature_units)
    to_unit = st.selectbox("To unit:", temperature_units)
    
    # Convert temperature units
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif to_unit == "Kelvin":
            result = value + 273.15
        else:
            result = value
    
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        else:
            result = value
    
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = value - 273.15
        elif to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
    
    st.write(f"{value} {from_unit} is equal to {result} {to_unit}.")

