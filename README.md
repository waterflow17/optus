## Optus BOM Container Web Service in Cloud

### App URL
- Application is [here](https://calm-inlet-96529.herokuapp.com)

### Demo video
- Demo video is [here](https://youtu.be/u_mK2QOtaq0)
`
### Design
- This project uses Python with Flask web service module to:
  - read the data from BOM data, url is [here](http://www.bom.gov.au/fwo/IDN60801/IDN60801.95765.json) 
  - parse and filter the temperature greater than 10.
  - return the json object
- It uses Docker container to host the python application mentioned above
- It is deployed and hosted by Heroku, a platform-as-a-service designed for developers, free for small apps.

### How it is organized
- Dockerfile describe how to build the image
- webapps contains python web service application including test files
- README.md is this file

### How to test
- Unit Test
  - The unit test cases are in webapp/tests.py
  - To run it, use `python3 webapp/tests.py`, (you need to have Flask module installed via pip3)
- Funtion Test
  - Use `$ python3 webapp/app.py` to start up local application and test it before pushing to heroku remote server.
- System Test
  - Testing senarios include
    - Mimic error response from BOM
    - Passing different temperature as parameters including invalid string
    - Check and compare with original BOM data.
  - Refer to 'How to use' section below for detailed instruction

### How to deploy and run
- Pre-requirement:
  - Install heroku, git, docker in your development environment. 
  - The detail installation instruction is beyond the scope of this document.
    Please refer to their websites for reference.
- Deploy
  - First create a heroku app
    <br>`$ heroku create`
  - Build the image and push to Container Registry: 
    <br>`$ heroku container:push web`
  - Then release the image to your app: 
    <br>`$ heroku container:release web`
- Run
  - Now open the app in your browser: 
    <br>`heroku open`
  - Note: in the example, the app has already deployed [here](https://calm-inlet-96529.herokuapp.com)

### How to use
- Main query, run the default and return information when temperature is greater than 10, with name,
    apparent_t (temperature), lat, lon.
    Example link is [here](https://calm-inlet-96529.herokuapp.com)
- Filter by temperature, by passing `/?apparent_t=15.5`, this will return information when tempeature is greater
    than 15.5 degree. Example link is [here](https://calm-inlet-96529.herokuapp.com/?apparent_t=15.5)
- Mimic error response from BOM, by passing `/?createErrorResponse=True`, this will return error message. Exampla    link is [here](https://calm-inlet-96529.herokuapp.com/?createErrorResponse=True)

### Notes
1. **Use field 'lon' instead of 'long'**
    - One of the requirement is to return field 'long' from BOM response, but I can't find any corresponding
fields. Instead I found 'lon' which is in the json response. 
2. Use user-agent
    - when using programs (either curl, or python web service request) to query BOM server, I got permission denied.
    - This is due to BOM to prevent web scrape practice
    - To get around this issue, I add user-agent in the web request header
3. **Use 10 instead of 20 as filtering temperature**
    - The requirement is to use 20, but after using it, it will return none records in our current weather.
    - So I use 10 degree instead. 
    - You can filter and pass any degree you want by using  `?apparent_t=20` in the url.
4. The host heroku/bom sometimes may have a glitche which I encoutnered this morning (20/07/2022), when demo app returned error message 'forbidden' (from BOM). I am not sure it is from heroku or BOM. After restarting the app, it was back working. 

