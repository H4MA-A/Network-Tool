from ArgumentParser import ArgumentParser
from Network import Network
from yaspin import yaspin
from termcolor import colored
import time
import pyfiglet
import sys


class Main:
    def launch(self):
        # initialize arguments
        arguments = ArgumentParser()
        arguments.parser()
        network = Network()
        # network scanner moduale
        if arguments.args.scanner:
            if arguments.checkNS:
                # @yaspin(text="scanning network now...")
                ip = arguments.args.target
                interface = arguments.args.interface
                with yaspin(text="scanning network...", color="red") as spinner:
                    list_results = network.scan(ip, interface)
                    spinner.write("✅ Scan complete")
                network.nsResult(list_results)
            else:
                print("noooooo")
        elif arguments.args.arpspoof:
            if arguments.checkAS:
                target = arguments.args.target
                spoofed_ip = arguments.args.spoofed
                interface = arguments.args.interface
                i = 0
                try:
                    mac_dest1 = network.scan(target, interface)[0]["mac"]
                    mac_dest2 = network.scan(spoofed_ip, interface)[0]["mac"]
                    while True:
                        with yaspin(text="spoofing...", color="red") as spinner:
                            network.arpSpoof(target, spoofed_ip, mac_dest1, interface)
                            network.arpSpoof(spoofed_ip, target, mac_dest2, interface)
                            time.sleep(2)
                except IndexError:
                    with yaspin(text="restoring...", color="red") as spinner:
                        spinner.write("Couldn't reach ip")
                except KeyboardInterrupt:
                    try:
                        with yaspin(text="restoring...", color="red") as spinner:
                            network.restore(target, spoofed_ip, interface)
                            network.restore(spoofed_ip, target, interface)
                            spinner.write("✅ Every thing is restored")
                    except IndexError:
                        print("[-] Couldn't restore!!")
            else:
                print("noooooo")
        else:
            # TO DO other moduals
            exit(0)

    def header(self):
        print(colored(pyfiglet.figlet_format("SECURINETS"), 'red'))
        if len(sys.argv) == 1:
            print(colored("\n [+]Welcome to network security workshop \n [!]This tool is for educational purpuses "
                          "only! \n [+]Please enter -h for more information", 'blue'))


m = Main()
m.header()
m.launch()
