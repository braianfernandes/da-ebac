import pandas as pd
gasolina_df = pd.read_csv('gasolina.csv', sep=',')

import seaborn as sns
grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='pastel')

grafico.figure.savefig(fname='gasolina.png', bbox_inches='tight')