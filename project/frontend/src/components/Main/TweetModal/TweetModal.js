import React, { Component } from 'react';
//import styles from './MainBox.css';
import './TweetModal.css';
import Aux from '../../../hoc/Aux/Aux';
//import { Button } from 'reactstrap';

class TweetModal extends Component {
    render(){
        return (
            <Aux>
                <div className="twitterMODAL">
                    <div className="info"> </div>
                    <div className="content"></div>
                    <div className="footer"></div>
                </div>
            </Aux>
        )
    }
}

export default TweetModal;