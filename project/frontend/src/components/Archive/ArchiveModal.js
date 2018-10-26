import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

import './ArchiveModal.css';
import Aux from '../../hoc/Aux/Aux';


const ArchiveModal = ({ data }) =>{

    return (<Aux>
          {data.map(el => {
              console.log(el);
            return (
    <div className="container"> 
            
            <div className="heading"></div>
            <header >
                
                <div className="bio" key={el.id}>
                    <img src={el.background} alt="background" className="bg" />
                </div>
                <div className="avatarcontainer">
                    <img src={el.img}  alt="avatar" className="avatar" />
                    <div className="hover">
                        <div className="icon-twitter"></div>                    
                    </div>
                </div>
            </header>
            
            <div className="content">
                <div className="desc">
                    <h3>{el.username}</h3>
                    <p>{el.text}</p>
                </div>            
                <div className="data">   
                    <span className="name">Name : {el.name} </span>
                    
                    <ul>
                        <li>
                            {el.retweet}
                            <span>Reteweet</span>
                        </li>
                        <li>
                            {el.favorite}
                            <span>Favorite</span>
                        </li>                       
                    </ul>                          
                </div>  
            </div>  
            <div className='bottom'>
                posted @ 
                    {el.location} <br/>
                </div>              
            </div>                   
          )}
          )}
    </Aux>)}
ArchiveModal.propTypes = {
  data: PropTypes.array.isRequired
};
export default ArchiveModal;