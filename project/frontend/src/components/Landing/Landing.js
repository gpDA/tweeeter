import React, { Component } from 'react';
import Aux from '../../hoc/Aux/Aux';
//import LandingMain from './LandingMain';
import MainBox from '../Landing/MainBox/MainBox';
class Landing extends Component {
    toMain = () => {
        this.props.history.replace('/data/');
    }
    
    render(){
        return (
            <Aux>

                <MainBox main={this.toMain} />               
                
            </Aux>
        )
    }
}

export default Landing;