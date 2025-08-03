# Importing advanced typing utilities
from typing import List, Tuple, Dict, Union, Optional, Any, Literal, TypedDict, Callable

# Basic Variable Annotations
n: int = 12
name: str = "Harsh"
num: float = 22.2

# Function with parameter and return type hints
def sum_numbers(a: int, b: int) -> int:
    return a + b

print(sum_numbers(12, int(12.2)))  # Explicit cast to match type hint

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type: variable can hold int or str
identifier: Union[int, str] = "ID123"
identifier = 12345  # Also valid

# Optional type: can be str or None
nickname: Optional[str] = None

# Any type: skips type checking
data: Any = "String"
data = 123

# Literal type: restricts allowed values
Status = Literal["pending", "approved", "rejected"]

def update_status(status: Status) -> None:
    print(f"Status updated to {status}")

update_status("approved")

# TypedDict: structured dictionary type
class User(TypedDict):
    name: str
    age: int
    email: str

user1: User = {"name": "Harsh", "age": 25, "email": "harsh@example.com"}

# Type Alias: complex type shortcut
Vector3D = Tuple[float, float, float]

def scale_vector(vector: Vector3D, scalar: float) -> Vector3D:
    return (vector[0] * scalar, vector[1] * scalar, vector[2] * scalar)

# Callable type: functions passed as arguments
def executor(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

print(executor(add, 10, 20))  # Output: 30
