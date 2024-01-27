import { DatePicker } from 'antd';
import { React, useState } from 'react';
import { convert_to_moments } from '../antd_common';


function RenderDateRangePicker(props) {
    const [_, setValue] = useState();
    const { onChange, value, showTime } = props;
    const detouredOnChange = (value) => {
        onChange(value);
        setValue(value);
    };
    let changed_entries = [
        ["onChange", detouredOnChange],
        ["value", convert_to_moments(value)],
    ];
    if (showTime && showTime.defaultValue) {
        changed_entries.push([
            "showTime",
            Object.fromEntries(
                Object.entries(showTime).concat([[
                    "defaultValue",
                    convert_to_moments(showTime.defaultValue),
                ]])
            ),
        ]);
    }
    return React.createElement(
        DatePicker.RangePicker,
        Object.fromEntries(Object.entries(props).concat(changed_entries))
    );
}

export default RenderDateRangePicker;
