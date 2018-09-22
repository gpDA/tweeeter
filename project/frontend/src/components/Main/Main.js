import React, { Component } from "react";
//import ReactDOM from "react-dom";
import DataProvider from "../Main/DataProvider";
import Table from "../Main/Table";

class Main extends Component {
    render(){
        return(
            <DataProvider endpoint="api/main/" 
            render={data => <Table data={data} />} />
        )
    }



}

export default Main;