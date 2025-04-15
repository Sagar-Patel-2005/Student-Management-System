-- This SQL file defines the schema for the Student Management System database.

-- Drop the students table if it exists (for development/testing purposes)
DROP TABLE IF EXISTS students;

-- Create the students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_number TEXT UNIQUE NOT NULL,
    grade TEXT
);

-- You can optionally insert some initial data here for testing:
-- INSERT INTO students (name, roll_number, grade) VALUES ('Alice', 'A101', '10');
-- INSERT INTO students (name, roll_number, grade) VALUES ('Bob', 'B202', '9');