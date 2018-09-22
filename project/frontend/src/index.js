import React from 'react';
import ReactDOM from 'react-dom';
import App from "./components/App";
import { BrowserRouter as Router} from 'react-router-dom';
//import { BrowserRouter as Router } from 'react-router-dom'; 

const app = (
    <Router>
        <App />
    </Router>
)
ReactDOM.render(app, document.getElementById('app'));