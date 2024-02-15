
import os
import pandas as pd

files = os.listdir('data') 


## Helper functions
def createPostID(row):
    """helper function: create a new value using music and author"""
    return f"{row['music']}_{row['author']}"

# splitter = lambda x: [s.strip() for s in x.split(',') if not s.type() == float]

# create 3 dfs: control data, save data, all data
onlyAllData = [f for f in files if 'data_all' in f] # filtering with list comprehension

control_dfs = []
save_dfs = []
all_dfs = []


for fN in onlyAllData: # folder with files that have all posts
    path = os.path.join('data', fN) # create file path
    df = pd.read_csv(path) # create dataframe

    # add column to indicate date/time collected
    df['collectionTime'] = fN[:11]

    # add column with unique post id
    df['postID'] = df.apply(createPostID, axis=1) # use axis=1 to process one row at a time

    # split hashtags into list
    #df['hashtag'] = df['hashtag'].apply(splitter)

    if 'control'in fN:
        control_dfs.append(df)
    else:
        save_dfs.append(df)

    all_dfs.append(df)


df_control = pd.concat(control_dfs, ignore_index=True)
df_save = pd.concat(save_dfs, ignore_index=True)
df_all = pd.concat(all_dfs, ignore_index=True)

print("control shape:", df_control.shape)
print("save shape:", df_save.shape)
print("all data shape:", df_all.shape)
