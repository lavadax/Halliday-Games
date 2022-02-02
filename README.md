<!-- PROJECT LOGO -->
<br />
<p align="center">
    <a href="https://halliday-games.herokuapp.com">
        <img src="static/images/logo.png" alt="Logo" width="200" height="200">
    </a>
</p>

<p align="center">
    <h2 align="center">Halliday Games</h2>
    <br />
    <p align="center">
        3rd milestone project for CodeInstitute course. This is mostly focused on Python, Flask and MongoDB.
        <br />
        <a href="#"><strong>Explore the docs »</strong></a>
        <br />
        <br />
        <a href="https://halliday-games.herokuapp.com">View Live Project</a>
        ·
        <a href="https://github.com/lavadax/Halliday-Games/issues">Report Bug</a>
        ·
        <a href="https://github.com/lavadax/Halliday-Games/issues">Request Feature</a>
    </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
    <summary><strong>Table of Contents</strong></summary>
    <ol>
        <li>
            <a href="#about-the-project">About The Project</a>
            <ul>
                <li><a href="#built-with">Built With</a></li>
            </ul>
        </li>
        <li>
            <a href="#deployment">Deployment</a>
            <ul>
                <li><a href="#github-pages">Github Pages</a></li>
                <li><a href="#forking-the-github-repository">Forking the GitHub Repository</a></li>
                <li><a href="#making-a-local-clone">Making a Local Clone</a></li>
            </ul>
        </li>
        <li>
            <a href="#usage">Usage</a>
            <ul>
                <li><a href="#wireframes">Wireframes</a></li>
                <li><a href="#user-stories">User Stories</a></li>
            </ul>
        </li>
        <li>
            <a href="#roadmap">Roadmap</a>
            <ul>
                <li><a href="#future-plans">Future Plans</a></li>
                <li><a href="#open-issues">Open Issues</a></li>
                <li><a href="#past-issues">Past issues</a></li>
                <li><a href="#site-changes">Site Changes</a></li>
            </ul>
        </li>
        <li>
            <a href="#testing">Testing</a>
            <ul>
                <li><a href="#validation">Validation</a></li>
                <li><a href="#testing-user-stories">Testing User Stories</a></li>
                <li><a href="#functional-testing">Functional Testing</a></li>
                <li><a href="#accessibility-testing">Accessibility Testing</a></li>
            </ul>
        </li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#acknowledgements">Acknowledgements</a></li>
    </ol>
</details>



<!-- ABOUT THE PROJECT-->
## About The Project  

Below you can see a few screenshots of the finished project.  
  
<!-- TODO Add screenshots of the live site -->

### Built With

