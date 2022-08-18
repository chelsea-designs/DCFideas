# Application Testing Details

[Main README.md file](README.md)

[View live version of website via Heroku](https://dcfideas.herokuapp.com/)

---

## Table of Contents 
* [Test User Stories](#test-user-stories)
* [Testing and Validation](#testing-and-validation) 
* [Bugs and Fixes](#bugs-and-fixes)
* [Further testing](#further-testing)

---

## **Test User Stories**
* **User Story 001 (User/Teacher):** as a new user/teacher I want to join DCF Ideas to store details about my ideas so that I can share them with my fellow colleagues.
	*   **Use Case 001-001 (C in User CRUD):** as a new user/teacher I want to register an account with the DCF Ideas.[Success](dcfideas/static/img/testing/user-stories/user001-001.png)
	*   **Use Case 001-002:** as a user/teacher I want to Log In to DCF Ideas [Success](dcfideas/static/img/testing/user-stories/user001-002.png)

*  **User Story 002 (User/Teacher):** as a user/Teacher I want the ability to manage my user profile so that I can have the best possible user/Teacher experience.
	*   **Use Case 002-001 (U in User CRUD):** as a user/teacher I want to reset my password. [Success 1](dcfideas/static/img/testing/user-stories/user002-001-1.png) [Success 2](dcfideas/static/img/testing/user-stories/user002-001-2.png)
	*   **Use Case 002-002 (D in User CRUD):** as a user/teacher I want to delete my account. [Success 1](dcfideas/static/img/testing/user-stories/user002-002-1.png) [Success 2](dcfideas/static/img/testing/user-stories/user002-002-2.png)

*  **User Story 003 (User/Teacher):** as a user/teacher I want to manage my stack/library of ideas in the DCF Ideas so that I can share my ideas with like-minded Teachers, and keep track of my growing list of ideas.
	*   **Use Case 003-001 (C in idea CRUD):** as a user/teacher I want to create a new idea from My Profile. [Success](dcfideas/static/img/testing/user-stories/user003-001.png)
	*   **Use Case 003-002 (C in idea CRUD):** as a user/teacher I want to create a new idea from shared ideas page. [Success](dcfideas/static/img/testing/user-stories/user003-002.png)
	*   **Use Case 003-003 (R in idea CRUD):** as a user/teacher I want to view one of my ideas in my profile. [Success](dcfideas/static/img/testing/user-stories/user003-003.png)
	*   **Use Case 003-004 (U in idea CRUD):** as a user/teacher I want to update/edit an existing idea in my profile. [Success](dcfideas/static/img/testing/user-stories/user003-004.png)
	*   **Use Case 003-005 (D in idea CRUD):** as a user/teacher I want to delete an existing idea in my profile. [Success](dcfideas/static/img/testing/user-stories/user003-005.png)
    *   **Use Case 003-006 (R in idea CRUD):** as a user/teacher I want to view one of my ideas in shared ideas page. [Success](dcfideas/static/img/testing/user-stories/user003-006.png)
	*   **Use Case 003-007 (U in idea CRUD):** as a user/teacher I want to update/edit an existing idea in shared ideas page. [Success](dcfideas/static/img/testing/user-stories/user003-007.png)
	*   **Use Case 003-008 (D in idea CRUD):** as a user/teacher I want to delete an existing idea in shared ideas page. [Success](dcfideas/static/img/testing/user-stories/user003-008.png)

*  **User Story 004 (User/Teacher):** as a user/teacher I want to filter and search for ideas so that I can find new lesson ideas. 
	*   **Use Case 004-001 (R in idea CRUD):** as a user/teacher I want to search for a specific idea in the shared ideas page. [Success](dcfideas/static/img/testing/user-stories/user004-001.png)
    *   **Use Case 004-002 (R in idea CRUD):** as a user/teacher I want to filter ideas by cam_cynnydd in the shared ideas page. [Success](dcfideas/static/img/testing/user-stories/user004-002.png)
    *   **Use Case 004-003 (R in idea CRUD):** as a user/teacher I want to filter ideas by subject in the shared ideas page. [Success](dcfideas/static/img/testing/user-stories/user004-003.png)
    *   **Use Case 004-004 (R in idea CRUD):** as a user/teacher I want to filter ideas by strand in the shared ideas page. [Success](dcfideas/static/img/testing/user-stories/user004-004.png)
    *   **Use Case 004-005 (R in idea CRUD):** as a user/teacher I want to view most recent posted ideas. [Success](dcfideas/static/img/testing/user-stories/user001-001.png)

*  **User Story 005 (User 'admin'):** as an admin I want to manage the posted ideas so that I can provide the best possible DCF Ideas experience for the users/Teachers.
	*   **Use Case 005-001 (C in idea CRUD):** as an admin I want to create some sample ideas to the shared ideas page so that I can start off the DCF Ideas with some ideas and also use for testing purposes. [Success](dcfideas/static/img/testing/user-stories/user005-001.png)
	*   **Use Case 005-002 (R in idea CRUD):** as an admin I want to view the posted ideas. [Success](dcfideas/static/img/testing/user-stories/user005-001.png)
	*   **Use Case 005-003 (U in idea CRUD):** as an admin I want to edit the posted ideas. [Success](dcfideas/static/img/testing/user-stories/user005-001.png)
	*   **Use Case 005-004 (D in idea CRUD):** as an admin I want to delete the posted ideas. [Success](dcfideas/static/img/testing/user-stories/user005-001.png)
	*   **Use Case 005-005 (C in USER ADMIN CRUD):** as an admin I want to be able to create a new user account. (On Mongo)
    *   **Use Case 005-006 (R in USER ADMIN CRUD):** as an admin I want to be able to view a list of all users. (On Mongo)
    *   **Use Case 005-007 (U in USER ADMIN CRUD):** as an admin I want to be able to update user's usernames. (On Mongo)
    *   **Use Case 005-008 (D in USER ADMIN CRUD):** as an admin I want to be able to delete a user's account. (On Mongo)


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

## **Bugs and Fixes**

### Bugs and Fixes
1. Bug: The mobile menu was appearing off screen, requiring user to scroll horizontally to find it.
   -  Fix: To fix this I used css to show borders for elements to inspect which might be causing unwanted scrolling. I saw this method [here](https://blog.wernull.com/2013/04/debug-ghost-css-elements-causing-unwanted-scrolling/). This showed me that an email address in the footer was overflowing off the screen to the right, I moved the email and phone as icons in the footer and this [fixed the issue](dcfideas/static/img/testing/mobile-menu-off-screen.png).
2. Bug: [The strand boxes were different heights and the 'View' buttons were not in line with each other.](dcfideas/static/img/testing/strand-boxes.png)
   -  Fix: [To fix this I added a min-height to all the boxes](dcfideas/static/img/testing/strand-box-fix-1.png), and then [changed the position of the 'View' buttons to absolute and bottom:0, then added margins and width to center it nicely.](dcfideas/static/img/testing/strand-box-fix-2.png)
3. Bug: [The footer was not right at the bottom of the page, it was leaving a gap](dcfideas/static/img/testing/footer-gap.png)
   -  Fix: [To fix this I used flexboxes](dcfideas/static/img/testing/footer-fix.png) following [this tutorial](https://css-tricks.com/couple-takes-sticky-footer/)
4. Bug: [You would see an IntegrityError](dcfideas/static/img/integrity-error.png) if you submitted the add idea form without selecting an option from the required drop downs. It should instead not submit the form and trigger the [validation as shown in other fields](dcfideas/static/img/validator.png).
   -  Fix: To fix this I changed the disabled option value from 0 to empty.


### Outstanding Bugs
- 1. Bug: Dropdown for strand should open down but opens up and improve styling of this.

---