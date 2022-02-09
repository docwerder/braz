import os

ddf_dir = '/Volumes/WERDERNASX/VIDEOSX/DDFNETWORK/DDFBUSTY_FUCKINHD_CO'
total_files = 0
for root, dirs, files in os.walk(ddf_dir, topdown=False):
    for name in files:
        total_files += 1
        file_name = name.split('-')[0]
        print('file_name = ', file_name)
