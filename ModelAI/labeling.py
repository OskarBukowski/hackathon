from tracemalloc import start
import pickle as pkl
import pandas as pd
import os
import sys
from os import path
from icecream import ic

ic.configureOutput(prefix='')

# Backups directory (after each 10 labels backup is created)
if not path.exists('/home/obukowski/Desktop/hackathon/backup'):
    os.mkdir('/home/obukowski/Desktop/hackathon/backup')

unlabeled_df = pd.read_csv('3.csv')

# Index of last labeled tweet if script terminated runtime
# Existence of this file indicates that backup was created
# If exists saved state is loaded
if path.exists('/home/obukowski/Desktop/hackathon/backup/state'):
    with open('/home/obukowski/Desktop/hackathon/backup/state', 'rb') as f:
        start_index, ones, zeros = pkl.load(f)
    out_df = pd.read_csv('/home/obukowski/Desktop/hackathon/labeled.csv')
else:
    start_index = 0
    ones = 0
    zeros = 0
    out_df = pd.DataFrame(columns = ['text', 'label'])

ic(start_index, ones, zeros)

for i, tweet in enumerate(unlabeled_df.loc[start_index:].iterrows()):
    text = tweet[1]['text']
    ic(zeros, ones, i)
    print(text + "\n")
    
    label = -1
    while label not in [0, 1, 2, 999]:
        try:
            label = int(input("INSERT LABEL[0, 1 are labels, 2 to discard tweet, 999 to save and exit]: "))
        except Exception:
            continue

    if label == 2:
        os.system('clear')
        continue
    
    elif label == 999:
        out_df.to_csv('/home/obukowski/Desktop/hackathon/labeled.csv', index=False)
        print(out_df)
        with open('backup/state', 'wb') as f:
            pkl.dump((i - 1, ones, zeros), f)
        sys.exit(0)
    else:
        # Create dataframe row and add to out_df
        if label: 
            ones += 1
        else: 
            zeros += 1
        temp_df = pd.DataFrame({'text': [text], 'label': [label]})
        out_df = out_df.append(temp_df).reset_index(drop=True)
    
        os.system('clear')
    
        if i%10 == 0 and i > 0:
            with open('/home/obukowski/Desktop/hackathon/backup/state', 'wb') as f:
                pkl.dump((i + 1, ones, zeros), f)
            out_df.to_csv(f'/home/obukowski/Desktop/hackathon/backup/backup_{i//10}', index=False)

out_df.to_csv('/home/obukowski/Desktop/hackathon/labeled.csv', index=False)

# Uwwagi: ... na końcu tweeta to retweet, chyba najlepiej discardowac
# Jezeli to są jakieś retweety do jakiegos trolla to zapiszcie gdziekolwiek jego nick to się sprawdzi jego konto