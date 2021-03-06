# GCP Utility tool

We can backfill any kind of bigquery sql to specific destination table with powerful python jinja templating feature. By default it can support date templates in your query. It will automatically convert to date template to date value in your query while executing.

Following are the available date templates you can use it in your query.

```bash
{{ds}} - YYYY-DD-MM date string 
{{ds_nodash}} - YYYYDDMM date string 
{{ds_yesterday}} - YYYY-DD-MM yesterday date string 
{{ds_yesterday_nodash}} - YYYYDDMM yesterday date string 
{{ds_tomorrow}} - YYYY-DD-MM tomorrow date string 
{{ds_tomorrow_nodash}} - YYYYDDMM tomorrow date string 

``` 

## Getting Started

### Installing

Use virtualenv to Install the dependancy packages 

```
pip install virtualenv
virtualenv venv
. ./venv/bin/activate
```

```
##### Windows:
python -m pip install virtualenv
python -m virtualenv venv
./venv/Scripts/activate
```

Install bq_client command line tool using pip

```bash
pip install gcp-utility
```

-h command will return the help content which contains all the available  options
```
bq_client -h
```

End with an example of getting some data out of the system or using it for a little demo

## Available option

```bash
usage: bq_client.py [-h] [-q QUERY] [-f] [-p PROJECT] [-ssql] [-dml]
                    [-d DESTINATION_TABLE] [-w WRITE_DESPOSITION]
                    [-qf QUERY_FILE] [-t TEMPLATE] [-tf TEMPLATE_FILE]
                    [-s START_DATE] [-e END_DATE] [-sf SERVICE_ACCOUNT_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        provide valid bigquery sql
  -f, --no-flattern     Flattern results
  -p PROJECT, --project_id PROJECT
                        provide valid project id
  -ssql, --standard-sql
                        Mention if using Standard sql
  -dml, --dml-statement
                        Mention if using DML statements in your query
  -d DESTINATION_TABLE, --destination-table DESTINATION_TABLE
                        <projectname>:<datasetid>.<tableid> provide valid
                        destination project-id
  -w WRITE_DESPOSITION, --write-desposition WRITE_DESPOSITION
                        Write disposition value
  -qf QUERY_FILE, --query-file QUERY_FILE
                        provide bigquery sql filepath
  -t TEMPLATE, --template TEMPLATE
                        provide template values
  -tf TEMPLATE_FILE, --template-file TEMPLATE_FILE
                        provide template file path
  -s START_DATE, --start-date START_DATE
                        Provide valid startdate (YYYY-MM-DD)
  -e END_DATE, --end-date END_DATE
                        Provide valid end date (YYYY-MM-DD)
  -sf SERVICE_ACCOUNT_PATH, --service-account-file-path SERVICE_ACCOUNT_PATH
                        provide valid path of service account json file
```
     

### passing raw query

you can pass the raw query to script that need to be execute

```
bq_client -q "select * from [sample_proj:datasetid.tableid]" -p destination_projectid -d dest_datasetid.tableid
```

### Using sql file

if your query is quite long, you can save it to text file and pass the path of it

```
bq_client --query-file "/path/sample.sql" -p destination_projectid -d dest_datasetid.tableid```

```

### Passing date parameter

In default it will substitute current date into template fields. but if you want to change the date value you can pass manually using start date parameter

```
bq_client --query-file sample.sql -p projectid -d dest_datasetid.tableid -s 2018-02-02

```

### Backfill

Pass start-date and end-date to script, it will backfill the data.

```
bq_client --query-file sample.sql -p projectid -d dest_datasetid.tableid -s 2018-02-02 -e 2018-02-10

```

### Development 
What things you need to install the software and how to install them

```
google-cloud-bigquery==1.24.0
Jinja2==2.11.2
```
