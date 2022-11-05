# TextAdventure

This repo is used to store all the projects that implementing the game Text Adventure, in a way so called "stepvis improvement"". 
We start by analysing a simple game written in structure of imperitive / functional programming

> **Further Reading: Programming paradigme**
  > - https://da.wikipedia.org/wiki/Programmeringsparadigme
  > - https://da.alegsaonline.com/art/79379


In the following 4-5 weekes, we are going to focus on re-writting the game while adding the following new features and concepts

* Class and inheritance
* Flow chart and UML diagram
* Modules and packages
* Design Principles and Design Patterns 
  - State pattern

During the project, you should be able to handle the following skills:
* Analysis and illustrate code structure by class diagram UML and/or flow chart.
* Apply advanced constructions in your programming, i.e. object-oriented programming with Polymorphism. 
* Organize your code into modules and packages. 
* Be able to code in a more well-structured way and give argumentation (design patterns and principles). 


## Introduction

The game "text adventure" is a type of IF (Interactive Fiction), here is one example:
https://eblong.com/zarf/zweb/dreamhold/

## Step 1
In this step we start to look at the game that are coded in the way of "functional programming". 

* We should describe the internal logic of the game with flow chart

### **Flow chart**

> **Further reading: Flow Chart**
  > - https://en.wikipedia.org/wiki/Flowchart#Common_symbols

> **Extra Reading: funcation calls and memory management**
 > - https://www.youtube.com/watch?v=OdQSWuG78Sk
 > - https://eecs280staff.github.io/notes/02_ProceduralAbstraction_Testing.html 


## Step 2

In this step, we should 
* Rewrite the code into object-oriendted structure 
* Draw the class diagram of UML
* Organize the code into modules and packages

### **Class inheritance and polymorphism**
- Explanation:
https://www.programiz.com/python-programming/polymorphism

- Exercises: https://pynative.com/python-object-oriented-programming-oop-exercise/

### **Class diagram**
*Do it yourself*: read through the UML tutuorial https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/ and try answer the following questions:
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

Read through the tutorial of python modules and try to answer the following question
https://docs.python.org/3/tutorial/modules.html

- What is a module in python and why do we need "modules"?
- How to get access the module name ?
- How do we make a module which are both executable and importable (by using the variable __name__)? 
- In how many ways can you import a module ?
- What can standard module sys do ?

- what is packages ?
- what is \_\_init__.py in a package ?


## Home Work
> - Change the codes of text adventure in Step1 into object oriented. You can follow the steps:
>> 1. Make a list of all the involved objects in the game. 
>> 2. Add the attributes and operations (methods) to each object (class) 
>> 3. Draw the UML class diagram. 
>> 4. Implement according to the UML (Optional, can wait til next time)

Or if you'd rather make you own story
> - Make a sketch (in words or drawing or both) of your own text adventure game. It must include at least four scenes, two characters, some inventories to collect and a win condition.
> - Follow the 1,2,3,4 from above