<!-- TODO Add/remove software/pages used -->
* [Gitpod](https://www.gitpod.io/) / [Gitpod Chrome extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki) - Used to develop the site and push the project to Github.
* [GitHub](https://github.com) - Used for version control.
* [Whimsical](https://whimsical.com/) - Used to set up the wireframes at the start of the dev cycle.  
* [favicon.io](https://favicon.io/favicon-converter/) - Used to generate the favicon files.  
* [heroku](https://heroku.com) - Used to host the project.  
* [MongoDB](https://www.mongodb.com) - Used to store server data which is used to populate site pages


<!-- DEPLOYMENT -->
## Deployment
<!-- TODO Add instructions on heroku deployment -->
### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. On the left hand side, click the "Pages" section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. Click "Save".
6. The page will automatically refresh.
7. Locate the now published site link in the Green box on the top part of the page.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
2. At the top right of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.



<!-- USAGE EXAMPLES -->
## Usage

### Wireframes

All wireframes are in a single file and can be found [here](https://github.com/lavadax/Halliday-Games/blob/master/documentation/wireframes/wireframes.png).

### User Stories

#### First Time Visitors

* As a new user, I want to easily understand the purpose of the site.  
* As a new user, I want to be able to easily navigate the site and access the content it provides.  
* As a new user, I want to easily find where to sign up an account.

#### Returning Visitors

* As a returning user, I want to easily log into my account.  
* As a returning user, I want to be able to easily navigate the site and submit new reviews.


<!-- ROADMAP -->
## Roadmap

0.1.0: Flask Setup: Finish setting up the start of the Flask app.
0.2.0: MongoDB Setup: Finish setting up the MongoDB collection and link it to the Flask app.
0.3.0: First Base: Finish setting up the base template, using Jinja.
0.4.0: Static Deployment: Flesh out the base template and include static files.
0.5.0: Navi: Set up functioning nav bar, start working on other pages.
0.6.0: Users: Set up user login and logout functionality.
1.0.0: Reviews: Add CRUD functionality to reviews.

### Future Plans

<!-- TODO Add plans -->
* Add Genre tags to all reviews and use these to do an aggregate search for top 3 reviewed genres in account information.

### Open Issues

See the [open issues](https://github.com/lavadax/Halliday-Games/issues) for a list of proposed features (and known issues).

### Past Issues

See the [closed issues](https://github.com/lavadax/Halliday-Games/issues?q=is%3Aissue+is%3Aclosed) for a list of the past issues.

Notable past issues:  
<!-- TODO Add major bugs encountered during dev process -->

* HTTP 405 on registration POST: I was getting HTTP 405 errors when attempting to sign up, as my registration form was set up to log in the user after successful registration, however I kept receiving the 405 due to not setting up a POST method on the login function.
  
* Unable to load profile: The href for the account button in the nav bar used to be "{{ url_for('get_account', username=session['user']) }}", while I used "user" instead of "username" in other pages, causing issues loading the page.

* AttributeError when changing password: While coding in the edit password function, I accidentally replaced a hyphen from my form input with an underscore.  
Due to this mistake, no value was being passed into the check_password_hash method and it kept returning an attribute error.  
Unfortunately I was overthinking the complexity of the issue as I had missed the mistake, and this didn't get fixed for about 30 mins until I caught the typo.

* Body too long: As the html main-content element is calculated to be the entire viewport height, excluding the header and footer height, the calculation didn't work as planned after introducing flash messages.  
The issue was fixed by overriding the margins applied to the h3 flash messages by Materialize css.  

* Logo not found in review or account: the logo, applied in base.html, would not load when opening a review page, or account details page.  
As these pages were the only ones that were an extra step removed from the root, the issue was clearly in the relative path used to load the image file.  
After some googling, the answer was found on (kezunlin.me)[https://kezunlin.me/post/1e37a6/] and the src attribute was adjusted to fix the issue.


### Site Changes

* Wireframes erronously didn't include an input field to add a review score in the "create review" page. This is added on the actual site.

* Initial plan was to add genre tags to all the reviews, and to add an aggregate search to show on the account page. however due to time limitations this idea was dropped and is now added in the future plans section as a potential addition post-submission.

<!-- TESTING -->
## Testing

### Validation
<!-- TODO Add code validation -->


### Testing User Stories
<!-- TODO Add user stories testing -->
#### First Time Visitor goals  
  

#### Returning Visitor Goals


### Functional Testing
<!-- TODO Add functional testing -->

### Accessibility Testing
<!-- TODO Add accessibility testing -->


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/lavadax/Halliday-Games/blob/master/LICENSE.txt) for more information.



<!-- CONTACT -->
## Contact

Lavadax - [Twitter](https://twitter.com/LavadaxTwitch) - [facebook](https://www.facebook.com/kevin.schepers.5)

Project Link: [Halliday Games](https://halliday-games.herokuapp.com)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
<!-- TODO Add acknowledgements -->
* [github.com/othneildrew](https://github.com/othneildrew/Best-README-Template): for providing the readme template.
* [github.com/Code-Institute-Solutions](https://github.com/Code-Institute-Solutions/SampleREADME): for filling in gaps in the readme template.
* [regex101.com](https://regex101.com/library/Yvqkci): for providing the base of the regex used for password pattern.
* [David Strencsev on stackoverflow](https://stackoverflow.com/questions/9343082/html5-input-pattern-search-for-quote): for showcasing how to search for quotes in regex by using hex notation.  
* [kezunlin.me](https://kezunlin.me/post/1e37a6/): for showcasing how to use jinja with static image links.
* [Code Institute python miniproject](https://github.com/Code-Institute-Solutions/TaskManagerAuth): For the basics on the user authentication functionality, as well as giving a framework and guide on how to get started.
* [diegueus9 on Stackoverflow](https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python): for showcasing how to get datetime in the correct format in python.
* [flask.palletsprojects.com](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/): for giving instructions on how to throw and handle http errors in flask.