from utilities_functions import scan_func
from utilities_functions import indices
import pandas as pd
import os
from tabulate import tabulate


number = range(1, 3)  # 3
page_content_db = pd.DataFrame()
page_number_db = {}
page_content_tmp = {}
page_columns = []

btas_db_1 = {}
ps1_db = pd.DataFrame()
ps2_db = {}
title_db = {}
db_sgs = pd.DataFrame()

for lf in number:
    actual_site = "https://www.brazzers.com/videos/site/95/shes-gonna-squirt/sortby/views/page/" + str(lf)
    site_name = actual_site.split('/')[-5].replace('-', ' ').title()
    #print('site_name: ', site_name)
    page_number = actual_site.split('/')[-2] + '/' + actual_site.split('/')[-1]
    page_number = page_number.replace('/', '_')
    db_page_tmp = scan_func(actual_site)
    db_page_video = [i for i in db_page_tmp if i.startswith('/video/')]
    #print('db_page_video: ', db_page_video)
    #print('len_db_page_video: ', len(db_page_video))

    db_page_ps = [i for i in db_page_tmp if i.startswith('/pornstar/')]
    ps1 = [h.split('/')[-1].replace('-','_') for h in db_page_ps[::2]]
    ps2 = [h.split('/')[-1].replace('-', '_') for h in db_page_ps[1::2]]
    title = [h.split('/')[-1].replace('-', '_') for h in db_page_video[::2]]
    site_tmp = [site_name]
    site = list(site_tmp) * 24

    ps1_db = pd.DataFrame(ps1)
    ps2_db = pd.DataFrame(ps2)
    title_db = pd.DataFrame(title)
    site_db = pd.DataFrame(site)
    # print('site_db: ', site_db)
    db_all_tmp = pd.concat([site_db, ps1_db, ps2_db, title_db], axis=1)
    custom_cols = ['Site', 'PS1', 'PS2', 'Title']
    db_all_tmp.columns = custom_cols
    db_sgs = pd.concat([db_sgs, db_all_tmp])

db_sgs = db_sgs.reset_index()
del db_sgs['index']

root = os.getcwd()
save_path = os.path.join(root, 'scanned_site_content')
save_file = os.path.join(save_path, 'db_sgs_site_content.csv')
print('save_file: ', save_file)

db_sgs_sliced = db_sgs.dropna()
print(tabulate(db_sgs_sliced, headers='keys', tablefmt='psql'))

db_sgs_sliced.to_csv(save_file)


