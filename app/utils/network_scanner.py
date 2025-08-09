import nmap

def scan_network(network_range='192.168.1.0/24'):
    """
    Scans the given network range for active hosts.

    Args:
        network_range (str): The network range to scan (e.g., '192.168.1.0/24').

    Returns:
        dict: A dictionary of active hosts with their details,
              or an empty dict if nmap is not found or an error occurs.
    """
    try:
        nm = nmap.PortScanner()
        # -sn: Ping Scan - disables port scanning
        # -T4: Timing template (aggressive)
        nm.scan(hosts=network_range, arguments='-sn -T4')
        
        hosts_list = []
        for host in nm.all_hosts():
            host_info = {
                'host': host,
                'hostname': nm[host].hostname(),
                'state': nm[host].state(),
            }
            if 'mac' in nm[host]['addresses']:
                host_info['mac'] = nm[host]['addresses']['mac']
            hosts_list.append(host_info)
            
        return {'hosts': hosts_list, 'scan_stats': nm.scanstats()}

    except nmap.PortScannerError:
        print("Nmap not found. Please install it on your system.")
        return {}
    except Exception as e:
        print(f"An error occurred during network scan: {e}")
        return {}

if __name__ == '__main__':
    # Example usage:
    # Note: This requires nmap to be installed on the system and may require root privileges.
    print("Starting network scan... (This may take a moment)")
    scan_results = scan_network()
    
    if scan_results and 'hosts' in scan_results:
        print("\nScan complete. Found the following hosts:")
        for device in scan_results['hosts']:
            print(f"- IP: {device['host']}, Hostname: {device['hostname']}, MAC: {device.get('mac', 'N/A')}, State: {device['state']}")
        print(f"\nScan Statistics: {scan_results['scan_stats']}")
    else:
        print("\nCould not perform network scan. Ensure nmap is installed and you have sufficient permissions.")
