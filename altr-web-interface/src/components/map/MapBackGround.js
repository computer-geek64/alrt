import React, { Component } from 'react'
import './styles/MapBackGround.css'

class MapBackGround extends Component {
  render() {

    return (
      <>
        <div className="containerMap">
            <video autoPlay loop muted className="bgVideo">
            <source src="http://10.192.142.58/static/firefighters.mp4" type="video/mp4"/>
            </video>
        </div>
      </>
    )
  }
}
export default MapBackGround;