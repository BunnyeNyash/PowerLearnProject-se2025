# Zoo Management System

A Python program demonstrating object-oriented programming (OOP) principles through a simple zoo management system. The program uses abstract classes, inheritance, and polymorphism to model different animals and their behaviors.

## Installation

1. Clone the repository:
   ```bash
   git clone  git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your_repo_name
   ```

## Usage

Run the program with:

```bash
python zoo_management.py
```

## Sample Output

The following output is produced when running the program:

```
Simba is a lion
Simba says Roar
Simba eats meat.
Simba goes to sleep

Ndovu is a elephant
Ndovu says Trumpet
Ndovu eats grass.
Ndovu goes to sleep

Bunnye is a parrot
Bunnye says Squawk
Bunnye eats seeds.
Bunnye goes to sleep
```

## Program Overview

The Zoo Management System showcases OOP concepts in Python:

- **Abstract Base Class**: The `Animal` class uses `ABC` to define a blueprint with abstract methods (`make_sound` and `eat`) that subclasses must implement.
- **Inheritance**: `Lion`, `Elephant`, and `Parrot` inherit from `Animal`, providing specific implementations for abstract methods.
- **Polymorphism**: Each animal type responds to the same method calls (`describe`, `make_sound`, `eat`, `sleep`) with unique behaviors.
- **Encapsulation**: Animal properties (e.g., `name`) are managed within the class, with behaviors defined through methods.

This design ensures flexibility and extensibility, allowing new animal types to be added easily.

## Requirements

- Python 3.x

No additional dependencies are required.

## 📚 References

- [Python Official Documentation: Classes and Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)
- [Abstract Base Classes in Python (Python Documentation)](https://docs.python.org/3/library/abc.html)
- [Object-Oriented Programming in Python - Real Python](https://realpython.com/python3-object-oriented-programming/)
- [Inheritance and Polymorphism in Python - GeeksforGeeks](https://www.geeksforgeeks.org/inheritance-and-polymorphism-in-python/)
