# DIY Shop User stories
The following list of user stories are part of the backlog of the seccond stage of development.
## Backlogs and Kanban boards

### DIY Site
- [DIY Site Kanban board in Github](https://github.com/users/Juanma1313/projects/5/views/1)
- [DIY Site Backlog (milestone) in Github](https://github.com/Juanma1313/dys/milestone/1)

### DIY Site
- [DIY Shop Kanban board in Github](https://github.com/users/Juanma1313/projects/6/views/1)
- [DIY Shop Backlog (milestone) in Github](https://github.com/Juanma1313/diyshop/milestone/1?closed=1)

# Table of Contents

- [EPIC: Setup initial development environment](#1-epic-setup-initial-development-environment)
- [EPIC: DIY Project creation and management](#4-epic-diy-project-creation-and-management)
- [EPIC: Searching DIY Projects](#17-epic-searching-diy-projects)
- [EPIC: User Shopping Cart](#22-epic-user-shopping-cart)
- [EPIC: User Shopping Cart Checkout](#26-epic-user-shopping-cart-checkout)
- [EPIC: User Profiles](#30-epic-user-profiles)
- [EPIC: User Messages and Notifications](#33-epic-user-messages-and-notifications)


#### [#1](https://github.com/Juanma1313/diyshop/issues/1) EPIC: Setup initial development environment

As a **developer**, I can **setup initial environment**, so that
**The website can be developed**

##### [#2](https://github.com/Juanma1313/diyshop/issues/2) USER STORY: Create Development Environment

As **developer**, I can **setup the development environment**,
so that **I can start developing the website**

###### Tasks

- [X] Task 1 – Install Visual Studio Code in local environment
- [X] Task 2 – Create website Github repository and start remote  environment
- [X] Task 3 – Install Django and all required libraries for runtime and development of the website
- [X] Task 4 – Create Django project and application
- [X] Task 5 - Create local database structures in SQLite3
- [X] Task 6 - Create fixtures from deployed DIY Site database and media storage
- [X] Task 7 - Upload fixtures to new database

###### Story Points: 13

##### [#3](https://github.com/Juanma1313/diyshop/issues/3) USER STORY: Administrate users

As **Administrator**, I can **Create/modify/delete user accounts and their privileges**, so that **I can assign who signs in on the website and who can create or modify content**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am an `Administrator` user
  **When** I am in any website page
  **Then** I can access the admin web page selecting the `Admin` option in the user menu
- Acceptance Criteria 2

  **Given** that I am an `Administrator` user
  **When** I am in admin website page
  **Then** I can add/delete/modify any user
- Acceptance Criteria 3

  **Given** that I am an `Administrator` user
  **When** I am in admin website page
  **Then** I can add/delete/modify any privilege of any user and any group

###### Tasks

- [X] Task 1 - Install and setup Django's allauth and its accounts and interfaces, extensions.
- [X] Task 2 - Create at least one administrator account
- [X] Task 3 - Customize allauth templates to the website base template
- [X] Task 4 - Create `Content Creators` user group with necessary  privileges for content creators

###### Story Points: 8

#### [#4](https://github.com/Juanma1313/diyshop/issues/4) EPIC: DIY Project creation and management

As a **user**, I can **add/modify/delete my own DIY projects**, so that **my DIY Projects can be published and access by other users on the website**

##### [#5](https://github.com/Juanma1313/diyshop/issues/5) USER STORY: Create a DIY project

As **registered user**, I can **Create a DIY project**, so that **I can publish it and share it on the website**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am in any website page
  **Then** I can access the `Add Project` option in the user menu
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I click on the `Add Project`option in the user menu
  **Then** I can create a new DIY Project
- Acceptance Criteria 3

  **Given** that I am a `Registered User`
  **When** I have created a new DIY Project
  **Then** The Created date, Modified_Date and Parent fields are
  automatically created for this DIY project

###### Tasks

- [X] Task 1 - Allow the `Add Project` option in the user menu in
  the base template for the main website
- [X] Task 2 - Allow the creation of new `Thing` for registered users

###### Story Points: 8

##### [#6](https://github.com/Juanma1313/diyshop/issues/6) USER STORY: Create DIY project details

As **Registered User**, I can **create the DIY project details**, so that **project can have a featured image and description**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I have created a new DIY Project (`Thing`)
  **Then** I can assign a Title, Status, and Featured Image
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I have created a new DIY Project (`Thing`)
  **Then** I can edit a WSWG document to the description
- Acceptance Criteria 3

  **Given** that I am a `Registered User`
  **When** I have created a new DIY Project (`Thing`)
  **Then** I need to use a Save button to permanently store the changes in the database

###### Tasks

- [X] Task 1 - Install Django Summernote extension for adding  embedded WSWG editing functionality.
- [X] Task 2 - Create the products/forms.ProductForm to accommodate all detail fields for the new `Thing`
- [X] Task 3 - Create the add_product template to accommodate the new ProductForm

###### Story Points: 8

##### [#7](https://github.com/Juanma1313/diyshop/issues/7) USER STORY: Create Instructions

As **Registered User**, I can **create project instructions for my DIY Projects**, so that **the users can read and follow them**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am in any website page
  **Then** I can access the `Add Instructions` option in the user menu
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I click on the `Add Instructions` option in the user menu
  **Then** I can create a new `Instructions` element
- Acceptance Criteria 3

  **Given** that I am a `Registered User`
  **When** I have created a new `Instructions` element
  **Then** I must assign the `Instructions` element to one of my existing DIY Projects

###### Tasks

- [ ] Task 1 - Allow the `Add Instructions` option in the user menu in the base template for the main website
- [ ] Task 2 - create a product/views.add_instructions to allow the creation of new `Instructions` element for registered users
- [ ] Task 3 - create the product/forms.ProductInstructions form to accommodate the Instructions data including Summernote edit functionality to the  `instructions` field to allow for the WSWG edit features.
- [ ] Task 4 - create the product add_instructions template to accommodate the product/forms.ProductInstructions form to present the page to the user.

###### Story Points: 8

##### [#8](https://github.com/Juanma1313/diyshop/issues/8) USER STORY: Create component

As **Registered User**, I can **create components for my DIY Projects**, so that **a user can view and gather the building blocks to fulfil the project**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I have created a DIY Project (`Thing`)
  **Then** I can assign it to any of my existing DIY Project

###### Tasks

- [ ] Task 1 - Modify the products/forms.ProductForm to allow assigning a parent DIY Project to the current `Thing`, making it a component of the parent DIY Project. The Parent DIY Project must belong to the registered user.

###### Story Points: 3

##### [#9](https://github.com/Juanma1313/diyshop/issues/9) USER STORY: Modify a DIY project details

As **Registered User**, I can **modify the DIY project details**, so that **the project can be corrected or upgraded**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am viewing my  DIY Project (Thing)
  **Then** I can use a button to bring a  page to modify my DIY Project
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I am modifying my DIY Project (Thing)
  **Then** I can change the Title, Author, Status, and Featured Image
- Acceptance Criteria 3

  **Given** that I am a `Registered User`
  **When** I am modifying my DIY Project (Thing)
  **Then** I can edit a WSWG document to the description

###### Tasks

- [X] Task 1 - Create the edit_product template to accomodate for the product/forms.ProductForm form and allow to update the DIY Project details
- [X] Task 2 - Modify the products and product_detail templates to provide 'edit'  button to the user's own DIY projects.

###### Story Points: 5

##### [#10](https://github.com/Juanma1313/diyshop/issues/10) USER STORY: Modify component

As **Registered User**, I can **modify my component's details**, so that **my components can be corrected or upgraded**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am viewing one of my Components (`Thing`)
  **Then** I can select a `edit` button to change the details
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I am modifying my Component (`Thing`)
  **Then** I can edit the description with a WSWG built-in editor
- Acceptance Criteria 3

  **Given** that I am a `Registered User`
  **When** I am modifying my DIY Project (`Thing`)
  **Then** I must use a `Save` button to permanently store the changes in the database

###### Tasks

- built in [#9](https://github.com/Juanma1313/diyshop/issues/9)

###### Story Points: 0

##### [#11](https://github.com/Juanma1313/diyshop/issues11/) USER STORY: Modify instructions

As **Registered User**, I can **modify my Instructions elements**, so that **the DIY Project can be corrected or upgraded**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am viewing a DIY Project (`Thing`)
  **Then** I can select the `edit`button of the Instructions element to change the Instructions
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I am modifying an Instructions element
  **Then** I can change the content of Instructions with a WSWG built-in editor
- Acceptance Criteria 3

  **Given** that I am a `Registered User`
  **When** I am modifying an Instructions element
  **Then** I must use a `Save` button to permanently store the changes in the database

###### Tasks

- [ ] Task 1 - create a products/views.edit_Instructions to query the Instructions data in the database
- [ ] Task 2 - Create the edit_Instructions template to accommodate  product/forms.ProductInstructions to allow updating of Instructions fields.

###### Story Points: 5

##### [#12](https://github.com/Juanma1313/diyshop/issues/12) USER STORY: Delete a project

As **Registered User**, I can **delete my DIY project**, so that **the project does no longer exist on the website**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Register User`
  **When** I select a DIY project of my own from the DIY Projects list
  **Then** I can delete the selected DIY Project
- Acceptance Criteria 2

  **Given** that I am a `Register User`
  **When** I am modifying my DIY Project on the website
  **Then** I can delete the current DIY Project
- Acceptance Criteria 3

  **Given** that I am a `Register User`
  **When** I have requested to delete one or more DIY projects of my own
  **Then** I will have to explicitly confirm the deletion

###### Tasks

- [X] Task 1 - create a products/views.delete_product to allow querying the deletion of the selected DIY Project from the database.
- [X] Task 2 - Modify the products and product_detail templates to provide 'delete'  button to the user's own DIY projects.

###### Story Points: 3

##### [#13](https://github.com/Juanma1313/diyshop/issues/13) USER STORY: Delete a owned Components

As **Registered User**, I can **delete a component**, so that **the component does no longer exist on the website**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am viewing my DIY Components `Things`
  **Then** I can delete an existing DIY Component
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I have requested to delete one or more DIY Components
  **Then** I will have to explicitly confirm the deletion

###### Tasks

Built in [#12](https://github.com/Juanma1313/diyshop/issues/12)

###### Story Points: 3

##### [#14](https://github.com/Juanma1313/diyshop/issues/14) USER STORY: Delete owned Instructions elements

As **Registered User**, I can **delete my Instructions elements**,
so that **those Instructions elements do no longer exist on the website**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am viewing my DIY Project (`Thing`)
  **Then** I can delete an existing Instructions element from the
  current DIY Project
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I have requested to delete one or more Instructions
  elements
  **Then** I will have to explicitly confirm the deletion

###### Tasks

- [X] Task 1 - create a products/views.delete_instructions allowing to query the deletion of the selected Instructions element from the database.
- [X] Task 2 - Modify the edit_Instructions, edit_product, and product_detail templates to provide 'delete' button to the user's own DIY projects.

###### Story Points: 5

##### [#15](https://github.com/Juanma1313/diyshop/issues/15) USER STORY: Change own DIY Project Published status

As **Registered User**, I can **change my DIY Project published status
**, so that **the DIY Project is available to other users when marked as
`Published` or hidden when it is marked as `Draft`**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** That I am a `Registered User`
  **When** I am creating or modifying a DIY Project
  **Then** I can toggle the published flag `Status` so that the DIY Project can be shown or hidden from viewing users.

###### Tasks

Built in [#6](https://github.com/Juanma1313/diyshop/issues/6) and [#9](https://github.com/Juanma1313/diyshop/issues/9)

###### Story Points: 0

##### [#16](https://github.com/Juanma1313/diyshop/issues/16) USER STORY: Change own DIY Component published status

As **Registered User**, I can **change my DIY Component published
status**, so that **the component information is available to users
when marked as `Published` or hidden when it is marked as `Draft`**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am creating or modifying a DIY Component
  **Then** I can toggle the published flag `Status` so that this
  Component can be shown or hidden from viewing
  users.

###### Tasks

Built in [#15](https://github.com/Juanma1313/diyshop/issues/15)

###### Story Points: 0

#### [#17](https://github.com/Juanma1313/diyshop/issues/17) EPIC: Searching DIY Projects

As a **user**, I can **sort, filter and search for DIY projects**, to **better find the ones that suit me best**.

##### [#18](https://github.com/Juanma1313/diyshop/issues/18) USER STORY: Manage DIY Projects Categories

As **Administrator**, I can **create/modify/delete categories to classify the DIY Projects in the database**, so that **users can filtrate DIY Projects by the categories of their interest**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Administrator`
  **When** I want a new Category to classify DIY Projects
  **Then** I can use the admin interface to add it to the list of Categories.
- Acceptance Criteria 2

  **Given** that I am a `Administrator`
  **When** I create  a new Category
  **Then** I assign an internal lowercase name to be used by the application, and a friendly name that will be shown in the webpage.
- Acceptance Criteria 3

  **Given** that I am a `Administrator`
  **When** I need to modify a Category
  **Then** I can use the admin interface to edit the internal and the friendly name.
- Acceptance Criteria 4

  **Given** that I am a `Administrator`
  **When** I need to delete a Category
  **Then** I can use the admin interface to delete the selected Category
- Acceptance Criteria 5

  **Given** that I am a `Administrator`
  **When** I have deleted a Category
  **Then** The DIY Projects that had that Category, stays without Category.

###### Tasks

- [X] Task 1 – Create product.Category class model that will be used to instantiate each Category object
- [X] Task 2 – Modify the DIY Project object model 'Thing' to include the Category model
- [X] Task 3 – Create the admin.CategoryAdmin view to handle Category elements in the Admin user interface.

###### Story Points: 5

##### [#19](https://github.com/Juanma1313/diyshop/issues/19) USER STORY: Filter DIY Projects by Categories

As **user**, I can **filter DIY Projects by Categories**, so that **I can narrow down the DIY Projects I want to review based on categories of their interest**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `user`
  **When** I want to filter DIY Projects by categories
  **Then** I can use the main navigation menu to select a particular filter

###### Tasks

- [X] Task 1 – Modify the main-nav template to displays a list of useful filtering options for one or several categories
- [X] Task 2 – Modify the products/views.all_products view tu include the selected filter to the database query for the DIY Projects list.

###### Story Points: 8

##### [#20](https://github.com/Juanma1313/diyshop/issues/20) USER STORY: Sorting DIY Projects

As **user**, I can **use a predefined sorting option from the main-nav bar**, so that **I can view the list of DIY Projects in a particular order**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `user`
  **When** I want to sort DIY Projects by date
  **Then** I can use the main navigation menu to select the new arrival to get the DIY Project list ordered from newer to older.
  **Then** I can use the dropdown sorting menu to select the Date(new to old) or Date (old to new) to get the DIY Project list ordered as selected
- Acceptance Criteria 2

  **Given** that I am a `user`
  **When** I want to sort DIY Projects by price
  **Then** I can use the main navigation menu to select the `By Price` option to get the DIY Project list ordered by price from lower to higher.
  **Then** I can use the dropdown sorting menu to select the Price(low to high) or Price(high to low) to get the DIY Project list ordered as selected
- Acceptance Criteria 3

  **Given** that I am a `user`
  **When** I want to sort DIY Projects by rating
  **Then** I can use the main navigation menu to select the `By Rating` option to get the DIY Project list ordered by rating  from higher to lower.
  **Then** I can use the dropdown sorting menu to select the Rating(low to high) or Rating(high to low) to get the DIY Project list ordered as selected
- Acceptance Criteria 4

  **Given** that I am a `user`
  **When** I want to sort DIY Projects by Category
  **Then** I can use the main navigation menu to select the `By Category` option to get the DIY Project list ordered by category from A to Z.
  **Then** I can use the dropdown sorting menu to select the Category(A to Z) or Category(Z to A) to get the DIY Project list ordered as selected
- Acceptance Criteria 5

  **Given** that I am a `user`
  **When** I want to sort DIY Projects by name
  **Then** I can use the dropdown sorting menu to select the Name(A to Z) or Name(Z to A) to get the DIY Project list ordered as selected

###### Tasks

- [X] Task 1 – Modify the main-nav template to displays the list of useful ordering options
- [X] Task 2 – Modify the products template include a dropdown list of the required ordering options
- [X] Task 3 – Modify the products/views.all_products view tu include the selected ordering to the database query for the DIY Projects list.

###### Story Points: 8

##### [#21](https://github.com/Juanma1313/diyshop/issues/21) USER STORY: Searching DIY Projects with text

As **user**, I can **search a text in DIY Projects**, so that **I can get a list of the DIY Projects containing the submitted text**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `user`
  **When** I want to search DIY Projects for specific text
  **Then** I can write the text to search and i will get a list of DIY Projects that contain the text in the name or the description

###### Tasks

- [X] Task 1 – Add a text search control to the base template
- [X] Task 2 – Modify the products/views.all_products view tu include the selected text to the database query for the DIY Projects list.

###### Story Points: 8

#### [#22](https://github.com/Juanma1313/diyshop/issues/22) EPIC: User Shopping Cart

As a **user**, I can **add DIY Project to my shopping cart**, to **be able to keep track of the added items and costs**.

##### [#23](https://github.com/Juanma1313/diyshop/issues/23) USER STORY: add Projects to the shopping cart

As **User**, I can **add a Non Free DIY Proyect to my cart**, so that **I can keep track of my selections and my costs**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `User`
  **When** I am in a DIY project details page of a non free DIY Project
  **Then** I can use the `+` or `-` buttons to adjust the number of kits I want to add to my shopping cart (Shopping Bag).
  **Then** I can use the `Add To Bag` button to add the selected numberof DIY project kits to my shopping cart (Shopping Bag)..

###### Tasks

- [X] Task 1 – Create the bag application
- [X] Task 2 – Create the session store mecanism to hold the shopping items added
- [X] Task 3 – Create the bag/views.add_to_bag view to allow for the shopping items to be added
- [X] Task 4 – modify the base template to include the shopping cart icon

###### Story Points: 13

##### [#24](https://github.com/Juanma1313/diyshop/issues/24) USER STORY: view the shopping cart content

As **User**, I can **see all the shopping items I currently have in my shipping cart**, so that **I can keep track of my selections and my costs**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `User`
  **When** I am in any web shop page
  **Then** I can click the shopping bag icon to bring the shopping bag details page.

###### Tasks

- [X] Task 1 – Create the bag/views.view_bag view to allow for the shopping items in the shopping cart to be displayed
- [X] Task 2 – Create the bag template to display the items and totals

###### Story Points: 5

##### [#25](https://github.com/Juanma1313/diyshop/issues/25) USER STORY: manage shopping items in the shopping cart

As **User**, I can **increment/decrement the number of shopping items I currently have in my shopping cart**, so that **I can adjust my selections and my costs**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `User`
  **When** I am in the shopping bag view detail page
  **Then** I can use the `+` or `-` buttons for any shopping item to adjust the number of that item I want to keep in my shopping cart.
  **Then** I can use the `Update` button to update the number of items in the shopping cart.
  **Then** I can use the `Remove` button to permanently delete that item from the shopping cart.

###### Tasks

- [X] Task 1 – Create the bag/views.adjust_bag view to allow for the shopping cart content to be modified
- [X] Task 2 – modify the bag template to include counter, update and remove options per each item in the shopping cart

###### Story Points: 5

#### [#26](https://github.com/Juanma1313/diyshop/issues/26) EPIC: User Shopping Cart Checkout

As user, I can checkout the content of my shopping cart, so that I am able to formalize the purchase and delivery of the content of the shopping cart.

##### [#27](https://github.com/Juanma1313/diyshop/issues/27) USER STORY: initiate checkout of the shopping cart

As **User**, I can **start the checkout process for the content of my sopping cart**, so that **I can show the order summary and the payment methods**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `User`
  **When** in the shopping cart detail page (Shopping Bag), I press the `Secure Checkout` button
  **Then** I am redirected to the checkout page, where the order form and order summary are presented.

###### Tasks

- [X] Task 1 – Create the checkout application
- [X] Task 2 – Create the checkout/models.Order class to instantiate order object
- [X] Task 3 – Create the checkout/forms.OrderForm form to handle all the required order fields
- [X] Task 4 – Create the checkout/views.checkout view to populate the order object from the shopping cart and start the payment transaction.
- [X] Task 5 – Create the checkout template to display the order form to the user

###### Story Points: 13

##### [#28](https://github.com/Juanma1313/diyshop/issues/28) USER STORY: Fill in the checkout form

As **User**, I can **fill in the checkout form**, so that **I provide full name, delivery and payment information**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `User`
  **When** in the checkout page
  **Then** I can see all the elements from the shopping bag with their cost
  **Then** I can see the delivery cost
  **Then** I can see the Grand total cost
- Acceptance Criteria 2

  **Given** that I am a `User`
  **When** in the checkout page, I press the `Adjust Bag` button
  **Then** I am redirected to the shopping cart detail page (Shopping Bag)
- Acceptance Criteria 3

  **Given** that I am a `Anonymous User`
  **When** in the checkout page, I press the `Sign Up` link
  **Then** I am redirected to the sign-up page
- Acceptance Criteria 4

  **Given** that I am a `Anonymous User`
  **When** in the checkout page, I press the `Sign In` link
  **Then** I am redirected to the sign-in page
- Acceptance Criteria 5

  **Given** that I am a `User` in the checkout page and I press the `Buy Now` button
  **When** the form data is not valid,
  **when** the database transaction has failed
  **when** the payment gateway transaction has failed
  **Then** cancel the order transactions on the database and payment gateway
  **Then** notify me of the problem

###### Tasks

- [X] Task 1 – Register with an online payment gateway service provider (Stripe)
- [X] Task 2 – Install and integrate the payment gateway service provider API

###### Story Points: 8

##### [#29](https://github.com/Juanma1313/diyshop/issues/29) USER STORY: submit the checkout order to the online payment service

As  **User**, I can **send the completed purchase form**, so that **the payment of the purchase order can be fulfilled**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `User`
  **When** in the checkout page with a valid checkout form, I press the `Buy Now` button
  **Then** the order is submited for payment to the external payment gateway.
- Acceptance Criteria 2

  **Given** that, an order has been submitted for payment to the external payment gateway.
  **When** the transaction is accepted
  **Then** The new purchase order is finally committed to the database
  **Then** An e-mail with the confirmation of the purchase is sent to the address that the user filled in the purchase form.
  **Then** The shopping cart is cleaned of all shopping items
  **Then** the user is redirected to the checkout_success page where all the details of the purchase order is displayed

###### Tasks

- [X] Task 1 – Create the checkout/views.checkout_success view to delete the shopping cart from the user session and render the chekout_success page.
- [X] Task 2 – Create the checkout_success template to display the relevant Order infomation.
- [X] Task 3 – Create the confirmation_emails templates for the e-mail subject and the e-mail body.
- [X] Task 4 – Create the checkout/emails.send_confirmation_email function to create the e-mail and send it to the address in the order.

###### Story Points: 8

#### [#30](https://github.com/Juanma1313/diyshop/issues/30) EPIC: User Profiles

As a **Registered User**, I can **set my billing information into a profile**, to **be able to use that profile for future checkouts**.

##### [#31](https://github.com/Juanma1313/diyshop/issues/31) USER STORY: Create a user profile

As **Registered User**, I can **save my billing information under my account**, so that **I can review, change and reuse it for future checkouts**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `User`
  **When** I sign up to the website
  **Then** An empty profile is created.
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** loading the checkout page
  **Then** the billing information (telephone, delivery address) is automatically filled in from my user profile
  **Then** a check button `save the delivery information to my profile` is checked by default
- Acceptance Criteria 3

  **Given** that I am a `Registered User`
  **When** in the checkout page
  **Then** I can change
  **Then** I have the option toggle the check button `save the delivery information to my profile`
- Acceptance Criteria 4

  **Given** that I am a `Registered User`
  **Given** that from the checkout page, I have successfully submitted a purchase order
  **When** the check button `save the delivery information to my profile` is checked
  **Then** The delivery information from the purchase order (telephone and address) is saved to my user profile

###### Tasks

- [X] Task 1 – Create the profiles application
- [X] Task 2 – Create the profiles.UserProfile class to instantiate user profile objects in a one-to-one relation with the User class
- [X] Task 3 – Create the profiles/views.profile view to access the database user profile
- [X] Task 4 – Update checkout/views.checkout view to read user profile information and feed it to new checkouts
- [X] Task 5 – Update checkout/models.Order class to include a user profile member

###### Story Points: 13

##### [#32](https://github.com/Juanma1313/diyshop/issues/32) USER STORY: View and Manage my Profile

As **Registered User**, I can **view and change my profile information under my account**, so that **I can adapt the information to future checkouts**

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `Registered User`
  **When** I am in my user profile page
  **Then** I can view and change the delivery information
  **Then** I can view all my previous successfully submitted orders
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** in my user profile page, I press the `Update InFormation` button
  **Then** The information shown in the `my profile` form is updated in the database

###### Tasks

- [X] Task 1 – Create the profiles/views.order_history to access to all the user orders
- [X] Task 2 – Create the profile/forms.UserProfileForm to accommodate the profile data into a template
- [X] Task 3 – Create the profile template to present the user profile as a web page

###### Story Points: 5

#### [#33](https://github.com/Juanma1313/diyshop/issues/33) EPIC: User Messages and Notifications

As a **User**, I can **be informed about results of my operations**, so that **I get confirmations, information, warnings and errors about my interaction with the website**.

##### [#34](https://github.com/Juanma1313/diyshop/issues/34) USER STORY: User Messages and Notifications

As a **User**, I can **be informed about results of my operations**, so that **I get confirmations, information, warnings and errors about my interaction with the website**.

###### Acceptance Criteria

- Acceptance Criteria 1

  **Given** that I am a `User`
  **When** I request sign up, sign in or sign out
  **Then** I receive a pop-up message that notifies me of the result of the request
- Acceptance Criteria 2

  **Given** that I am a `Registered User`
  **When** I request to modify my email or password
  **Then** I receive a pop-up message that notifies me of the result of the request
- Acceptance Criteria 3

  **Given** that I am a `User`
  **When** I request DIY Project ordering, filtering or searching
  **Then** I receive a pop-up message whenever there is an error in the request
- Acceptance Criteria 4

  **Given** that I am a `Registered User`
  **When** I create, edit or delete a DIY Project
  **Then** I receive a pop-up message with the result of the operation
- Acceptance Criteria 5

  **Given** that I am a `User`
  **When** I modify my shopping cart, adding or deleting products
  **Then** I receive a pop-up message with the result of the operation
- Acceptance Criteria 6

  **Given** that I am a `User`
  **When** I receive a pop-up message with a success result of a shopping cart operation
  **Then** the pop-up message contains a summary of my shopping cart
  **Then** the pop-up provides the button `Go To Secure Chakout` to directly go to the checkout page.
- Acceptance Criteria 7

  **Given** that I am a `User`
  **When** I request a checkout
  **Then** I receive a pop-up message that notifies me of the result of the request
- Acceptance Criteria 8

  **Given** that I am a `User`
  **When** I modify my profile
  **Then** I receive a pop-up message with the result of the operation

###### Tasks

- [X] Task 1 – Set up Django messages framework to use flash messages for user notification
- [X] Task 2 – Add messages of type Success, Info, Warning and Error for the results of all the user operations
- [X] Task 3 – Create a Shopping Cart template for all the messages related to the shopping Cart
- [X] Task 4 – Modify the Base template to Incorporate Bootstrap-Toasts to the Django message system

###### Story Points: 8
