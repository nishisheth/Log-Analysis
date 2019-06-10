#!/usr/bin/env python

import psycopg2

try:
    connection = psycopg2.connect(database="news")
    cursor = connection.cursor()
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)


QUERY_FOR_THREE_MOST_POPULAR_ARTICLES = """
        select A.title, count(L.id) as total
        from articles A left outer join log L
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

QUERY_FOR_MORE_THAN_1_PERCENT_ERRORS = """
        select TO_CHAR(time,'FMMonth DD, YYYY') as log_date,
        ROUND((SUM(
                CASE WHEN status = '404 NOT FOUND' THEN 1
                ELSE 0
                END) / count(*)::NUMERIC)*100,1) AS percentage
        from log group by log_date
        HAVING ROUND((SUM(
                CASE WHEN status = '404 NOT FOUND' THEN 1
                ELSE 0
                END) / count(*)::NUMERIC)*100,1) > 1;
"""


def run_db_query(query):
    cursor.execute(query)
    return cursor.fetchall()
    cursor.close()


def get_three_most_popular_articles():
    return run_db_query(QUERY_FOR_THREE_MOST_POPULAR_ARTICLES)


def most_popular_article_authors():
    return run_db_query(QUERY_FOR_MOST_POPULAR_ARTICLE_AUTHOR)


def days_with_high_errors():
    return run_db_query(QUERY_FOR_MORE_THAN_1_PERCENT_ERRORS)


def print_question1_report():
    ans1_rows = get_three_most_popular_articles()
    for row in ans1_rows:
        print "%s - %d views" % (row[0], row[1])


def print_question2_report():
    ans2_rows = most_popular_article_authors()
    for row in ans2_rows:
        print "%s - %d views" % (row[0], row[1])


def print_question3_report():
    ans3_rows = days_with_high_errors()
    format = '% errors'
    for row in ans3_rows:
        print "%s -  %s%s" % (row[0], row[1], format)


def print_report():
    print """ >>>>>>>>>  Report data <<<<<<<<<<"""

    print "\n\n----------------------------------------"
    print "Question 1: What are the most popular three articles of all time?"
    print "----------------------------------------"
    print_question1_report()

    print "\n\n----------------------------------------"
    print "Question 2: Who are the most popular article authors of all time?"
    print "----------------------------------------"
    print_question2_report()

    print "\n\n----------------------------------------"
    print "Question 3: On which days more than 1% of requests lead to errors?"
    print "----------------------------------------"
    print_question3_report()


if __name__ == '__main__':
    print_report()
