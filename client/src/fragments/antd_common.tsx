import dayjs from "dayjs";


export function convert_to_moment(arg) {
    if (!arg) {
        return arg;
    }
    const arg_type = arg.constructor.name;
    if (arg_type == "Moment" || arg_type == "m" || arg_type == "k") {
        return arg;
    }
    return dayjs(arg);
}

export function convert_to_date(value) {
    return value
        ? value.toDate
            ? value.toDate()
            : value
        : value;
}

export function convert_to_moments(values) {
    return values ? values.map(convert_to_moment) : values;
}



