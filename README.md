# Person Class

The `Person` class represents a basic model of a person with attributes such as name, age, and gender. It also includes a method to introduce the person by printing their information.

## Features

- Represents a person with attributes: name, age, and gender.
- Provides a method to introduce the person by printing their information.

## Usage

1. Import the `Person` class into your Python script or interactive environment:

    ```python
    from person import Person
    ```

2. Create an instance of the `Person` class by providing values for the attributes (`name`, `age`, `gender`):

    ```python
    person2 = Person("JaredOkoth", 25, "male")
    ```

3. Call the `introduce()` method on the instance to display the person's information:

    ```python
    person2.introduce()
    ```

    Output:
    ```
    Hi, my name is JaredOkoth. I am 25 years old and my sex is male.
    ```

## Example

```python
from person import Person

# Create a person instance
person2 = Person("JaredOkoth", 25, "male")

# Introduce the person
person2.introduce()

