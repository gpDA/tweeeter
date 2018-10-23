import React, {Component} from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import './Chart.css';
import Aux from '../../../hoc/Aux/Aux';
import {Doughnut, Line} from 'react-chartjs-2';

class Chart extends Component{
    constructor(props){
        super(props);
        this.state = {
            piechartData:{
                labels: ['#isawNYU','#NYUabudhabi','#NYUcas','#NYUcourant','#NYUdental','#NYUgallatin','#NYUifa','#NYUlaw','#NYUnursing','#NYUpublichealth','#NYUschoolofmed','#NYUshanghai','#NYUsilver','#NYUsps','#NYUsteinhardt','#NYUstern','#NYUtisch','#NYUwagner'],
                datasets:[
                    {
                        label: 'population',
                        data: [
                            0, //isaw
                            //2727, //nyu
                            1, //abudhabi
                            0, //cas
                            0, //courant
                            0, //dental
                            1, //gallatin
                            0, //ifa
                            38, //law
                            0, //nursing
                            0, //publichealth
                            1, //schoolofmed
                            0, //shanghai
                            2, //silver
                            3, //sps
                            10, //steinhardt
                            59, //stern
                            4, //tisch
                            6, //wagner

                        ],
                        backgroundColor:[
                            '#065535', //isaw
                            //'#800080', //nyu
                            '#ffc0cb', //abudhabi
                            '#ffa500', //cas
                            '#ff7f50', //courant
                            '#0e2f44', //dental
                            '#008080', //gallatin
                            '#66cdaa', //ifa
                            '#f6546a', //law
                            '#fef65b', //nursing
                            '#0099cc', //publichealth
                            '#3b5998', //schoolofmed
                            '#00ff7f', //shanghai
                            '#b4eeb4', //silver
                            '#990000', //sps
                            '#ff6666', //steinhardt
                            '#ffc3a0', //stern
                            '#7fffd4', //tish
                            '#133337', //wagner

                        ]
                    }
                ]
            },
            lineData:{
                labels: ['English', 'Dutch', 'Spanish', 'Russian', 'Turkish', 'Portuguese', 'Indonesian','Japanese','Thai','Itlian','Arabic','French','Polish','Ukranian','Vietnamese','Chinese','German','Romanian','Unknown','Hungarian','Czech'],
                datasets: [
                    {
                      label: 'My First dataset',
                      fill: false,
                      lineTension: 0.1,
                      backgroundColor: 'rgba(75,192,192,0.4)',
                      borderColor: 'rgba(75,192,192,1)',
                      borderCapStyle: 'butt',
                      borderDash: [],
                      borderDashOffset: 0.0,
                      borderJoinStyle: 'miter',
                      pointBorderColor: 'rgba(75,192,192,1)',
                      pointBackgroundColor: '#fff',
                      pointBorderWidth: 1,
                      pointHoverRadius: 5,
                      pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                      pointHoverBorderColor: 'rgba(220,220,220,1)',
                      pointHoverBorderWidth: 2,
                      pointRadius: 1,
                      pointHitRadius: 10,
                      data: [1691, 1, 14, 838, 96, 4, 115, 3, 3, 12, 5, 11, 1, 35, 11, 1, 4, 2, 3, 1, 1]
                    }
                  ]                
            },

        }
    }
    render(){
        return(
            <div className="chart">
                <Doughnut 
                    data={this.state.piechartData}
                    options={{
                        title:{
                            display: true,
                            text: 'helwrnkldsf',
                            fontSize: 15
                        },
                        legnd:{
                            display: true,
                            position:'right'
                        }
                    }}
                />
                <Line 
                    data={this.state.lineData}
                />                
            </div>
        )
    }
}


Chart.propTypes = {

};
export default Chart;