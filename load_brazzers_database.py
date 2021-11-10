import pandas as pd
import os
import glob
import itertools


def load_bra_db(bra_dir):
    bra_dir = '/Volumes/WERDERNASX/VIDEOSX/BRAZZERS'
    bgb_dir = os.path.join(bra_dir, 'baby_got_boobs')
    bblib_dir = os.path.join(bra_dir, 'big_butts_like_it_big')
    btas_dir = os.path.join(bra_dir, 'big_tits_at_school')
    btaw_dir = os.path.join(bra_dir, 'big_tits_at_work')
    btis_dir = os.path.join(bra_dir, 'big_tits_in_sports')
    btiu_dir = os.path.join(bra_dir, 'big_tits_in_uniform')
    bwb_dir = os.path.join(bra_dir, 'big_wet_butts')
    bbex_dir = os.path.join(bra_dir, 'brazzers_extra')
    bzv_dir = os.path.join(bra_dir, 'brazzers_vault')
    ddm_dir = os.path.join(bra_dir, 'dirty_masseur')
    dda_dir = os.path.join(bra_dir, 'doctor_adventures')
    dwap_dir = os.path.join(bra_dir, 'day_with_a_pornstar')
    mlib_dir = os.path.join(bra_dir, 'milf_like_it_big')
    mgb_dir = os.path.join(bra_dir, 'mommy_got_boobs')
    mic_dir = os.path.join(bra_dir, 'moms_in_control')
    plib_dir = os.path.join(bra_dir, 'pornstars_like_it_big')
    tlib_dir = os.path.join(bra_dir, 'teens_like_it_big')
    rws_dir = os.path.join(bra_dir, 'real_wife_stories')
    sgs_dir = os.path.join(bra_dir, 'shes_gonna_squirt')
    cfnm_dir = os.path.join(bra_dir, 'clothed_female_naked_men')

    # Better Way:

    # Change the directory
    # os.chdir(bgb_dir)
    bgb_files = sorted(glob.glob(r'{}/*.mp4'.format(bgb_dir)))
    bblib_files = sorted(glob.glob(r'{}/*.mp4'.format(bblib_dir)))
    btas_files = sorted(glob.glob(r'{}/*.mp4'.format(btas_dir)))
    btaw_files = sorted(glob.glob(r'{}/*.mp4'.format(btaw_dir)))
    btis_files = sorted(glob.glob(r'{}/*.mp4'.format(btis_dir)))
    btiu_files = sorted(glob.glob(r'{}/*.mp4'.format(btiu_dir)))
    bwb_files = sorted(glob.glob(r'{}/*.mp4'.format(bwb_dir)))
    bbex_files = sorted(glob.glob(r'{}/*.mp4'.format(bbex_dir)))
    bzv_files = sorted(glob.glob(r'{}/*mp4'.format(bzv_dir)))
    dwap_files = sorted(glob.glob(r'{}/*.mp4'.format(dwap_dir)))
    ddm_files = sorted(glob.glob(r'{}/*mp4'.format(ddm_dir)))
    dda_files = sorted(glob.glob(r'{}/*mp4'.format(dda_dir)))
    mlib_files = sorted(glob.glob(r'{}/*mp4'.format(mlib_dir)))
    mgb_files = sorted(glob.glob(r'{}/*mp4'.format(mgb_dir)))
    mic_files = sorted(glob.glob(r'{}/*mp4'.format(mic_dir)))
    plib_files = sorted(glob.glob(r'{}/*mp4'.format(plib_dir)))
    tlib_files = sorted(glob.glob(r'{}/*mp4'.format(tlib_dir)))
    rws_files = sorted(glob.glob(r'{}/*mp4'.format(rws_dir)))
    sgs_files = sorted(glob.glob(r'{}/*mp4'.format(sgs_dir)))
    cfnm_files = sorted(glob.glob(r'{}/*mp4'.format(cfnm_dir)))

    ps_list_1 = []
    ps_list_2 = []
    title_list = []
    site_name = []
    link_name = []

    for lf in itertools.chain(bgb_files, bblib_files, btas_files, btaw_files,
                              btis_files, btiu_files, bwb_files, bbex_files,
                              bzv_files, cfnm_files, dwap_files, ddm_files,
                              dda_files, mlib_files, mgb_files, mic_files,
                              plib_files, rws_files, sgs_files, tlib_files):

        # for lf in itertools.chain(rws_files[:113]):
        # print(lf)
        site_string = lf.split('/')[-2]
        # print(site_string)
        site_with_ps = lf.split('/')[-1].split('-')[0]  # .split('-')[0]
        # print('ps1_tmp: ', site_with_ps)
        if site_string in site_with_ps:
            ps_only = site_with_ps.replace(site_string + '_', "")
            # print('ps_only: ', ps_only)
            if "__" in ps_only:
                ps_first = ps_only.split('__')[0]
                # print('ps_first: ', ps_first)
                firstname_1 = ps_first.split('_')[0]
                surname_1 = ps_first.split('_')[1]
                ps_first_new = firstname_1.capitalize() + ' ' + surname_1.capitalize()
                # print('ps_first_new', ps_first_new)

                ps_second = ps_only.split('__')[1]
                # print('ps_Second: ', ps_second)
                firstname_2 = ps_second.split('_')[0]
                surname_2 = ps_second.split('_')[1]
                ps_second_new = firstname_2.capitalize() + ' ' + surname_2.capitalize()
                # print('ps_second_new', ps_second_new)

                ps_list_1.append(ps_first_new)
                ps_list_2.append(ps_second_new)

            else:
                # ps_first = ps_only.split('_')[0]
                # print('XX')
                firstname_1 = ps_only.split('_')[0]
                # print('fn1: ', firstname_1)
                surname_1 = ps_only.split('_')[1]
                # print('sn1: ', surname_1)

                ps1_new = firstname_1.capitalize() + ' ' + surname_1.capitalize()
                # print('ps1_new: ', ps1_new)
                ps_list_1.append(ps1_new)
                ps_list_2.append('')

        title_string_small = lf.split('/')[-1].split('-')[1].split('.mp4')[0].split('_')[:-1]
        title_string_big = ' '.join(title_string_small).title()
        title_list.append(title_string_big)

        site_name.append(lf.split('/')[-2].replace('_', ' ').title())
        link_name.append(lf)

    ps_1_db = pd.DataFrame(ps_list_1)
    ps_2_db = pd.DataFrame(ps_list_2)
    title_list_db = pd.DataFrame(title_list)
    site_name_db = pd.DataFrame(site_name)
    link_name_db = pd.DataFrame(link_name)

    df_all = pd.concat([site_name_db, ps_1_db, ps_2_db, title_list_db, link_name_db], axis=1)
    df_all.columns = ['Site Name', 'Pornstar 1', 'Pornstar 2', 'Title', 'Link']

    for lf in df_all['Site Name'].unique():
        print(lf, ':', len(df_all[df_all['Site Name'] == lf]['Site Name']))
    print('Length overall: ', len(df_all['Title']))
    df_bra_nice = df_all.set_index(['Site Name', 'Pornstar 1']).sort_index()
    return df_all
    # qgrid_widget = qgrid.show_grid(df_bra_nice)
    # qgrid_widget