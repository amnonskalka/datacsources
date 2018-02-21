from contextlib import closing
from func import *

csv_output = '/home/amnon/output_all.csv'

with closing(mysql_connection()) as conn:
    query_df = pd.read_sql(query, conn)
csv_df = csv_to_df()

csv_grouped = csv_df.groupby(['user_id']).sum()
csv_grouped = pd.DataFrame(csv_grouped).reset_index()

mrg = mrg_df(query_df, csv_grouped)
ip_info = ip_check(mrg)
full_df = merge_ip(mrg, ip_info)
final_grp = full_df[['continent', 'country', 'ACV']]

final_calc = final_grp.groupby(['continent', 'country'], as_index=False).sum()
final_calc.to_csv(csv_output, encoding='utf-8', index=False)
