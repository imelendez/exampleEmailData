#!/usr/bin/env python
# coding: utf-8

import pandas as pd


# # Person Data - cons.csv
#import cons.csv
data = pd.read_csv('cons.csv',delimiter=',')
emailData = pd.read_csv('cons_email.csv',delimiter=',')


primaryemails=emailData.loc[emailData['is_primary']==1]
# # Merge Person and Email data
mergeForEmailAndSource = pd.merge(primaryemails[['cons_id','email','cons_email_id','is_primary']], data[['cons_id','source','create_dt','modified_dt']], on='cons_id', how='inner')


# # Subscription data - cons_email_chapter_subscription.csv
subsData = pd.read_csv('cons_email_chapter_subscription.csv',delimiter=',')

# # Merge Person Email and Subscription Data for final table
finaltable = pd.merge(mergeForEmailAndSource[['cons_email_id','cons_id','email','source','create_dt','modified_dt']], subsData[['cons_email_id','isunsub']], on='cons_email_id', how='inner')


# ## Final Table 1 Email | Source | IsUnSub | Create Date | Modified Date

correctorder=finaltable[['cons_id','email','source','isunsub','create_dt','modified_dt',]]

#Making sure the cons_id are unique, checking no duplicates are in my list
correctorder['cons_id'].duplicated().any() 
#parsing date string to a date type in pandas
correctorder['created_dt']= pd.to_datetime(correctorder['create_dt'])
correctorder['created_dt'] = correctorder['created_dt'].dt.date

#correct order
correctorder=correctorder[['cons_id','email','source','isunsub','created_dt','modified_dt',]]


# # Output final result person table to CSV
correctorder.to_csv('finaltable1.csv',index=False)

datesTable=correctorder['created_dt'].value_counts()

# # Create dates CSV output 

#CSV file has column with dates and corresponding counts
datesTable.to_csv('dates.csv')

# the end




