import os
import pandas as pd
from tabulate import tabulate

final_db = pd.DataFrame()
db_tmp = pd.DataFrame()

for root, dirs, files in sorted(os.walk(os.getcwd())):
   for name in sorted(files):

       complete_file_name = os.path.join(root, name)
       print('complete_file_name: ', complete_file_name)
       if ".DS_Store" in complete_file_name:
           continue
       elif "original_scanned" in complete_file_name:
           print('goin')
           continue
       elif "db_final_complete" in complete_file_name:
           continue
       elif ".ipynb" in complete_file_name:
           continue
       elif ".py" in complete_file_name:
           continue
       else:
           # print('file: ', complete_file_name)
           print('complete_file: ', complete_file_name)
           db_tmp = pd.read_csv(complete_file_name, index_col=0)
           #print('db_tmp: ', db_tmp)
           final_db = pd.concat([final_db, db_tmp])
print('final_db: ', final_db)
print('debug2')
final_db = final_db.reset_index()
del final_db['index']
# print(tabulate(final_db, headers='keys', tablefmt='psql'))

root = os.getcwd()
save_path = os.path.join(root, 'scanned_site_content')
save_final_file = os.path.join(root, 'db_final_complete.csv')
#print('save_file: ', save_final_file)

#ggg = final_db[final_db['Site'] == 'nan']['Site']
print('cols.. ', final_db['Site'].unique())
final_db.to_csv(save_final_file)
#print(tabulate(final_db, headers='keys', tablefmt='psql'))