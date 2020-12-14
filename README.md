# AirBnB - clone

<div align="center"><img src="images/Airbnb clone.gif" width="500" height="450"/>

---
<div align="left">

## Resources:books:
Read or watch:
* [cmd - module](https://docs.python.org/3.4/library/cmd.html)
* [uuid - module](https://docs.python.org/3.4/library/uuid.html)
* [Datatime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args / kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)

---
<div align="left">

## Learning Objectives:bulb:
What you should learn from this project:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---
<div align="center">

### [1. BaseModel](./models.base_model.py)
* Class BaseModel that defines all common attributes/methods for other classes.

### [2. Store first object](./models.file_storage.py)
* FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.

### [3. Console 0.0.1](./console.py)
* Contains the entry point of the command interpreter:
---
<div align="left">

## **How it works?**

```python3
Interactive mode:

$ ./console.py

  (hbnb)
```
```python3
Non-Interactive mode:

$ echo "command" | ./console.py

  (hbnb)
```
---
## **Commands**
```
* quit - command for exit the program.

* EOF - Command for quit the console and exit the program.

* create - Command for create a new instance of BaseModel.

* show - Prints the string representation of an instance based on the class name and id

* all - Prints all string representation of all instances based or not on the class name.

* destroy - Deletes an instance based on the class name and id.

* update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
```
---
## Example

```python3
$ ./console.py

$ (hbnb) create BaseModel

$ 911ffd9b-286e-43dd-b877-507d046c7d50

$ (hbnb) show BaseModel 911ffd9b-286e-43dd-b877-507d046c7d50

 [BaseModel] (911ffd9b-286e-43dd-b877-507d046c7d50) {'id': '911ffd9b-286e-43dd-b877-507d046c7d50', 'updated_at': datetime.datetime(2020, 11, 3, 16, 10, 1, 535325), 'created_at': datetime.datetime(2020, 11, 3, 16, 10, 1, 535297)}

$ (hbnb) update BaseModel 911ffd9b-286e-43dd-b877-507d046c7d50 first_name "test"

$ (hbnb) show BaseModel 911ffd9b-286e-43dd-b877-507d046c7d50

 [BaseModel] (911ffd9b-286e-43dd-b877-507d046c7d50) {'id': '911ffd9b-286e-43dd-b877-507d046c7d50', 'updated_at': datetime.datetime(2020, 11, 3, 16, 10, 1, 535325), 'created_at': datetime.datetime(2020, 11, 3, 16, 10, 1, 535297), 'first_name': '"test"'}

$ (hbnb) quit

$
```
---
<div align="center">

## Authors
* **Juliana Monroy Perez** - [julianamonr03](https://github.com/julianamonr03)
<div <li><a href="https://twitter.com/julianamonroy03"><img src="images/TweeterIcon.png"></a></li>
</div>

* **Julian Camilo Torres** - [camilo6](https://github.com/Camilo6)

<div <li><a href="https://twitter.com/CamiloTorresR_"><img src="images/TweeterIcon.png"></a></li>
</div>

# AirBnB_clone_v2
