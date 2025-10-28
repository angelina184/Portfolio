SELECT * FROM table_issued;

-- project tasks
-- Create a New Book Record
-- "978-1-60129-456-2', 'To Kill a Mockingbird', 'Classic', 6.00, 'yes', 'Harper Lee', 'J.B. Lippincott & Co.')"
-- VERCHAR mist be iside ' ' not in " "
SELECT * FROM books;
-- adds at the end
INSERT INTO books(isbn, book_title, category, rental_price, status, author, publisher) 
VALUES ('978-1-60129-456-2', 'To Kill a Mockingbird', 'Classic', 6.00, 'yes', 'Harper Lee', 'J.B. Lippincott & Co.');

--Update an Existing Member's Address
SELECT * FROM members;
-- UPDATES AND adds at the end
UPDATE members
SET
	member_address = '100 Vlad St'
WHERE member_id = 'C101';

--Delete a Record from the Issued Status Table 
-- Objective: Delete the record with issued_id = 'IS121' from the issued_status table.
SELECT * FROM issued_table;
DELETE FROM issued_table
WHERE issued_id = 'IS121';

--Task 4: Retrieve All Books Issued by a Specific Employee 
-- Objective: Select all books issued by the employee with emp_id = 'E101'.

SELECT *
FROM issued_table
WHERE issued_emp_id = 'E101'


--Task 5: List Members Who Have Issued More Than One Book 
-- Objective: Use GROUP BY to find members who have issued more than one book.
SELECT 
	issued_emp_id,
	COUNT(issued_id) AS nb_books_issued
FROM issued_table
GROUP BY 1
HAVING COUNT(issued_id) > 1

--Task 6: Create Summary Tables: Used CTAS to generate new tables based on query results 
-- each book and total book_issued_cnt**
CREATE TABLE book_cnts
AS
SELECT 
	b.isbn,
	b.book_title,
	COUNT(ist.issued_book_isbn) AS nb_issued
FROM books as b
JOIN issued_table as ist
ON ist.issued_book_isbn = b.isbn
GROUP BY 1,2;

SELECT * FROM books
book_cnts;


-- Task 7. Retrieve All Books in a Specific Category
SELECT * FROM issued_table
WHERE category = 'Classic'
-- Task 8: Find Total Rental Income by Category and number of times it was issued
SELECT 
	b.category,
	SUM(b.rental_price),
	COUNT(b.category)
FROM books as b
INNER JOIN issued_table as it
ON it.issued_book_isbn = b.isbn
GROUP BY category;

--9.List Members Who Registered in the Last 180 Days
SELECT * FROM members
WHERE reg_date >= CURRENT_DATE - INTERVAL '180 days'
SELECT CURRENT_DATE
INSERT INTO members(member_id, member_name, member_address, reg_date)
VALUES 
('C320','Sam','234 Zanb St','2025-06-01'),
('C329','Jam','134 Zarg St','2025-06-03'),
('C317','Dam','254 Lanb St','2025-05-01');


--10.List Employees with Their Branch Manager's Name and their branch details
SELECT * FROM employees
SELECT * FROM branch

SELECT e1.*,
		e2.emp_name as manager,
		b.manager_id
FROM employees as e1
JOIN branch as b
ON b.branch_id = e1.branch_id

JOIN employees as e2
ON b.manager_id = e2.emp_id
	
-- 11.Create a Table of Books with Rental Price Above a Certain Threshold, threshold = 5
CREATE TABLE books_price_gt5
AS
SELECT * FROM books
WHERE rental_price >= 5 

SELECT * FROM books_price_gt5

--12.Retrieve the List of Books Not Yet Returned
SELECT * FROM return_status
SELECT * FROM issued_table
SELECT * FROM members

SELECT 
	DISTINCT it.issued_book_name
FROM issued_table AS it
LEFT JOIN return_status AS rs
ON rs.issued_id = it.issued_id
WHERE rs.return_date is null


