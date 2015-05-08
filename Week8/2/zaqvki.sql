SELECT FirstName || " " || LastName AS employee_name, Title AS title
FROM employees;

SELECT *
FROM employees
WHERE city = "Seattle";

SELECT *
FROM employees
WHERE city = "London";

SELECT FirstName || ' ' || LastName AS employee_name, Title AS title
FROM employees
WHERE Title LIKE "%Sales%";

SELECT  FirstName || ' ' || LastName AS employee_name, TitleOfCourtesy AS title_of_courtesy, Title AS title
FROM employees
WHERE TitleOfCourtesy IN ('Ms.', 'Mrs.') AND  Title LIKE "%Sales%";

SELECT  FirstName || ' ' || LastName AS employee_name, BirthDate AS birth_date
FROM employees
ORDER BY BirthDate
LIMIT 5;

SELECT  FirstName || ' ' || LastName AS employee_name, HireDate AS hire_date
FROM employees
ORDER BY HireDate
LIMIT 5;

SELECT FirstName || ' ' || LastName AS employee_name, ReportsTo AS reports_to
FROM employees
WHERE ReportsTo IS NULL;

SELECT employee.FirstNam || " " || employee.LastName AS employee_name,
       boss.FirstName || " " || boss.LastName AS boss_name
FROM employees employee JOIN employees boss
WHERE employee.ReportsTo = boss.EmployeeID;

SELECT  COUNT(EmployeeID) AS number_of_female_employees
FROM employees
WHERE TitleOfCourtesy IN ('Ms.', 'Mrs.');

SELECT  COUNT(EmployeeID) AS number_of_male_employees
FROM employees
WHERE TitleOfCourtesy IN ('Mr.');

SELECT City,  COUNT(EmployeeID) 
FROM employees
GROUP BY City;

SELECT FirstName || ' ' || LastName AS employee_name, Orders.ordersID AS order_id
FROM Employees JOIN Orders
ON Employees.employeeID = Orders.EmployeeID;

SELECT orders.orderID AS order_id, shippers.CompanyName AS company_name
FROM orders JOIN shippers
ON orders.shipVia = shippers.shipperID;

SELECT ShipCountry AS ship_country, COUNT(OrderID) AS order_count
FROM Orders
GROUP BY ShipCountry
ORDER BY order_count DESC;

SELECT COUNT(orders.OrderID), employees.FirstName || ' ' || employees.LastName AS employee_name
FROM orders JOIN employees
ON orders.EmployeeID = employees.EmployeeID
GROUP BY orders.EmployeeID
ORDER BY COUNT(orders.OrderID) DESC
LIMIT 1;

SELECT COUNT(orders.OrderID), customers.ContactName AS customer_name
FROM orders JOIN customers
ON orders.CustomerID = customers.CustomerID
GROUP BY orders.CustomerID
ORDER BY COUNT(orders.OrderID) DESC
LIMIT 1;

SELECT orders.OrderID AS order_id, 
		employees.FirstName || ' ' || employees.LastName AS employee_name, 
		customers.ContactName AS customer_name
FROM orders JOIN employees
ON orders.EmployeeID = employees.EmployeeID
JOIN customers
ON orders.CustomerID = customers.CustomerID

SELECT customers.ContactName AS customer_name, orders.ShipName AS shipper_name
FROM customers
JOIN orders ON customers.CustomerID IN (
SELECT orders.CustomerID
FROM orders
WHERE orders.ShipVia = shippers.ShipperID);












