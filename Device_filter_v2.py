__author__ = 'ubantu'
#!/usr/bin/env python

"""A simple python script template.
"""
#https://mkaz.github.io/2014/07/26/python-argparse-cookbook/
import os
import sys
import argparse
from shc.topo import *
# Add count if more than 1
# check for duplicate entries
# add skip list
# make search case in-sensetive
def device_filter(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--verbose', action='store_true', help='verbose flag')
    parser.add_argument('-a', '--account', help= "account id of the device")
    parser.add_argument('-s', '--site', help= "device site id")
    parser.add_argument('-l', '--location', help= "location id of the device")
    parser.add_argument('-t', '--type', help= "device type id")
    parser.add_argument('-n', '--num', help= "device num", type=int)
    parser.add_argument('-vid', '--virtual_id', help= "device virtual id", type=int)
    parser.add_argument('-r', '--role', help= "device role id")
    parser.add_argument('-f', '--file', help= "Input file", type=argparse.FileType('r'))
    # parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    # parser.add_argument('-o', '--outfile', help="Output file",
    #                     default=sys.stdout, type=argparse.FileType('w'))
    args = parser.parse_args(arguments)
    total_devices = 0
    filter_dict = {}
    if args.account:
        filter_dict['device_account'] = args.account

    if args.location:
        filter_dict['device_location'] = args.location

    if args.site:
        filter_dict['device_site'] = args.site

    if args.type:
        filter_dict['device_type'] = args.type

    if args.num:
        filter_dict['device_num'] = args.num

    if args.virtual_id:
        filter_dict['device_virtual_id'] = args.virtual_id

    if args.role:
        filter_dict['device_role'] = args.role

    # filter_dict['device_role'] = 'VC'
    interested_devices_list = []

    print('args.file')
    print(args.file)

    if args.file:
        f = args.file
    else:
        # file_name = 'shc_devices.txt'
        # file_name = 'shc_device_exceptions.txt'
        file_name = 'shc_devices_complete.txt'
        # open(file_name) as f
        f = open(file_name)
    # with open(file_name) as f:
    for line in f:
        line = line.strip()
        if line.split(' '):
            line = line.split(' ')[0]
        hostname = line.split('.')[0]

        if hostname:
            total_devices += 1
            naming = DeviceNamingConvention(hostname)
            if naming.is_validate_filter(filter_dict):
                #filter_dict = {'device_location':'WECH', 'device_type':'RS', 'device_role':'PE'}
                #print naming.filter_device(filter_dict)
                if naming.filter_device(filter_dict):
                    interested_devices_list.append(hostname)
                if args.verbose:
                    print naming.get_verbose()

            else:
                print('Not a valid filter')
                break
    if interested_devices_list:
        if interested_devices_list.__len__() > 1:
            print '\nMatching Devices %d out of total %d\n' %(interested_devices_list.__len__(), total_devices)
        else:
            print '\nMatching Device\n'
        for device in interested_devices_list:
            print device
    else:
        print 'No matching device found for user filter: %s' %args
    return interested_devices_list

if __name__ == '__main__':
    device_filter(sys.argv[1:])
    # sys.exit(device_filter(sys.argv[1:]))
    


#
# configured_host_list
# ['stnamc-02-sa01', 'stnamc-03-sa01', 'stnamc-11-sa01', 'stnamc-12-sa01', 'stnamc-21-sa01', 'stnamc-31-sa01', 'stnamc-32-sa01', 'STNBW-01-SA01', 'STNBW-11-SA01', 'STNBW-33-SA01', 'stnhlv-12-sa01', 'stnhlv-13-sa01', 'stnhlv-21-sa01', 'stnhlv-22-sa01', 'stnhoov-01-sa01', 'stnhoov-02-sa01', 'stnhoov-03-sa01', 'stnhoov-04-sa01', 'stnhoov-05-sa01', 'STNHOOV2-11-SA01', 'STNHOOV2-21-SA01', 'STNHOOV2-31-SA01', 'STNHOOV2-41-SA01', 'stnhoov-ps-sa01', 'stnlgo-21-sa01', 'STNLGO-21-SA02', 'stnmed-002-sa01', 'stnmed-004-sa03', 'stnmed-04-sa01', 'stnmed-103-sa01', 'stnmed-103-sa02', 'stnmed-104-sa01', 'stnmed-109-sa03', 'stnmed-120-sa01', 'stnmed-120-sa02', 'stnmed-14-sa01', 'stnmed-202-sa01', 'stnmed-202-sa02', 'stnmed-204-sa01', 'stnmed-304-sa01', 'stnmed-304-sa02', 'stnmed-35-sa01', 'stnmed-35-sa02', 'stnmed-ps5-sa01', 'stnnc-a11-sa01', 'stnnc-a11-sa02', 'stnnc-a21-sa01', 'stnnc-a21-sa02', 'stnnc-a31-sa01', 'stnnc-a31-sa02', 'stnnc-b11-sa01', 'stnnc-b11-sa02', 'stnnc-b21-sa01', 'stnnc-b21-sa02', 'stnnc-b31-sa01', 'stnnc-b41-sa01', 'stnnc-b41-sa02', 'stnnc-c11-sa01', 'stnnc-c11-sa02', 'stnnc-c21-sa01', 'stnnc-c21-sa02', 'stnnc-c41-sa01', 'stnnc-c41-sa02', 'stnnc-d11-sa01', 'stnnc-d11-sa02', 'stnnc-d21-sa01', 'STNNWK-21-SA01', 'stnpgm2-12-sa01', 'stnpgm2-23-sa01', 'STNSBCC-21-SA01', 'STNSBCC-21-SA02', 'STNSBCC-22-SA01', 'STNSBCC-22-SA02', 'STNSBCC-31-SA01', 'STNSBCC-31-SA02', 'STNSBCC-32-SA02', 'stnsri-21-sa01', 'stnvis-11-sa01', 'stnvis-11-sa02', 'stnvis-21-sa01', 'stnvis-21-sa02', 'STNVIS-22-SA01', 'STNVIS-23-SA01']
# unknow_error_list
# ['stnmed-303-sa01']
# host_list_no_l200 = ['stnatl-1820-sa01', 'stnbos-13-sa01-sn', 'stnbos-23-sa01-sn', 'stnbos-33-sa01-sn', 'STNBW-12-SA01', 'stnbw-ps3trlr-sa04', 'stnfor-cp-sa01', 'stnfor-l29-sa01', 'stnfor-l30-sa01', 'STNLAC-11-SA01', 'STNLAC-11-SA02', 'stnlad-03-sa01', 'stnlad-04-sa01', 'stnmall-m384-sa01', 'stnmc-wech-sa01', 'stnmed-004-sa01', 'stnmed-004-sa02', 'stnmed-105-sa01', 'stnmed-105-sa02', 'stnmed-106-sa01', 'stnmed-106-sa02', 'stnmed-107-sa01', 'stnmed-107-sa02', 'stnmed-108-sa01', 'stnmed-108-sa02', 'stnmed-109-sa01', 'stnmed-109-sa02', 'stnmed-111-sa01', 'stnmed-203-sa01', 'stnmed-203-sa02', 'stnmed-205-sa01', 'stnmed-205-sa02', 'stnmed-23-sa01-sn', 'stnmed-303-sa02', 'STNMED-ECH-SA01', 'stnmed-ech-sa01-sn', 'stnmed-ech-sa02', 'stnmed-ops-sa01', 'stnmid-21-sa01', 'stnmid-21-sa02', 'stnnc-bdd-sa01', 'STNNWK-DTELAB182-SA01', 'stnpatc-2445-sa01', 'stnpgm2-22-sa01', 'STNPS4-LL4-SA02', 'STNSBCC-32-SA01', 'stnstc-bj27-sa01', 'stnstc-bj27-sa02', 'stnstc-bj37-sa01', 'stnstc-bj37-sa02']
# for el in host_list_no_l200:
#     print el
#
# uha_host_list
# ['UHACAM01-035-SA01', 'UHAGAT01-103-SA01', 'UHAHAY01-001-SA01', 'UHAJOS02-227-SA01', 'UHAOAK01-004-SA01']
# not_able_to_access = ['STNBOS-23-SA01', 'stnbos-41-sa01-sn', 'STNBW-22-SA01', 'STNHOOV2-02-SA01', 'STNLAC-11-SA01_STNLAC-11-SA02_HA', 'stnmed-202-sa01_stnmed-202-sa02_ha', 'stnmed-EDEXT-sa01', 'stnmed-hc010-sa01', 'stnmed-mritrlr-sa01', 'STNSCC-11Conf-sa01', 'UHAGAT03-008-SA01']
# print 'Some of below devices are not accessiable'
# for el in not_able_to_access:
#     print el
