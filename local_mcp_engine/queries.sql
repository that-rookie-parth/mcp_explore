-- name: create_table
CREATE TABLE IF NOT EXISTS people (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT NOT NULL, age INTEGER NOT NULL, 
  profession TEXT NOT NULL
);

-- name: insert_person
INSERT INTO people (name, age, profession) 
VALUES 
  (:name, :age, :profession);

-- name: get_all_people
SELECT * FROM people;

-- name: remove_person
DELETE FROM people WHERE id = :id;