# EcommerceWebsite

Full-Stack project utilizing the **LAMP stack**.  

- **OS:** Ubuntu Linux  
- **Languages Used:** Bash, PHP, Python  
- **Technologies Used:** MySQL, Tagsoup  

---

## Getting this Project Running on Your Local Ubuntu Machine

### 1. Clone the Repository
Ensure that you have `git` installed and set up:

```
git clone https://github.com/ghxlam/EcommerceWebsite
cd EcommerceWebsite
```
### 2. Updating and Installing Dependencies:
```
sudo apt update && sudo apt upgrade -y
sudo apt install apache2 mysql-server php libapache2-mod-php php-mysql -y
sudo apt install python3 python3-pip openjdk-11-jre curl -y
pip3 install mysql-connector-python
```
### 3. Configure MySQL
```
sudo systemctl start mysql
sudo mysql -u root
```
Inside MySQL, Run this:      
```
CREATE DATABASE Dunder_Mifflin;
CREATE USER 'ghxlam'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON Dunder_Mifflin.* TO 'ghxlam'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
Now, log in as the new user:
```
mysql -u ghxlam -p Dunder_Mifflin
```
Then create the products table:
```
CREATE TABLE Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50),
    product_name VARCHAR(255),
    product_description TEXT,
    product_price DECIMAL(10,2),
    image_url TEXT,
    review_score VARCHAR(20)
);
EXIT;
```

### 4. Running The Project Scripts
We are going to scrape the data and populate the database
```
bash products.sh quill.txt staples.txt
```
***IMPORTANT: IF THAT GIVES AN ERROR, YOU MAY NEED TO DO THIS***
```
cd "xhtmlfiles copy"
     for file in *.xhtml; do
          python3 ../parser.py "$file"
     done
cd ..
```
***This step is necessary because websites may change over time, affecting the output from the `curl` command.***

### 5. Running the Web Server
**Option 1:** Use PHP Built-In Server
```
php -S localhost:8000
```
**Option 2:** Use Apache Web Server
```
sudo cp -r ./src/* /var/www/html/
sudo systemctl restart apache2
```
Then visit http://localhost in your web server.

⚠️ Note: The Apache method sometimes works but is not guaranteed 100% due to potential conflicts with the index.html file.


# Important Notes about the Project
- The files `quill.txt` and `staples.txt` hold the URLs for the products to be downloaded.
- The Bash script, `products.sh`, will download the URLs and then use tagsoup to turn the files into xhtml files.
- The Bash script also calls a Python script, `parser.py`, that goes through the DOM data which was downloaded and proceeds to extract that data into a MySQL Database.
- Then, the Bash script does clean up, deleting all the files that were originally downloaded for storage management.
- Once the MySQL Database has been populated, a PHP script will extract the data from the database and display the products on the page simulating an E-Commerce platform.
