# coding=utf-8

# pip install xlrd
# pip install openpyxl
# pip install pandas
# pip install numpy

from operator import index
import pandas as pds
import numpy as npy
import math
import sys

pds.options.mode.chained_assignment = None

# df = pds.read_excel("./test.xlsx")
df = pds.read_excel(sys.argv[1])
# print(df)
# print(type(df))

# print(df.iloc[:,0])
fam_uni = npy.unique(npy.sort(df.iloc[:,0]))
# print(fam_uni)

df2 = pds.DataFrame(columns=[df.columns.tolist()[0], df.columns.tolist()[1], df.columns.tolist()[2], 'Ratios', 'LnRatio', 'NegMul'])

for fam in fam_uni:
  ndf = df.loc[df.iloc[:,0] == fam]
  # print(ndf)
  gen_spe_dic = ndf.set_index([df.columns.tolist()[1]])[df.columns.tolist()[2]].to_dict()
  fam_spe_sum = sum(ndf.iloc[:,2])
  res = []
  ln_res = []
  mul_res = []
  for gen in ndf.iloc[:,1]:
    gen_res = gen_spe_dic[gen] / fam_spe_sum
    res.append(gen_res)
    gen_ln_res = math.log(gen_res, math.e)
    ln_res.append(gen_ln_res)
    gen_mul_res = gen_res * (-(gen_ln_res))
    mul_res.append(gen_mul_res)
  ndf['Ratios'] = res
  ndf['LnRatio'] = ln_res
  ndf['NegMul'] = mul_res
  # print(ndf)
  df2 = df2.append(ndf)
# print(df2)

df2.to_excel(sys.argv[1].split('.')[0] + "_result.xlsx", index=None)