-- Task 13: Identify Members with Overdue Books
-- Write a query to identify members who have overdue books (assume a 30-day return period). 
--Display the member's_id, member's name, book title, issue date, and days overdue
-- 2024-08-24

SELECT 
	it.issued_member_id,
	m.member_name,
	it.issued_book_name,
	it.issued_date,
	rs.return_date,
	DATE '2024-08-24' - it.issued_date as over_due_days
FROM members as m
JOIN issued_table as it
ON it.issued_member_id = m.member_id

LEFT JOIN  return_status as rs
ON it.issued_id = rs.issued_id
WHERE 
	(it.issued_date + INTERVAL '30 days') > DATE '2024-08-24'
	OR
	rs.return_date IS NULL
ORDER BY 1

--------------------------------------
SELECT 
    ist.issued_member_id,
    m.member_name,
    ist.issued_date,
    -- rs.return_date,
    DATE '2024-08-24' - ist.issued_date as over_dues_days
FROM issued_table as ist
JOIN 
members as m
    ON m.member_id = ist.issued_member_id

LEFT JOIN 
return_status as rs
ON rs.issued_id = ist.issued_id
WHERE 
    rs.return_date IS NULL
    AND
    (DATE '2024-08-24' - ist.issued_date) > 30
ORDER BY 1

--Task 14: Update Book Status on Return
--Write a query to update the status of books in the books table to "Yes" when they are returned (based on entries in the return_status table).
UPDATE books
SET status = 'no'
WHERE isbn = '978-0-451-52994-2';

--UPDATE RETURN STATUS MANUALLY
ALTER TABLE return_status
ADD COLUMN book_qualiti VARCHAR(15);

UPDATE return_status  
SET book_qualiti = 'Good';

INSERT INTO return_status (return_id, issued_id, return_date, book_qualiti)
VALUES ('RS124', 'IS130', CURRENT_DATE, 'Bad');

UPDATE books
SET status = 'yes'
WHERE isbn = '978-0-451-52994-2';

--Store Procedures (automaticly)
CREATE OR REPLACE PROCEDURE add_return_records(
	p_return_id VARCHAR(10),
	p_issued_id VARCHAR(10),
	p_book_quality VARCHAR(15)
)
LANGUAGE plpgsql
AS $$
DECLARE --for declaring variables
	var_isbn VARCHAR(20);
	var_book_name VARCHAR(75);
BEGIN
	--all logic
	-- insert into return_status when user writed data about the book they return
	INSERT INTO return_status (return_id, issued_id, return_date, book_qualiti)
	VALUES (p_return_id, p_issued_id, CURRENT_DATE, p_book_quality);

	SELECT 
		issued_book_isbn,
		issued_book_name
	INTO
		var_isbn,
		var_book_name
	FROM issued_table
	WHERE issued_id = p_issued_id;
	
	UPDATE books
	SET status = 'yes'
	WHERE isbn = var_isbn;

	RAISE NOTICE 'Thank you for returning the book: %', var_book_name;
END;
$$;


--Testing Function add_return_records()
issued_id ='IS135'
ISBN = '978-0-307-58837-1'

SELECT * FROM issued_table
WHERE issued_book_isbn = '978-0-307-58837-1';

SELECT * FROM return_status
--DELETE FROM return_status
WHERE issued_id = 'IS135';

SELECT * FROM books
WHERE isbn = '978-0-307-58837-1';
--calling function
CALL add_return_records('RS444', 'IS135', 'Good');


--task 15: Branch Performance Report
--Create a query that generates a performance report for each branch, showing the number of books issued, the number of books returned, and the total revenue generated from book rentals.

select * from branch

--return_id
select * from return_status

--issued_emp_id,issued_id
select * from issued_table

--branch_id
select * from employees

--rental_price
select * from books

