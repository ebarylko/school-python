#ch4ex2.py
#EItan

error_troubleshoot = {
    "Error 102": "check to make sure the moniter's power cord is plugged in",
    "Error 204": "Yourhard drive is full. Use the disk utility to fill up some space.",
    "Error 399": "No boot device was found",
    "Error 1214": "Reboot the device to install updates",
}


def error_message(error):
    #pre: takes an error message
    #post: returns the troubleshoot message
    return error_troubleshoot.get(error) or "Error not found"


