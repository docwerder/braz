
#% Script for getting the df of the choosen PS

import pandas as pd
import math
import sys
# from IPy# thon.core.display import display, HTML

#display(HTML("<style>.container {width:90% !important; }</style>"))

sys.path.append('/Users/joerg/repos/braz')
from utilities_functions import scan_func

pd.set_option('display.max_rows', None)

class dfActualPS():
    def __init__(self, actual_ps, brazzers_site_ps, max_pagelength, csv_file_final):
        super().__init__()
        self.brazzers_site_ps = brazzers_site_ps
        self.max_pagelength = max_pagelength
        self.actual_ps = actual_ps
        self.csv_file_final = csv_file_final
        self.lst_max_pagelength = [self.max_pagelength]
        self.df_curent_final = pd.DataFrame()
        self.titles_in_df_curent_final = pd.DataFrame()
        self.search_string = ""

            # self.actual_ps, self.brazzers_site_ps, max_page_len_of_chosen_model
    def createDfActualPS(self):
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
        self.df_chosen_ps = pd.DataFrame()
       
        # root_site = self.brazzers_site_ps
        for number in self.max_pagelength:        
            for page_nr in range(1, int(number) + 1):
                # print('page_nr: ', page_nr)
                actual_site = self.brazzers_site_ps + str(page_nr)
                # print('actual_site: ', actual_site)
                site_name = actual_site.split('/')[-5].replace('-', ' ').title()
                # print('site_name: ', site_name)
                
                db_page_tmp = scan_func(actual_site)
                #print('db_page_tmp: ', db_page_tmp)
                db_page_video = [i for i in db_page_tmp if i.startswith('/video/')]
                #print('db_page_video: ', db_page_video)
                db_page_ps = [i for i in db_page_tmp if i.startswith('/pornstar/')]
                # db_page_ps = [i for i in db_page_tmp if i.startswith('/models/')]
                ps1 = [h.split('/')[-1].replace('-','_') for h in db_page_ps[::2]]
                ps2 = [h.split('/')[-1].replace('-', '_') for h in db_page_ps[1::2]]
                
                title = [h.split('/')[-1].replace('-', '_') for h in db_page_video[::2]]
                
                site_tmp = [site_name]
                
                site = list(site_tmp) * 24
                                
                ps1_db = pd.DataFrame(ps1)
                ps2_db = pd.DataFrame(ps2)
                title_db = pd.DataFrame(title)
                site_db = pd.DataFrame(site)
                # print('Site_db: ', site_db)
                db_all_tmp = pd.concat([site_db, ps1_db, ps2_db, title_db], axis=1)
                custom_cols = ['Site', 'PS1', 'PS2', 'Title']
                #print('db_all_tmp: ', db_all_tmp)
                db_all_tmp.columns = custom_cols
                db_actual_site_name = pd.concat([db_actual_site_name, db_all_tmp])
                #print('db_all_tmp: ', db_all_tmp)
                # print('db_actual_site_name:\n ', db_actual_site_name)

            df_tmp = db_actual_site_name
            #print('db_actual_site_name: ', db_actual_site_name)
        
        df_chosen_model_tmp = db_actual_site_name
        #rint('df_chosen_model_tmp: ', df_chosen_model_tmp)
        self.df_chosen_ps = df_chosen_model_tmp[df_chosen_model_tmp['PS1'].notna()]
        #print('self.df_chosen_ps: ', self.df_chosen_ps)
        #print('count of titles: ', len(self.df_chosen_ps))
        return self.df_chosen_ps

    def getTitlesInDfFinal(self):
        print('self.actual_ps: ', self.actual_ps)
        self.df_curent_final = pd.read_csv(self.csv_file_final , index_col=[0])
        self.titles_in_df_curent_final = self.df_curent_final[(self.df_curent_final['PS1'] == self.actual_ps) |
                                                    (self.df_curent_final['PS2'] == self.actual_ps) |
                                                    (self.df_curent_final['PS3'] == self.actual_ps) |
                                                    (self.df_curent_final['PS4'] == self.actual_ps) |
                                                    (self.df_curent_final['PS5'] == self.actual_ps) |
                                                    (self.df_curent_final['PS6'] == self.actual_ps) |
                                                    (self.df_curent_final['PS7'] == self.actual_ps) |
                                                    (self.df_curent_final['PS8'] == self.actual_ps) |
                                                    (self.df_curent_final['PS9'] == self.actual_ps) |
                                                    (self.df_curent_final['PS10'] == self.actual_ps)][['Title']]
        print('== INFOS ABOUT THE TITLES: ==')
        print(f'Count of df_current_final: {len(self.df_curent_final)}')
        print(f'Current_titles in df_final of {self.actual_ps}: {len(self.titles_in_df_curent_final)}')
        print(f'Count of {self.actual_ps} of braz_sides: {len(self.df_chosen_ps)}')
        print(f'==')
        return self.titles_in_df_curent_final

    # dataFrame, chosen_model_df, search_string
    def getMissingTitles(self):
        zz = 0
        missing_titles = []
        print("Chosen PS: ", self.actual_ps)
        for single_title in self.df_chosen_ps['Title']:
            found_titles = self.search_titles(self.titles_in_df_curent_final, single_title)
            #print('found_titles: ', found_titles)
            if found_titles.empty:
                missing_titles.append(single_title)
            sttr = f"nr: {zz}  Title: {single_title} DF empty: {found_titles.empty}"
            #print(sttr)
            zz = zz+1
        return missing_titles
    # search_string
    def search_titles(self, titles_in_df_curent_final, search_string):
        self.titles_in_df_curent_final = titles_in_df_curent_final
        self.search_string = search_string
        mask = (self.titles_in_df_curent_final.applymap(lambda x: isinstance(x, str) and self.search_string in x)).any(1)
        #print('mask: ', dataFrame[mask]['Title'])
        return self.titles_in_df_curent_final[mask]#['Title']