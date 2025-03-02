import streamlit as st
import time 


#setting the page

st.set_page_config(page_title="My Unit convertor", page_icon="🔄" , layout = "centered")

st.title("UNIT CONVERTOR")


# sidebar
unit_type = st.sidebar.radio("Select unit type",["Length","Weight","Temperature","Currency"]) # this set up the sidebar with differnt conversions
#conversion mechanism
def convert (value,from_unit,to_unit,conversion_dict):
    return value * conversion_dict[from_unit] / conversion_dict[to_unit]


#length

def length_converter():
    st.subheader("📏 Length Converter")
    units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Yards": 0.9144, "Feet": 0.3048}
    
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", units.keys())
    to_unit = st.selectbox("To", units.keys())
    
    if st.button("Convert", use_container_width=True):
        with st.spinner("Converting..."):
            time.sleep(1)
            result = convert(value, from_unit, to_unit, units)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")


#weight

def weight_convertor():
    st.subheader("Weight Converter")
    units = {"Kilograms":1,"Grams":0.01,"Pounds":0.45359}

    value = st.number_input("Enter Value",min_value=0.0,format="%.4f")
    from_unit = st.selectbox("From",units.keys())
    to_unit = st.selectbox("To",units.keys())


    if st.button("convert",use_container_width=True):
        with st.spinner("Converting..."):
            time.sleep(1)
            result = convert(value,from_unit,to_unit,units)
            st.success(f"{value}{from_unit}= {result:.4f}{to_unit}")

# Temperature

def temperature_converter():
    st.subheader("Temperature Converter")
    scales = ["Celsius","Farheniet","Kelvin"]
    
    value = st.number_input("Enter Value", format="%.2f")
    from_unit = st.selectbox("From", scales)
    to_unit = st.selectbox("To", scales)

    if st.button("Convert", use_container_width=True):
        with st.spinner("Converting..."):
            time.sleep(1)
            if from_unit == to_unit:
                result = value
            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")






# currency convertor
# Converts using the latest rates right now!
def currency_converter():
    st.subheader("Currency Convertor")
    currencies = {"USD":1,"EUR":0.91,"GBP":0.78,"INR":83.0,"JPY":150.0}
    value = st.number_input("Enter Value",min_value=0.0,format="%.2f")
    to_currency = st.selectbox("To",currencies.keys())
    from_currency = st.selectbox("from",currencies.keys())



    if st.button("Convert",use_container_width=True):
        with st.spinner("Fetching the latest rates..."):
            time.sleep(1)
            result = convert(value,from_currency,to_currency,currencies)
            st.success(f"{value}{from_currency}= {result:.2f}{to_currency}")

# style_metric_cards()



#conversion type

if unit_type == "Length":
    length_converter()
elif unit_type =="Weight":
    weight_convertor()
elif unit_type == "Temperature":
    temperature_converter()
elif unit_type=="Currency":
    currency_converter()
