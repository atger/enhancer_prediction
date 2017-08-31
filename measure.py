import re
import nolds
import numpy as np
import pandas as pd

def read_seq(s):
    p = re.compile(r'>.*\n')
    d = p.split(open(s).read(),maxsplit=0)
    d = [i.replace('\n','') for i in d]
    return d[1:]

def lwalk(x):                                                 
    disp = []                 
    count = 0                               
    for i in x:                     
        if 'A' == i or 'G' == i:           
            count += 1                    
        elif 'T' == i or 'C' == i:           
            count -= 1                                                
        disp = np.append(disp,count)          
    return disp

def autocorrelation(x,lag):
    i = pd.Series(x)
    return pd.Series.autocorr(i,lag)

def ratio_value_number_to_time_series_length(x):
    if len(x) == 0:
        return np.nan
    return len(set(x))/len(x)

def load_feature(s):                                          
    rw = [lwalk(i) for i in s]
    sd = [np.std(i) for i in rw]
    dfa = [nolds.dfa(i) for i in rw]
    hurst = [nolds.hurst_rs(i) for i in rw]
    sampen = [nolds.sampen(i) for i in rw]
    ac = [autocorrelation(i,100) for i in rw]
    rvntsl = [ratio_value_number_to_time_series_length(i) for i in rw]
    ac_200 = [autocorrelation(i,200) for i in rw]
    ac_300 = [autocorrelation(i,300) for i in rw]
    lyapr = [nolds.lyap_r(i) for i in rw]
    inpv = pd.DataFrame([sd,dfa,hurst,sampen,ac,rvntsl,ac_200,ac_300,lyapr])
    return inpv.transpose()

