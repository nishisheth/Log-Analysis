import psycopg2

try:
    connection = psycopg2.connect(database = "news")
    cursor = connection.cursor()
    print ("********* Checking connection to database ********")
    print("You are connected to database successfully!")
    print ("**************************************************")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)