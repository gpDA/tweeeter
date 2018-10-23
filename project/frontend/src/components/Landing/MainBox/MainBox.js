import React, { Component } from 'react'
//import styles from './MainBox.css';
import './MainBox.css';
import Aux from '../../../hoc/Aux/Aux';
//import nyuLogo from '../../../assets/school.png';
//import twitterLogo from '../../../assets/twitter.png';
import twitterLogo from '../../../assets/purple_bird.png';
import { withRouter } from 'react-router-dom'
import { Image } from 'react-bootstrap';

const MainBox = ({history}) => (
    //render(){
        //render(){
        //return (
            <Aux>
                <div className="boxM">
                    <div className="left">
                        <div className="left1"></div>
                        <div onClick={() => history.push('/data')}  className='lgbt-l'><i className="fa fa-pie-chart"></i><i className="fa fa-line-chart"></i><i className="fa fa-bar-chart"></i></div>                                            
                        <div className="left2"></div>
                    </div>
                    <Image onClick={() => history.push('/')} src={twitterLogo} className="logo" alt='twitterlogo'/>   
                    <div className="right">
                        <div className="right1"></div>
                        <div onClick={() => history.push('/archive')}  className='lgbt-r'><i className="fa fa-archive"></i><i className="fa fa-cloud-upload"></i><i className="fa fa-book"></i></div>
                        <div className="right2"></div>
                    </div>                    
                </div>
            </Aux>
        //)
    //}
)

export default withRouter(MainBox);