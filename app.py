import streamlit as st
from lista_hibrida import ListaHibrida as lh

st.set_page_config(page_title="Lista Híbrida - Estrutura de Dados", layout="wide")

st.title("Lista Híbrida com Busca e Reordenação")
st.caption("Trabalho de Estrutura de Dados — Busca Binária, Sequencial e Intercalação Automática")

if "lista" not in st.session_state:
    st.session_state.lista = lh()

lista: lh = st.session_state.lista
st.divider()

col_dir1, col_dir2 = st.columns(2)

with col_dir1:
    st.subheader("Inserir Chave na Cauda")
    nova_chave = st.number_input("Digite um número inteiro para inserir:", step=1, value=0, key="input_inserir")

    if st.button("Inserir na Cauda", type="primary"):
        sucesso, mensagem = lista.inserir(int(nova_chave))
        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)

with col_dir2:
    st.subheader("Buscar Chave")
    chave_busca = st.number_input("Digite um número inteiro para pesquisar:", step=1, value=0, key="input_buscar")

    if st.button("Realizar Busca"):
        resultado = lista.buscar(int(chave_busca))

        if resultado["encontrado"]:
            st.success(f"Encontrado! **Local:** {resultado['local']}")
        else:
            st.warning("Chave não encontrada na estrutura.")

        m1, m2, m3 = st.columns(3)
        m1.metric("Iterações Binárias", resultado["iteracoes_binaria"])
        m2.metric("Iterações Sequenciais", resultado["iteracoes_sequencial"])
        m3.metric("Total de Iterações", resultado["total_iteracoes"])

st.divider()

st.subheader("Estado Atual da Lista Híbrida")

col_est1, col_est2 = st.columns(2)

with col_est1:
    st.markdown(f"**Região Ordenada** ({len(lista.regiao_ordenada)} elementos)")
    st.json({
        "Primeiros 5 elementos": lista.regiao_ordenada[:5],
        "Últimos 5 elementos": lista.regiao_ordenada[-5:],
        "Total armazenado": len(lista.regiao_ordenada)
    })

with col_est2:
    st.markdown(f"**Cauda Não Ordenada** ({len(lista.cauda)}/10 elementos)")
    st.write(lista.cauda if lista.cauda else "*(Cauda vazia)*")
    st.progress(len(lista.cauda) / 10)

st.divider()

with st.expander("Componentes Streamlit Utilizados e Trechos de Código (Requisito 7)"):
    st.markdown("""
    Abaixo estão destacados os principais componentes visuais e de controle do Streamlit aplicados nesta solução:

    1. **`st.session_state`**: Utilizado para manter a instância da classe `ListaHibrida` persistente durante a navegação do usuário.
       ```python
       if "lista" not in st.session_state:
           st.session_state.lista = ListaHibrida()
       ```

    2. **`st.number_input`**: Entrada de dados numéricos para captação dos valores de inserção e busca.
       ```python
       nova_chave = st.number_input("Digite um número inteiro para inserir:", step=1)
       ```

    3. **`st.button`**: Botões de ação para disparar os métodos `inserir` e `buscar`.
       ```python
       if st.button("Inserir na Cauda"):
           ...
       ```

    4. **`st.metric`**: Exibição das métricas de desempenho da busca (iterações binárias, sequenciais e total).
       ```python
       st.metric("Iterações Binárias", resultado["iteracoes_binaria"])
       ```

    5. **`st.progress`**: Visualização gráfica do limite da cauda (0 a 10 elementos) antes da intercalação automática.
       ```python
       st.progress(len(lista.cauda) / 10)
       ```

    6. **`st.columns`**: Divisão da interface em colunas para organização dos formulários e exibição paralela de dados.
       ```python
       col1, col2 = st.columns(2)
       ```
    """)