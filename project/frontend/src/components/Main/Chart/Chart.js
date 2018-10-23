import React, {Component} from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import './Chart.css';
import Aux from '../../../hoc/Aux/Aux';
import {Doughnut, Line} from 'react-chartjs-2';
import ReactHeatmap from 'react-heatmap-grid';

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
            heatmapData:{
                yLabels: ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],
                xLabels: ['1am','2am','3am','4am','5am','6am','7am','8am','9am','10am','11am','noon','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm','10pm','11pm','midnight'],
                data:[
                    [6,2,2,0,3,4,3,7,4,4,6,4,4,4,7,5,6,12,4,11,0,4,2,1],
                    [4,8,0,0,0,0,0,1,4,2,3,4,4,6,5,10,7,13,10,3,2,5,7,5],
                    [1,3,6,7,5,1,1,0,5,0,2,2,4,8,4,5,18,10,17,22,80,60,32,6],
                    [52,57,46,52,18,80,19,79,27,71,18,80,10,89,24,74,7,92,99,34,26,21,18,41],
                    [23,12,21,13,26,17,39,16,24,28,20,25,23,16,30,56,13,21,40,30,11,11,16,3],
                    [10,12,9,12,8,10,9,22,14,8,11,12,0,1,38,25,27,9,11,15,0,16,15,16],
                    [8,4,2,5,4,1,6,6,8,7,10,4,5,7,12,16,12,12,12,13,9,1,4,15]
                ]
            },            

        }
    }
    render(){
        return(
            <div className="charts">
            <div className="dought">
                <Doughnut
                    data={this.state.piechartData}
                    width={1000}
                    height={400}
                    options={{
                        maintainAspectRatio: false,
                        title:{
                            display: true,
                            text: 'helwrnkldsf',
                            fontSize: 15
                        },
                        legend:{
                            display: false,
                        }
                    }}
                />
            </div>
            <div className="line">
                <Line 
                    data={this.state.lineData}
                /> 
            </div>
            <div className="heapmap">
                <ReactHeatmap
                    xLabels={this.state.heatmapData.xLabels}
                    yLabels={this.state.heatmapData.yLabels}
                    yLabelTextAlign={"right"}
                    xLabelsLocation={"bottom"}
                    data={this.state.heatmapData.data}
                />
            </div>
            </div>
        )
    }
}


Chart.propTypes = {

};
export default Chart;