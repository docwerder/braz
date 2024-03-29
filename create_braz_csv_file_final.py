import pandas as pd
import os
import glob
import sys  
sys.path.append('/Users/joerg/repos/development/utilities_functions')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
#from tabulate import tabulate

import numpy as np
#import qgrid
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from mnt_functions import mnt_WERDERNAS
from mnt_functions import mnt_WERDERNAS2
from mnt_functions import mnt_WERDERNASX
from mnt_functions import mnt_WERDERNAS2X
mnt_WERDERNAS()
mnt_WERDERNAS2()
mnt_WERDERNASX()
mnt_WERDERNAS2X()




bra_dir = '/Volumes/WERDERNASX/VIDEOSX/BRAZZERS'
bra_dir_2 = '/Volumes/WERDERNAS2X/VIDEOS2X/BRAZZERS2'

# Go through the root folder
# With next we get the folder structure under the
# root folder

next(os.walk(bra_dir))
bra_dir_db=sorted(next(os.walk(bra_dir))[1])

next(os.walk(bra_dir_2))
bra_dir_db_2 = sorted(next(os.walk(bra_dir_2))[1])

# with selected_dirs we will get the chosen folders for looping through...

selected_dirs = [bra_dir_db[i] for i in [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                            15, 16, 17, 19, 20, 21, 23]]

selected_dirs_2 = [bra_dir_db_2[i] for i in [0, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22]]


selected_dirs_final = [selected_dirs, selected_dirs_2]


tmp_files_db = {}
df_final_tmp_2 = {} # formerly tmp_files_db_2
tmp_files_db_tmp = []
tmp_files_location_db = {}
tmp_files_location_db_tmp = []
tmp_files_site_tmp = []
tmp_files_site_db = {}

tmp_files_title_db = {}
tmp_files_title_db_2 = {}
tmp_files_title_db_tmp = []

link_files_tmp = []
link_files_db = {}


# going through the chosen folders selected_dirs
for lf in selected_dirs:
    # print(f'Scanning folder on WERDERNASX: {lf}')
    tmp_dir = os.path.join(bra_dir,lf)
    tmp_files = sorted(glob.glob(r'{}/*.mp4'.format(tmp_dir)))
    

    for lf_tmp in tmp_files:
        # print('lf_tmp: ', lf_tmp )
        site_string = lf_tmp.split('/')[-2]
        location = lf_tmp.split("/")[2]
        # site_with_ps = lf_tmp.split('/df_final_my_db_10_08_22')[-1].split('-')[0]
        site_with_ps = lf_tmp.split('/df_final_10_03_23')[-1].split('-')[0]
        
        ps_all = lf_tmp.split("-")[0].split(site_string + "_")[1]
        ps_single = ps_all.split("__")
        tmp_files_location_db_tmp.append(location)
        tmp_files_location_db = pd.DataFrame(tmp_files_location_db_tmp)
        tmp_files_db_tmp.append(ps_single)
        tmp_files_db = pd.DataFrame(tmp_files_db_tmp)
        tmp_files_site_tmp.append(site_string)
        tmp_files_site_db = pd.DataFrame(tmp_files_site_tmp)

        title_string = lf_tmp.split('/')[-1].split('-')[-1].split('.mp4')[0]
        tmp_files_title_db_tmp.append(title_string)
        tmp_files_title_db = pd.DataFrame(tmp_files_title_db_tmp)

        link_files_tmp.append(lf_tmp)
        link_files_db = pd.DataFrame(link_files_tmp)

    df_final_tmp_2 = pd.concat([tmp_files_site_db, tmp_files_db, tmp_files_location_db, tmp_files_title_db, link_files_db], axis=1)

