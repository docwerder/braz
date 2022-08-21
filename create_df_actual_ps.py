# Script for creating the df of the actual PS..
import pandas as pd
from utilities_functions import scan_func

def create_df_actual_ps(actual_ps, chosen_model_brazz_site, max_page_len_of_chosen_model):
    page_content_db = pd.DataFrame()
    page_number_db = {}
    page_content_tmp = {}
    page_columns = []
    ps1_db = pd.DataFrame()
    ps2_db = {}
    title_db = {}
    db_actual_site_name = pd.DataFrame()
    db_final_tmp = pd.DataFrame()
    db_actual_site_name_sliced = pd.DataFrame()

       
        
    for root_site, number in zip(chosen_model_brazz_site[:], max_page_len_of_chosen_model):
        print('max..' , number)
    
        # max_page_number = math.ceil(int(number) / 24)
        
        for page_nr in range(1, int(number) + 1):
            print('page_nr: ', page_nr)
            actual_site = root_site + str(page_nr)
            site_name = actual_site.split('/')[-5].replace('-', ' ').title()
                
            #print('site_name: ', site_name)
            db_page_tmp = scan_func(actual_site)
            print('db_page_tmp: ', db_page_tmp)
            db_page_video = [i for i in db_page_tmp if i.startswith('/video/')]
            print('db_page_video: ', db_page_video)
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
            #print('Site_db: ', site_db)
            db_all_tmp = pd.concat([site_db, ps1_db, ps2_db, title_db], axis=1)
            custom_cols = ['Site', 'PS1', 'PS2', 'Title']
            #print('db_all_tmp: ', db_all_tmp)
            db_all_tmp.columns = custom_cols
            db_actual_site_name = pd.concat([db_actual_site_name, db_all_tmp])
            #print('db_all_tmp: ', db_all_tmp)
            #print('db_actual_site_name:\n ', db_actual_site_name)

        df_tmp = db_actual_site_name
        #print('db_actual_site_name: ', db_actual_site_name)
        
    df_chosen_model_tmp = db_actual_site_name
    chosen_model_df = df_chosen_model_tmp[df_chosen_model_tmp['PS1'].notna()]

    print('count of titles: ', len(chosen_model_df))
    return chosen_model_df