import streamlit as st
from PIL import Image

st.title('📰 Revisor Literário!')


st.image("topi/imagem/image_home.jpeg", width = 600)



st.markdown(
    """
    <div style='width: 600px; text-align: justify; font-size: 18px'>
        Descubra o poder da síntese: transforme artigos, textos e documentos em resumos 
    claros e objetivos com apenas um clique. Aqui você transforma textos complexos em resumos claros e objetivos. 
    Simplifique sua leitura, economize tempo e acesse o essencial de cada obra em instantes!
    </div>
    """,
    unsafe_allow_html=True
)

"\n"

st.subheader("PROPÓSITO DO SITE")
st.markdown("""
    <div style=' width: 600px; text-align: justify; font-size: 18px'>
    O Revisor Literário tem como objetivo oferecer uma ferramenta prática e eficiente para a extração e 
    organização de informações relevantes de artigos acadêmicos. Ideal para estudantes, professores e 
    pesquisadores, o site simplifica tarefas como a revisão de literatura e a análise de conteúdo em 
    pesquisas científicas. Com ele, é possível acessar rapidamente os dados essenciais de um artigo, 
    economizando tempo e tornando o processo de pesquisa mais produtivo.
        
    """,
    unsafe_allow_html=True
    )


"\n"
"\n"
"\n"

st.subheader(" RESUMO DO FUNCIONAMENTO")
st.markdown("""
    <div style=' width: 600px; text-align: justify; font-size: 18px'>
    O Revisor Literário, hospedado na plataforma Streamlit, foi desenvolvido para facilitar a análise 
    de artigos acadêmicos. Com uma interface intuitiva, permite que o usuário faça o upload de um artigo
    em formato PDF e, a partir disso, o sistema extrai automaticamente os principais elementos do conteúdo, 
    como: ano de publicação, título, autores, resumo, palavras-chave, problema de pesquisa, metodologia, 
    resultados, implicações e lacunas identificadas.
    Após a extração das informações, o usuário pode baixar os dados em formato CSV, tornando o 
    processo de organização e análise muito mais ágil e eficiente. Essa funcionalidade foi criada 
    para otimizar a revisão e o levantamento de dados acadêmicos, proporcionando uma solução rápida 
    e precisa para quem precisa gerenciar múltiplas fontes de informação de forma sistemática.
       </div>
    
    """,
    unsafe_allow_html=True
    )

