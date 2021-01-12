CREATE =  {
    "Category":
            "CREATE TABLE Category("
            "id INT UNSIGNED NOT NULL AUTO_INCREMENT," 
            "name VARCHAR(60) NOT NULL,"
            "PRIMARY KEY(id)) ENGINE=INNODB",

    "Product":
            "CREATE TABLE Product("
            "id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
            "name TEXT NOT NULL,"
            "nutriscore CHAR(1) NOT NULL,"
            "url TEXT NOT NULL,"
            "store TEXT NULL,"
            "description TEXT NULL,"
            "openfoodfact_id BIGINT UNSIGNED NOT NULL,"
            "category_id INT  UNSIGNED NOT NULL,"
            "PRIMARY KEY(id),"
            "FOREIGN KEY (category_id) REFERENCES Category(id)) ENGINE=INNODB",
        
        "User": 
            "CREATE TABLE User("
            "id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
            "pseudo VARCHAR(50) NOT NULL,"
            "PRIMARY KEY(id))",
            
        "Substitute": 
                "CREATE TABLE Substitute("
                "id INT UNSIGNED NOT NULL AUTO_INCREMENT,"
                "substitute_id INT UNSIGNED NOT NULL,"
                "substituted_product_id INT UNSIGNED NOT NULL, "
                "user_id INT UNSIGNED NOT NULL,"
                "PRIMARY KEY(id),"
                "FOREIGN KEY (substitute_id) REFERENCES Product(id),"
                "FOREIGN KEY (substituted_product_id) REFERENCES Product(id),"
                "FOREIGN KEY (user_id) REFERENCES User(id)"
                ") ENGINE=INNODB"
                 
}

INSERT = {
    "insert" : 'INSERT INTO %s (%s) VALUES (%s)'
 }


UPDATE = {
     "update_category": 'UPDATE Category SET name = "%s" WHERE id=%s',
     "update_product": 'UPDATE Product SET name = "%s", nutriscore = "%s", url = "%s", store="%s", description="%s", openfoodfact_id="%s", category_id="%s" WHERE id=%s',
     "update_substitute": 'UPDATE Substitute SET substitute_id = "%s", substituted_product_id="%s", user_id="%s" WHERE id=%s'
 }


SELECT = {
    "select_all" : "SELECT * FROM %s",
    "select_all_where": 'SELECT * FROM %s WHERE %s ="%s"',
    "select_proposition_substitute": "SELECT * FROM Product WHERE Category_id = %s AND (Product.nutriscore <= '%s' AND Product.id <> %s) ORDER BY nutriscore ASC LIMIT 1",
    "select_substitute": "SELECT product.id, product.name, product.nutriscore, product.url, product.store, product.description, product.openfoodfact_id, product.category_id from Product Join substitute on (Product.id=%s) WHERE user_id=%s",
    "select_id_user" : " SELECT * FROM User WHERE pseudo in ('%s')",
    "select_id_where_sub_id" : 'SELECT id FROM Substitute WHERE substitute_id= "%s" AND user_id=%s'
    
}
 
DROP = {
    "DROP": "DROP TABLE %s"
}

