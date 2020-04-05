import React, { useState } from 'react';
import { AutoComplete, Input } from 'antd';


const Search = ({ geojson, selectionCallback }) => {

    const options = geojson.features.map(r => ({ value: r.properties.Place }));
    const [opts, setOpts] = useState(options);
    const [value, setValue] = useState('');

    const handleSearch = (search) => {
        const newOpts = options.filter(
            r => r.value
                .toString()
                .toLowerCase()
                .includes(search.toLowerCase())
        );
        setOpts(newOpts);
    };

    const handleSelect = (selection) => {
        const feature = geojson.features.filter(r => r.properties.Place === selection);
        selectionCallback(feature[0]);
        setValue('');
    };

    const handleChange = (data) => {
        setValue(data);
    };

    return (
        <AutoComplete
            style={{ position: "absolute", top: 10, right: 45, width: 200, zIndex: 1000 }}
            options={opts}
            onSearch={handleSearch}
            onSelect={handleSelect}
            value={value}
            onChange={handleChange}
        >
            <Input.Search size="small" placeholder="search here" enterButton controlled/>
        </AutoComplete>
    )
}

export default Search;