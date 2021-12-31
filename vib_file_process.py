import pandas as pd
import os
import shutil

cur_path = os.getcwd()
inputfile = input("input file directory: ")

data = pd.read_csv(inputfile, encoding='CP949')

for i in range(len(data)):
    if not os.path.exists(data.loc[i, 'Position']):
        os.mkdir(data.loc[i, 'Position'])

    prefix = 'SIG0'
    suffix = ['_APS(Ch1).csv', '_APS(Ch2).csv', '_Block(Ch1).csv', '_Block(Ch2).csv',
              '_COH(Ch2,Ch1).csv',  '_H(Ch2,Ch1).csv']

    for j in range(len(suffix)):

        if data.loc[i, 'SIG1'] < 100:
            prefix = 'SIG00'
        elif data.loc[i, 'SIG1'] >= 1000:
            prefix = 'SIG'

        filename = prefix+str(data.loc[i, 'SIG1'])+suffix[j]
        srcfile = os.path.join(cur_path, filename)
        dstfile = os.path.join(cur_path, data.loc[i, 'Position'], filename)
        shutil.move(srcfile, dstfile)

        if data.loc[i, 'SIG2'] < 100:
            prefix = 'SIG00'
        elif data.loc[i, 'SIG2'] >= 1000:
            prefix = 'SIG'

        filename = prefix+str(data.loc[i, 'SIG2'])+suffix[j]
        srcfile = os.path.join(cur_path, filename)
        dstfile = os.path.join(cur_path, data.loc[i, 'Position'], filename)
        shutil.move(srcfile, dstfile)
