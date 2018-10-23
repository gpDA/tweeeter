import React, {Component} from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import './Chart.css';
import Aux from '../../../hoc/Aux/Aux';
import {Doughnut} from 'react-chartjs-2';

class Chart extends Component{
    constructor(props){
        super(props);
        this.state = {
            chartData:{
                labels: ['Boston','Worcester','Springfield','Lowell'],
                datasets:[
                    {
                        label: 'population',
                        data: [
                            617523,
                            213124,
                            123124,
                            21341,

                        ],
                        backgroundColor:[
                            'rgba(255,09,132,0.6)',
                            'rgba(255,123,132,0.6)',
                            'rgba(255,239,132,0.6)',
                            'rgba(255,09,111,0.6)'
                        ]
                    }
                ]
            }
        }
    }
    render(){
        return(
            <div className="chart">
                <Doughnut 
                    data={this.state.chartData}
                    width={100}
                    height={50}
                    options={{
                    
                    }}
                />
            </div>
        )
    }
}


Chart.propTypes = {

};
export default Chart;