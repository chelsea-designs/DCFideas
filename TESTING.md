# Application Testing Details

[Main README.md file](README.md)

[View live version of website via Heroku](https://dcfideas.herokuapp.com/)

---

## Table of Contents 
* [Test User Stories](#test-user-stories)
* [Testing and Validation](#testing-and-validation) 
* [Manual testing](#manual-testing)
* [Bugs and Fixes](#bugs-and-fixes)
* [Further testing](#further-testing)

---

#### *New Visitor*
1. As a first time visitor, I want the main purpose of the site to be immediately clear.
2. As a first time visitor, I want the look of the site to be visually appealing.
3. As a first time visitor, I want the layout of the site to be well structured and easy to navigate.
4. As a first time visitor, I want to have an idea of the content that the site offers, before deciding to register.
5. As a frist time visitor, I want to be able to easily find and use the registration page, if I choose to register.
6. As a first time visitor, I want to see ways of communicating with the site's creators, via social media or a contact page.

- The Home Page has been designed to be simplistic, yet fully evidence what the site is about. In addition to this, the purpose of the site is also mentioned in the Footer. The colour palette used, was chosen to keep the site as visually appealing as possible. The home page is essentially split in to two sections, the first being the main title and image for the site with a call to action button, the second being a section that hosts the weekly featured content, controlled by the sites admin. This gives a visitor an idea of what content the site holds. The Footer hosts a contact us section where users can reach out to the sites creator. Non-registered users will also have access to the registration page through a link in the navbar.

    - [Navbar](/documentation/images/testing-images/navbar.png)
    - [Home Page](/documentation/images/testing-images/home-page.png)
    - [Weekly Featured Section](/documentation/images/testing-images/weekly-featured.png)
    - [Footer](/documentation/images/testing-images/footer.png)
    - [Registration Page](/documentation/images/testing-images/registration-page.png)

#### *Registered User*
1. As a registered user, I want to be able to login with a set of registered credentials.
2. As a registered user, I want to be able to logout of my account.
3. As a registered user, I want to be able to change my user credentials.
4. As a registered user, I want to be able to see all ideas posted by other members.
5. As a registered user, I want to be able to create a new idea to be added to the library.
6. As a registered user, I want to be able to edit or delete posts that I have created myself.
7. As a registered user, I want to be able to see a profile page where I can review my own idea posts.
8. As a registered user, I want to be able to quickly serach for relevant ideas.
9. As a registered user, I want to be able to delete my account in full, if I no longer wish to remain a member.

- Once Registered, users will be taken to their profile page. From here, they will have the functionality to log back out via the Navbar or manage their user account details. Users when managing their account will have three options: 1. Update their email address. 2. Update their password. 3. Delete their user account.
- Registered users will alsb be able to see a list of their own submitted ideas on their profile page, as well as have the functionality to update or delete each individual idea that they have created.
- Registered users will have access to a specific ideas page, where all user submitted ideas are listed. If the user has nno ideas already created, they will be able to do so, via the Add New idea button. The Add New idea will take the user to a form based page, where they can input the necessary details of the idea they would like to create. This page features a serch feature that allows user to search for specific ideas by strand. The page also features the update and delete functionality on ideas created by the specific user

    - [Navbar](/documentation/images/testing-images/navbar.png)
    - [Profile](/documentation/images/testing-images/profile-page.png)
    - [Profile Management Section](/documentation/images/testing-images/profile-management.png)
    - [Update Email](/documentation/images/testing-images/update-email.png)
    - [Change Password](/documentation/images/testing-images/change-password.png)
    - [Delete Account](/documentation/images/testing-images/delete-account.png)
    - [User Created ideas](/documentation/images/testing-images/my-ideas.png)
    - [Edit idea](/documentation/images/testing-images/edit-idea-page.png)
    - [ideas Page](/documentation/images/testing-images/ideas-page.png)
    - [Add New idea Button](/documentation/images/testing-images/add-new-idea.png)
    - [Add idea Page](/documentation/images/testing-images/add-idea.png)
    - [Search Function](/documentation/images/testing-images/search-box.png) 

#### *Site Administrator*
1. As a site Administrator, I would want to be able to control the ideas added.
2. As a site Administrator, I would want to be able to view all idea posts added by users, update and delete where necessary, keeping the site up-to date.
3. As a site Administrator, I would want to be able to add new users or delete users who have issues with functionality.

- Users registered as the administrator for the site will have access to all content that a reqular user would, with the addition of access to an admin dashboard.

## Testing and Validation

### [Lighthouse (Google Dev Tools)](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en)
- For the purposes of lighthouse testing, I am happy with scores about 90 for all 4 metrics.
- Reports per page:
   - Home Page - [Desktop Success](dcfideas/static/img/testing/lighthouse-desktop-home.png) and [Mobile Success](dcfideas/static/img/testing/lighthouse-mobile-home.png)
   - About Page - [Desktop Success](dcfideas/static/img/testing/lighthouse-desktop-about.png) and [Mobile Success](dcfideas/static/img/testing/lighthouse-mobile-about.png)
   - Ideas Page - [Desktop Success](dcfideas/static/img/testing/lighthouse-desktop-ideas.png) and [Mobile Success](dcfideas/static/img/testing/lighthouse-mobile-ideas.png)
   - Full Idea Page - [Desktop Success](dcfideas/static/img/testing/lighthouse-desktop-full-idea.png) and [Mobile Success](dcfideas/static/img/testing/lighthouse-mobile-full-idea.png)
   - Login Page - [Desktop Success](dcfideas/static/img/testing/lighthouse-desktop-login.png) and [Mobile Success](dcfideas/static/img/testing/lighthouse-mobile-login.png)
   - Register Page - [Desktop Success](dcfideas/static/img/testing/lighthouse-desktop-register.png) and [Mobile Success](dcfideas/static/img/testing/lighthouse-mobile-register.png)
   - Profile Page - [Desktop Success](dcfideas/static/img/testing/lighthouse-desktop-profile.png) and [Mobile Success](dcfideas/static/img/testing/lighthouse-mobile-profile.png)

### [Am I Responsive](http://ami.responsivedesign.is/)
- To [view images](dcfideas/static/img/testing/am-i-responsive.png) of the website on various devices.

### [Javascript: JSHint](https://jshint.com/)
- Validating the JS code of the project was done by pasting code into JSHint.
- Addressing errors and warnings: JSHint shows [an error](dcfideas/static/img/testing/jshint.png) for unused variables however these are function names used in other files therefore I'm happy to disregard these warnings.

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- Validating the CCS code of the project was done by pasting code in by direct input method.
- Addressing errors and warnings: W3C CSS validator showed one [one error](dcfideas/static/img/testing/w3c-css-before.png), this was because the 0 had no unit, I [changed the 0 to be 0s](dcfideas/static/img/testing/css-unit-fix.png), this [solved the issue](dcfideas/static/img/testing/w3c-css-before.png).

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- Note the W3C Validator for HTML does not understand the Jinja templating syntax, therefore to validate the HTML code for this project I right clicked and used 'View Source Code', copied and pasted this code in by direct input method, this avoided issues with Jinja. 
- Testing and results per page:
   - Home Page - [No errors](dcfideas/static/img/testing/w3-html-home.png)
   - About Page - [No errors](dcfideas/static/img/testing/w3-html-about.png)
   - Ideas Page - [One Error](dcfideas/static/img/testing/w3-html-ideas.png)
   - Full Idea Page - [No errors](dcfideas/static/img/testing/w3-html-full-idea.png)
   - Login Page - [No errors](dcfideas/static/img/testing/w3-html-login.png)
   - Register Page - [No errors](dcfideas/static/img/testing/w3-html-register.png)
   - Error 404 Page - [No errors](dcfideas/static/img/testing/w3-html-404.png)
- One Error: The one error I received on the ideas page is because of the space between the href and class attribute, this is due to the formatter splitting onto two lines as the row was too long.

### [Python: PEP8 Online](http://pep8online.com/)
- Validating the Python code of the project was done by pasting the code from each Python file in turn into PEP8 Online.
- Addressing errors and warnings: PEP8 Online showed [one error](/documentation/images/testing-images/pep8-python-before.png), for every python file, this was because it requires a blank line at the end of every Python file. Once I added a blank line, all python files passed:
   - [models.py Passed](dcfideas/static/img/testing/pep8-python-models.png)
   - [routes.py Passed](dcfideas/static/img/testing/pep8-python-routes.png)
   - [run.py Passed](dcfideas/static/img/testing/pep8-python-run.png)
   - [init.py Passed](dcfideas/static/img/testing/pep8-python-init.png)

### [Accessibility: Wave](https://wave.webaim.org/)
- To validate the HTML code of the project by pasting code in by direct input method. Note the W3C Validator for HTML does not understand the Jinja templating syntax therefore if there are warnings related to this, this can be safely ignored.
- Testing and results per page:
   - Home Page - [Redundant Link Error](dcfideas/static/img/testing/wave-home.png)
   - About Page - [Redundant Link Error and Skipped Heading](dcfideas/static/img/testing/wave-about.png)
   - Ideas Page - [Redundant Link Error and Skipped Heading](dcfideas/static/img/testing/wave-ideas.png)
   - Login Page - [Redundant Link Error and Skipped Heading](dcfideas/static/img/testing/wave-login.png)
   - Register Page - [Redundant Link Error](dcfideas/static/img/testing/wave-register.png)
- The 'Redundant Link Errors' are due to the site logo and home page both linking to the same page and being near to each other. I'm happy to disregard this alert as it is common industry practice to do this.
- The 'Skipped Heading' error appears on some pages but not others, due to the h4 in the shared footer. Some pages do not have h3, while others do, causing the skipped heading alert.

---
## **Manual testing**
Manual testing of all elements and functionality on every page
1. Logo - click on the logo, returns to the “Home” section on all pages.
2. Navbar 
   - if *a new visitor* clicks on the Home link on any page - They are redirected to the Home page.
   - if *a new visitor* clicks on the Login link on any page - They are redirected to the Login page.
   - if *a new visitor* clicks on the Register link on any page - They are redirected to the Registration page. 
   - if *Registered user* clicks on the idea link - They are redirected to the ideas page.
   - if *Registered user* clicks on the Profile link - They are redirected to the Profile page.
   - if *Registered user* clicks on the Log Out link - They are logged out of their account and redirected to the Login page.
   - if *Admin user* clicks on Admin link - They are redirected to the Admin Dashboard page.
3. Footer 
   - if *any user* clicks on the Instagram link - They will be redirected to the generic site for Instagram.
   - if *any user* clicks on the LinkedIn link - They will be redirected to the LinkedIn Page for Andrew Llewellyn.
   - if *any user* clicks on the Twitter link - They will be redirected to the generic site for Twitter.
   - if *any user* clicks on the GitHub link - They will be redirected to the GitHub Profile Page for Andrew Llewellyn.
4. Floating to top button 
   - When the Return To Top button appears on the screen - clicking the button, moves the view back up to the top of the page.
5. Home Page
   - if *any user* clicks on the Registration Button - They are redirected to the Registration page.
   - if *any user* clicks on each Weekly Featured idea card link - They are redirected to the specified external link.
6. Registration & Sign Up Page
   - if *a new visitor* types in a "Username", "Email" and "Password" to the required fields - validation is given if correct and feedback is given if incorrect.
      - if the visitor then clicks on the "Register" button, their details are added to the database They are redirected to the Profile page and feedback is given to the user that they are registered.
   - if *any user* clicks on the "Login Here" link - They are redirected to the Login page.
7. Log in Page
   - if *Registered users* type in their user details in the "Username" and "Password" fields validation is given if correct and feedback is given if incorrect.
      - if the user then clicks on the "Login" button, the user is logged in. They are redirected to the Profile page and feedback is given to the user that they are logged in.
   - if *any user* clicks on the "Sign up here!" link - They are redirected to the Registration page.
8. Profile Page 
   - if *Registered user* clicks on the "Update Email" button - They are faced with a pop-up to enter a new Email address.
   - if *Registered user* clicks on the "Update Password" button - They are faced with a pop-up to enter a new Password.
   - if *Registered user* clicks on the "Delete Account" button - They are faced with a pop-up to delete the account.
      - if the user types in the correct user password and clicks the "Delete" button - the account is deleted from the database and a is given to the user, who is redirected to the Registration page.
      - if the user clicks on "Cancel" - they go back to the Profile page
9. ideas Page
   - if *Registered user* types text in the search field and click on the "Search" button", the relevant matching idea is shown. If there are no matching ideas, the user is alerted to try again or add a new idea. 
   - if the user clicks on the "Reset" button, the search field is reset.
   - if *Registered user* clicks on the "Add New idea" - They are redirected to the Add idea page.
   - if *Registered user* clicks on the idea Link button on the idea card - They are redirected to the specified external link.
   - if *Registered user* created the idea - they can see the Edit & Delete buttons. This functionality is also visible to any admin of the site.
      - if the user clicks on each idea card "Delete" Button - The user is show a modal where they must confirm deletion. If deletion is confirmed the idea is deleted, removed from the database and the user gets a confirmation. If deletion is cancelled, the user is taken back to the ideas page.
      - if the user clicks on each idea card "Edit" Button - They are redirected to the Edit idea page.
10. Add idea Page
   - if *Registered user or Admin User* clicks on "Choose strand" they can select a current strand.
   - if *Registered user or Admin User* types text in to the input fields, validation is given if correct and feedback is given if incorrect.
   - if *Registered user or Admin User* wants to select a date, a date picker opens with the current date and a date can be selected.
   - if *Registered user or Admin User* clicks on the "Add idea" button, a new idea is added to the database and a success message is given to the user.
   - if *Registered user or Admin User* clicks on cancel - go to ideas Page.
   - if *Admin User* clicks on the Weekly Featured idea toggle button, the idea is added to weekly featured section of home page.
11. Edit idea Page
   - a view of the current details of the idea appears.
   - if clicking on "Choose strand" they can select a current strand.
   - if typeing in text in fields, validation is given if correct and feedback is given if incorrect.
   - if the user wants to select a date, a date picker opens with the current date and a date can be selected.
   - if clicking on the "Update idea" button, the idea is updated in the database and a success message is given to the user.
   - if clicking on cancel - the user is taken back to the ideas Page.
   - if *Admin User* clicks on the Weekly Featured idea toggle button, the idea is added to weekly featured section of home page.
12. Add New strand page
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Admin user* click on the "Add strand" button, a new strand is added to the database and a success message is given to the user.
   - if *Admin user* click on cancel, they are redirected back to Admin Dashboard Page.
13. Edit strand page
   - view current details of strand
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect. 
   - if *Admin user* click on the "Update strand" button, the strand is updated in the database and a success message is given to the user.
   - if *Admin user* click on cancel they are redirected back to Admin Dashboard Page.

---

## **Bugs and Fixes**

### Bugs and Fixes
1. Bug: The mobile menu was appearing off screen, requiring user to scroll horizontally to find it.
   -  Fix: To fix this I used css to show borders for elements to inspect which might be causing unwanted scrolling. I saw this method [here](https://blog.wernull.com/2013/04/debug-ghost-css-elements-causing-unwanted-scrolling/). This showed me that an email address in the footer was overflowing off the screen to the right, I moved the email and phone as icons in the footer and this [fixed the issue](dcfideas/static/img/testing/mobile-menu-off-screen.png).
2. Bug: [The strand boxes were different heights and the 'View' buttons were not in line with each other.](dcfideas/static/img/testing/strand-boxes.png)
   -  Fix: [To fix this I added a min-height to all the boxes](dcfideas/static/img/testing/strand-box-fix-1.png), and then [changed the position of the 'View' buttons to absolute and bottom:0, then added margins and width to center it nicely.](dcfideas/static/img/testing/strand-box-fix-2.png)
3. Bug: [The footer was not right at the bottom of the page, it was leaving a gap](dcfideas/static/img/testing/footer-gap.png)
   -  Fix: [To fix this I used flexboxes](dcfideas/static/img/testing/footer-fix.png) following [this tutoria](https://css-tricks.com/couple-takes-sticky-footer/)


### Outstanding Bugs
- Dropdown for strand should open down but opens up.

---

### Deployment
- Ensured deployed page on Heroku loads up correctly.
- Ensured Debug variable in app.py file is set to False.
- Confirmed that there is no difference between the deployed version and the development version.