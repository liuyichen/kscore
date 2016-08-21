# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    vpcClient = s.create_client("vpc", "cn-beijing-6", use_ssl=False)
    eipClient = s.create_client("eip", "cn-beijing-6", use_ssl=False)

    allVpcs=vpcClient.describe_vpcs()
    #allEips=eipClient.describe_addresses(MaxResults=7,NextToken='OA==')
    allEips=eipClient.describe_addresses(MaxResults=7)
#print dir(client)
#pprint.pprint(res)
#pprint.pprint(allEips)

#prettyPrinter().pprint(allVpcs)
prettyPrinter().pprint(allEips)

