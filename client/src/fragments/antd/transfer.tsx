import { Transfer } from 'antd';
import React from 'react';

const RenderTransfer = React.forwardRef((props, ref) => {
    // FIXME: we should not have to remove targetKeys (not a big deal, but seems that this is not supported on Python side)
    let { defaultTargetKeys, onChange, targetKeys, ...rest } = props;
    const [_targetKeys, setTargetKeys] = React.useState(defaultTargetKeys);
    const renderOnChange = (nextTargetKeys, direction, moveKeys) => {
        setTargetKeys(nextTargetKeys);
        if (onChange) {
            onChange(nextTargetKeys);
        }
    };
    return (
        <Transfer
            ref={ref}
            targetKeys={_targetKeys}
            onChange={renderOnChange}
            {...rest}
        ></Transfer>
    );
});

export default RenderTransfer;
