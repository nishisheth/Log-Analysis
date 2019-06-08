import psycopg2

try:
    connection = psycopg2.connect(database = "news")
    cursor = connection.cursor()
    print ("********* Checking connection to database ********")
    print("You are connected to database successfully!")
    print ("**************************************************")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)


QUERY_FOR_THREE_MOST_POPULAR_ARTICLES = """
        select A.title, count(L.id) as total from articles A left outer join log L  
        on L.path = concat('/article/',A.slug)
        group by A.title order by total desc;
        """

QUERY_FOR_MOST_POPULAR_ARTICLE_AUTHOR = """

        select au.name, au_views.total  
        from authors au left join 
        (select A.author, count(L.id) as total from articles A 
            left join log L on L.path = concat('/article/',A.slug) 
        group by A.author) as au_views on au_views.author=au.id
        group by au.name, au_views.total 
        order by au_views.total desc;

        """

def run_db_query(query):
    cursor.execute(query)
    return cursor.fetchall()
    cursor.close()

def get_three_most_popular_articles():
    return run_db_query(QUERY_FOR_THREE_MOST_POPULAR_ARTICLES)

def most_popular_article_authors():
    return run_db_query(QUERY_FOR_MOST_POPULAR_ARTICLE_AUTHOR)

def print_question1_report():
    ans1_rows = get_three_most_popular_articles()
    for row in ans1_rows:
        print "%s - %d views" % (row[0],row[1])

def print_question2_report():
    ans2_rows = most_popular_article_authors()
    for row in ans2_rows:
        print "%s - %d views" % (row[0],row[1])
       

def print_report():
    print """ >>>>>>>>>  Report data <<<<<<<<<< \n\n"""
    print "----------------------------------------"
    print "Answer for question 1:"
    print "----------------------------------------"
    print_question1_report()
    print "----------------------------------------\n\n"
    print "Answer for question 2:"
    print "----------------------------------------"
    print_question2_report()
    print "----------------------------------------"

    
print_report()

