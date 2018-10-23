import React, { Component } from 'react';
import Aux from '../../hoc/Aux/Aux';
//import LandingMain from './LandingMain';
import MainBox from '../Landing/MainBox/MainBox';
import Chart from '../Main/Chart/Chart';
class Landing extends Component {     
    
    render(){
        return (
            <Aux>
                <MainBox 
                    />
                <Chart />

                
            </Aux>
        )
    }
}

export default Landing;