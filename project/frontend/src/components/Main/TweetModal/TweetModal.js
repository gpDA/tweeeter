import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import './TweetModal.css';
import Aux from '../../../hoc/Aux/Aux';
const TweetModal = ({ data }) =>{
    return (<Aux>
          {data.map(el => {
              //console.log(el);
            return (
    <div className="container"> 
            
            <div className="heading"></div>
            <header >
                
                <div className="bio" key={el.id}>
                    <img src={el.background} alt="background" className="bg"></img>
                </div>
                <div className="avatarcontainer">
                    <img src={el.img}  alt="avatar" className="avatar"></img>                    
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
                    <ul>
                        <li>
                            {el.retweet}
                            <span>Reteweet</span>
                        </li>
                        <li>
                            {el.favorite}
                            <span>Favorite</span>
                        </li>
                        <li>
                            {el.name}
                            <span>Name</span>
                        </li>                        
                    </ul>                          
                </div>  
            </div>  
            <div className='bottom'>
                posted @ 
                    {el.location} <br/>
                    {el.year} {el.month}. {el.date} at {el.hour} {el.min}                
                </div>              
            </div>                    
          )}
          )}
    </Aux>)}
TweetModal.propTypes = {
  data: PropTypes.array.isRequired
};
export default TweetModal;