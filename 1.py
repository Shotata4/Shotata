import streamlit as st
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def newton_method(x0):
    x = x0
    for i in range(100):
        x = x - np.dot(np.linalg.inv(Hessian(x)), gradient(x))
    return x

def my_app():
    st.title("Newton Method Optimization")
    st.write("3D Surface Plot")
    x0 = st.number_input("Enter Initial x value")
    y0 = st.number_input("Enter Initial y value")
    xmin = st.number_input("Enter Minimum x value")
    xmax = st.number_input("Enter Maximum x value")
    ymin = st.number_input("Enter Minimum y value")
    ymax = st.number_input("Enter Maximum y value")
    x = np.linspace(xmin, xmax, 100)
    y = np.linspace(ymin, ymax, 100)
    X, Y = np.meshgrid(x, y)
    Z = Rosenbrock(X,Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    if st.button("Minimize"):
        x0 = newton_method(np.array([x0, y0]))
        st.write("Minimum point is at:", x0)

my_app()