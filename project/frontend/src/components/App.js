import React, { Component } from "react";
import ReactDOM from "react-dom";
import {Route, Switch} from 'react-router-dom';
import Landing from '../components/Landing/Landing';
import Main from '../components/Main/Main';



class App extends Component {
    render(){
        return(
            <Switch>
                <Route exact path='/' component={Landing} /> 
                <Route path='/data'  component= {Main} />
                
            </Switch>
            
        )
    }  

}

export default App;
