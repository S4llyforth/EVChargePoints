# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:50:13 2021

@author: TomEdwards
"""

import pandas as pd  
import numpy as np

#===========GET DATA========================
#House Type Data
#CTSOP = pd.read_excel('table_CTSOP3.1_2015.xlsx')
#CTSOP1 = CTSOP[['GEOGRAPHY','BA_CODE', 'ECODE','AREA_NAME','BAND','BUNGALOW','FLAT_MAIS','HOUSE_TERRACED','HOUSE_SEMI','HOUSE_DETACHED','ANNEXE','OTHER']]
#CTSOP1 = CTSOP1.loc[CTSOP1['BAND'] == 'All']

#Historical Vehicle data
VEH0132a = pd.read_excel('VEH0132.xlsx',sheet_name = 'VEH0132a',skiprows = 6)
del VEH0132a['Region/Local Authority']
#VehColList  = VEH0132a.columns.tolist()
#VehColList = VehColList[2:]
VEH0132a = pd.melt(VEH0132a, id_vars=['ONS LA Code'])
VEH0132a[['Year','Quarter']] = VEH0132a['variable'].str.split(' ',expand=True)
#VEH0132a['DateTime'] = pd.to_datetime(VEH0132a['variable'])

#historical chargepoint data
HCPD = pd.read_csv('national-charge-point-registry (version 1).csv')
#HCPD = HCPD[(HCPD['dateCreated'] != '0000-00-00 00:00:00') | (HCPD['dateCreated'] != '230')]
HCPD['DateTime'] = pd.to_datetime(HCPD['dateCreated'])
HCPD['year'] = pd.DatetimeIndex(HCPD['DateTime']).year
HCPD['quarter'] = pd.DatetimeIndex(HCPD['DateTime']).quarter
HCPD['quarter'] = 'Q' + HCPD['quarter'].astype(str)