import React, { Component } from 'react';
import Aux from '../../hoc/Aux/Aux';
import DataProvider from '../Archive/DataProvider';
import ArchiveModal from '../Archive/ArchiveModal';
class Archive extends Component {
    render(){
        return(
            <Aux>
                <DataProvider endpoint="/api/archive/" 
                render={data => <ArchiveModal data={data} />} />
            </Aux>
        )
    }



}

export default Archive;