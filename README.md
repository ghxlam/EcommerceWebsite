# EcommerceWebsite
Full-Stack project utilizing the LAMP stack.
- Project was done on an Ubuntu Linux OS.
- Languages Used: Bash, PHP, Python
- Technologies Used: MySQL, Tagsoup

# Getting this Project Running on your Local Ubuntu Machine:
1. Clone the repository on your local machine.
     - Ensure that you have git installed and set up
     - git clone https://github.com/ghxlam/EcommerceWebsite
2. Update and Installing Dependencies:
     - sudo apt-get update
     - Intalling MySQL:
     - sudo apt install mysql-client-core-8.0

# Important Notes about the Project
- The files quill.txt and staples.txt hold the URLs for the products to be downloaded.
- The Bash script, products.sh, will download the URLs and then use tagsoup to turn the files into xhtml files.
- The Bash script also calls a Python script, parser.py, that goes through the DOM data which was downloaded and proceeds to extract that data into a MySQL Database.
- Then, the Bash script does clean up, deleting all the files that were originally downloaded for storage management.
- Once the MySQL Database has been populated, a PHP script will extract the data from the database and display the products on the page simulating an E-Commerce platform.
