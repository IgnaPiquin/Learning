import sqlite3

# Connect to the database
connection = sqlite3.connect('FirstPracticeProyect.db')
cursor = connection.cursor()

# Sample data for CategoryID, ProductName, ProductPrice, ProductQuantity
data = [
    (2, "Manaos", 200, 10),
    (7, "Cocaine", 150, 5),
    (8, "Pork Belly", 300, 8),
    (9, "Banana", 100, 12)
]

# Adding 50 rows with different CategoryIDs from the data list
for _ in range(1):
    for category_id, product_name, product_price, product_quantity in data:
        query = f'''
            INSERT INTO Purchases (PurchaseDate, CategoryID, ProductName, ProductPrice, ProductQuantity)
            VALUES("2023-06-11", {category_id}, "{product_name}", {product_price}, {product_quantity});
        '''
        cursor.execute(query)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Rows added successfully!")