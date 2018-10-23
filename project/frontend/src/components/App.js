import React, { Component } from "react";
import ReactDOM from "react-dom";
import {Route, Switch} from 'react-router-dom';
import Landing from '../components/Landing/Landing';
import Main from '../components/Main/Main';
import Archive from '../components/Archive/Archive';


class App extends Component {
    render(){
        return(
            <Switch>
                <Route exact path='/' component={Main} /> 
                <Route path='/data'  component= {Landing} />
                <Route path='/archive'  component= {Archive} />
                
            </Switch>
            
        )
    }  

}

export default App;
