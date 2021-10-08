#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import glob
import time

tbl_files = []
for file in glob.glob("*.tbl"):
    tbl_files.append(file)


table_col_map = {}

table_col_map['part'] = ['P_PARTKEY','P_NAME','P_MFGR','P_BRAND','P_TYPE','P_SIZE','P_CONTAINER','P_RETAILPRICE','P_COMMENT']
table_col_map['partsupp'] = ['PS_PARTKEY','PS_SUPPKEY','PS_AVAILQTY','PS_SUPPLYCOST','PS_COMMENT']
table_col_map['nation'] = ['N_NATIONKEY', 'N_NAME', 'N_REGIONKEY', 'N_COMMENT']
table_col_map['orders'] = ['O_ORDERKEY','O_CUSTKEY','O_ORDERSTATUS','O_TOTALPRICE','O_ORDERDATE','O_ORDERPRIORITY','O_CLERK','O_SHIPPRIORITY','O_COMMENT']
table_col_map['customer'] = ['C_CUSTKEY','C_NAME','C_ADDRESS','C_NATIONKEY','C_PHONE','C_ACCTBAL','C_MKTSEGMENT','C_COMMENT']
table_col_map['supplier'] = ['S_SUPPKEY','S_NAME','S_ADDRESS','S_NATIONKEY','S_PHONE','S_ACCTBAL','S_COMMENT']
table_col_map['lineitem'] = ['L_ORDERKEY','L_PARTKEY','L_SUPPKEY','L_LINENUMBER','L_QUANTITY','L_EXTENDEDPRICE','L_DISCOUNT','L_TAX','L_RETURNFLAG','L_LINESTATUS','L_SHIPDATE','L_COMMITDATE','L_RECEIPTDATE','L_SHIPINSTRUCT','L_SHIPMODE','L_COMMENT']
table_col_map['region'] = ['R_REGIONKEY', 'R_NAME', 'R_COMMENT']



def convert_to_json(file_name):
    file_name_without_extension = file_name.split('.')[0]
    col = table_col_map[file_name_without_extension]
    col.append('dump')
    df = pd.read_table(file_name, sep='|', header=None)
    df.columns = col
    df.drop('dump', inplace=True, axis=1)
    output_file_name = file_name_without_extension.upper() + '.json'
    df.to_json(output_file_name,orient='records')

strat_time = start_func_time =  end_time = time.time()

for file in tbl_files:
    strat_time = time.time()
    convert_to_json(file)
    end_time = time.time()
    print("Time taken to convert %s table: %.2f s" %(file, end_time - strat_time))

end_time = time.time()

print("Total time taken: %.2f s" %(end_time - start_func_time))





