import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from pydantic import BaseModel
from openai import OpenAI

openai_api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)

st.title("📊 Upload e Análise de Artigo Científico")

# Texto de introdução
st.write("""
    Aqui você fará o upload de um artigo científico em formato PDF, e ele será analisado automaticamente.
    O resultado incluirá:
    - Ano em que foi escrito.
    - Título do artigo.
    - Nome dos autores.
    - Resumo do artigo.
    - Tags para pesquisa.
    - Metodologias utilizadas.
    - Resultados, implicações e lacunas identificadas.
""")

# Função para extrair texto de um PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Prompt para o modelo GPT
prompt = '''
    Você receberá o conteúdo de um artigo científico. Realize uma análise completa do artigo com base nos parâmetros abaixo:
    - Ano: ano em que o artigo foi publicado
    - Titulo: título do artigo
    - Autores: lista de strings contendo os nomes dos autores do artigo
    - Resumo: faça um resumo bem detalhado sobre o que se trata o artigo, faça algo bem objetivo, mas que fique bem explicado
    - Tags: lista de tags que podem ajudar na pesquisa do artigo
    - Metodologia: descrição resumida das metodologias aplicadas no artigo
    - Resultados: resumo do principal fato relevante do artigo
    - Implicacoes: análise das implicações e relevância dos resultados no contexto da área
    - Lacunas: identificação de lacunas no estudo ou oportunidades para futuras pesquisas
'''

# Modelo de estrutura do artigo
class ResumoArtigo(BaseModel):
    Ano: int
    Titulo: str
    Autores: list[str]
    Resumo: str
    Tags: list[str]
    Metodologia: str
    Resultados: str
    Implicacoes: str
    Lacunas: str

# Função para definir o modelo do gpt usado e para obter o resumo
def obter_resumo_artigo(texto):
    completacao = client.beta.chat.completions.parse(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": texto}
        ],
        response_format=ResumoArtigo,
    )

    return completacao.choices[0].message.parsed




# Upload do arquivo PDF no Streamlit
pdf_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if pdf_file:
    # Exibe mensagem de processamento
    st.write("Processando o arquivo PDF...")

    # Extrai o texto do PDF
    texto_extraido = extract_text_from_pdf(pdf_file)
    
    # Chama o modelo para análise
    with st.spinner("Analisando o conteúdo do artigo..."):
        resultado = obter_resumo_artigo(texto_extraido)
    
    # Exibe o resultado
    st.subheader("Resumo Estruturado do Artigo:")
    dados = pd.DataFrame(resultado)
    dados.columns = ['Variáveis', "Respostas"]
   
    st.table(dados)
    #st.dataframe(dados, hide_index=True)#


   
# Convertendo em csv 
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(dados)

        # Botão de download
    st.download_button( 
        label="Download data as CSV",
        data=csv,
        file_name="large_df.csv",
        mime="text/csv",
        icon="🚨"
        )

