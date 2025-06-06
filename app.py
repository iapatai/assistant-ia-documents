import streamlit as st
import pandas as pd
import docx
import PyPDF2

st.set_page_config(page_title="Assistant IA Documentaire", layout="wide")
st.title("📊 Assistant IA - Analyse de fichiers")

uploaded_file = st.file_uploader("📁 Dépose un fichier (Excel, Word, PDF)", type=["xlsx", "xls", "docx", "pdf"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]
    
    if file_type in ["xlsx", "xls"]:
        df = pd.read_excel(uploaded_file)
        st.subheader("Aperçu du fichier Excel")
        st.dataframe(df)
        st.write("Colonnes disponibles :", df.columns.tolist())

    elif file_type == "docx":
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        st.subheader("Contenu du fichier Word")
        st.text_area("Texte extrait", text, height=300)

    elif file_type == "pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = "\n".join(page.extract_text() or "" for page in pdf_reader.pages)
        st.subheader("Contenu du fichier PDF")
        st.text_area("Texte extrait", text, height=300)

    else:
        st.warning("Format de fichier non pris en charge.")
