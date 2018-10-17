import React, { Component } from 'react';
import Aux from '../../hoc/Aux/Aux';
import DataProvider from '../Main/TweetModal/DataProvider';
import TweetModal from '../Main/TweetModal/TweetModal';
import SearchBar from '../Main/SearchBar/SearchBar';
class Main extends Component {
    render(){
        return(
            <Aux>
                <SearchBar />
                <DataProvider endpoint="/api/tweet/" 
                render={data => <TweetModal data={data} />} />
            </Aux>
        )
    }



}

export default Main;