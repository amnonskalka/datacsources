import pymysql
import pandas as pd
import pygeoip

raw_data = pygeoip.GeoIP('/home/amnon/GeoLiteCity.dat')
query = 'select * from customers'
csv_path = r'/home/amnon/Downloads/Company_ACV.csv'


def mysql_connection():
    connection = pymysql.connect(unix_socket='/var/run/mysqld/mysqld.sock',
                                 user='amnon',
                                 password='root',
                                 db='test',
                                 charset='utf8mb4')
    return connection


def csv_to_df():
    use_columns = ['user_id', 'ACV']
    csv_df = pd.read_csv(csv_path, usecols=use_columns)
    return csv_df


def mrg_df(query_df, csv_grouped):
    merge_df = pd.merge(query_df, csv_grouped, how='left', left_on=['user_id'], right_on=['user_id'], left_index=False,
                        right_index=False)
    merge_df = merge_df[
        ['email', 'segment', 'industry', 'owner_manager_email', 'platform', 'go_live_date', 'stage', 'created_from_ip',
         'user_id', 'ACV']
    ]
    return merge_df


def ip_check(mrg):
    ip_df = []
    for x in mrg['created_from_ip']:
        data = raw_data.record_by_name(x)
        if isinstance(data, dict):
            country = data['country_name']
            continent = data['continent']
            ip_df.append({'ip': x, 'country': country, 'continent': continent})

    ip_df = pd.DataFrame(ip_df)
    return ip_df


def merge_ip(mrg, ip_info):
    df_with_geo = pd.merge(mrg, ip_info, how='left', left_on=['created_from_ip'], right_on=['ip'], left_index=False,
                           right_index=False)
    df_with_geo = df_with_geo[
        ['email', 'segment', 'industry', 'owner_manager_email', 'platform', 'go_live_date', 'stage', 'created_from_ip',
         'continent', 'country', 'user_id', 'ACV']
    ]
    return df_with_geo
