import numpy as np
from scipy import optimize

import streamlit as st
st.sidebar.title("最適化パラメーター")

#最適化する関数
def objective_function(x):
    return x**2 + x

#最適化する関数の範囲
x_min = st.sidebar.number_input("xの最小化", value=10.0, step=0.1)
x_max = st.sidebar.number_input("xの最大化", value=10.0, step=0.1)

#最適化のアルゴリズムの選択
algorithm = st.sidebar.selectbox("最適化アルゴリズム", ["BFGS", "L-BFGS-B", "CG", "Newton-CG", "TNC"])

#最適化実行ボタン
if st.sidebar.button("最適化実行"):
    #最適化
    result = optimize.minimize(objective_function, x0=0.0, bounds=[(x_min,x_max)], method=algorithm)

    #結果を表示
    st.write(result)

    