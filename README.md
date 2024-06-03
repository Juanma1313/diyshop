# ![DIY Site logo](static/diy-logo.png)  **DIY Shop** 

>|by Juan Manuel de las Heras Arroyo|
>|:---:|

# Introduction

The DIY site, as a first stage, was intended to be a repository of small-scale construction projects, designed so that anyone can carry them out by following the instructions posted on the repository in a genuine Do-It-Yourself style.

The DIY Shop, as the second stage, implementes a fully functional E-Commerce solution that allows users tu upload/download/manage their own content, allowing the owner to sell the parts and materials that users may need to acomplice the published DIY Projects.

Public access to this website can be made completely anonymous, allowing the users to browse the entire published repository, and encouraging them to register on a permanent basis, which will also allow users to mark which projects are their favourites.

In the first stage of implementation (**DIY Site**), people of any age and skill level could explore the projects named "Things" that are publicly presented in this repository, and use the DIY project published instructions to replicate them. The contents of the projects (things) were uploaded into the repository by the creator users whom require private access, with certain privileges assigned by an administrator, in order to access the repository management system.

In this second fase (**DIY Shop**), we expand the initial implementation to include E-Commerce functionality, including features like user profiles, shopping kart, online payment, e-mail confirmation, allow users to add content trough website pages, sofisticated message notification for the user, product search capabilities, product navigation using categories, links to Facebook busines page and newsleter subscription.

From a technical standpoint, this site is implemented in Python, JavaScript, HTML and CSS languages, on the Django framework and using MVC design. It includes user authentication, email validation and full CRUD functionality to manage the content of the repository.

