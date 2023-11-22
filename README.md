# ProShop
An Ecommerce web app based on Django Rest and React.js


## Tools and Technologies
### Backend
- Django Rest Framework
- PostgreSQL

### Frontend
- [React.js](https://reactjs.org/) - A JavaScript library for building user interfaces
- [React Bootstrap](https://react-bootstrap.github.io/) - Bootstrap-based frontend framework for React
- [Bootswatch](https://bootswatch.com/) - Free themes for Bootstrap.


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
