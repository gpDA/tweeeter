import React, { Component } from "react";
import PropTypes from "prop-types";
import ArchiveModal from '../Archive/ArchiveModal';
import Aux from '../../hoc/Aux/Aux';

import Spinner from '../Main/Spinner/Spinner';
import './ArchiveModal.css';
import './DataProvider.css';
import MainBox from '../Landing/MainBox/MainBox';
import { Button } from 'react-bootstrap';
class DataProvider extends Component { 
  static propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired
  }
  
  state = {
    data: [],
    loaded: false,
    buttonClicked: '',
    filteredData: [],
    clicked: ''
  }

  onButtonClicked = (e, val) => {

    //console.log(e.target.id);
    this.setState({ 
      buttonClicked: val,
      clicked: e.target.id,
      filteredData: this.state.data.filter(el => {
        return el.type == val
      })
    });
  }

  componentDidMount() {
    fetch(this.props.endpoint)
      .then(response => {
        if (response.status !== 200) {
          return;
        }
        return response.json();
      })
      .then(data => this.setState({ data: data, loaded: true }));
  };

  render() {
    const { data, loaded, filteredData, buttonClicked } = this.state;
   
    let bts = document.getElementsByClassName("btn");
    for (let i=0; i< bts.length; i++){
      if(bts[i].id == this.state.clicked){
        bts[i].classList.add("active");
      }
      else if(bts[i].classList.contains("active")){
        bts[i].classList.remove("active");
      }
  }

    let arr;
    if (buttonClicked === '' || buttonClicked === 'all') {
      arr = data;
    } else {
      arr = filteredData
    }
    return (
      <Aux>
        <MainBox 
            />        
        <div className="bts">
          <Button id="4" onClick={(e) => this.onButtonClicked(e,"all")} >All #NYU tweets</Button>        
          <Button id="1" onClick={(e) => this.onButtonClicked(e,"popular")} >Most Popular #NYU tweet</Button>
          <Button id="2" onClick={(e) => this.onButtonClicked(e,"near")} >Posted nearby Campus #NYU tweet</Button>
          <Button id="3" onClick={(e) => this.onButtonClicked(e,"recent")} >Most Recent #NYU tweet</Button>
        </div>
        { loaded ?
          (<div className="archiveContainer">
            <ArchiveModal data={arr} />      
          </div>)
          : (<Spinner />)
        }
      </Aux>
    );
        
  }
}
export default DataProvider;