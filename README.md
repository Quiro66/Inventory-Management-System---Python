# 🛒 Inventory Management System - Python

## 🧾 Requirements

- Python 3.7+
- Run from terminal: `python main.py`

## 🧠 Funcionalidades

- **📥 Add products**  
Stores product name, price, and quantity in a dynamic structure.
Validates that the entered data is correct and unique.

- **🔍 Consult products**  
Allows you to search for a product by name and display its price and quantity.
If it's not found, the user is notified.

- **💰 Actualizar precios**  
Change the price of an existing product by entering its name and new value.

- **🗑️ Eliminar productos**  
Deletes a product from the inventory by name, if it exists. and you must confirm whether you want to delete it or not.

- **🧮 Calcular valor total del inventario**  
Use a `lambda` function to calculate `price * quantity` for all products.
shows the user the total price of all products with two decimal places.

```bash
-------------------------------
Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
-------------------------------
Choose an option: 1
///ADD PRODUCT///
Add the product name: ps5 pro
add the product price: 3600
Add the product amount: 15
product added successfully
-------------------------------
Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
-------------------------------
Choose an option: 2
///SEARCH PRODUCT///
add name to search for product: ps4
Name: ps4
 Price: $3000
 Amount: 70
-------------------------------
Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
-------------------------------
Choose an option: 3
///UPDATE PRODUCT///
add name to search for product: ps5
Name: ps5
 Price: $5000
 Amount: 20
add new price: 5200
updated product price
Name: ps5
 Price: $5200
 Amount: 20
-------------------------------
Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
-------------------------------
Choose an option: 4
///DELETED PRODUCT///
add name to search for product: xboxone
product does not exist
///DELETED PRODUCT///
add name to search for product: xbox one
Product found
Name: xbox one
Price: $3500
Amount: 20
Do you want to delete the product? enter (y) as if and (n) as not:y
product removed
-------------------------------
Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
-------------------------------
Choose an option: 5
///CALCULATE INVENTORY VALUE///
The calculation of the total value of the inventory is:
$448090.00
-------------------------------
Inventory management
1. Add product
2. Search product
3. Update price product
4. Deleted product
5. calculate inventory value
6. Exit
-------------------------------
Choose an option: 6
```
@quiro66
