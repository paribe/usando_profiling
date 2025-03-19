# Importar as bibliotecas necessárias
import pandas as pd
from ydata_profiling import ProfileReport

# Criar um DataFrame a partir dos dados fornecidos
# Primeiro, vamos criar o arquivo CSV a partir dos dados que você forneceu
with open('dados.csv', 'w') as f:
    f.write("codigo;nome;cidade;sp\n")
    f.write("1;paulo;sao paulo;sp\n")
    f.write("2;davi;sao paulo;sp\n")
    f.write("3;relampago;sao paulo;sp\n")

# Ler o arquivo CSV
# Note que estamos usando o parâmetro sep=';' porque os dados estão separados por ponto e vírgula
df = pd.read_csv('dados.csv', sep=';')

# Exibir o DataFrame para verificar se os dados foram carregados corretamente
print("DataFrame carregado:")
print(df)
print("\n")

# Gerar o relatório de profile
profile = ProfileReport(df, title="Relatório de Análise Exploratória")

# Salvar o relatório como HTML
profile.to_file("relatorio_analise.html")

# Também é possível exibir um resumo mínimo no notebook
print("Resumo do relatório gerado:")
profile.to_notebook_iframe()