CREATE TABLE branch_reports AS
SELECT 
	br.branch_id,
	br.manager_id,
	COUNT(it.issued_id) AS number_bk_issuesd,
	COUNT(rs.return_id) AS nb_bk_returned,
	SUM(b.rental_price) AS total_revenue
FROM branch AS br
JOIN employees AS e ON br.branch_id = e.branch_id
JOIN issued_table AS it ON it.issued_emp_id = e.emp_id
LEFT JOIN return_status AS rs ON it.issued_id = rs.issued_id
JOIN books AS b ON it.issued_book_isbn = b.isbn
GROUP BY 1, 2;

--Task 16: CTAS: Create a Table of Active Members
-- Use the CREATE TABLE AS (CTAS) statement to create a new table active_members containing members who have issued at least one book in the last 2 months.
SELECT DISTINCT issued_member_id
FROM issued_table
WHERE issued_date > (DATE '2024-06-24' - INTERVAL '6 month');

SELECT *
FROM members
WHERE member_id IN (
	SELECT DISTINCT issued_member_id
	FROM issued_table
	WHERE issued_date > (DATE '2024-06-24' - INTERVAL '6 month')
);
--Task 17: Find Employees with the Most Book Issues Processed
--Write a query to find the top 3 employees who have processed the most book issues. 
--Display the employee name, number of books processed, and their branch.


SELECT * FROM employees;
SELECT 
	e.emp_name,
	--everything from branch
	b.*,
	COUNT(it.issued_id) AS nb_book_issued
FROM issued_table AS it
JOIN employees AS e ON e.emp_id = it.issued_emp_id 
JOIN branch AS b ON b.branch_id = e.branch_id
GROUP BY 1, 2
ORDER BY nb_book_issued DESC
LIMIT 3;


/*
Task 19: Stored Procedure Objective: 
Create a stored procedure:
    -manage the status of books in a library system. 
	
Description: Write a stored procedure that updates the status of a book in the library based on its issuance. 
The procedure should function as follows: The stored procedure should take the book_id as an input parameter.
 -check if the book is available (status = 'yes'). 
 - If the book is available, it should be issued, and the status in the books table should be updated to 'no'. 
  If(status = 'no'), the procedure should return an error message indicating that the book is currently not available.

*/

SELECT * FROM books;
SELECT * FROM issued_table;

CREATE OR REPLACE PROCEDURE add_issue_book(
	p_issued_id VARCHAR(10),
	p_issued_member_id VARCHAR(10),
	p_issued_book_isbn VARCHAR(25),
	p_issued_emp_id VARCHAR(10)
	--procedure languege postgres sql
LANGUAGE plpgsql
AS $$ --start of function body
DECLARE
	var_status VARCHAR(10);
BEGIN
	--checks if the book is available (status = yes)
	SELECT 
		status
	INTO
		var_status
	FROM books
	--certain line with data not the whole table
	WHERE isbn = p_issued_book_isbn;

	IF var_status = 'yes' THEN
		INSERT INTO issued_table (issued_id, issued_member_id, issued_date, issued_book_isbn, issued_emp_id)
		VALUES (p_issued_id, p_issued_member_id, CURRENT_DATE, p_issued_book_isbn, p_issued_emp_id);	
		RAISE NOTICE 'Book record added successfully for book ISBN %', p_issued_book_isbn; 

		UPDATE books
		SET status = 'no'
		WHERE isbn = p_issued_book_isbn;
	ELSE
		RAISE NOTICE 'Book is not available, book ISBN: %', p_issued_book_isbn; 
	END IF;
END;
$$;

--Testing
SELECT * FROM books
WHERE isbn = '978-0-375-41398-8';
--'978-0-553-29698-2' -- yes
--'978-0-375-41398-8' -- no

SELECT * FROM issued_table;

CALL add_issue_book('IS141', 'C110', '978-0-553-29698-2', 'E104');
CALL add_issue_book('IS142', 'C110', '978-0-375-41398-8', 'E104');



