# 🏦 BankAccount - Encapsulation in Python

This project demonstrates **encapsulation**, one of the core principles of Object-Oriented Programming (OOP), using a simulated **secure bank account system** in Python.

It highlights:
- Private attributes using double underscores (`__`)
- Controlled access to internal data through public methods
- Data hiding and name mangling
- A realistic use case: managing a bank account's balance and transaction history securely

---

## 📁 Files

| File             | Description                                      |
|------------------|--------------------------------------------------|
| `bank_account.py`| Contains the `BankAccount` class implementation |
| `README.md`      | This documentation file                         |

---

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   
2. Navigate to the project directory:
   ```bash
   cd <your-repo-name>
   ```

## Usage

Run the program with:

```bash
python bank_account.py
```

### Sample Output

```
Deposited 200
Withdrew 100
Balance: 600
Accessing transaction history...
History: ['Deposited 200', 'Withdrew 100']
Error: 'BankAccount' object has no attribute '__log_access'
Updated Balance: 1000
```

## Encapsulation Benefits

Encapsulation protects internal state, making code:
- More secure
- Easier to debug and maintain
- Less prone to unexpected external interference

## Name Mangling

Private attributes like `__balance` use name mangling. Accessing them is possible but discouraged:

```python
print(account._BankAccount__balance)  # Avoid this!
```

Python’s private variables are a convention, not strictly enforced. Respect this for code integrity.

## References

- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Encapsulation in Python](https://www.geeksforgeeks.org/encapsulation-in-python/)

