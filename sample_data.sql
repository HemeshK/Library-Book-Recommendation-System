-- Insert Users
INSERT INTO Users (name) VALUES
('Alice'),
('Bob'),
('Charlie'),
('Diana'),
('Ethan'),
('Fiona');

-- Insert Books
INSERT INTO Books (title, author) VALUES
('Pride and Prejudice', 'Jane Austen'),
('1984', 'George Orwell'),
('The Great Gatsby', 'F. Scott Fitzgerald'),
('To Kill a Mockingbird', 'Harper Lee'),
('Moby-Dick', 'Herman Melville'),
('Harry Potter and the Sorcerers Stone', 'J.K. Rowling'),
('The Lord of the Rings', 'J.R.R. Tolkien'),
('The Catcher in the Rye', 'J.D. Salinger'),
('Brave New World', 'Aldous Huxley'),
('The Hobbit', 'J.R.R. Tolkien');

-- Insert Borrow History
INSERT INTO BorrowHistory (user_id, book_id, borrow_date) VALUES
-- Alice borrows
(1, 1, '2025-01-10'),
(1, 2, '2025-01-15'),
(1, 6, '2025-02-01'),

-- Bob borrows
(2, 2, '2025-01-20'),
(2, 3, '2025-01-25'),
(2, 7, '2025-02-02'),

-- Charlie borrows
(3, 1, '2025-01-18'),
(3, 4, '2025-02-05'),
(3, 8, '2025-02-12'),

-- Diana borrows
(4, 5, '2025-02-01'),
(4, 6, '2025-02-08'),
(4, 9, '2025-02-15'),

-- Ethan borrows
(5, 3, '2025-01-22'),
(5, 7, '2025-02-10'),
(5, 10, '2025-02-18'),

-- Fiona borrows
(6, 4, '2025-01-30'),
(6, 8, '2025-02-11'),
(6, 10, '2025-02-20');
