import streamlit as st

st.set_page_config(
    page_title = "Revisão literária",
    page_icon = "🗞️",
    layout = "centered",
    initial_sidebar_state = "expanded")



paginas = {
    "Home":[
    st.Page("topi/Paginas/home.py", 
        title = "🏠 Página Inicial", icon = "", default = True)
    ],
    "Revisões": [
    st.Page("topi/Paginas/tes.py", 
        title = "📰 Upload e resultado", icon = "")  
    ]

}

pg = st.navigation(paginas)
pg.run() 
