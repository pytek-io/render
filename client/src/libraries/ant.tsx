import {
  registerModule,
  registerMethod,
  registerModuleDeferred,
  registerComponent,
} from "../app";
import { useState } from "react";

// const ANT_URI = "https://cdnjs.cloudflare.com/ajax/libs/antd/4.15.6/antd.min.js";
const ANT_URI = "https://cdnjs.cloudflare.com/ajax/libs/antd/4.15.6/antd.js";
const MOMENT_URI =
  "https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.1/moment.min.js";

export function register() {
  registerModuleDeferred("ant", async () => {
    // const module = await loadScript("antd", ANT_URI);
    const [dayjsModule, module] = await Promise.all([
      import("dayjs"),
      import("antd"),
    ]);
    const dayjs = dayjsModule.default;
    window["dayjs"] = dayjs;
    const stringToTime = (s: string) => (s != null ? dayjs(s) : s);
    registerModule("ant", module);
    registerMethod("create_ant_callable", (category_name, type, args) => {
      const method = module[category_name][type];
      return () => method(args || {});
    });

    registerMethod("call_ant_free_function", (category_name, type, args) => {
      return module[category_name][type](args || {});
    });
    const { DatePicker, TimePicker, Transfer } = module;
    function convert_to_moment(arg) {
      if (!arg) {
        return arg;
      }
      const arg_type = arg.constructor.name;
      if (arg_type == "Moment" || arg_type == "m" || arg_type == "k") {
        return arg;
      }
      return dayjs(arg);
    }

    function convert_to_date(value) {
      return value
        ? value.toDate
          ? value.toDate()
          : value
        : value;
    }

    const MyTimePicker = ({ value, defaultValue, ...rest }) => {
      return (
        <TimePicker
          {...rest}
          value={convert_to_moment(value)}
          defaultValue={convert_to_moment(defaultValue)}
        ></TimePicker>
      );
    };
    registerComponent("TimePicker", MyTimePicker, "ant");
    const MyTimeRangePicker = ({ value, defaultValue, ...rest }) => {
      return (
        <TimePicker.RangePicker
          {...rest}
          value={convert_to_moments(value)}
          defaultValue={convert_to_moments(defaultValue)}
        ></TimePicker.RangePicker>
      );
    };
    MyTimePicker.RangePicker = MyTimeRangePicker;
    function MyDatePicker(props) {
      const [_, setValue] = useState();
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

    registerComponent("DatePicker", MyDatePicker, "ant");
    const convert_to_moments = (values) =>
      values ? values.map(convert_to_moment) : values;

    function MyDateRangePicker(props) {
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

    MyDatePicker.RangePicker = MyDateRangePicker;

    const MyTransfer = React.forwardRef((props, ref) => {
      // FIXME: we should not have to remove targetKeys (not a big deal, but seems that this is not supported on Python side)
      let { defaultTargetKeys, onChange, targetKeys, ...rest } = props;
      const [_targetKeys, setTargetKeys] = React.useState(defaultTargetKeys);
      const myOnChange = (nextTargetKeys, direction, moveKeys) => {
        setTargetKeys(nextTargetKeys);
        if (onChange) {
          onChange(nextTargetKeys);
        }
      };
      return (
        <Transfer
          ref={ref}
          targetKeys={_targetKeys}
          onChange={myOnChange}
          {...rest}
        ></Transfer>
      );
    });
    registerComponent("Transfer", MyTransfer, "ant");
    registerMethod("useForm", module.Form.useForm);
    registerMethod("stringToTime", stringToTime);
    registerMethod("stringToDate", stringToTime);
    registerMethod("autoCompleteFilterOption", (inputValue, option) => {
      return (
        option.value.toUpperCase().indexOf(inputValue.toUpperCase()) !== -1
      );
    });
  });
}
