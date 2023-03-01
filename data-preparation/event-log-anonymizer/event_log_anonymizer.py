from anonymizedf.anonymizedf import anonymize
import pandas as pd

event_log_name = 'ibm_pm_sdlc'

data_frame = pd.read_csv('{}.zip'.format(event_log_name))
anonymizer = anonymize(data_frame)

for column_name in ['Created_By', 'Assignee', 'Assigner']:
    anonymizer.fake_names(column_name)
    data_frame[column_name] = data_frame['Fake_{}'.format(column_name)]
    del data_frame['Fake_{}'.format(column_name)]



file_name = '{}_anonymized.zip'.format(event_log_name)
data_frame.to_csv('{}'.format(file_name), escapechar='"', index=False,
                  compression={'method': 'zip', 'archive_name': '{}_anonymized.csv'.format(event_log_name)})