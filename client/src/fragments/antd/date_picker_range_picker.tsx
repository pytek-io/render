import React, { useState } from 'react';
import { DatePicker } from 'antd';
import { convert_to_moments } from '../antd_common';


function RenderDateRangePicker(props) {
    const [_, setValue] = useState();
    let { onChange, value, showTime, defaultValue } = props;
    const detouredOnChange = (value) => {
        onChange(value);
        setValue(value);
    };
    if (showTime) {
        showTime = { ...showTime, defaultValue: convert_to_moments(showTime.defaultValue) }
    }
    return React.createElement(
        DatePicker.RangePicker,
        {
            ...props,
            onChange: detouredOnChange,
            value: convert_to_moments(value),
            defaultValue: convert_to_moments(defaultValue),
            showTime: showTime,
        }
    );
}

export default RenderDateRangePicker;
