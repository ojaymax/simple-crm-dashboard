  -- Create Contacts Table
CREATE TABLE contacts (
    contact_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    company VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Interactions Table
CREATE TABLE interactions (
    interaction_id INT PRIMARY KEY AUTO_INCREMENT,
    contact_id INT,
    type VARCHAR(50),
    notes TEXT,
    interaction_date DATETIME,
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id)
);

-- Create Deals Table
CREATE TABLE deals (
    deal_id INT PRIMARY KEY AUTO_INCREMENT,
    contact_id INT,
    deal_name VARCHAR(100),
    deal_stage VARCHAR(50),
    amount DECIMAL(10, 2),
    expected_close_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id)
);

-- Create Tasks Table
CREATE TABLE tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    contact_id INT,
    task_description VARCHAR(255),
    due_date DATE,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id)
);

-- Create Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(50)
);

-- Insert Sample Contacts
INSERT INTO contacts (name, email, phone, company)
VALUES 
('John Doe', 'john@example.com', '08012345678', 'Doe Ltd'),
('Sarah James', 'sarah@brightsolutions.com', '08145678901', 'Bright Solutions'),
('Michael Ade', 'michael@adeholdings.com', '08099887766', 'Ade Holdings');

-- Insert Interactions
INSERT INTO interactions (contact_id, type, notes, interaction_date)
VALUES 
(1, 'Call', 'Discussed website redesign options', '2025-06-15 10:30:00'),
(2, 'Email', 'Sent proposal for software project', '2025-06-20 14:45:00'),
(3, 'Meeting', 'Met at conference, shared company profile', '2025-06-10 09:00:00');

-- Insert Deals
INSERT INTO deals (contact_id, deal_name, deal_stage, amount, expected_close_date, status)
VALUES 
(1, 'Website Redesign', 'negotiation', 2000.00, '2025-07-15', 'open'),
(2, 'CRM System Purchase', 'prospect', 5000.00, '2025-08-01', 'open'),
(3, 'Mobile App Development', 'closed-won', 8000.00, '2025-05-30', 'closed-won');

-- Insert Tasks
INSERT INTO tasks (contact_id, task_description, due_date, is_completed)
VALUES 
(1, 'Follow up on proposal', '2025-06-28', FALSE),
(2, 'Call to schedule demo', '2025-06-27', FALSE),
(3, 'Send invoice', '2025-06-25', TRUE);

-- Insert Users
INSERT INTO users (name, email, role)
VALUES 
('Victor Lucky', 'victor@example.com', 'Account Manager'),
('Jane Smith', 'jane@company.com', 'Sales Lead');
