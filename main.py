#Biblioteca do pandas para ler csv e transformar em dataframe
import pandas as pd

#Biblioteca do ydata_profiling para gerar o relatório de perfil dos dados
from ydata_profiling import ProfileReport

#Ler o arquivo csv e transformar em dataframe (Usando um método da classe pandas que faz a leitura do arquivo csv)
df = pd.read_csv('data.csv')

#Gerar o relatório de perfil dos dados
profile = ProfileReport(df, title="Profiling Report") 

#Exibir o relatório de perfil dos dados
profile.to_file("relatorio_perfil_dados.html")


