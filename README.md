# Online Catalogue & Shop Management

Python & MySQL

### Key Features of [NG_random_search.py](NG_random_search.py)
| Feature | Description |
|:--:|:--:|
| Run Counter | It keeps a track of how many times the program has been executed since `13th May 2022`. It uses file handling on [run.txt](run.txt) to do so. |
| Keyword Search | You don't need to enter name of country, denomination and currency type separately, you can give input in any order in a single statement. |


## Abstract

In this project, we will try to develop an interface to facilitate the posting and fetching of information about currency which is part of our collection. The idea is to develop a program that will allow viewers of the collection to look for the currency they are interested in by entering the country it belongs to. In case the collector does not have any currency of that country, it will allow the user to add information about it from his side by filling details in fields like year, description, country, denomination and composition. In case the currency the user is looking for is present in the collection, the user will be presented with a choice whether he is looking for a coin or a banknote. Based on the user input, the interface will display all the relevant currency and the user will be able to search for a particular currency by entering its denomination. The user will be able to view the information of the currency and whether it is available for trading or not.
In this project, we will also allow the users to create customer accounts, where they can see the cart subtotal and the items, if they wish to buy currency which is available for sale. 
The essence of this project is to create a fully functional interactive collection display gallery as seen on the instagram page owned by us [@numismatic_gallery_](https://instagram.com/numismatic_gallery_)

---

## Introduction of the Numismatic Gallery Management System

We will make this project by using Python and text file handling. It will be a menu-driven program, in which we will use different user-defined functions for different actions that the user wants to perform. Some of the actions that the user will be able to perform are:
<pre>
✯ View details                          ✯ Add details
✯ Delete details                        ✯ Admin mode  
✯ User login                            ✯ Update details
✯ View Cart                             ✯ Exit
</pre>

Some of the functions that we will develop for the same purpose are as follows:

<mark>Functions developed:</mark>

***country( )***: This function will look at whether the currency of the entered country exists in the collection or not.

***add_coin( )***: This function will help the user to enter information about the currency coin that is not yet part of the collection.

***add_note( )***: This function will help the user to enter information about the currency note that is not yet part of the collection.

***delete_coin( )***: This function will help the user to delete information about the currency coin which may be incorrect.

***delete_note( )***: This function will help the user to delete information about the currency coin which may be incorrect.

***accounts( )***:  This function will help in managing the customer accounts.

---
## Literature Study of Numismatic Gallery Management System

### 1. Introduction

> **1.1 Purpose:** The purpose of this document is to build an online system to manage the collection of coins and banknotes and to ease the collection management. The users/collectors must be able to post and fetch the information about an item. Also, users can create their accounts and login to them to see the contents of their shopping cart in case they want to buy from Numismatic Gallery.

> **1.2 Intended Audience:** This project is a prototype for the collection management system and will be available worldwide. The targeted audience are the collectors of numismatic items, who can fetch information such as year of mint, composition material, availability, design, estimated value, etc. of the collectible they possess or buy the item they wish for.

> **1.3 Project scope:** The purpose of this project is to create a convenient and easy-to-use application for collectors, searching for information or trying to buy items. Above all, we hope to provide a comfortable user experience along with the best pricing available. The Numismatic Gallery Management System will allow collectors to:
- Store and manage detailed information about their coin collection.
- Securely browse their collection through a login system.
- Add desired coins to a shopping cart for potential purchase.
- Complete transactions through the integrated shop feature.

> **1.4 References:** The reference for user interface for this software may be taken from the websites:
 [Home Page](https://multiverseweb.github.io/coinshop/) and  [Login Window](https://multiverseweb.github.io/login/) .

> **1.5  Definitions, Acronyms, and Abbreviations:**
- Python: The programming language used for software development.
- File Handling: The database management system used for data storage.
- SRS: Software Requirement Specification.

### 2. Overall Description

> **2.1 Product Perspective:** The Coin Collector Database Management System is a standalone web-based application. It interfaces with a text file database to store and retrieve coin collection and shopping cart data. The project database system stores the following information:
Item Details: It includes the information of collectibles that are already available for sale and users can fetch the information about these items or can buy them too.
Customer Details: It includes the customer account details such as customer name, password and items in cart.

> **2.2 Product Features:**
>> *2.2.1 User Authentication:*
- Users can register using their name and password.
- Secure login mechanism for accessing the system.
>> *2.2.2 Coin Collection Management:*
- Users can add, edit, and delete coin entries.
- Each coin entry includes details such as coin name, year, country, condition, and description.
- Organise collections based on attributes (e.g., year, country, condition).
>> *2.2.3 Shopping Cart Management:*
- Users can add and manage items in their shopping cart.
- Cart contents can be reviewed and modified.
- Users can complete purchases through the shopping cart.
>> *2.2.4 Shop:*
- Displays available coins for sale.
- Listings include coin name, year, country of origin, price, and availability.
>> **2.3 User Classes and Characteristics:**
- Collectors: Registered users who can manage their coin collections and make purchases.
- Admin: System administrators responsible for managing user accounts and shop listings.

> **2.4 Operating Environment:** The operating environment for the system is as follows:
 - Distributed Database	
 - Client/Server system
 - Operating System: Windows 
 - Database: MySQL
 - Backend: Python

### 3. Functional Requirements

Detailed functional requirements are specified in Section 2.2.

### 4. Non-Functional Requirements
> **4.1 Performance Requirements:**
- The system shall provide a responsive user experience.
- Database operations should be optimised for minimal latency.
> **4.2 Security Requirements:**
- User data and transactions shall be securely encrypted.
- Authentication shall prevent unauthorised access.
- Data backup and recovery mechanisms shall be implemented.
> **4.3 Usability Requirements:**
- The user interface shall be intuitive and user-friendly.

### 5. Methodology Used
> **5.1 User Interface**
 Mobile View



Desktop View


> **5.2 Hardware Interface:**
- A browser that supports HTML, CSS and JavaScript.
> **5.3  Performance:**
- The application shall load quickly and respond to user interactions in a timely manner.
- The sky map rendering shall be smooth, even on devices with lower 
processing power.
> **5.4  Open Source:**
- This should be an open source web software in which users should be able to copy the information they want.

> **5.5 Software Interfaces:**

| Software Used | Description |
|:----------:|---:|
| Operating System| We have chosen the Windows operating system for its supporting environment and its user-friendliness. |
| Database|To save records, we have chosen MySQL Database.|
|Backend Language|We have chosen Python for its more interactive support.|

> **5.6 Communication Interface:**
 The project supports all types of web browsers and devices.

### 6. Constraints
> **6.1 Data Storage:**
Dependent on scalable databases for user accounts and interactions, adhering to privacy regulations.
> **6.2  Internet Connectivity:**
Platform requires an active internet connection for access.

### 7. Conclusion
This Software Requirement Specification (SRS) document serves as a comprehensive guide for the development of the Numismatic Gallery Management System, ensuring that all specified requirements are addressed. Detailed requirements ensure a secure, accessible, and user-friendly environment, supported by ongoing maintenance and future enhancements.

---
---

## Flowchart
![Image](flowchart.png)

## DFDs
![Image](https://github.com/multiverseweb/shop-and-opensource/blob/main/ngms-dfd0,1.png?raw=true)
![Image](ngms-dfd2.svg)

## Conclusion

In summary, the Collection Management System, developed using Python and MySQL, seamlessly integrated with a dedicated website frontend, stands as a sophisticated solution for enthusiasts managing their coin and banknote collections. The project's strength lies in the combination of Python's flexibility for backend logic and MySQL's prowess as a relational database, fostering efficient data management.

The MySQL database serves as a robust backend, ensuring the structured storage of user account details and collection items. This relational model facilitates quick and organised retrieval, updating, and deletion of data, contributing to a smooth and responsive user experience.

The frontend, embedded within a user-friendly website, significantly elevates the accessibility and usability of the system. The graphical interface enhances user interaction, offering features such as responsive design, dynamic updates, and intuitive navigation. This not only simplifies the user experience but also opens avenues for customization, branding, and extended user engagement.

Moreover, Python's adaptability augurs well for future expansions. The system can seamlessly incorporate advanced features, such as fortified user authentication methods, detailed item descriptions, and sophisticated search functionalities. The combination of a powerful backend, a user-centric frontend, and Python's extensibility establishes a foundation that accommodates the evolving needs of collectors.

In essence, the Collection Management System, with its Python-MySQL synergy and a dedicated website frontend, transcends the basic requirements of a collection management platform. It not only caters to the fundamental functionalities but also lays the groundwork for a scalable, customizable, and immersive user experience in the ever-evolving world of collection management.

---
---

[Link to frontend.](https://multiverseweb.github.io/login/)
---
Tejas' Codes :)
