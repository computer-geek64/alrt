import React, { Component } from 'react';
import MapBackGround from './MapBackGround';
import SimpleMap from './SimpleMap';

class Map extends Component {
  render() {

    return (
      <>
        <MapBackGround />
        <div>
          <SimpleMap />
        </div>
      </>
    )
  }
}
export default Map;
