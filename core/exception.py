def unsupported_exception():
    return "\033[91mError: PySil library does not support your operating system.\033[0m"


def unsupported_func():
    return "\033[91mError: Currently function your trying to use is unavailable for your operating system.\033[0m"


def battery_plugged_error():
    return "\033[91mError: Cannot detect remaining battery time because your pc is plugged in.\033[0m"


def no_battery_left_error():
    return "\033[91mError: Cannot detect remaining batter, because its about to run out.\033[0m"


def feature_not_implemented_yet():
    return "\033[91mError: Feature not implemented yet - should be available in next version.\033[0m"
