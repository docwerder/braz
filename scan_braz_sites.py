from bs4 import BeautifulSoup
import requests

video_string = "video"
ps_string = "pornstar"

title_db = []
ps_name_db = []
db_btaw = []
db_rws = []

# btaw_site = 'https://www.brazzers.com/site/71/big-tits-at-work/page/2'
big_tits_at_school_site = 'https://www.brazzers.com/videos/site/75/big-tits-at-school/sortby/views/page/2'
real_wife_stories_site = 'https://www.brazzers.com/videos/site/81/real-wife-stories/sortby/views/page/1'
doctor_adventures_site = 'https://www.brazzers.com/videos/site/62/doctor-adventures/sortby/views/page/1'
big_tits_in_uniform_site = 'https://www.brazzers.com/videos/site/89/big-tits-in-uniform/sortby/views/page/1'
big_wet_butts_site = 'https://www.brazzers.com/videos/site/65/big-wet-butts/sortby/views/page/1'
baby_got_boobs_site = 'https://www.brazzers.com/videos/site/66/baby-got-boobs/sortby/views/page/1'
mommy_got_boobs_site = 'https://www.brazzers.com/videos/site/67/mommy-got-boobs/sortby/views/page/1'
big_tits_at_work_site = 'https://www.brazzers.com/videos/site/71/big-tits-at-work/sortby/page/1'
pornstars_like_it_big_site = 'https://www.brazzers.com/videos/site/77/pornstars-like-it-big/sortby/page/1'
milf_like_it_big_site = 'https://www.brazzers.com/videos/site/78/milfs-like-it-big/sortby/page/1'
teens_like_it_big_site = 'https://www.brazzers.com/videos/site/80/teens-like-it-big/sortby/page/1'
big_butts_like_it_big_site = 'https://www.brazzers.com/videos/site/82/big-butts-like-it-big/sortby/page/1'
big_tits_in_sports_site = 'https://www.brazzers.com/videos/site/83/big-tits-in-sports/sortby/page/1'
brazzers_vault_site = 'https://www.brazzers.com/videos/site/84/brazzers-vault/sortby/page/1'
day_with_a_pornstar_site = 'https://www.brazzers.com/videos/site/87/day-with-a-pornstar/page/1'
zz_series_site = 'https://www.brazzers.com/videos/site/92/zz-series/sortby/page/1'
dirty_masseur_site = 'https://www.brazzers.com/videos/site/94/dirty-masseur/sortby/page/1'
shes_gonna_squirt_site = 'https://www.brazzers.com/videos/site/95/shes-gonna-squirt/sortby/page/1'
brazzers_extra_site = 'https://www.brazzers.com/videos/site/96/brazzers-exxtra/sortby/page/1'
cfnm_site = 'https://www.brazzers.com/videos/site/98/cfnm/sortby/page/1'
moms_in_control_site = 'https://www.brazzers.com/videos/site/99/moms-in-control/sortby/page/1'


btaw_site_tmp = requests.get(big_tits_at_school_site)
rws_site_tmp = requests.get(real_wife_stories_site)
dda_site_tmp = requests.get(doctor_adventures_site)
btiu_site_tmp = requests.get(big_tits_in_uniform_site)
bwb_site_tmp = requests.get(big_wet_butts_site)

btaw_soup_tmp = BeautifulSoup(btaw_site_tmp.content, 'html.parser')
rws_soup_tmp = BeautifulSoup(rws_site_tmp.content, 'html.parser')
dda_soup_tmp = BeautifulSoup(dda_site_tmp.content, 'html.parser')
btiu_soup_tmp = BeautifulSoup(btiu_site_tmp.content, 'html.parser')
bwb_soup_tmp = BeautifulSoup(bwb_site_tmp.content, 'html.parser')


print(f'scanning Site: {big_tits_at_school_site}, response: {btaw_site_tmp}')
print(f'scanning Site: {real_wife_stories_site}, response: {rws_site_tmp}')
print(f'scanning Site: {doctor_adventures_site}, response: {dda_site_tmp}')
print(f'scanning Site: {big_tits_in_uniform_site}, response: {btiu_site_tmp}')
print(f'scanning Site: {big_wet_butts_site}, response: {bwb_site_tmp}')

data_btaw_page = btaw_soup_tmp.find_all('a')
data_rws_page = rws_soup_tmp.find_all('a')

for link in data_btaw_page:
    db_btaw.append(link.get('href'))

for link in data_rws_page:
    db_rws.append(link.get('href'))


print('db_btaw: ', db_btaw)
print(db_rws)
