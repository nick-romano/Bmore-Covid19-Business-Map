import React, { useState } from 'react';
import { getCapitalLetters } from './utils';
import ReactMapboxGl, { Cluster, Marker, ZoomControl } from 'react-mapbox-gl';
const mapBoxCreds = require('./credentials.json');


const Map = ReactMapboxGl(mapBoxCreds);

const styles = {
    clusterMarker: {
        width: 35,
        height: 35,
        borderRadius: '50%',
        backgroundColor: '#51D5A0',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: 'white',
        border: '2px solid #56C498',
        cursor: 'pointer'
    },
    marker: {
        width: 25,
        height: 25,
        borderRadius: '50%',
        backgroundColor: '#1890ff',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        border: '2px solid #096dd9'
    }
};

const PlaceMap = ({ geojson, selected, selectionCallback, zoom, setZoom }) => {

    const [center, setCenter] = useState([-76.612294, 39.287074]);


    const clusterClick = (coordinates, pointCount, getLeaves) => {
        // setCenter(coordinates);
        // setZoom([17]);
    }

    const clusterMarker = (coordinates, pointCount, getLeaves) => (
        <Marker
            key={coordinates.toString()}
            coordinates={coordinates}
            style={styles.clusterMarker}
            onClick={() => clusterClick(coordinates, pointCount, getLeaves)}
        >
            <div>{pointCount}</div>
        </Marker>
    )
    return (
        <Map
            // eslint-disable-next-line
            style="mapbox://styles/mapbox/streets-v9"
            containerStyle={{
                height: '100vh',
                width: '100vw',
                overflowX: "hidden",
                overflowY: "hidden"
            }}
            center={selected && selected.geometry && selected.geometry.coordinates ? selected.geometry.coordinates : center}
            zoom={zoom}
        >
            <ZoomControl />
            <Cluster ClusterMarkerFactory={clusterMarker} zoomOnClick>
                {geojson.features.filter(r => r.geometry != null).map((feature, key) => {
                    return (
                        <Marker
                            key={key}
                            style={styles.marker}
                            coordinates={feature.geometry.coordinates}
                            data-feature={feature}
                            onClick={() => {
                                setCenter(feature.geometry.coordinates);
                                selectionCallback(feature);
                            }}
                        >
                            <div title={feature.properties.Place} style={{cursor: "pointer", color: "#FFF"}}>
                                {getCapitalLetters(feature.properties.Place.toString())}
                            </div>
                        </Marker>
                    )
                })}
            </Cluster>
        </Map>
    );
}

export default PlaceMap;