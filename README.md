# datacsources
The target was to calculate how much revenue (=ACV) is the company making per country and per continent.
To have the ability to calculate it, I needed to preform the following steps:
1. Import data from various sources (MySQL, CSV file)
2. Adjustment of the data structure to a uniform form
3. Extract Geo targeting of ip
4. Merge all the data
5. Calculate and Export the result

To collect the data from the MySQL DB and the revenue transactions from the CSV file, each one to different pandas DataFrame, I used "read_csv" and "read_sql" functions.
In the second step I was needed to aggregate the revenue transactions so it will fit into the metadata structure and we will have to possibility to join the DataFrames together. I've done it by grouping the transactions  by the user_id and sum the revenue for each one.
I got the Geo targets from the user ip's by using pygeoip (based on maxmind DB)  and create DataFrame that contain IP, Country and Continent.
After collecting all necessary data i joined them together to one datafarme that will be the base of the final calculation, I joined the metadata and the revenue by user_id and then joined the Geo targeting by the IP address.

To perform the necessary calculation I grouped the merged data by continent, by country and export the results to csv file
