import React, { Component } from 'react';
import './SearchBar.css';
import Aux from '../../../hoc/Aux/Aux';
import { Button } from 'react-bootstrap';

class SearchBar extends Component {
    constructor(props){
        super(props);
        this.state = {
            isToggleOn: false,
            item : ''
        };

        this.handleClick = this.handleClick.bind(this);
    }
    handleClick(e){
        
        var idnum = e.target.id;
        
        var clickedItem = document.getElementById(idnum);
        console.log(clickedItem);
        
        if(clickedItem.classList.contains("active") && this.state.isToggleOn){
            clickedItem.classList.remove("active");
            this.state.isToggleOn;
        }
        this.setState(prevState => ({
            isToggleOn: !prevState.isToggleOn,
            item : idnum
        }));
        e.stopPropagation();
    }

    render(){
        
        var bttn = document.getElementsByClassName("btn");
        for (let i=0; i< bttn.length; i++){
            if(bttn[i].id == this.state.item && this.state.isToggleOn){
                bttn[i].classList.add("active");
                this.state.isToggleOn;
                console.log(this.state.isToggleOn);
            }
            else if(bttn[i].classList.contains("active")){
                bttn[i].classList.remove("active");
            }
        }
        return (
            <Aux>
                <div className="bts" onClick={this.handleClick}>
                <Button id="1">Hi</Button>
                <Button id="2">Hello</Button>
                <Button id="3">bye</Button>
                </div>   
            </Aux>
        )
    }
}

export default SearchBar;