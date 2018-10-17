import React, { Component } from 'react';
import './SearchBar.css';
import Aux from '../../../hoc/Aux/Aux';
import { Button } from 'react-bootstrap';

class SearchBar extends Component {
    render(){
        return (
            <Aux>
                <Button>Click me!</Button>
            </Aux>
        )
    }
}

export default SearchBar;