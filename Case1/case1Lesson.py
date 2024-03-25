import pandas as pd
import pm4py

log_csv = pd.read_csv('https://raw.githubusercontent.com/paoloceravolo/BIS2022/main/Event%20Logs/CallCenterLog.csv', sep=',')

# convert the date colument to date format
log_csv['Start Date'] = pd.to_datetime(log_csv['Start Date'])
log_csv['End Date'] = pd.to_datetime(log_csv['End Date'])

# format datafram for PM4PYT
log_csv = pm4py.format_dataframe(log_csv, case_id='Case ID', activity_key='Activity', timestamp_key='End Date')

log_csv