# going through the chosen folders selected_dirs_2
for lf in selected_dirs_2:
    # print(f'Scanning folder on WERDERNAS2X: {lf}')
    # print('selected_dirs_2: ', selected_dirs_2)

    tmp_dir = os.path.join(bra_dir_2, lf)
   
    tmp_files = sorted(glob.glob(r'{}/*.mp4'.format(tmp_dir)))
    # print('tmp_files: ', tmp_files)
    for lf_tmp in tmp_files:
        
        site_string = lf_tmp.split('/')[-2]
        location = lf_tmp.split("/")[2]
        site_with_ps = lf_tmp.split('/')[-1].split('-')[0]
        
        ps_all = lf_tmp.split("-")[0].split(site_string + "_")[1]
        # print('ps_all: ', ps_all)

        ps_single = ps_all.split("__")
        # print('ps_single: ', ps_single)
        tmp_files_location_db_tmp.append(location)
        tmp_files_location_db = pd.DataFrame(tmp_files_location_db_tmp)
        tmp_files_db_tmp.append(ps_single)
        tmp_files_db = pd.DataFrame(tmp_files_db_tmp)
        tmp_files_site_tmp.append(site_string)
        tmp_files_site_db = pd.DataFrame(tmp_files_site_tmp)

        title_string = lf_tmp.split('/')[-1].split('-')[-1].split('.mp4')[0]
        tmp_files_title_db_tmp.append(title_string)
        tmp_files_title_db = pd.DataFrame(tmp_files_title_db_tmp)

        link_files_tmp.append(lf_tmp)
        link_files_db = pd.DataFrame(link_files_tmp)

    df_final_tmp_2 = pd.concat([tmp_files_site_db, tmp_files_db, tmp_files_location_db, tmp_files_title_db, link_files_db], axis=1)



df_final_tmp_2.columns = ['Site', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'PS6', 'PS7', 'PS8', 'PS9', 'PS10', 'Location', 'Title', 'Link']
df_final_tmp_2.loc[(df_final_tmp_2["PS2"].isnull()), "PS2"] = "no_name"
df_final_tmp_2.loc[(df_final_tmp_2["PS3"].isnull()), "PS3"] = "no_name"
df_final_tmp_2.loc[(df_final_tmp_2["PS4"].isnull()), "PS4"] = "no_name"
df_final_tmp_2.loc[(df_final_tmp_2["PS5"].isnull()), "PS5"] = "no_name"
df_final_tmp_2.loc[(df_final_tmp_2["PS6"].isnull()), "PS6"] = "no_name"
df_final_tmp_2.loc[(df_final_tmp_2["PS7"].isnull()), "PS7"] = "no_name"
df_final_tmp_2.loc[(df_final_tmp_2["PS8"].isnull()), "PS8"] = "no_name"
df_final_tmp_2.loc[(df_final_tmp_2["PS9"].isnull()), "PS9"] = "no_name"
df_final_tmp_2.loc[(df_final_tmp_2["PS10"].isnull()), "PS10"] = "no_name"
df_final_tmp_2['Site'] = df_final_tmp_2['Site'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS1'] = df_final_tmp_2['PS1'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS2'] = df_final_tmp_2['PS2'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS3'] = df_final_tmp_2['PS3'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS4'] = df_final_tmp_2['PS4'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS5'] = df_final_tmp_2['PS5'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS6'] = df_final_tmp_2['PS6'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS7'] = df_final_tmp_2['PS7'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS8'] = df_final_tmp_2['PS8'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS9'] = df_final_tmp_2['PS9'].map(lambda name:name.replace('_', ' ').title())
df_final_tmp_2['PS10'] = df_final_tmp_2['PS10'].map(lambda name:name.replace('_', ' ').title())

df_final_tmp_2 = df_final_tmp_2.fillna('No Name')
#custom_cols = ['Site', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'PS6', 'PS7', 'PS8', 'PS9', 'PS10', 'Title', 'Location', 'Link']
custom_cols_new = ['Site', 'PS1', 'PS2', 'PS3', 'Title', 'PS4', 'PS5', 'PS6', 'PS7', 'PS8', 'PS9', 'PS10', 'Location', 'Link'] 

df_bra_final = df_final_tmp_2[custom_cols_new]
#print('df_bra_final: \n ', df_bra_final)
#print(tabulate(df_bra_final, headers='keys', tablefmt='psql'))

# saved_csv_file = input('Enter the name of the csv_file: ')
saved_csv_file = r"/Users/joerg/repos/brazGUI/csv_data/df_final_13_07_23.csv"
df_bra_final.to_csv(saved_csv_file)