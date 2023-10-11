from Capgemini.capgemini import get_capgemini
from Zoho.zoho import get_zoho
from Deloit.deloit import get_deloit
from infosys.infosys import get_infosys
from mindtree.mindtree import get_mindtree
from Unify.unify import get_unify
from Ysquare.ysqure import get_ysqure
from Ust.ust import get_ust
from Parallel.parallel import get_parallel
from Pubmatic.pubmatic import get_pubmatic
from Spider.spider import get_spider
import pandas as pd
import time
import threading

start = time.time()

CAPGEMINI_DF = get_capgemini()
ZOHO_DF = get_zoho()
DELOIT_DF  = get_deloit()
INFOSYS_DF = get_infosys()
MINDTREE_DF = get_mindtree()
UNIFY_DF = get_unify()
YSQURE_DF = get_ysqure()
UST_DF = get_ust()
PRALLRL_DF = get_parallel()
PUBMATIC_DF = get_pubmatic()
SPIDER_DF = get_spider()

print(time.time() - start)

writer = pd.ExcelWriter('carrer_data_crawler_Jan_22_2023.xlsx', engine='xlsxwriter')

CAPGEMINI_DF.to_excel(writer, sheet_name='CAPGEMINI')
ZOHO_DF.to_excel(writer, sheet_name='ZOHO')
DELOIT_DF.to_excel(writer, sheet_name='DELOIT')
INFOSYS_DF.to_excel(writer, sheet_name = 'INFOSYS')
MINDTREE_DF.to_excel(writer, sheet_name = 'MINDTREE')
UNIFY_DF.to_excel(writer, sheet_name= 'UNIFY')
YSQURE_DF.to_excel(writer, sheet_name= 'YSQURE')
UST_DF.to_excel(writer, sheet_name= 'UST' )
PRALLRL_DF.to_excel(writer, sheet_name= 'PARALLEL')
PUBMATIC_DF.to_excel(writer, sheet_name= 'PUBMATIC')
SPIDER_DF.to_excel(writer, sheet_name= 'SPIDER')
writer.close()



