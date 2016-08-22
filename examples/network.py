#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    vpcClient = s.create_client("vpc", "cn-shanghai-2", use_ssl=False)
    #eipClient = s.create_client("eip", "cn-beijing-6", use_ssl=False)
    eipClient = s.create_client("eip", "cn-shanghai-2", use_ssl=False)
    slbClient = s.create_client("slb", "cn-shanghai-2", use_ssl=False)

    allVpcs=vpcClient.describe_vpcs()
    allNics=vpcClient.describe_network_interfaces()
    #allEips=eipClient.describe_addresses(MaxResults=7,NextToken='OA==')
    #allEips=eipClient.describe_addresses(MaxResults=7)
    allEips=eipClient.describe_addresses(**{'Filter.1.Name':'instance-type','Filter.1.Value.1':'Ipfwd'})
    #allEips=eipClient.describe_addresses(Filter.1.Name='instance-type',Filter.1.Value='Slb')
    allListeners=slbClient.describe_listeners(**{'Filter.1.Name':'load-balancer-id','Filter.1.Value.1':'5acac037-531c-414e-bb6f-c639c8948a57'}) 

    #pprint.pprint(allEips)

    #prettyPrinter().pprint(allVpcs)
    prettyPrinter().pprint(allEips)
    prettyPrinter().pprint(allNics)
    for item in allEips['AddressesSet']:
       print item['PublicIp']
       print item['AllocationId']
    #eipClient.associate_address(**{'AllocationId':'1cd0da05-8a3e-4c8e-8230-e6d39b85331e','InstanceType':'Ipfwd','InstanceId':'bede9a1c-d3a7-4b31-82e6-6699790ad1a3', 'NetworkInterfaceId':'fec81567-a4c7-4460-a998-54f407e77c0a'})
    prettyPrinter().pprint(allListeners)
    for item in allListeners['ListenerSet']:
       print item['ListenerName']
       print item['ListenerId']
