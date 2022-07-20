## This is project to read from BOM data, filter and display result as json

### Design
- BOM data is from this [URL](http://www.bom.gov.au/fwo/IDN60801/IDN60801.95765.json) 
- It uses Python with Flask web service module to:
  - read the data from bom url (shown above)
  - parse and filter the temperature greater than 10.
  - return the json object
- It uses Docker container to host the python application mentioned above
- It is deployed via Heroku, a platform-as-a-service designed for developers, free for small apps.

### How it is organized
- Dockerfile describe how to build the image
- webapps contains python web service application including test files

### How to deploy and run
- Pre-requirement:
  - Install heroku, git, docker in your development environment. 
- Deploy
  - First create a heroku app
    `$ heroku create`
  - Build the image and push to Container Registry: `$ heroku container:push web`
  - Then release the image to your app: `$ heroku container:release web`
  - Now open the app in your browser: `heroku open`
  - Note: in the example, the app has already deployed [here](https://calm-inlet-96529.herokuapp.com)
