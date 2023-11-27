# ProShop
An Ecommerce web app based on Django Rest and React.js


## Tools and Technologies
### Backend
- [Django Rest Framework](https://www.django-rest-framework.org/) - The web framework for building APIs with Django
- [Django cors headers](https://pypi.org/project/django-cors-headers/) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses
- [Pillow](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library
- [PostgreSQL](https://www.postgresql.org/) - The database for storing data


### Frontend
- [React.js](https://reactjs.org/) - A JavaScript library for building user interfaces
- [React Bootstrap](https://react-bootstrap.github.io/) - Bootstrap-based frontend framework for React
- [Bootswatch](https://bootswatch.com/) - Free themes for Bootstrap.
- [Font Awesome](https://fontawesome.com/) - The web's icon set and toolkit.
- [React Router](https://reactrouter.com/) - Declarative routing for React.
- [React Router Bootstrap](https://www.npmjs.com/package/react-router-bootstrap) - Integration between React Router and React Bootstrap.
- [Axios](https://axios-http.com/docs) - Promise based HTTP client for the browser and node.js
- [Redux](https://redux.js.org/) - A Predictable State Container for JS Apps


## Development Setup
### Frontend
#### Prerequisites
- Node.js
- npm
#### Steps
##### React
- Create a react app
```bash
$ npx create-react-app frontend
```
- Remove the default unnecessary files
- Go to the frontend dir and start the server
```bash
$ cd frontend
$ npm start
```
##### Bootstrap
- Install react-bootstrap for using bootstrap components in react
```bash
$ npm install react-bootstrap
```
- Choose a theme from [Bootswatch](https://bootswatch.com/), download the css file and put it in the src dir.
- Import the bootstrap css file in the index.js file
##### Font Awesome
- Go to [cdnjs](https://cdnjs.com/) and search for font-awesome
- Copy the link tag and paste it in the index.html file
##### React Router
- Install react-router-dom and react-router-bootstrap
```bash
$ npm install react-router-dom react-router-bootstrap
```
##### Axios
- Install axios
```bash
$ npm install axios
```
- Add a proxy in the package.json file
```json
"name": "frontend",
"proxy": "http://localhost:8000",
```
##### Redux
- Install redux, react-redux, redux-thunk and redux-devtools-extension
```bash
$ npm install redux react-redux redux-thunk redux-devtools-extension
```
- Add the redux devtools extension to the chrome browser

### Backend
#### Prerequisites
- Python
- pip
- virtualenvwrapper
#### Steps
- Create a virtual environment
```bash
$ mkvirtualenv proshop
```
- Install Django and Django Rest Framework
```bash
$ pip install django djangorestframework
```
- Create a django project
```bash
$ django-admin startproject backend
```
- django-cors-headers
    - Install the package
        ```bash
        $ pip install django-cors-headers
        ```
    - Add `corsheaders` to `INSTALLED_APPS` in `settings.py`
    - Add `corsheaders.middleware.CorsMiddleware` to `MIDDLEWARE` in `settings.py`
    - Add allowed hosts
        ```python
            CORS_ALLOWED_ORIGINS = [
                "http://localhost:3000",
            ]
        ```

