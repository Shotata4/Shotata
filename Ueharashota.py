import numpy as np
from scipy import optimize
import streamlit as st
st.sidebar.title("最適化パラメーター")

def objective_function(x):
    return x**2 + x

x_min = st.sidebar.number_input("xの最小化", value=10.0, step=0.1)
x_max = st.sidebar.number_input("xの最大化", value=10.0, step=0.1)

algorithm = st.sidebar.selectbox("最適化アルゴリズム", ["BFGS", "L-BFGS-B", "CG", "Newton-CG", "TNC"])

if st.sidebar.button("最適化実行"):
    result = optimize.minimize(objective_function, x0=0.0, bounds=[(x_min,x_max)], method=algorithm)

    st.write(result)