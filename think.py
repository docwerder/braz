from tabulate import tabulate
import pandas as pd

df = pd.DataFrame({'col_two' : [0.0001, 1e-005 , 1e-006, 1e-007],
                   'column_3' : ['ABCD', 'ABCD', 'long string', 'ABCD']})

print(tabulate(df, headers='keys', tablefmt='psql'))