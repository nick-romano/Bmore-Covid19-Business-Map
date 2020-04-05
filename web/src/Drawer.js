import React from 'react';
import { Drawer, Descriptions } from 'antd';
import { isMobile } from 'mobile-device-detect';
import isUrl from 'is-url';

const AppDrawer = ({ selected, clearSelected }) => {
    const props = selected ? selected.properties : undefined;

    const createLinks = (menu) => {
        if(isUrl(menu)){
            return (
                <a href={props.Menu} target="_blank" rel="noopener noreferrer">{props.Menu}</a>
            )
        } else {
            return (
                <span>{menu}</span>
            )
        }
    }

    return (
        <Drawer
            visible={selected !== undefined}
            placement={ isMobile ? "bottom" : "left"} 
            mask={false}
            //  
            onClose={() => clearSelected(undefined)}
            height="35vh"
            width="300px"
        >
            {selected &&
                <Descriptions title={props.Place} layout="vertical" column={1}>
                    <Descriptions.Item label="Menu">
                        {createLinks(props.Menu)}
                    </Descriptions.Item>
                    <Descriptions.Item label="Hours">{props.Hours}</Descriptions.Item>
                    <Descriptions.Item label="Direct Order">{createLinks(props.DirectOrder)}</Descriptions.Item>
                    <Descriptions.Item label="Third Party">{createLinks(props.ThirdParty)}</Descriptions.Item>
                    <Descriptions.Item label="Neighborhood">{props.Neighborhood}
                    </Descriptions.Item>
                    <Descriptions.Item label="Address">
                        {props.Address}
                    </Descriptions.Item>
                </Descriptions>
            }
        </Drawer>
    )
}

export default AppDrawer;