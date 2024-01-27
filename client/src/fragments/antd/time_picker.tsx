import { TimePicker } from 'antd';
import { convert_to_moment } from '../antd_common';

const RenderTimePicker = ({ value, defaultValue, ...rest }) => {
    return (
      <TimePicker
        {...rest}
        value={convert_to_moment(value)}
        defaultValue={convert_to_moment(defaultValue)}
      ></TimePicker>
    );
  };

export default TimePicker;