- Access the website [DIY Shop](https://diyshop-e5a99a0c89cb.herokuapp.com/) Deployed on Heroku service
- Access the repository [diyshop](https://github.com/Juanma1313/diyshop) stored in Github

# Table of Contents

[Introduction](#introduction)

[Busines Model](#busines-model)

- [Marketing Strategy](#marketing-strategy)
  - [Market Target](#market-target)
  - [Marketing techniques](#marketing-techniques)
    - [The `Share your DIY project` technique](#the-share-your-diy-project-technique)
    - [SEO](#seo)

[User experience (UX)](#user-experience-ux)

- [Functional specifications](#functional-specifications)
  - [The User](#the-user)
  - [Goals](#goals)
  - [Customer Requirements](#customer-requirements)
    - [Initial Customer requirements for users](#initial-customer-requirements-for-users)
    - [Other inital requirements](#other-initial-requirements)
    - [DIY Shop Customer requirements for users](#diy-shop-customer-requirements-for-users-second-stage)
    - [DIY Shop Additional Requirements](#additional-requirements)
  - [Development plan](#development-plan)
    - [DIY Shop User Stories](#diy-shop-user-stories)
      - [Backlogs and Kanban boards](#backlogs-and-kanban-boards)
        - DIY Site
          - [DIY Site Kanban board in Github](https://github.com/users/Juanma1313/projects/5/views/1)
          - [DIY Site Backlog (milestone) in Github](https://github.com/Juanma1313/dys/milestone/1)
        - DIY Site
          - [DIY Shop Kanban board in Github](https://github.com/users/Juanma1313/projects/6/views/1)
          - [DIY Shop Backlog (milestone) in Github](https://github.com/Juanma1313/diyshop/milestone/1?closed=1)
  - [Web Site Sketches](#web-site-sketches)
  - [Database](#database)

[Features](#features)

- [Users Home page](#users-home-page)
- [Footer](#footer)
- [Users Navigation Bar](#users-navigation-bar)
- [Sign Up](#sign-up)
- [Sign In](#sign-in)
- [Sign Out](#sign-out)
- [Email](#email)
- [DIY Project details](#diy-project-details-1)
- [Administration pages](#administration-pages)

[Future Enhancements](#future-enhancements)

[Testing](#testing)

[Testing Strategy](#testing-strategy)

[Validating the Source](#validating-the-source)

- [Django Python code](#django-python-code)
- [CSS code](#css-code)
- [HTML cod](#html-code)

[Testing the application](#testing-the-application)

[The development environment](#the-development-environment)

- [Resources](#resources)

[Deployment](#deployment)

- [How to deploy the project on Heroku](#how-to-deploy-the-project-on-heroku)
- [Create a clone of this repository](#create-a-clone-of-this-repository)

[Acknowledgements](#acknowledgements)

# Busines Model

Since this initiative is oriented towards the sale of its products in a non-face-to-face manner and through online transactions, it clearly falls within the scope of an E-Commerce business model.  
The target customer of this business is a retail customer, which is why a business-to-customer or what is cooquially called B2C strategy is imposed.

## Marketing Strategy

In our case, the product being sold is not really the product being advertised, since what is promoted on this website is information on how to carry out small do-it-yourself (DIY) projects, but what is really being sold are the parts and kits to carry out these projects.
So the main strategy is to make DIY projects attractive so that customers are compelled to buy the necessary parts and pieces, which in normal conditions, to find them individually in the conventional market, is a major inconvenience for the customer.

### Market Target

The target customer profile of the products sold in this business are those individuals or groups who have time for leisure, are handyman, are curious about technology, or simply have fun making things themselves. I believe that this customer profile would include Bricolage enthusiasts, tinkerers, makers, craft artists, decorators, dyers, Hobbies enthusiasts, Gadget snobs, electronics fans, robotics aficionados, etc.

### Marketing techniques

We can use various sales techniques to maximize the audience and consequently increase visits and, desirably, also product sales.

#### The ‘Share your DIY project’ technique

By allowing users to upload their own projects for sharing, it increases the amount and diversity of content available. And while these shared projects cannot be directly monetized, on the other hand they increase the attractiveness of the website and, consequently, promote a greater presence of the platform on the internet.

It must also be taken into account that this type of technology is associated with infrastructure costs that have to be cost-effective. The storage capacity and connection times used in these shared projects have to be compensated with the sales of parts and kits. One way of offsetting these costs is to reach agreements with content creators to also offer parts and construction kits from their own projects.

#### SEO

In order for search engines such as Google to find this platform and offer it among the best proposals, we have made a list of the words and phrases that could best suit the internet searches of potential customers.

In choosing the words and phrases, we have taken into account the clients, the purpose of the website and the DIY projects that belong to the business, but we cannot take into consideration the products that are sold, as they are not part of our marketing strategy, nor can we consider the DIY projects shared by users, as we don't know which, when or if they will be uploaded.

This busines would be operating in Spain, so a set of this words in spanish should be also included, but since the website default lenguage is English, and currently does not support multilanguage. We will avoid this part for now.

>##### SEO Keywords and phrases
>
>| Client      | Busines         | Miscelaneous  | Sentences                   |
>|:-----------:| --------------- | ------------- | --------------------------- |
>| tinkerer    | DIY Project     | open hardware | expand my mind              |
>| electronics | Shared projects | open software | feel achievement            |
>| robotics    | fun and usefull | DIY Tools     | a project for me            |
>| maker       | DIY upload      | circuits      | activity for your free time |
>| Hobby       | DIY download    | actuators     | projects that are fun       |
>| animatronics| DIY Shop        | woodwork      | Learn while building        |
>| bricolage   | DIY build       | woodwork      | do it yourself              |

#### GDPR
Concerning the General Data Protection Regulation, I have generated the privacy policy with a generic **Privacy Policy Generator** and attach the resulting document as a link on the base footer of the website.

* The [GDPR Generator](https://www.privacypolicygenerator.info/)
* The [GDPR document](https://www.termsfeed.com/live/cbea6af5-9e7f-4028-be6e-babac606f61d)


#### Social Media

One of the customer requirements is to have a link to a DIY Shop Facebook webpage. 
- Link to [DIY Shop in Facebook](https://www.facebook.com/people/DIY-Site/61559945799160/)

![Screen capture of DIY Shop Facebook Page](assets/doc/screencaptures/screenshot-facebook-diyshop.png)

# User experience (UX)

DIY Site aims to be a friendly public site for users to access DIY style projects that they can replicate. The presentation of the content is dynamic and attractive, and the information about the projects is clear and easy to read.

Registered users will also be able to add and edit their own creations. This administrative interface is geared towards a more functional purpose, so that project content can be easily edited and expanded.

## Functional specifications

### The User

There are four types of users segregated by their role and purpose.

- **Anonymous:** A non registered user
- **Regular:** A registered user
- **Creator:** A user with privileges to add/edit/publish owners content
- **Administrator:** User that can validate users and perform all  
  actions.

### Goals

- For all users, the user interface should be minimalistic and intuitive
- For anonymous and regular users the user interface should be friendly, dynamic, clear and fun.
- For Creators and administrators, The user interface should be clear, flexible and functional.

### Customer requirements

#### Initial Customer requirements for users

The following are the customer requirements that are part of the user stories list for the initial delivery iteration backlog.

| Epic                                                   | Story | Requirements for users                        | Anonymous | Regular | Creator | Admin |
| ------------------------------------------------------ | ----- | --------------------------------------------- | --------- | ------- | ------- | ----- |
| [#38](https://github.com/Juanma1313/diyshop/issues/38) | 12    | Register an account using e-mail and password | x         |         |         |       |
| [#38](https://github.com/Juanma1313/diyshop/issues/38) | 13    | Validate own e-mail                           |           | x       | x       | x     |
| [#38](https://github.com/Juanma1313/diyshop/issues/38) | 14    | Login in main page with e-mail and password   | x         | x       | x       | x     |
| [#38](https://github.com/Juanma1313/diyshop/issues/38) | 15    | Change e-mail                                 |           | x       | x       | x     |
| [#38](https://github.com/Juanma1313/diyshop/issues/38) | 16    | Delete own e-mail account                     |           |         | x       | x     |
| [#37](https://github.com/Juanma1313/diyshop/issues/37) | 17    | Register own account using user and password  |           |         |         | x     |
| [#37](https://github.com/Juanma1313/diyshop/issues/37) | 17    | Login in admin page with user and password    |           |         | x       | x     |
| [#37](https://github.com/Juanma1313/diyshop/issues/37) | 17    | Change own user data (name, lastname)         |           |         | x       | x     |
| [#38](https://github.com/Juanma1313/diyshop/issues/38) | 18    | Change own password                           |           | x       | x       | x     |
| [#37](https://github.com/Juanma1313/diyshop/issues/37) | 17    | Delete own user-account                       |           |         |         | x     |
| [#38](https://github.com/Juanma1313/diyshop/issues/38) | 35    | Sign out/log out                              |           | x       | x       | x     |
| [#37](https://github.com/Juanma1313/diyshop/issues/37) | 17    | Administrate users and password               |           |         |         | x     |
| [#41](https://github.com/Juanma1313/diyshop/issues/41) | 19    | view list of published DIY projects           | x         | x       | x       | x     |
| [#41](https://github.com/Juanma1313/diyshop/issues/41) | 20    | View details of a published DIY project       | x         | x       | x       | x     |
| [#41](https://github.com/Juanma1313/diyshop/issues/41) | 21    | View published components of a DIY project    | x         | x       | x       | x     |
| [#41](https://github.com/Juanma1313/diyshop/issues/41) | 20    | View instructions of a DIY project            | x         | x       | x       | x     |
| [#38](https://github.com/Juanma1313/diyshop/issues/38) | 22    | Mark a DIY project as own favourite           |           | x       | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 23/24 | Create a DIY project and its details          |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 26    | Create components (DIY subprojects)           |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 25    | Create instructions                           |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 27    | Modify a DIY project and its details          |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 28    | Modify a component and its details            |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 29    | Modify the instructions of a DIY project      |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 30    | Delete a DIY project and its details          |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 31    | Delete a component                            |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 32    | Delete instructions                           |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 33    | Change state published/Draft a DIY project    |           |         | x       | x     |
| [#39](https://github.com/Juanma1313/diyshop/issues/39) | 34    | Change state published/Draft a component      |           |         | x       | x     |

#### Other initial requirements

- There should be a main landing page to display the content.
- There should be an administrator page for manage users and content.
- Web pages should be able to be used from desktops and mobile devices
- Content and user informations should be stored in Elephant  
PostgreSQL servers
- Multimedia content (Images, videos, data files, etc) should be  
stored in Cloudinary servers.
- The web site should be able to be deployed on Heroku servers from  
GitHub
- The project should be develop under Agile methodology.

#### DIY Shop Customer requirements for users (second stage)

The following are the customer requirements that are part of the user stories list for the second delivery iteration backlog.

| Epic                                                   | Description                               |
| ------------------------------------------------------ | ----------------------------------------- |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | EPIC: DIY Project creation and management |
| [#17](https://github.com/Juanma1313/diyshop/issues/17) | EPIC: Searching DIY Projects              |
| [#22](https://github.com/Juanma1313/diyshop/issues/22) | EPIC: User Shopping Cart                  |
| [#26](https://github.com/Juanma1313/diyshop/issues/26) | EPIC: User Shopping Cart Checkout         |
| [#30](https://github.com/Juanma1313/diyshop/issues/30) | EPIC: User Profiles                       |
| [#33](https://github.com/Juanma1313/diyshop/issues/33) | EPIC: User Messages and Notifications     |

| Epic                                                   | Story                                                  | Requirements for users                                              | Anonymous | Regular | Creator | Admin |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------------------- | --------- | ------- | ------- | ----- |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#5](https://github.com/Juanma1313/diyshop/issues/5)   | USER STORY: Create a DIY project                                    |           | X       | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#6](https://github.com/Juanma1313/diyshop/issues/6)   | USER STORY: Create DIY project details                              |           | X       | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#7](https://github.com/Juanma1313/diyshop/issues/7)   | USER STORY: Create Instructions                                     |           |         | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#8](https://github.com/Juanma1313/diyshop/issues/8)   | USER STORY: Create component                                        |           | X       | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#9](https://github.com/Juanma1313/diyshop/issues/9)   | USER STORY: Modify a DIY project details                            |           | X       | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#10](https://github.com/Juanma1313/diyshop/issues/10) | USER STORY: Modify component                                        |           | X       | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#11](https://github.com/Juanma1313/diyshop/issues11/) | USER STORY: Modify instructions                                     |           |         | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#12](https://github.com/Juanma1313/diyshop/issues/12) | USER STORY: Delete a project                                        |           | X       | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#13](https://github.com/Juanma1313/diyshop/issues/13) | USER STORY: Delete a owned Components                               |           | X       | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#14](https://github.com/Juanma1313/diyshop/issues/14) | USER STORY: Delete owned Instructions elements                      |           |         | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#15](https://github.com/Juanma1313/diyshop/issues/15) | USER STORY: Change own DIY Project Published status                 |           | X       | X       | X     |
| [#4](https://github.com/Juanma1313/diyshop/issues/4)   | [#16](https://github.com/Juanma1313/diyshop/issues/16) | USER STORY: Change own DIY Component published status               |           | X       | X       | X     |
| [#17](https://github.com/Juanma1313/diyshop/issues/17) | [#18](https://github.com/Juanma1313/diyshop/issues/18) | USER STORY: Manage DIY Projects Categories                          |           |         | X       | X     |
| [#17](https://github.com/Juanma1313/diyshop/issues/17) | [#19](https://github.com/Juanma1313/diyshop/issues/19) | USER STORY: Filter DIY Projects by Categories                       | X         | X       | X       | X     |
| [#17](https://github.com/Juanma1313/diyshop/issues/17) | [#20](https://github.com/Juanma1313/diyshop/issues/20) | USER STORY: Sorting DIY Projects                                    | X         | X       | X       | X     |
| [#17](https://github.com/Juanma1313/diyshop/issues/17) | [#21](https://github.com/Juanma1313/diyshop/issues/21) | USER STORY: Searching DIY Projects with text                        | X         | X       | X       | X     |
| [#22](https://github.com/Juanma1313/diyshop/issues/22) | [#23](https://github.com/Juanma1313/diyshop/issues/23) | USER STORY: add Projects to the shopping cart                       | X         | X       | X       | X     |
| [#22](https://github.com/Juanma1313/diyshop/issues/22) | [#24](https://github.com/Juanma1313/diyshop/issues/24) | USER STORY: view the shopping cart content                          | X         | X       | X       | X     |
| [#22](https://github.com/Juanma1313/diyshop/issues/22) | [#25](https://github.com/Juanma1313/diyshop/issues/25) | USER STORY: manage shopping items in the shopping cart              | X         | X       | X       | X     |
| [#26](https://github.com/Juanma1313/diyshop/issues/26) | [#27](https://github.com/Juanma1313/diyshop/issues/27) | USER STORY: initiate checkout of the shopping cart                  | X         | X       | X       | X     |
| [#26](https://github.com/Juanma1313/diyshop/issues/26) | [#28](https://github.com/Juanma1313/diyshop/issues/28) | USER STORY: Fill in the checkout form                               | X         | X       | X       | X     |
| [#26](https://github.com/Juanma1313/diyshop/issues/26) | [#29](https://github.com/Juanma1313/diyshop/issues/29) | USER STORY: submit the checkout order to the online payment service | X         | X       | X       | X     |
| [#30](https://github.com/Juanma1313/diyshop/issues/30) | [#31](https://github.com/Juanma1313/diyshop/issues/31) | USER STORY: Create a user profile                                   |           | X       | X       | X     |
| [#30](https://github.com/Juanma1313/diyshop/issues/30) | [#32](https://github.com/Juanma1313/diyshop/issues/32) | USER STORY: View and Manage my Profile                              |           | X       | X       | X     |
| [#33](https://github.com/Juanma1313/diyshop/issues/33) | [#34](https://github.com/Juanma1313/diyshop/issues/34) | USER STORY: User Messages and Notifications                         | X         | X       | X       | X     |

#### Additional requirements

In addition to the [initial customer requirements](#other-initial-requirements), the following list of requirements has been issued in this second phase.

- Admin pages should add Category, Profile and Order management.
- Multimedia content (images, videos, data files, etc.) should be stored in scalable cloud-based storage (AWS S3 services).
- DIY projects should be categorized.
- Users should have the ability to search, sort and filter published DIY projects.
- Users should have a shopping cart with session persistence where they can store the products they wish to purchase.
- There must be an online payment functionality provided by a payment gateway service (Stripe Payments with Elements).
- The website must keep a record of all payment transactions.
- Users should have a customizable profile where they can store default delivery information.
- Payments should be confirmed to the user by email.
- Users should be able to create and manage the content of their own DIY projects \*\* not \*\* using the Django-admin framework.
- Users must be informed of the result of their interactions with the website via a pop-up messaging system (Django-messages + Bootstrap-Toasts).
- The website must have a link to its Facebook social network page.
- The website must have a News Letter registration service.

### Development plan

- Link to [**Development plan for first stage (DIY Site)**](https://github.com/Juanma1313/diyshop#development-plan)

Following the same guidelines applied to the first phase of development, the development must be managed under the **AGILE** methodology.
_**Epics**_, and their corresponding _**user stories**_ must be defined and, when needed, meet a consensus between the developers and the project owner through agreed acceptance criteria. Also, from a more technical point of view, development tasks and their corresponding _**story points**_ are defined in order to better evaluate the development effort.  
The following information lists all these issues. 

> [!NOTE]
> Please follow the links fro `epics` and `user stories` to access the full information stored on github.

#### DIY Shop User Stories

Since the detailed list of the `epics` and `user stories` is too longwinded to be usefull in this doccument, I have written it in a separated doccument. here is a link to the [**DIY Shop Stories**](assets/doc/diy-shop-user-stories.md) document.

#### Backlogs and Kanban boards

##### DIY Site

- [DIY Site Kanban board in Github](https://github.com/users/Juanma1313/projects/5/views/1)
- [DIY Site Backlog (milestone) in Github](https://github.com/Juanma1313/dys/milestone/1)

##### DIY Site

- [DIY Shop Kanban board in Github](https://github.com/users/Juanma1313/projects/6/views/1)
- [DIY Shop Backlog (milestone) in Github](https://github.com/Juanma1313/diyshop/milestone/1?closed=1)

#### Web Site Sketches

To outline the design of the website, I have created the following sketches to guide the development of the user interface. 

Since for the administration of the website I will mainly rely on the Django administration interface, and even though it will be customized, I didn't find the need to design the wireframes of those pages, since the style is already defined in the framework and regular users will not access it anyways. 
Likewise, the ***user profile*** and ***edit product*** pages are based on the Django-forms and Django-Crispy frameworks, so their aesthetics are already pre-established.

For this type of website content, I assume that the DIY Projects authors will produce descriptions and instructions with long texts, so the main design is also oriented towards large screens. I then adapted this contents so that it can also be viewed by an eventual user of a small screen device.



##### Base Page 

This design only sketches the header and footer of the pages. This should be consistent across all webpages of the website.
it displays logo and brand, all the navegation options, access to the user menus and the sopping cart. In the footer it is intended to display company information and bring access to the company social media networks.

![Base Page](assets/media/image2.png)

##### Home page

This page is the landing page and displays a carousel of images and phrases that define the website. 
It also brings acces to the rest of the webpages as well as the Facebook DIY shop webpage and the Newsletter subscription form.

![Home Page](assets/media/image3.png)

##### DIY projects page

This page shows the list of available DIY projects and bring access to the details of each one.

![DIY projects page](assets/media/image30.png)


##### DIY project Details page
This page is where the chosen DIY Project is displayed, with all its `Components` and `Instructions` to be followed by the user.

![DIY project Details page](assets/media/image4.png)

#### Database Schema

It is a customer requirement to use the services of Elephant as an external SQL service to host the website database. This service provider has servers running PostgreSQL servers.

Since the development framework is based on Django, we will take advantage of its built in user management functionality from its allauth package, which deployes its own database structures.

Django's Allauth uses, among others, the `auth_user`, `account_emailconfirmation` and `account_emailaddress` database tables depicted on the left of the following figure, which are included in this figure in order to identify their relationships with the database structures specific to the DIY Shop website.

To store the user's billing preferences, the `profiles-userprofile` table stores user information such as phone number or delivery address, and maintains a ***one-to-one*** relationship with the `auth_user` table, which means that there can only be one profile for each user. This table is very important for billing, as it is the only connection between users and their orders.

The table `products_thing` stores the details of the DIY projects and components. A special detail of the implementation is that this table has a **cyclic reference to itself** in order to accommodate a tree structure for the DIY components, which in turn are DIY projects themselves. So, in reality, this structure is two models in one. Allowing, in my opinion, greater flexibility with greater simplicity.

The table `products_instructions` stores the details of the DIY Project Instructions and a ***one-to-many*** relationship with its corresponding DIY Project.

The table `products_thing_likes` functions as an intermediate table that stores references to all of each user's favourite DIY Projects as a ***many to many*** relationship.

To classify DIY products, the `products_categoty` table stores all classification categories with a **many-to-one** relationship with the `products_thing` table. This means that each DIY product can belong to only one category. Maybe in a third iteration of this project we can change that, to allow DIY projects to have multiple categories, and thus improve the search tool for the user.

In order to keep track of all user purchases, the `checkout_order` table stores all successfully submitted orders, and the `checkout_orderlineitem` table stores all DIY Projects purchased in each order, with a ***many-to-one*** relationship between the two tables. The `checkout_order` table, in turn, maintains a ***many-to-one*** relationship with the `profiles_userprofile` table to identify the owner of the order, while the `checkout_orderlineitem` table maintains a ***many-to-one*** relationship with the `products_thing` table to identify each DIY project purchased.

All these tables are automatically created by Django from the application model classes `Thing`, `Instructions`, `Category`, `UserProfile`, `Order` and `OrderLineItem`, so with a few classes, all the necessary database structures are created.

Although there is no specific class for the `diy_thing_likes table`, it is also produced by Django when it recognizes the ***many-to-many*** relationship between the `Thing` class and the `User` class in the `products` application model.

#### Database ERD Model

![Database Schema](assets/media/image5.png)

## Features

#### Users Home page

The ***home page** or **landing page** is presented on the root page of the site's domain. Since the main purpose of this page is to welcome users and provide them access to the rest of the site, I designed it in a minimalist way, with a simple carousel banner advertising the benefits of the website.

A large black button redirects the user to the DIY projects page, while the Facebook link opens the DIY Shop Facebook page and the newsletter form allows the user to sign up for the DIY Shop newsletter service.

![](assets/media/image6.png)

#### Footer

This bar appears at the BOTTOM of all user web pages containing breaf company information, and links to the social media sites where the owner busine have presence.
This bar will not be presented to small screen devices since takes too much screen realstate and provides little utilitie.

There is also an icon, allways present, at the bottom right corner at the footer, that will scroll the web page to the top, which it is usefull with long pages.

![Footer bar](assets/media/image7.png)

#### Users Navigation Bar

The main navigation bar appears at the top of all user web pages, and maintains the minimalist style. It provides the following features:
- Brand logo and name which works as a link to the home page. 
- Search bar, where users can search DIY projects using words or phrases that may be in their name or description.
- Main navigation bar with options to bring up the DIY product list in particular order or categories.
- white user icon that opens a user drop-down menu, which changes to yellow and displays the username underneath, when the user is logged in.
- White shopping bag icon that opens the shopping bag page, which changes to yellow and shows underneath it the total cost of the shopping bag when the cost is greater that 0.00.

![normal nav bar](assets/media/image8.png)

When the device's screen is not large enough, this bar changes to save space and make it clearer for the user, and the main navegation bar changes to a dropdown menu.

| Small Screen Device Navigation Bar | Small Screen Device Main Navigation dropdown menu|
|:-:|:-:|
| ![small nav bar](assets/media/image31.png) | ![small main nav bar](assets/media/image32.png) |

##### User Main Navigation Menu
This menu, sitting in the center of the Navigation bar, and under the search bar, provides a serie of menus from where the user can choose to order and filter the Project list. 

| All Projects sorting Menu | Electronics filtering Menu | Crafts and Workshop filtering menu | Other sorting/filtering menu |
|:-:|:-:|:-:|:-:|
| ![All Projects sorting Menu](assets/media/image33.png) | ![Electronics filtering Menu](assets/media/image34.png) | ![Crafts and Workshop filtering menu](assets/media/image35.png) | ![Other sorting/filtering menu](assets/media/image36.png) |
||


##### User Dropdown Menu

Clicking on the user icon displays the user menu as a drop-down menu, and its content varies depending on the user's context.

###### User Menu options:

> **Admin:** This menu option redirects the administrator to the admin web page so that he/she can perform administrative tasks.

> **Add Project:** This menu option redirects the registered user to the add_product web page so that he/she can create a new DIY project.

> **My Profile** This menu option redirects the registered user to his/her profile page so that he/she can edit the default delivery information.

> **E-mail:** This menu option redirects the registered user to the accounts/email webpage so that the user can self-manage his/her email addresses.

> **Sign Up:** This menu option redirects the non registered user to the accounts/registration web page so that he/she can self-register on the website.

> **Sign In:** This menu option redirects the non registered user to the accounts/login webpage so that the user can sign in the website with an email address.

> **Sign Out:** This menu option redirects the registered user to the accounts/logout webpage so that the user can sign out the website.

###### Drop-down Menu content.

| Anonymous User menu |  Registered User menu | Administrators/Content Creators user menu|
|:-:|:-:|:-:|
| ![Anonymous user menu](assets/media/image9.png) | ![Regular user menu](assets/media/image10.png) | ![Administrators user menu ](assets/media/image11.png) |
||

#### Sign Up Webpage

![sign up webpage](assets/media/image12.png)

#### Sign In Webpage

![sign in webpage](assets/media/image13.png)

#### Sign Out Webpage

![sign out webpage](assets/media/image14.png)

#### Email Webpage

![email webpage](assets/media/image15.png)

#### DIY Projects List

This page displays a list of DIY projects according to the filter, order or search options selected by the user.
There are few options to land on this page:
- Selecting the `check out our latest projects` button from the `Home Page` will bring the list of DIY projects ordered by date (new to old)
- Selecting one of the options of the `All Project` from the main navigation menu will bring the list of DIY projects ordered by Price (low to high),  Rating (high to low), Category (A to Z), or All (unsorted).
- Selecting one of the options of any other option from the main navigation menu will bring the list of DIY projects ordered by the corresponding assiciated categories to that option. 
- Selecting one of the sorting options in the `Sort By` dropdown list
- After finishing with a checkout or shopping bag operation will bring the list of DIY projects unordered by default.

If the user is the author of any of the DIY Projects, both `Edit` and `Delete` buttons will apear at the bottom of those DIY Projects.
If the user is an administrator or a registered Content Creator, both 'Edit' and 'Delete' buttons will apear at the bottom of all DIY Projects.

Clicking on any DIY Project will bring up that DIY project detail page.

>[!NOTE]
> For the time being, the ‘Delete’ option will only be available to administrators, even when the `Delete` link is available to other users. This is a design decision under discussion with the customer. :-)

![diy projects list](assets/media/image37.png)


#### DIY Project Details

Once the user has selected a DIY project link, the details webpage is displayed, giving access to the details, the DIY components and the Instructions, so that the user can follow them to reproduce the object described in the project.

The layout of this page is highly dependent on the design of the DIY project author, as the description fields and instructions are displayed as HTML documents that can be fully customized with colours, images, videos, etc., allowing for a very flexible result.The order in which the information is presented is one of the few limitations that have been set when displaying the DIY project. Starting with the Projets details, then the list of components followed by the list of instructions ordered by title.

Clicking on the `Heart Icon` the registered user can toggle the `like` flag fro this DIY project, and the likes counter will be updated

If the current DIY project has price greater that €0.00, the the button `Add to bag` will be displayed, otherwise, the `Free Access` label will be display instead of the price.

By clicking on the `Add to bag` button, the current DIY project will be added to the shopping bag as many times as indicated by the step control next to it.

If the user is an administrator, a content creator or  the author og the DIY project, the buttons `Edit`and `Delete` will be available.


>[!NOTE]
> For the time being, the ‘Delete’ option will only be available to administrators, even when the `Delete` link is available to other users. This is a design decision under discussion with the customer. :-)


![diy project details ](assets/media/image16.png)

#### User Shopping Bag
This page shows de details of the DIY projects that the user has added to the shopping cart.

It is possible to change the amount of a DIY Project you want to order by changing the value of the step control next to int, and the clicking the `Update` link.

It is also possible to delete the item from the list clicking on the 'Delete'link next to it.

Pressing the `Secure Checkout` button will bring up the **Checkout Page** to purchase the items from the list.

Pressing the `keep shopping` button will bring up the **DIY projects list page**

![User shopping bag](assets/media/image38.png)

#### Checkout Page

When the user decide to purchase the content of the Shopping bag, he/she will be redirected to this **checkout page** where the default delivery information from the user profile will populate the delivery form, and a list of the shopping bag items to purchase and all the cost and totals will be displayed.

The user can modify any information from the `Details` or `Delivery` forms, and fill up a valid credit card information 

Whe the user clicks the `Buy Now` button, the forms will be checked for valid information, and if all is ok, the order will be submitted to the payment gateway service that will perform the transaction. If the information is not valid, a message indicating the problem will be displayed, requesting the user to correct the problem. 

The the transaction has been aprooved, the **Checkout Success page** will be shown presenting the purchase order information.

![checkout page](assets/media/image39.png)

![checkout success](assets/media/image40.png)

#### Administration pages

All the administrative tasks have been delegated to Django Allauth extensions, wich brings a lot of development releaf, but also comes with layout design limitations. Only the logo, website name and color schemas are customized using a modified copy of the original Django Allouth templates.

##### Content Creators homepage

This page gives the content creators access to all DIY project (Things), individual instructions documents or any document attachment stored by Django's Sumernote extension.

![Content Creators homepage](assets/media/image17.png)

##### DIY-Things webpage

This page provides a list of the DIY projects (Things) created. The filter pannel will allow the creator to narrow down the list based on its parent project, the published status and the creation date. We can also search a particular text in the title or description text of the DIY projects if we want to locate a particular project.

Marking the desired Things we can use the Delete/Publish/Set as draft actions on any number of selected Things at once.

Clicking on any Thing's tytle from the list will present the Change Thing page for the selected Thing, where all the DIY Project data can be edited

![DIY-Things webpage](assets/media/image18.png)

##### Change Thing webpages

This is probably the most complex administrative web page on this website. It combines the functions of adding/deleting/modifying DIY project details, components and instructions on a single page. It is designed so that the Creator can manage the DIY project information without having to navigate through many pages or make unnecessary clicks.

Once you have made changes to your DIY Project, there are three ways to save. Save all changes and return to the list, save all changes and continue editing in the current DIY Project, or save all changes and create a new blank DIY Project. Exiting this page or reloading without saving, will immediately delete all changes made to the DIY Project.

On this web page we can distinguish three areas: the details of the DIY Project at the top, followed by the list of components called "Things", and at the bottom, the list of instructions called "Instructions".

![Change Thing webpages](assets/media/image19.png)

###### Change the DIY Project details

This upper area of the "Change Thing webpage" allows the content creator to change the Title, the Author, and the Status (Draft/Published). It allows also to assign a Featured Image that will be used in the list of DIY Projects at the home page.

The most important element that can be modified in this area areis the Description. This field has an embebded WSIWYG editor from the Django Sumernote extension, that allows to insert text, images, videos, links and any HTML/CSS needed to present the project. It is the responsability of the creator to write a description that will be displayed correctly to the final user .

![](assets/media/image20.png)

###### Change the DIY Project _**Components (Things)**_

The DIY Components (Things) of a DIY Project (Thing) are in fact themselves Thing elements, so they can also be edited like a normal DIY Project. The only difference is that DIY Components have a "parent" object to which they belong.

New DIY Components can be added using the "Add another Thing" link at the bottom of the list.

![Change the DIY Project_1](assets/media/image21.png)

On the Change Thing web page, each of its DIY Components are listed under "Things", and only their Title, Author, Status and Description are shown. To minimize screen space and rendering time, the Description is hidden by default, but can be displayed and edited using the `show` link next to the 'DESCRIPTION' label.

![Change the DIY Project_2](assets/media/image22.png)

The rest of the information about a DIY component is not displayed, but can be edited by clicking on the 'change' link next to the DIY component name, which will bring up a new, separate modal Change Thing page for this DIY component.

###### Change the DIY Project _**Instructions**_

On the Change Thing website, each of your DIY Instructions is listed under "INSTRUCTIONSS", and only its Title is displayed. To minimise screen space and rendering time, the Description is hidden by default, but can be displayed and edited using the `show` link next to the 'INSTRUCTIONS' label.

Note: The list name "INSTRUCTIONSS" is automatically created by Django admin based on the name assigned to the class model. More research on Django is needed to modify this name or further customize the layout of the list.

The list of Instructions is ordered by Title. This is useful if you need to maintain a particular order in the instructions, so assigning titles such as "Step 01", "Step 02", etc. could be used to maintain a strict order.

New Instructions elements can be added using the "Add another Instructions" link at the bottom of the list.

![Change the DIY Project_1](assets/media/image23.png)

Instructions field, like the Description fields, has an embebded WSIWYG editor from the Django Sumernote extension, that allows to insert text, images, videos, links and any HTML/CSS needed to present the instructions. It is the responsability of the creator to write a Instructions element that will be displayed correctly to the final user.

![Change the DIY Project_2](assets/media/image24.png)

The Instructions element can be also edited by clicking on the 'change' link next to the DIY Instructions element title, which will bring up a new, separate modal Change Instructions page.

##### DIY-Instructions webpage

This page provides a list of the Instruction items created, and is a convenient way to access a particular Instruction item without having to open the DIY Project to which it belongs.

The filtering panel will allow the creator to narrow down the list according to their DIY Project (By Thing) or by the parent of the DIY Project. It is also possible to search on a specific text in the title or in the text of the DIY Project Instructions if we want to locate a specific Instructions element.

By marking the desired Instruction items, the Delete action can be used on any number of selected Instruction items at the same time.

Clicking on the title of any Instructions item in the list opens its Change Instructions page, where the Instructions data can be edited.

![DIY-Instructions webpage](assets/media/image25.png)

##### Change Instructions webpage

In this page Instructions item data can be edited.

Once all the required changes to the Instructions item have been made, there are three ways to save the data. Save all changes and return to the list, save all changes and continue editing in the current Instructions item, or save all changes and create a new blank Instructions item. Exiting this page or reloading without saving, will immediately delete all changes made to the Instructions item.

![Change Instructions webpage](assets/media/image26.png)

The Instructions field has an embebded WSIWYG editor from the Django Sumernote extension, that allows to insert text, images, videos, links and any HTML/CSS needed to present the instructions. It is the responsability of the creator to write a Instructions element that will be displayed correctly to the final user.

The Instructions elements are presented to the end user sorted by Title. This is useful if a particular order needs to be maintained in the instructions, so assigning titles such as "Step 01", "Step 02", etc. could be used to maintain a strict order. Special care should be taken when changing the Title, as it may affect the order in which the instructions are presented to the end-user.

##### Administrators webpage

This web page is only available when the user is an administrator, and provides full access to all website settings.

This documentation only shows the main admin page, as the DIY pages are the same as described for content creators, and the rest can be found in the Django documentation.

![Administrators webpage](assets/media/image27.png)

## Future Enhancements

In a future implementation, the following capabilities would be desired:

- Users should be able to browse the list of their favorite DIY Projects
- User creating DIY Project should be able to upload data files for sharing (STL, CAD, Gerber, etc.)
- There should be a supervisor, automatic or manual, to validate new user DIY Projects.
- Users should be able to comment on and rate any DIY Project
- There should be a moderator function, automatic or manual, to validate and control user comments.
- Users should be able to loging using their social networks accounts
- The user should be able to exchange messages directly with other users.
- Users should be able to receive compensation for their DIY projects sold.
- Users should have the option to donate for any free shared content
- There should be other payment methods like Paypal, Scrow, Bank transfer, etc.


## Testing

### Testing Strategy

Since the webpages for the unknown or regular users that are the webpages handled from scratch by the project which are minimalistic and simple, and the administrative pages are mostly handled by a well tested Django Allauth extensions, I decided that a manual testing strategy for the application can be easier to deploy and more effective in terms of time and human efforts.

As for the code validation, I use online applications to check that the source code for all the languages used are in line with the required standards.

### Validating the Source

#### Django Python code

In order to validate the python code as PEP8 compliant, I have run it througt "Flacke8" tool and checked the results
There was no error found in any of my python files.

#### CSS code

In order to validate the CSS code, I tried to pass the url of the deployed website to the CSS validator from W3C, but there where many warnings related to the many third party extensions used by Bootstrap and others.

I decide to validate only the style.css file that is really the only one I have customized. The result is as follows:

![CSS code validation](assets/media/image28.png)

Unfortunately the result is in spanish, but translates to "Congratulations!, No errors found" and "This document is CSS version 3

- SVG Valid!",

The validator only reported 2 warnings regarding two features from a vendor extension, which its no problem.

#### HTML code

In order to validate HTML, I pass the following deployed website urls to the HTML validator from W3C:
- [Home page](https://diyshop-e5a99a0c89cb.herokuapp.com/)
- [products page]( https://diyshop-e5a99a0c89cb.herokuapp.com/products/)
- [product detail page](https://diyshop-e5a99a0c89cb.herokuapp.com/products/1/)
- [user profile page](https://diyshop-e5a99a0c89cb.herokuapp.com/profile/)
- [user shopping bag](https://diyshop-e5a99a0c89cb.herokuapp.com/bag/)
- [checkout page](https://diyshop-e5a99a0c89cb.herokuapp.com/checkout/)

Only "Warning: The type attribute is unnecessary for JavaScript resources. " were detected.


### Testing the application

Most of the bugs have been detected and fixed in the development process. And Deployment in Heroku counts for me as a Smoke Test for the application. Then all the specific features can be tested.

In order to test most of the developed features, I created a list of test cases to run in the deployed website

<table><tbody><tr><td><strong>TC-01 - user website navigation</strong></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td><strong>Done</strong></td><td><strong>Step</strong></td><td><strong>Description</strong></td><td><strong>Expectations</strong></td><td><strong>Result</strong></td><td><strong>Pass</strong></td><td><strong>Additional info</strong></td></tr><tr><td>x</td><td>1</td><td>Navigate to the home page</td><td>Home page is shown</td><td>OK</td><td>x</td><td>-</td></tr><tr><td>x</td><td>2</td><td>The banner carrousel</td><td>automatically move left one picture every 3 seconds</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>3</td><td>In any page click on header brand logo</td><td>redirects to home page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>4</td><td>In any page click on header brand name</td><td>redirects to home page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>5</td><td>Anonymous user in any page click on user menu button</td><td>offers `Sign Up` and `Sign In` options</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>6</td><td>Regular signed-in user in any page click on user menu button</td><td>offers `E-mail` and `Sign Out` options</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>7</td><td>Administrator or creator signed-in user in any page click on user menu button</td><td>offers `Admin`, `E-mail`, and `Sign Out` options</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>8</td><td>In any page click on `Sign Up` option menu</td><td>redirects to the sign-up page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>9</td><td>In any page Click on `Sign In` option menu</td><td>redirects to the sign-in page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>10</td><td>Anonymous user In Home page click on 'Join us..' link</td><td>redirects to the sign-in page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>X</td><td>11</td><td>Signed in user In Home page click on 'Check out ...' link</td><td>Redirects to the DIY project list below</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>12</td><td>In Home page click on `&lt;` on the banner carrousel</td><td>moves the carrousel one picture left</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>13</td><td>In Home page click on `&gt;` on the banner carrousel</td><td>Moves the carrousel one picture right</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>14</td><td>In Home page click on any DIY project picture</td><td>redirects to the selected DIY Project details page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>15</td><td>In Home page click on any DIY project Title</td><td>redirects to the selected DIY Project details page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>16</td><td>In DIY Project details page click on heart icon (likes)</td><td><p>The heart icon toggles the fill colour</p><p>The number of likes change accordingly</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>17</td><td>In any page click on any social media icon at the footer</td><td>Opens the new webpage to the corresponding social network</td><td>OK</td><td>x</td><td>Action works correctly but does not point to any particular social account.</td></tr></tbody></table>

<table><tbody><tr><td><strong>TC-02 – Unregistered user sign-up procedure</strong></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td><strong>Done</strong></td><td><strong>Step</strong></td><td><strong>Description</strong></td><td><strong>Expectations</strong></td><td><strong>Result</strong></td><td><strong>Pass</strong></td><td><strong>Additional info</strong></td></tr><tr><td>x</td><td>1</td><td>In sign-up page enter an invalid email, a valid username and valid passwords, and push sign-up button (e.g. “theemail” as email)</td><td>Message indicating invalid email</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>2</td><td>In sign-up page enter a valid email, an invalid username and valid passwords, and push sign-up button (e.g. “test!!user” as user name)</td><td>Message indicating invalid user name</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>3</td><td>In sign-up page enter a valid email, a valid username and two different passwords, and push sign-up button</td><td>Message indicating passwords must be the same</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>4</td><td>In sign-up page enter a blank email, a valid username and valid passwords, and push sign-up button</td><td>Message indicating to fill email</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>5</td><td>In sign-up page enter a valid email, a blank username and valid passwords, and push sign-up button</td><td>Message indicating to fill username</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>6</td><td>In sign-up page enter a valid email, a valid username and empty passwords, and push sign-up button</td><td>Message indicating to fill passwords</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>7</td><td>In sign-up page enter a valid email, a valid username and valid passwords, and push sign-up button</td><td><p>Redirected to confirm-email page.</p><p>An e-mail requesting to confirm the account is sent to the email with the “confirmation link”</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>8</td><td>In sign-up page enter an existing valid email, a different valid username and valid passwords, and push sign-up button</td><td><p>Redirected to confirm-email page.</p><p>An e-mail warning of a duplicate e-mail attempt is sent to the email</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>9</td><td>Navigate to a valid ‘confirmation link’</td><td>Presents the email confirmation page with a confirm button</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>10</td><td>Navigate to an invalid ‘confirmation link’</td><td><p>Presents the email confirmation page with the “invalid confirmation link” message</p><p>Offers a “request a password reset” link</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>11</td><td>In an email confirmation page press the confirm button</td><td>Redirected to sign-in page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>12</td><td>In sign-up page enter a valid email, an existing valid username and valid passwords, and push sign-up button</td><td>Message indicating that the username already exists</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>13</td><td>In the sign-in page click the ‘sign up’ link</td><td>redirects to the sign-up page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr></tbody></table>

<table><tbody><tr><td><strong>TC-03 – registered user sign-in procedure</strong></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td><strong>Done</strong></td><td><strong>Step</strong></td><td><strong>Description</strong></td><td><strong>Expectations</strong></td><td><strong>Result</strong></td><td><strong>Pass</strong></td><td><strong>Additional info</strong></td></tr><tr><td>x</td><td>1</td><td>In sign-in pag enter an invalid email, a valid passwords, and push sign-in button (e.g. “username” as email)</td><td>Message indicating invalid email</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>2</td><td>In sign-in page enter a blank email, a valid password, and push sign-in button</td><td>Message indicating to fill email</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>3</td><td>In sign-in page enter a valid registered email, an incorrect password, and push sign-in button</td><td>Message indicating wrong email or password</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>4</td><td>In sign-in page enter a valid non registered email, and password, and push sign-in button</td><td>Message indicating wrong email or password</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>5</td><td>In sign-in page enter a valid registered email and correct password, and push sign-in button</td><td><p>Redirects to home page</p><p>User menu button shows the username</p><p>User menu options are ‘e-mail’ and ‘Sign Out’</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr></tbody></table>

<table><tbody><tr><td><strong>TC-04 – registered user reset password procedure</strong></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td><strong>Done</strong></td><td><strong>Step</strong></td><td><strong>Description</strong></td><td><strong>Expectations</strong></td><td><strong>Result</strong></td><td><strong>Pass</strong></td><td><strong>Additional info</strong></td></tr><tr><td>x</td><td>1</td><td>In sign-in page click the ‘Forgot your Password?’ link</td><td>Redirects to password-reset page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>2</td><td>In password-reset page enter a blank email and press ‘reset’ button</td><td>Message indicating to fill email</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>3</td><td>In password-reset page enter an invalid email and press ‘reset’ button</td><td>Message indicating invalid email</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>4</td><td>In password-reset page enter a valid unregistered email and press ‘reset’ button</td><td><p>Redirects to reset-done page</p><p>presents a message saying that the reset email is sent</p><p>An email is sent to the email address with a link to the sign-up page</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>5</td><td>In sign-in page enter a valid registered email and correct password, and push sign-in button</td><td><p>Redirects to reset-done page</p><p>presents a message saying that the reset email is sent</p><p>An email is sent to the email address with a link to the change-password page</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>6</td><td>In password-change page enter blank passwords and press change password button</td><td>Message indicating to fill passwords</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>7</td><td>In password-change page enter different passwords and press change password button</td><td>Message indicating to fill same passwords</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>8</td><td>In password-change page enter correct passwords and press change password button</td><td><p>Redirects to change-password-done page.</p><p>The new password is active</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr></tbody></table>

<table><tbody><tr><td><strong>TC-05 – signed in user change e-mail procedure</strong></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td><strong>Done</strong></td><td><strong>Step</strong></td><td><strong>Description</strong></td><td><strong>Expectations</strong></td><td><strong>Result</strong></td><td><strong>Pass</strong></td><td><strong>Additional info</strong></td></tr><tr><td>x</td><td>1</td><td>In any page Click on `E-mail` option menu</td><td>Redirects to email-addresses page</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>2</td><td>In email-addresses page enter a blank email and press ‘Add Email’ button</td><td>Message indicating to fill email</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>3</td><td>In email-addresses page enter an invalid email and press ‘Add Email’ button</td><td>Message indicating invalid email</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>4</td><td>In email-addresses page enter a valid already registered email and press ‘Add Email’ button</td><td>Message indicating email address already registered</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>5</td><td>In email-addresses page enter a valid non registered email and press ‘Add Email’ button</td><td><p>A message is displayed requesting to confirm the email address.</p><p>An e-mail requesting to confirm the account is sent to the email address with the “confirmation link”</p><p>The email-address page is reloaded</p><p>The new email address is added to the users email addresses list and it is marked as Unverified</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>6</td><td>In email-addresses page select an unverified email address and press ‘Make Primary’ button</td><td>Message indicating that the email address has not been verified</td><td>OK</td><td>x</td><td>&nbsp;</td></tr><tr><td>x</td><td>7</td><td>In email-addresses page select a verified email address and press ‘Make Primary’ button</td><td><p>A message is displayed confirming that the email address is primary now.</p><p>An e-mail requesting to confirm the account is sent to the email address with the “confirmation link”</p><p>The email-address page is reloaded</p><p>The selected email address is marked as Primary</p><p>The new email address is active for next sign-in</p></td><td>OK</td><td>x</td><td>&nbsp;</td></tr></tbody></table>

## The development environment

For the development of this application the following list of frameworks, services and resources where used

> Microsoft Visual Studio Code v1.87 for linux was used as de IDE for the development.

> Git was used for version control and file transfer between the IDE and the repository in GitHub.

> GitHub is the online service that stores the development project

> Moqups.com is the online service I used to create the UI sketches for the website

> GIMP 2.10 used for all the image manipulation.

> PGAdmin IV was used to verify and generate the ERD representation for the SQL database

> Django v3.2.24 was used for the runtime frameworks

> Bootstrap v5.3.3 is used for the front end development as a CDN service

> ElephantSQL is the online service that hosts the SQL database for development and the deployed version

> AWS S3 services from Amazon to host the media files for the deployed version

> Fontawesome is the service that provides with fonts and icons as a CDN service

> Stripe is the online payment gateway service

> Gmail smtp services for sending E-mail messages to users.

> Heroku is the online service that hosts the web site for the deployed version.

### Resources

> Ghithub online documentation

> The Django and its extensions (Allauth, Sumernote, etc) online documentation

> The HTML and CSS documentation

> Bootstrap 3 online documentation

> Bootstrap 5 online documentation

> The Code Institute reference material.

Files and Images

> diy-projects-01.jpg from constructionmarketingassociation.org

> diy-projects-02.jpg from homeaddict.io

> diy-projects-03.webp from greenbuildinginsider.com

> diy-projects-04.jpg from www.simplifiedbuilding.com

> diy-projects-05.jpg youtube.com/c/NoSkillsRequired

> diy-projects-06.jpg youtube.com/TrendVerse Talks

> DIY Project "Reed Dryer for Basson"

Author: Juan Manuel de las Heras

Images: Juan Manuel de las Heras

> DIY Project "Soldering Fumes Extractor"

Author: Giovanni Aggiustatutto

Images: Giovanni Aggiustatutto

> DIY Project "Baby Groot Webcam"

Author: Juan Manuel de las Heras

Images: Juan Manuel de las Heras

> DIY Project "Terminator T850 animatronics"

Author: Juan Manuel de las Heras

Images: Juan Manuel de las Heras

## Deployment

The site was deployed via Heroku. Access the site using the following link -[**DIY Shop**](https://diyshop-e5a99a0c89cb.herokuapp.com/)  

For the deployment in Heroku, we assume that the media files server and the database server is already defined and a base database is restored from a backup. Otherwise, the process of deployment must be done using a development environment first, and use the fixtures from Django to populate the database with the minimum information. In that scenario, first clonning the repository could be a better choice.

There is a set of fixtures files under [products/fixtures/] and the corresponding media files under [media]. They can be used to populate the database with initial example data. 

### How to deploy the project on Heroku

Sign up / Log in to [Heroku](https://www.heroku.com/)

From the main Heroku Dashboard page select 'New' and then 'Create New App'

Give the project a name and select the region, then select create app.

I used ‘diyshop’ as the name for my Heroku app

Once finished creating the app, navigate to the setting tab, and select the `Reveal Config Vars` in the config vars section. And create the following variables:

- DEVELOPMENT
  - Values: "True" or "False"
- SECRET_KEY
  - Example: "9087zxcv98z798bv^=098zxcv098xzcv09*u2dsd2u+&hddf0^^uj"
- ALLOWED_HOSTS
  - Example: "127.0.0.1,localhost, diyshop-1c0dad79f0a0.herokuapp.com"
- DATABASE_URL
  - Example: "postgres://cmftklgz:gYdAbasasdasdasdsadsad234@dumbo.db.elephantsql.com/cmftklgz"
- ACCOUNT_EMAIL_VERIFICATION
  - Values: "none" or "mandatory"
- EMAIL_FROM_DEFAULT
  - Example: "sales-dep@diyshop.com"
- EMAIL_HOST
  - Example: "smtp.gmail.com"
- EMAIL_HOST_USER
  - Example: "diyshop@gmail.com"
- EMAIL_HOST_PASSWORD
  - Example: "asldknlmalsm"
  - Note:  gmail smtp servers do not accept user passwords but application passwords can be used.
- STRIPE_PUBLIC_KEY
  - Example: "pk_test_51PasdfASDFasdfasDFasdFASDFasdfag$%234weADSfGzdgLg9vUarbSvl1IBriGElYtCE0PIjVDJCkVwCM7v4hascasdcSD43"
- STRIPE_SECRET_KEY
  - Example: "sk_test_51PGzdg23re0987asdlkj34ot5245098uwrve09jvlñkwevkjwgSERVWERVwervwerfQErvñmekfvoieLg9vUarbSvaBPVn0TH8"
- STRIPE_WH_SECRET
  - Example: "whsec_9ff13b16lñknsadvTWsdafvadv299106f445ef6f269b02236aa87180952ecf8387046f2322cee5d28f"
  - Note:To run application in local enironment use stripe cli tool command

        $ ./stripe listen --forward-to 127.0.0.1:8000/checkout/wh
- USE_AWS
  - Values: "True" or "False"
- AWS_STORAGE_BUCKET_NAME
  - Example: "diyshop"
- AWS_S3_REGION_NAME
  - Example: "us-west-1"
- AWS_ACCESS_KEY_ID
  - Example: "KAIAXYKJQI5SCKKCUDVN"
- AWS_SECRET_ACCESS_KEY
  - Example: "iP87W4SDFD/6RWQyiasdf134134feqwwef4EU86U"


This variables would have to be defined in the env.py file of the project if the application runs in the local computer of a development environment.

In Heroku, navigate to the “Deploy” tab and use the option “GitHub (connect to GitHub)”

Scroll down and click on “Connect to GitHub”

In the repository search option, type the name of this repository or your own repository name if you have cloned it, and then use the “Connect” option and wait for the new “Deploy Branch” option appear.

Use the “Deploy Branch” option and wait until the deployment is complete.

Once you receive the message “The app was successfully deployed” you can access the deployed applications

Once the application is deployed, do not forget to assign the ALLOWED_HOSTS variable from the step 4 if it was not assigned earlier.

### Create a clone of this repository

Creating a clone enables you to make a copy of the repository allowing  
you to run the application in your local development environment:

1. Navigate to [This repository](https://github.com/Juanma1313/diyshop)
2. click on the arrow on the green ‘code’ button at the top of the list of files
3. select the ‘HTTP’ option to clone using the web URL and copy the URL to your clipboard.
4. At you local computer, use the console and change your directory to the disk directory where you want the application to be cloned.
5. At the console prompt, type 'git clone ' and paste the https link from your clipboard, followed by enter
6. once the git command has finished, you should have a local copy of the repository that can be opened by a IDE of your choice and for  example, push it to a new repository in GitHub to deploy it from your own repository

## Acknowledgements

- Giovanni Aggiustatutto author of the “Soldering fumes extractor” DIY  
  Project included in the deployed website as demo.
- Ainhoia de las Heras Hombrados for her help in the authoring of the  
  “Reed Dryer for Bassoon” DIY Project included in the deployed  
  website as demo.
- CI Student Care members, for their patience and care in dealing with  
  my case.
- StackOverflow with some problems specifically with Python and Django
