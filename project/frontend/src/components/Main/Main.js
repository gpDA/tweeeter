import React, { Component } from 'react';
import Aux from '../../hoc/Aux/Aux';
import DataProvider from '../Main/TweetModal/DataProvider';
import Chart from '../Main/Chart/Chart';
import TweetModal from '../Main/TweetModal/TweetModal';
class Main extends Component {
    render(){
        return(
            <Aux>
                <Chart />
                <DataProvider endpoint="/api/tweet/" 
                render={data => <TweetModal data={data} />} />
            </Aux>
        )
    }



}

export default Main;