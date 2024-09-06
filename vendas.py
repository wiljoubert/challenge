import pandas as pd


# Função principal para executar o processamento
def processa():

    arquivo_csv = 'vendas.csv'
    chunksize = 1000

     # Inicializar um DataFrame vazio para armazenar os dados processados
    df_list = []

    # Ler o arquivo CSV em chunks
    for chunk in pd.read_csv(arquivo_csv, chunksize=chunksize):
        df_list.append(chunk)

    # Concatenar todos os chunks em um único DataFrame
    df = pd.concat(df_list, ignore_index=True)

    
    # Perguntas sobre os dados
    # 1 - Identifique o produto mais vendido em termos de quantidade e canal.
    grouped = df.groupby(['Item Type', 'Sales Channel'])['Units Sold'].sum().reset_index()
    most_sold_product = grouped.loc[grouped['Units Sold'].idxmax()]
    print("### Produto mais vendido por quantidade e canal")
    print(most_sold_product)

    # 2 - Determine qual pais e regiao teve o maior volume de vendas (em valor).
    grouped = df.groupby(['Country', 'Region'])['Total Profit'].sum().reset_index()
    max_sales = grouped.loc[grouped['Total Profit'].idxmax()]
    print("### Pais e regiao com maior volume de vendas")
    print(max_sales)

    # 3 - Calcule a media de vendas mensais por produto, considerando o periodo dos dados disponiveis.
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.to_period('M')
    media_vendas_mensais = df.groupby(['Item Type', 'Month'])['Units Sold'].mean().reset_index()
    print("### Media mensal por produto")
    print(media_vendas_mensais)


if __name__ == '__main__':
    processa()
