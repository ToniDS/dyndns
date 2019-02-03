#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# author: InterNetworX, info →AT→ inwx.de

#############################################################################
###### This is an example of how to use the inwx class #######

from inwx import domrobot, prettyprint, getOTP
from configuration import get_account_data
#import pycurl

def main():
    api_url, username, password, shared_secret = get_account_data(True, config_section="live")
    inwx_conn = domrobot(api_url, True)
    loginRet = inwx_conn.account.login({'user': username, 'pass': password})

    if 'resData' in loginRet:
        loginRet = loginRet['resData']

    if 'tfa' in loginRet and loginRet['tfa'] == 'GOOGLE-AUTH':
        loginRet = inwx_conn.account.unlock({'tan': getOTP(shared_secret)})

    domain = "tonihds.de"
    checkRet = inwx_conn.domain.check({'domain': domain})
    print((prettyprint.domain_check(checkRet)))

if __name__ == '__main__':
    main()
