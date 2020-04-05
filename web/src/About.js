import React from 'react';
import { Button, Modal } from 'antd';

function info() {
    Modal.info({
        title: 'About',
        content: (
            <div>
                <p>This map is sourced from /u/Ueatsoap's Google 
                    <a href="https://docs.google.com/spreadsheets/d/13WirtfPlWtnLJJs_5EAa0A79UJ72iGcvhthlF6KYAus"> spreadsheet</a><br></br>
                    Data is rebuilt every night based on changes in the spreadsheet.<br></br>
                    Locations are derived from Google Maps.
                </p>
            </div>
        ),
        onOk() { },
    });
}

const AboutButton = () => {

    return (
        <Button
            style={{ position: "absolute", top: 40, right: 45, width: 200, zIndex: 1000 }}
            type="primary"
            size="small"
            onClick={info}
        >About This Map</Button>
    )
}

export default AboutButton;