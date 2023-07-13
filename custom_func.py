import os, sys
import uproot
import pandas as pd
import numpy as np

def make_df(tree, branches, samplename):
    awkarray = tree.arrays(branches)
    df = pd.DataFrame(awkarray.to_list())
    df['sample'] = samplename
    return df

#Normalizing variables from 0 to 1
def normalize_col(df, col):
    if df[col].max() != df[col].min():
        df[col] = (df[col]-df[col].min()) / (df[col].max()-df[col].min())
    else:
        print('Scaling error: max and min are the same!')
    return df

def print_info(df, samplename, txtfile):
    num = df[df["sample"] == samplename].shape[0]
    nsig =df[(df["sample"]==samplename)&(df["truth"]==1)].shape[0]
    nbkg =df[(df["sample"]==samplename)&(df["truth"]==0)].shape[0]
    if num!= 0:
        sig_frac = nsig*100/num
        bkg_frac = nbkg*100/num
    else:
        sig_frac = -1
        bkg_frac = -1
    statement=f'Sample : {samplename}; \tnCandidates = {num}; nsig = {nsig} ({sig_frac:.1f}%), nbkg = {nbkg} ({bkg_frac:.1f}%)'
    print(statement)
    txtfile.write(statement)
    txtfile.write('\n')
    
def find_tpr_fnr_auc(true, pred):
    fpr, tpr, _ = roc_curve(true, pred)
    auc_score   = auc(tpr,1-fpr)
    tpr=tpr*100
    fnr=(1-fpr)*100
    return fnr, tpr, auc_score
