import { TimePicker } from 'antd';
import { convert_to_moments } from '../antd_common';

const RenderTimeRangePicker = ({ value, defaultValue, ...rest }) => {
    return (
        <TimePicker.RangePicker
            {...rest}
            value={convert_to_moments(value)}
            defaultValue={convert_to_moments(defaultValue)}
        ></TimePicker.RangePicker>
    );
};


export default RenderTimeRangePicker;
