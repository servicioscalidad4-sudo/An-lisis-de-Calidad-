import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Ejecutivo - Renacer", layout="wide")

# Colores Corporativos
COLOR_GOLD = "#c8a951"
COLOR_DARK = "#1a0e2a"

st.markdown(f"""
    <style>
    .main {{ background-color: #f4f7f6; }}
    .stMetric {{ background-color: white; border-left: 5px solid {COLOR_GOLD}; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}
    </style>
    """, unsafe_allow_html=True)

# ... (Aquí va el resto de tu código que ya tienes) ...
# Asegúrate de usar los colores en los gráficos:
# fig_bar = px.bar(..., color_discrete_sequence=[COLOR_DARK])
