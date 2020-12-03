import os
import sys
import shutil
import pandas as pd
from functions import get_folder


folder_frame = 'C:\\Users\\Angel\\Documents\\Ironhack\\web_project\\files'
energy_flow = 'generation'
data_type = 'real'
rows_to_skip = 15


def main():

    out_filename = f'{folder_frame}\\{energy_flow}-{data_type}.csv'
    folder,files = get_folder(folder_frame,energy_flow, data_type) # Get folder with files to be joined

    if len(files):

        print(f'{energy_flow}-{data_type}', end='')
        sys.stdout.flush()

        with open(out_filename, 'w') as outfile:
            for i, file in enumerate(files):

                print('.', end = '')
                sys.stdout.flush()

                with open(f'{folder}\\{file}', 'r') as readfile:

                    if i == 0:

                        for _ in range(rows_to_skip - 1):
                            readfile.readline()

                    else:
                        for _ in range(rows_to_skip):
                            readfile.readline()

                    for line in readfile.readlines():
                        outfile.write(line)

        print('Processing...', end = '')
        sys.stdout.flush()

        df = pd.read_csv(out_filename)
        df.columns = [column.strip(' ').replace(' ','_').lower() for column in df.columns]
        df.to_csv(out_filename, index=False, float_format='%.3f')

        print('Done')

    else:
        # If no files where found in folder the system-data is skipped
        print(f'\n{energy_flow}-{data_type} data not found.\n')

    print('----Finished----')


if __name__ == '__main__':
    main()
