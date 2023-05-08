import streamlit as st

st.title("Tabel Periodik")

tombol = st.button("Na")

if tombol:
    nilai_arna = 23
    st.success(f"Ar Na adalah {nilai_arna}")
	
hitung = st.button("Na")

if hitung:
    nilai_arfe = 56
    st.success(f"Ar Fe adalah {nilai_arfe}")