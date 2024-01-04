SELECT Product.product_name, Sales.year, Sales.price
FROM Sales 
inner JOIN Product  ON Sales.product_id = Product.product_id;
