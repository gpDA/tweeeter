import React, { Component } from "react";
import ReactDOM from "react-dom";
import {Route, Switch} from 'react-router-dom';

import Landing from '../components/Landing/Landing';
import Main from '../components/Main/Main';



class App extends Component {
    render(){
        return(
            <Switch>
                <Route path='/data'  component= {Main} />                
                <Route exact path='' component={Landing} /> 
            </Switch>
            
        )
    }  

}

export default App;
