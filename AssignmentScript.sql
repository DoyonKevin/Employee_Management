USE Assignment;
GO

SELECT * FROM dbo.employees;
SELECT * FROM departments;
SELECT * FROM dbo.addresses;

-- The full data for each Employee with their address as a string, department name, and manager name
SELECT 
	e1.employ_id,e1.employ_name,e1.employ_age,e1.employ_salary,
	e2.employ_name 'Manager Name',
	d.depart_name,
	a1.street_name + ', ' + a1.city_name  + ', ' + a1.state_name AS 'Address'

FROM
	employees e1
LEFT JOIN
	departments d
ON 
	e1.depart_id = d.depart_id
LEFT JOIN
	employees e2
ON
	e2.employ_id = e1.manager_id
LEFT JOIN
	addresses a1
ON 
	e1.address_id = a1.address_id;

-- the 5 highest paid and lowest paid employees
SELECT
	*
FROM
	employees
WHERE
	employ_salary IN (
	SELECT 
		employ_salary
	FROM
		employees
	ORDER BY
		employ_salary DESC
	OFFSET 0 ROWS
	FETCH NEXT 5 ROWS ONLY
	)
UNION
SELECT
	*
FROM
	employees
WHERE
	employ_salary IN(
	SELECT
		employ_salary
	FROM
		employees
	ORDER BY
		employ_salary ASC
	OFFSET 0 ROWS
	FETCH NEXT 5 ROWS ONLY
	)
ORDER BY
	employ_salary DESC;
-- The total salary for each department, the manager's name, sorted by highest total
SELECT
	d.depart_name,e1.employ_name AS 'Manager', SUM(e2.employ_salary) 'Sum Salary'
FROM
	departments d
LEFT JOIN
	employees e1
ON
	 e1.employ_id = d.depart_manage
LEFT JOIN
	employees e2
ON 
	d.depart_id = e2.depart_id
GROUP BY
	d.depart_name, e1.employ_name
ORDER BY
	'Sum Salary' DESC;


-- Each employee that lives in a given state (The state can be hard coded for now)
SELECT
	employ_id, employ_name
FROM
	employees
WHERE
	address_id IN (
	SELECT DISTINCT
		address_id
	FROM
		addresses
	WHERE 
		state_name = 'Texas'
	);