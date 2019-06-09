# Log Analysis 

The objective of the Logs Analysis Project is to to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. This is a Python program using the psycopg2 module to connect to the PostgreSQL database. 

# Requirements
- Python 2.7.x or greater - The code uses ver 2.7.10
- [Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager
- [VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product.
- Git - An open source version control system

# How to run this tool?

**1.** Download the VM configuration or clone the repoaitory from [here](https://github.com/udacity/fullstack-nanodegree-vm). Note the path where you downloaded it as it will be used in other steps.

**2.** Download the database from [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

Put the file called `newsdata.sql` into the `vagrant/` directory, which is shared with your virtual machine.

**3.** Download the python programs (`Reportingtool.py`) from the current folder. Then, copy them to the `vagrant/` folder.

**4.** Navigate to the Udacity folder in your bash interface and inside that cd into the vagrant folder.

**5.** Open Git Bash and launch the VM with `vagrant up`.

**6.** Run `vagrant ssh` to log in to the newly installed Linux VM.

**7.** Change the directory to `vagrant/` folder.

**8.** Load the database by using `psql -d news -f newsdata.sql`.

**9.** To explore the databse by using `psql -d news`.

**10.** Run the program using `python Reportingtool.py`. You should see output of reporting tools as shown in `reportingtool_output.txt` file. This tool runs queries to get data for below questions.

# Questions

**1. What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
    
**2. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**3. On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)
