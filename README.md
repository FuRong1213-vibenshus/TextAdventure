# TextAdventure

This repo is used to store all the projects that implementing the game Text Adventure, in a way so called "stepvis improvement"". 
We start by analysing a simple game written in structure of imperitive / procedure programming. Herby our first concept is introduced:

## Programing Paradigm
The definitions of paragraming paradigm can be found in the book "Programmering" from systime **[Programmeringsparadigmer](https://https://programmering.systime.dk/?id=178)**.


> **Further Reading: Programming paradigme**
  > - https://da.wikipedia.org/wiki/Programmeringsparadigme
  > - https://da.alegsaonline.com/art/79379


In the following 4-5 weekes, we are going to focus on re-writting the code of this game while adding the following new features and concepts

* Classes and inheritance
* Flow chart and UML diagram
* Modules and packages
* Design Principles and Design Patterns* 
  - State pattern*

The goal of this project is to let you gain the following skills:
* Analysis and illustrate code structure by class diagram UML and/or flow chart.
* Apply advanced constructions in your programming, i.e. object-oriented programming with Polymorphism. 
* Organize your code into modules and packages. 
* Be able to code in a more well-structured way and give argumentation* (design patterns and principles). 


## Introduction
The game "text adventure" is a type of IF (Interactive Fiction), here is one example:
https://eblong.com/zarf/zweb/dreamhold/

## Step 1
In this step we start to look at the game that are coded in the way of "procedural programming". 

* We should describe the internal logic of the game with flow chart

### **Flow chart**

This article [Rutediagrammer](https://programmering.systime.dk/?id=148) introduces the basic technical skills of drawing flow chart.

> **Further reading: Flow Chart**
  > - https://en.wikipedia.org/wiki/Flowchart#Common_symbols

### **Function calls\***
> **Extra Reading: funcation calls and memory management**
 > - https://www.youtube.com/watch?v=OdQSWuG78Sk
 > - https://eecs280staff.github.io/notes/02_ProceduralAbstraction_Testing.html 


## Step 2

In this step, we should 
* Rewrite the code into object-oriendted structure 
* Draw the class diagram of UML
* Organize the code into modules and packages

### **Class inheritance and polymorphism**
- Some useful reading materials: 
  * **[Objektorienteret Programmering](https://programmering.systime.dk/?id=207)**
  * https://thepythonguru.com/python-inheritance-and-polymorphism/
  * https://www.programiz.com/python-programming/polymorphism
  * https://www.geeksforgeeks.org/difference-between-inheritance-and-polymorphism/

- Exercises: https://pynative.com/python-object-oriented-programming-oop-exercise/


### **Class diagram**
*Do it yourself*: read through the [UML tutuorial]( https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/) and try answer the following questions:
 - What is UML class diagram ? What can UML class diagram visualize ?
 - What are the three main components in the UML Class notation
 - This tutorial https://www.gleek.io/blog/class-diagram-arrows.html introduced several relations between classes. In our project, we are going to use the following ones. Make sure that you understand the meaning of these relations.
 can you find examples of each relation from the game text adventure ?
    - Generalization
    - Association
    - Aggregation
    - Composition
- Analyse the "class diagram for an ATM system" in this article, https://www.lucidchart.com/pages/uml-class-diagram. Describe the relations between the classes **Bank**, **Customer**, **ATM**, **Account**, **ATM transactions**, **Current Account** and **Saving Account**

### **Packages and Modules**

Read **Carfully** through the tutorial of python modules and try to answer the following question
https://docs.python.org/3/tutorial/modules.html

- What is a module in python and why do we need "modules"? josef
- How to get access the module name ? fabian
- How do we make a module which are both executable and importable (by using the variable __name__) alfred? 
- In how many ways can you import a module (william)?
- What can standard module sys do Dona?
- what is packages sahel?
- what is \_\_init__.py in a package (anna thore)?

### Do it yourself
- try to make a small project as described in this link
https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
- Analyse the dependencies in step2 
  - by hand
  - by tools pydeps https://github.com/thebjorn/pydeps

## Step 3
In thi step our program is improved with a loading function, which can read the a text based map and load the geographical information of scenes as part of the game initialization. 

The goal of this step is to repeat the concept of data types and data processing in python. 

### Data Types
- [list](https://docs.python.org/3/tutorial/datastructures.html)
  * [W3school](https://www.w3schools.com/python/python_lists.asp)
  * [Programiz](https://www.programiz.com/python-programming/list)
- [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
  * [W3school](https://www.w3schools.com/python/python_dictionaries.asp)
  * [RealPython](https://realpython.com/python-dicts/)
- [numpy array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
  * [Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html) 

### Data Processing
- [map](https://realpython.com/python-map-function/) 
- [lambda functions](https://www.w3schools.com/python/python_lambda.asp)


## Exercise

- [A Prize No One Can Win](https://open.kattis.com/problems/aprizenonecanwin)
- [Heir's Dilemma](https://open.kattis.com/problems/heirsdilemma)
- [Best Relay Team](https://open.kattis.com/problems/bestrelayteam)
- [SMIL](https://open.kattis.com/problems/smil)
- [Ferry Loading](https://open.kattis.com/problems/ferryloading4)
- [A Classy Problem](https://open.kattis.com/problems/classy)
- [Harshad Numbers](https://open.kattis.com/problems/harshadnumbers)



## Step 4

We are going to refactor our code by adding more consideration in software design principles and eventually, applying the state pattern to achieve a cleaner, better maintainable result.

### **Design Principles SOLID\***
This article explains the SOLID principles in software design. https://towardsdatascience.com/solid-coding-in-python-1281392a6a94



### **Design Pattern\*** 
#### **Concept**
> **Further reading**
> (For them are interested, not but required)
> https://www.netsolutions.com/insights/software-design-pattern/
#### **State pattern**

https://refactoring.guru/design-patterns/state/python/example 

>**Do it yourself**: Draw the class diagram uml of this code. [state_concepts.py](https://github.com/FuRong1213-vibenshus/TextAdventure/blob/a513665ff777145cdc6a1f0149fba91f05208cec/state_concepts.py)

#### **Implementation**
I am using this package [transitions](https://github.com/pytransitions/transitions#hsm) for the part of state machine implementation in step 4. 



## Home Work
- Change the codes of text adventure in Step1 into object oriented. You can follow the steps:
  1. Make a list of all the involved objects in the game. 
  2. Add the attributes and operations (methods) to each object (class) 
  3. Draw the UML class diagram. 
  4. Implement according to the UML. 
  5. Organize the project into properly modules and packages *

Or if you'd rather make you own story
- Make a sketch (in words or drawing or both) of your own text adventure game. It must include at least four scenes, two characters, some inventories to collect and a win condition.
- Follow the 1,2,3,4 from above











