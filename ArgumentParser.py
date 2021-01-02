#!/usr/bin/python3

import argparse
import pyfiglet


class ArgumentParser:
    argumentParser = None
    args = None

    def __init__(self):
        self.args

    def parser(self):
        arg = argparse.ArgumentParser(description="[+]Welcome to network security workshop \n [!]This tool is for "
                                                  "educational purpuses only!")
        # arguments to specify main function
        arg.add_argument("--scan", "-s", action="store_true", default=False, dest="scanner",
                         help="Scan the network [!]you have to specify the network interface and the ip range")
        arg.add_argument("--arpspoof", "-as", action="store_true", default=False, dest="arpspoof",
                         help="Perform an arp spoofing attack")
        arg.add_argument("--dnspoof", "-ds", action="store_true", default=False, dest="dnspoof",
                         help="Perform an dns spoofing attack")
        arg.add_argument("--sniff", "-sn", action="store_true", default=False, dest="sniff", help="Sniff the network")
        arg.add_argument("--deauth", "-d", action="store_true", default=False, dest="deauth",
                         help="Perform a deauth attack")
        arg.add_argument("--fakeap", "-f", action="store_true", default=False, dest="fakeap",
                         help="lunch fake acces points")
        arg.add_argument("--darpspoof", "-das", action="store_true", default=False, dest="daropspoof",
                         help="Detect an arp spoofing")
        arg.add_argument("--dfakeap", "-df", action="store_true", default=False, dest="dfa",
                         help="Detect fake acces points")
        # option to attacks
        arg.add_argument("--interface", "-i", dest="interface", help="specify Network interface name")
        arg.add_argument("--target", "-t", dest="target", help="specify the target ip")
        arg.add_argument("--spoofed", "-sp", dest="spoofed", help="Specify the ip you want tp spoof")
        # to do the args

        opt = arg.parse_args()
        self.argumentParser = arg
        self.args = opt

    # Network Scanner arguments check
    def checkNS(self):
        if not self.args.target and not self.args.interface:
            self.argumentparser.error("[-] Please specify the target IP address (Or range) And Interface name")
        if not self.args.target:
            self.argumentparser.error("[-] Please specify the target IP address (Or range)")
        elif not self.args.interface:
            self.argumentparser.error("[-] Please specify the network interface name")
        else:
            return True

    # ARP spoofer arguments check
    def checkAS(self):
        if not self.args.target and not self.args.interface and not self.args.spoofed:
            self.argumentparser.error(
                "[-] Please specify the target IP address And Interface name and the ip adress you want to spoof")
        elif not self.args.target:
            self.argumentparser.error("[-] Please specify the target IP address")
        elif not self.args.interface:
            self.argumentparser.error("[-] Please specify the network interface name")
        elif not self.args.spoofed:
            self.argumentparser.error("[-] Please specify the adress you want to spoof")
        else:
            return True
