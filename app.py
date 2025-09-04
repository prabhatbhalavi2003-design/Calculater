
import streamlit as st
from src.addition import add
from src.subtraction import minus
from src.Divison import divide
from src.Multiplication import multiply
st.title("Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

option = st.selectbox("Mathamatical Operation", 
        ("Addition", "Subtraction",  "Divison", "Multiplication"))  

if st.button("Calculate"):
  if option == "Addition":
     result = add(a, b)
  if option == "Subtraction":
     result = minus(a, b)
  if option == "Multiplication":
     result = multiply(a, b)
  if option == "Divison":
     result = divide(a, b)
     

  st.write(f"The result is {result}")