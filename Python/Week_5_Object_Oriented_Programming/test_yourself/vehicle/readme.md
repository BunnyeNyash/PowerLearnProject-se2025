# Vehicle Management System

A Python program demonstrating object-oriented programming (OOP) principles through a vehicle management system. The program uses abstract classes, inheritance, and properties to model different vehicles and their behaviors.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your_repo_name
   ```

## Usage

Run the program with:

```bash
python vehicle_management.py
```

## Sample Output

The following output is produced when running the program:

```
Tesla moves silently on electricity.
Tesla uses Electricity power.
Starting Tesla's engine...
----------------------------
Yamaha zooms ahead on two wheels.
Yamaha uses Petrol power.
Starting Yamaha's engine...
----------------------------
Jeep drives off-road with diesel power.
Jeep uses Diesel power.
Starting Jeep's engine...
----------------------------
```

## Program Overview

The Vehicle Management System showcases OOP concepts in Python:

- **Abstract Base Class**: The `Vehicle` class uses `ABC` to define a blueprint with abstract methods (`move`, `fuel_type`) and an abstract property (`vehicle_type`) that subclasses must implement.
- **Inheritance**: `Car`, `Bike`, and `ElectricScooter` inherit from `Vehicle`, providing specific implementations for abstract methods.
- **Polymorphism**: Each vehicle type responds to the same method calls (`move`, `fuel_type`, `start_engine`) with unique behaviors.
- **Properties**: The `describe` property provides a formatted description, and `vehicle_type` is defined as an abstract property (though not implemented in `ElectricScooter` in the provided code, which may raise an error if accessed).
- **Encapsulation**: Vehicle attributes (e.g., `name`, `max_speed`) are managed within the class, with behaviors defined through methods.

**Note**: The `vehicle_type` property is abstract but not implemented in the provided subclasses. This could raise a `NotImplementedError` if accessed. The sample output suggests the code runs without accessing `vehicle_type`.

This design promotes extensibility, allowing new vehicle types to be added easily.

## Requirements

- Python 3.x

No additional dependencies are required.

## 📚 References

- [Python Official Documentation: Classes and Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)
- [Abstract Base Classes in Python (Python Documentation)](https://docs.python.org/3/library/abc.html)
- [Python Properties - Real Python](https://realpython.com/python-property/)
- [Inheritance and Polymorphism in Python - GeeksforGeeks](https://www.geeksforgeeks.org/inheritance-and-polymorphism-in-python/)
