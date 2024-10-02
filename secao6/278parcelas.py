from datetime import datetime
from dateutil.relativedelta import relativedelta

DATA_INICIO = datetime.strptime("20/12/2020", "%d/%m/%Y")
EMPRESTIMO = 1_000_000
MESES_PARCELA = 5*12

for i in range(1, MESES_PARCELA+1):
    DATA_INICIO = DATA_INICIO + relativedelta(months=+1)
    print(f'Parcela {i}x. Referente a: {DATA_INICIO.strftime("%m/%Y")}. O valor é de R$ {EMPRESTIMO/MESES_PARCELA:.2f}')
