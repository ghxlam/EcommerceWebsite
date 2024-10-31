# EcommerceWebsite
# Full-Stack project utilizing the LAMP stack.

# Getting this Project Running on your Local Machine:
1. Copy the repository on your local machine. (Project was done on a Linux OS, a VM running linux should be fine)

# Important Notes about the Project
- The files quill.txt and staples.txt hold the URLs for the products to be downloaded.
- The Bash script, products.sh, will download the URLs and then use tagsoup to turn the files into xhtml files.
- The Bash script also calls a Python script, parser.py, that goes through the DOM data which was downloaded and proceeds to extract that data into a MySQL Database.
- Then, the Bash script does clean up, deleting all the files that were originally downloaded for storage management.
- Once the MySQL Database has been populated, a PHP script will extract the data from the database and display the products on the page simulating an E-Commerce platform.
