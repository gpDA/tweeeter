import React, { Component } from 'react';
//import styles from './MainBox.css';
import './MainBox.css';
import Aux from '../../../hoc/Aux/Aux';
import nyuLogo from '../../../assets/school.png';
import twitterLogo from '../../../assets/twitter.png';
//import { Button } from 'reactstrap';

class MainBox extends Component {
    render(){
        return (
            <Aux>
                <div className="boxM">
                    <div className="left">
                        <div className="left1"></div>
                        <div className="left2"></div>
                    </div>
                    <div className="mainBOX">   
                        <div className= "Content">
                            <img src={nyuLogo} className="nyu" alt='nyuLogo' />
                            <span>x</span>
                            <img src={twitterLogo} className="tweet" alt='twitterLogo' />
                        </div>
                    </div>   
                    <div className="right">
                        <div className="right1"></div>
                        <div className="right2"></div>
                    </div>                    
                </div>
                <div className="boxModal">
                <p className="p1">All About </p> 
                <p onClick={this.props.main} className="p2"><span className="nyu">New York University</span> at <span className="twt">Twitter</span></p> 
                </div>
            </Aux>
        )
    }
}

export default MainBox;