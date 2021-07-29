import React, { useState } from 'react';
import './App.css';
import Map from './Map'
import Drawer from './Drawer';
import Search from './Search';
import About from './About';
const geojson = require('./places.json');


function App() {
  const [selected, setSelected] = useState(undefined);
  const [zoom, setZoom] = useState([11]);

  const _setSelected = (feature) => {
    window.location.href = `${window.location.href}`
    setSelected(feature);
  }

  const _handleSearch = (feature) => {
    setZoom([17]);
    setSelected(feature);
  }

  return (
    <main>
      <Search geojson={geojson} selectionCallback={_handleSearch} />
      <About />
      <Map
        geojson={geojson}
        selected={selected}
        selectionCallback={_setSelected}
        zoom={zoom}
        setZoom={setZoom}
      />
      <Drawer selected={selected} clearSelected={_setSelected}></Drawer>
    </main>
  )
}

export default App;
