import streamlit as st
from pint import UnitRegistry

# Initialize Pint UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# Define a function to perform the conversion
def convert_units(value, from_unit, to_unit):
    try:
        quantity = Q_(value, from_unit)
        converted_quantity = quantity.to(to_unit)
        return converted_quantity.magnitude
    except:
        return None

# Streamlit App
st.set_page_config(page_title="Unit Converter", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
    }
    .stNumberInput>div>div>input {
        border: 2px solid #4CAF50;
        border-radius: 4px;
    }
    .stSelectbox>div>div>div {
        border: 2px solid #4CAF50;
        border-radius: 4px;
    }
    .stMarkdown h1 {
        color: #4CAF50;
    }
    .stMarkdown h2 {
        color: #4CAF50;
    }
    .stMarkdown h3 {
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("Unit Converter")
st.markdown("""
Convert any unit to another in real-time, Supports length, mass, temperature, volume, speed, and more.
""")

# Define supported units
unit_categories = {
    "Length": ["meter", "foot", "inch", "mile", "kilometer", "light_year"],
    "Mass": ["kilogram", "gram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "gallon", "cubic_meter", "cubic_inch"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour"],
    "Energy": ["joule", "calorie", "btu", "electron_volt"],
}

# Input fields
col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("Enter value:", value=1.0, step=0.1)

with col2:
    category = st.selectbox("Select unit category:", list(unit_categories.keys()))

with col3:
    from_unit = st.selectbox("Select from unit:", unit_categories[category])

# Target unit
target_unit = st.selectbox("Select target unit:", unit_categories[category])

# Convert button
if st.button("Convert"):
    result = convert_units(value, from_unit, target_unit)
    if result is not None:
        st.success(f"✅ *{value} {from_unit} = {result:.4f} {target_unit}*")
    else:
        st.error("❌ Invalid conversion. Please check your units.")

# Add references and explanations
st.markdown("""
### Supported Units and Examples
Here are some commonly used units and their categories:

#### Length
- *meter (m), **foot (ft), **inch (in), **mile (mi), **kilometer (km), **light_year (ly)*
- Example: 5 feet to meters, 10 kilometers to miles

#### Mass
- *kilogram (kg), **gram (g), **pound (lb), **ounce (oz), **ton (ton)*
- Example: 10 kg to pounds, 150 grams to ounces

#### Temperature
- *celsius (°C), **fahrenheit (°F), **kelvin (K)*
- Example: 32 celsius to fahrenheit, 100 kelvin to celsius

#### Volume
- *liter (L), **gallon (gal), **cubic_meter (m³), **cubic_inch (in³)*
- Example: 1 gallon to liters, 5 cubic meters to gallons

#### Speed
- *meter_per_second (m/s), **kilometer_per_hour (km/h), **mile_per_hour (mph)*
- Example: 60 mph to km/h, 10 m/s to km/h

#### Energy
- *joule (J), **calorie (cal), **btu (BTU), **electron_volt (eV)*
- Example: 1000 joules to calories, 500 BTU to joules

### How It Works
1. Enter a value.
2. Select the unit category (e.g., Length, Mass).
3. Select the source unit (e.g., feet).
4. Select the target unit (e.g., meters).
5. Click *Convert* to see the result.

""")