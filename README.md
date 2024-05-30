# Project 5 E-commerce Website: The Phone Shop

An E-Commerce website featuring the sale of electronic products, Main features implemented by the app include Login and logout with the use of sessions for authentication, stripe payment, usage of databases to store and retrieve data, stylesheets make use of Bootstrap 5.

### Live link - https://mmunson94.pythonanywhere.com/

Admin Credentials - 
- Username = mmunson94
- Password = mmunson94

## Table of contents:

- [Overview](#Overview)
- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Screenshots](#Screenshots)
- [Technology Used](#TechnologyUsed)
- [Contributing](#Contributing)
- [License](#License)
- [Testing](#Testing)
- [Bugs](#Bugs)

## Overview 

This project aims to provide a user friendly experience for customer to purchase electronic products. The website also allows the owner to process payments and handle errors if they may occur providing the owner with a seamless product. 

For customers, the platform offers a secure and intuitive interface for browsing, selecting, and purchasing electronic goods, supported by robust features such as session-based login and logout for secure authentication, and a streamlined payment process through Stripe. 

For the owner, the website facilitates efficient management of transactions and customer interactions, leveraging a comprehensive database for storing and retrieving data, and implementing error-handling mechanisms to ensure smooth operations. Enhanced with Bootstrap 5 for modern and responsive design, this project aspires to create a reliable and engaging shopping environment while simplifying the backend processes for the owner.

https://github.com/mmunson94/Mmunson-P5-Phone-shop/assets/114744383/f7aec36b-0856-45fe-b037-dfc06004420a

## Features

User Authentication:

- Login and Logout: Secure login and logout functionality using session-based authentication to ensure user data privacy and account security.

Payment Integration:

- Stripe Payment Gateway: Integration with Stripe for secure and efficient processing of credit card payments, providing a reliable checkout experience for customers.

Database Management:

- Data Storage and Retrieval: Utilises a database to store product information, user details, order histories, and other relevant data, ensuring quick access and management.

User Interface and Experience:

- Bootstrap 5 Stylesheets: Implements Bootstrap 5 for a responsive and visually appealing design, ensuring a user-friendly interface that works across various devices and screen sizes.
- Visual feedback for succesful database transactions and prompts for empty or incorrect fields submitted. These include, Add to cart, Login/Logout, Newsletter subscription box, etc.

E-Commerce Functionalities:

- Product Catalog: Display of electronic products with detailed descriptions, prices, and images.
- Shopping Cart: Allows customers to add, remove, and manage products they intend to purchase.
- Order Processing: Facilitates the processing of customer orders from checkout to confirmation.
- Sorting: able to filter through product type and brand.
  
Error Handling:

Error Management: Implements mechanisms to handle errors gracefully, providing informative messages to users and maintaining the integrity of the shopping experience. These features collectively aim to create an efficient and enjoyable shopping experience for customers while offering the website owner a robust platform for managing sales and customer interactions.

- Uses messages array to handle routes that are unavailable.
- Custom 404 page also designed to handle routes that are not found.
- Specific detailed payment failure screens.
- Login failure messages.
- During the sending of the newsletter confirmation email, if an invalid email is supplied the app can handle it gracefully.

<br>

## Installation

### 1. Create a virtual enviroment (optional): 
Recommended that you use a virtual enviroment to run the app.

#### How to create a virtual enviroment
Make sure you have [Python](https://www.python.org/downloads/) installed (Python3 is recommended).
Once you have Python installed create the virtual enviroment by typing:
```
python -m venv /path/to/new/virtual/enviroment
```
e.g. 
```
python -m venv /documents/michael
```
This would create a virtual in your /documents/michaeldirectory


### 2. Activate the virtual enviroment:
```
source venv/bin/activate
```
Once you're finished with your virtual enviroment you can also exit or quit by typing.
```
deactivate
```


### 3. Install the prerequisite packages:
Make sure you have `postgresql` installed, if not, you can install it via [homebrew](https://brew.sh)
```
brew install postgresql
```

The list of packages required for this app are saved in the requirements.txt. Depending on your Python installation you can either use pip or pip3.
Run this command in the terminal to install the packages:
```
pip install -r requirements.txt
```

### 4. Run the server:
In order the run the server execute this command:
```
python manage.py runserver
```



## Deployment

Edit deployement section !
 
Deployment Process on PythonAnywhere:

1. Create an Account:
- Sign up for a PythonAnywhere account and log in.

2. Set Up a New Web App:
- Go to the "Web" tab and click "Add a new web app".
- Choose the manual configuration option for a more customized setup.
- Select the appropriate Python version for your project.

3. Upload Your Code:
- Upload your project files to PythonAnywhere via the "Files" tab or use Git to clone your repository.

4. Configure Virtual Environment:
- Create and activate a virtual environment to manage your dependencies.
- Install required packages using pip install -r requirements.txt.

5. Set Up WSGI File:
- Edit the WSGI configuration file to point to your application.
- Ensure the file imports your Flask or Django app correctly.

6. Database Setup:
- Configure your database settings.
- Run migrations if necessary.

7. Static Files Configuration:
- Configure the static files path if your project uses static files like CSS and JavaScript.

8. Test and Launch:
- Check for any errors in the "Web" tab under "Error logs".
- Reload the web app to apply changes and test your deployment.

For more detailed instructions, refer to the PythonAnywhere official documentation.

## Usage

The project aims to provide simple and efficient usage to both customer and owner. For an e-commerce website like The Phone Shop that provides the sale of electronic goods, the customer-centric approach is crucial to ensure a seamless and satisfying shopping experience. From the aspect of the owner, the goal is to ensure the platform operates smoothly, efficiently, and profitably enabling the owner to add/remove stock with ease, --.

Product Catalog:

- Extensive Selection: Offers a wide range of electronic products, from the latest gadgets to essential accessories, ensuring customers can find what they need.
- Detailed Descriptions: Provides comprehensive product descriptions, specifications, and high-quality images to help customers make informed decisions.
- Search and Filter: Features search and filter options to help customers easily find products based on categories and brands.

User-Friendly Interface:

- Layout and Theme: Ensures easy navigation with a clean, well-organized layout that guides customers effortlessly through the shopping process.
- Responsive Design: Adapts seamlessly to different devices, including desktops, tablets, and smartphones, offering a consistent experience across all platforms.
  
Customer accounts 

- Secure Login: Ensures secure account management with strong authentication mechanisms.

Shopping Cart and Checkout:

- Easy Cart Management: Allows customers to easily add, remove, and modify items in their shopping cart.
- Checkout: Offers a quick and secure checkout process with multiple payment options.
- Guest Checkout: Enables customers to make purchases without creating an account, enhancing convenience for one-time buyers.

on from owner aspect
include:
Screenshots in section


## Technology Used

In order to build the website, various software tools and technologies were used:

#### Frontend
- HTML/CSS: For structuring and styling the web pages.
- JavaScript: For adding interactivity and dynamic content.
- Bootstrap: For responsive design and pre-styled components.

#### Backend
- Python: The primary programming language used.
- Django/Flask: Python web frameworks for building the backend and handling HTTP requests.
- WSGI Servers: Gunicorn for serving the web application.

#### Database
- PostgreSQL: For storing and managing data.

#### Deployment
- Pythonanywhere: Hosting platform to deploy the app.
  
## Contributing

Mission Statement:

At The Phone Shop, our mission is to revolutionise the way people shop for electronics by providing a seamless, secure, and personalized online shopping experience. We aim to offer all ranges of electronic goods from the latest models to older gens with competitive prices and exceptional customer service the cornerstone of this endeavor. Our commitment is to guarantee our customers with the tools and technology they need to enhance their lives, whilst ensuring prices are affordable fostering a customerbase who trust us for quality, reliability, and convenience.

Things to improve service:

- Seasonal Sales: Runs regular promotions and seasonal sales to attract and retain customers.
- Discount Codes: Offers discount codes and vouchers to incentivize purchases.
guidelines
- Email Campaigns: Sends targeted email campaigns with personalized offers, new arrivals, and upcoming sales.
- Product Reviews: Encourages customers to leave reviews and ratings for products, helping others make informed decisions.
- Feedback Mechanism: Allows customers to provide feedback on their shopping experience, helping the site to continuously improve.
- Rewards Points: Implements a loyalty program where customers earn points for purchases, reviews, and referrals, which can be redeemed for discounts or special offers.
- Exclusive Offers: Provides exclusive deals and early access to sales for loyal customers.
- Real-Time Updates: Allows customers to track their orders in real-time, providing updates on the status of their shipment.
- Help centre: Through the use of live chats, email, telephone.

## License

mit license


## Testing

table format
testing the fuctionality
20 entries fetures tested
headers include
expected rseult
outcome


## Validation

## Bugs
- active
- resolved

## future improvements



