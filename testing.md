<p align="center">
    <a href="https://halliday-games.herokuapp.com">
        <img src="static/images/logo.png" alt="Logo" width="200" height="200">
    </a>
</p>

# Functional Testing

## Route Testing

A big part of the manual testing included testing the routes and ensuring that all the ending points were accessible/directed properly from all the starting points.  
As this was a pretty expansive phase, I've added the route tests in a table to keep things more organized.  
  
![routing](https://github.com/lavadax/Halliday-Games/blob/master/documentation/routing.png)  
  
On top of the tests that are visible in the table, every button and nav element was tested on every page.  
In order to test the last part of regular user behaviour, all forms were also tested with valid and invalid data.  
This includes data that won't pass the requirements of the form validation, but also data that clashes with back-end checks (such as registering a username that's already taken, changing password while both the old and new password are the same, etc.)  
  
## Brute Force Testing  
  
The last part that was tested was the less kosher part, which involved manipulating the URL to go to pages that don't exist, make small typos in review or user IDs that are passed along, attempt to access reviews or change passwords for accounts that aren't used in the current session, etc.  
  
As quite a bit of time was spent beforehand to set up 403 and 404 routes, these were all working as intended and redirected accordingly.  
From the 403 and 404 pages as a starting point, you can also see in the above table that I attempted to access all other pages as intended, and everything worked fine there as well.