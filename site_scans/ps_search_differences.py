import pandas as pd
import math
import sys
from tabulate import tabulate

# Read the relevant csv-files as dataframes.
df_my_db = pd.read_csv('df_final_my_db_py_21_04_2022.csv', index_col=[0])
df_final = pd.read_csv('df_final_inklusive_ms.csv', index_col=[0])



# First try: Define the PS manually...

difference_titles_db = []
ps_col = []
total_title_list = pd.DataFrame()
db_total_difference = pd.DataFrame()

ps_db = ['Krissy Lynn', 'Nicolette Shea', 'Rebecca More', 'Ava Addams', 'Jasmine Jae']

for ps_name in ps_db:
    print(ps_name)

    ps_name_for_df_final = ps_name.lower().replace(' ', '_')  # firstname_surname
    ps_name_for_my_db = ps_name      # Firstname Surname

    title_string = ''

# Evaluate the occurance of the ps_name the the df_final and in my_db

    ps_title_in_my_db = df_my_db[df_my_db['PS1'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS2'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS3'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS4'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS5'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS6'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS7'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS8'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS9'].str.contains(ps_name_for_my_db) |
                                 df_my_db['PS10'].str.contains(ps_name_for_my_db) &
                                 df_my_db['Title'].str.contains(title_string)]
#print(tabulate(ps_title_in_my_db, headers='keys', tablefmt='psql'))
    number_ps_title_in_my_db = len(ps_title_in_my_db)
    print('Titles of {} in my_db: {} '.format(ps_name, number_ps_title_in_my_db ))

# Search titles of selected PS in df_final:
# There are only two PS columns..
    ps_title_in_df_final = df_final[df_final['PS1'].str.contains(ps_name_for_df_final) |
                                 df_final['PS2'].str.contains(ps_name_for_df_final) &
                                 df_final['Title'].str.contains(title_string)]

    number_ps_title_in_df_final = len(ps_title_in_df_final)
    print('Titles of {} in df_final: {} '.format(ps_name, number_ps_title_in_df_final ))

# Extract the two title-columns of df_final and my_db to get the difference-titles,
# which are not in my_db

    ps_name_title_only_in_my_db = ['_'.join(x.split('_')[:-1]) for x in ps_title_in_my_db['Title']]
    ps_name_title_only_in_df_final = [x for x in ps_title_in_df_final['Title']]

#print(ps_name_title_only_in_df_final)
#print(ps_name_title_only_in_my_db)

    difference_title_list = list(set(ps_name_title_only_in_df_final).difference(ps_name_title_only_in_my_db))
    total_title_list = pd.DataFrame(difference_title_list)
    db_total_difference = pd.concat([db_total_difference, total_title_list], axis=1)




    # difference_titles_db.append(difference_title_list)
#print(difference_titles_db)
#print(type(difference_titles_db))

    #total_title_list.column = ps_name
    #total_db = {'PS': ps_name}
    print('numbers difference-titles: ' ,  len(list(difference_title_list)))

db_total_difference.columns = ps_db
print(tabulate(db_total_difference, headers='keys', tablefmt='psql'))