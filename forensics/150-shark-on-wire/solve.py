#!/usr/bin/env python3
import dpkt
import io
import struct
import sys
from collections import Counter
from ipaddress import ip_address


VERBOSE = 1


def trace(*args, **kwargs):
    if VERBOSE: print(*args, file=sys.stderr, flush=True, **kwargs)


def walk_pcap(f):
    pcap = dpkt.pcap.Reader(f)
    dlt = pcap.datalink()

    for t, data in pcap:
        try:
            if dlt == 0:
                x = struct.unpack('I', data[:4])[0]
                if x == 2:
                    ip = dpkt.ip.IP(data[4:])
                elif x == 30:
                    ip = dpkt.ip6.IP6(data[4:])
                else:
                    continue

            elif dlt == 1:
                eth = dpkt.ethernet.Ethernet(data)
                ip = eth.data
                if isinstance(ip, bytes):
                    ip = dpkt.ip.IP(ip)

            elif dlt == 101:
                ip = dpkt.ip.IP(data)

            else:
                trace('** skipping dlt', dlt)
                continue

            yield (t, ip)

        except GeneratorExit:
            raise
        except:
            # if VERBOSE: trace(sys.exc_info())
            pass


def solve(fn='capture.pcap'):
    dest = ip_address('10.0.0.12')
    flag = list()

    with open(fn, 'rb') as f:
        for t, ip in walk_pcap(f):
            if isinstance(ip.data, (dpkt.udp.UDP,)):
                if ip_address(ip.dst) == dest:
                    flag.append(ip.data.data)

    flag = b''.join(flag)
    return flag


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
