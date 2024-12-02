import streamlit as st
import streamlit.components.v1 as components

with open("pages/About me.html", 'r', encoding='utf-8') as html:
    source_code = html.read()

components.html(source_code,height=850)

