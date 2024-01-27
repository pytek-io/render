import React from "react";
import { DatePicker } from 'antd';
import { convert_to_moment } from '../antd_common';


function RenderDatePicker(props) {
    const [_, setValue] = React.useState();
    const onChange = (value) => {
        props.onChange(value);
        setValue(value);
    };
    let props_clone = Object.fromEntries(Object.entries(props));
    props_clone.onChange = onChange;
    props_clone.value = convert_to_moment(props.value);
    if (props_clone.showTime != undefined && props_clone.showTime.constructor.name == "Object") {
        props_clone.showTime["defaultValue"] = convert_to_moment(props_clone.showTime["defaultValue"])
    }
    props_clone.disabledDate = props.disabledDate
        ? (value) => {
            return props.disabledDate(convert_to_date(value))
        }
        : props.disabledDate;
    return React.createElement(DatePicker, props_clone);
}

export default DatePicker;
