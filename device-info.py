import psutil
import platform
from datetime import datetime


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        
        
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")




# Boot Time
print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")



# let's print CPU information
print("="*40, "CPU Info", "="*40)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")




# Memory Information
print("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")



# Disk Information
print("="*40, "Disk Information", "="*40)
print("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")



# Network information
print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")



#
#
#======================================== System Information ========================================
#System: Darwin
#Node Name: 192.168.1.18
#Release: 24.5.0
#Version: Darwin Kernel Version 24.5.0: Tue Apr 22 19:54:25 PDT 2025; root:xnu-11417.121.6~2/RELEASE_ARM64_T6020
#Machine: arm64
#Processor: arm
#======================================== Boot Time ========================================
#Boot Time: 2025/5/25 19:28:24
#======================================== CPU Info ========================================
#Physical cores: 10
#Total cores: 10
#Max Frequency: 3504.00Mhz
#Min Frequency: 702.00Mhz
#Current Frequency: 3504.00Mhz
#CPU Usage Per Core:
#Core 0: 13.9%
#Core 1: 8.9%
#Core 2: 7.0%
#Core 3: 5.0%
#Core 4: 0.0%
#Core 5: 0.0%
#Core 6: 0.0%
#Core 7: 2.0%
#Core 8: 0.0%
#Core 9: 0.0%
#Total CPU Usage: 4.0%
#======================================== Memory Information ========================================
#Total: 16.00GB
#Available: 3.14GB
#Used: 5.62GB
#Percentage: 80.4%
#==================== SWAP ====================
#Total: 11.00GB
#Free: 914.69MB
#Used: 10.11GB
#Percentage: 91.9%
#======================================== Disk Information ========================================
#Partitions and Usage:
#=== Device: /dev/disk3s1s1 ===
#  Mountpoint: /
#  File system type: apfs
#  Total Size: 460.43GB
#  Used: 10.48GB
#  Free: 99.96GB
#  Percentage: 9.5%
#=== Device: /dev/disk3s6 ===
#  Mountpoint: /System/Volumes/VM
#  File system type: apfs
#  Total Size: 460.43GB
#  Used: 11.00GB
#  Free: 99.96GB
#  Percentage: 9.9%
#=== Device: /dev/disk3s2 ===
#  Mountpoint: /System/Volumes/Preboot
#  File system type: apfs
#  Total Size: 460.43GB
#  Used: 6.59GB
#  Free: 99.96GB
#  Percentage: 6.2%
#=== Device: /dev/disk3s4 ===
#  Mountpoint: /System/Volumes/Update
#  File system type: apfs
#  Total Size: 460.43GB
#  Used: 3.37MB
#  Free: 99.96GB
#  Percentage: 0.0%
#=== Device: /dev/disk1s2 ===
#  Mountpoint: /System/Volumes/xarts
#  File system type: apfs
#  Total Size: 500.00MB
#  Used: 6.02MB
#  Free: 481.49MB
#  Percentage: 1.2%
#=== Device: /dev/disk1s1 ===
#  Mountpoint: /System/Volumes/iSCPreboot
#  File system type: apfs
#  Total Size: 500.00MB
#  Used: 5.39MB
#  Free: 481.49MB
#  Percentage: 1.1%
#=== Device: /dev/disk1s3 ===
#  Mountpoint: /System/Volumes/Hardware
#  File system type: apfs
#  Total Size: 500.00MB
#  Used: 2.35MB
#  Free: 481.49MB
#  Percentage: 0.5%
#=== Device: /dev/disk3s5 ===
#  Mountpoint: /System/Volumes/Data
#  File system type: apfs
#  Total Size: 460.43GB
#  Used: 331.27GB
#  Free: 99.96GB
#  Percentage: 76.8%
#=== Device: /dev/disk5s1 ===
#  Mountpoint: /Library/Developer/CoreSimulator/Volumes/iOS_21A328
#  File system type: apfs
#  Total Size: 8.31GB
#  Used: 7.52GB
#  Free: 784.88MB
#  Percentage: 90.8%
#Total read: 1.31TB
#Total write: 1.08TB
#======================================== Network Information ========================================
#=== Interface: lo0 ===
#  IP Address: 127.0.0.1
#  Netmask: 255.0.0.0
#  Broadcast IP: None
#=== Interface: lo0 ===
#=== Interface: lo0 ===
#=== Interface: en0 ===
#  IP Address: 192.168.1.18
#  Netmask: 255.255.255.0
#  Broadcast IP: 192.168.1.255
#=== Interface: en0 ===
#=== Interface: en0 ===
#=== Interface: en0 ===
#=== Interface: en0 ===
#=== Interface: bridge100 ===
#  IP Address: 192.168.64.1
#  Netmask: 255.255.255.0
#  Broadcast IP: 192.168.64.255
#=== Interface: bridge100 ===
#=== Interface: bridge100 ===
#=== Interface: bridge100 ===
#=== Interface: anpi2 ===
#=== Interface: anpi0 ===
#=== Interface: anpi1 ===
#=== Interface: en4 ===
#=== Interface: en5 ===
#=== Interface: en6 ===
#=== Interface: en1 ===
#=== Interface: en2 ===
#=== Interface: en3 ===
#=== Interface: bridge0 ===
#=== Interface: ap1 ===
#=== Interface: awdl0 ===
#=== Interface: awdl0 ===
#=== Interface: llw0 ===
#=== Interface: llw0 ===
#=== Interface: vmenet0 ===
#=== Interface: vmenet1 ===
#=== Interface: vmenet2 ===
#=== Interface: vmenet3 ===
#=== Interface: vmenet4 ===
#=== Interface: vmenet5 ===
#=== Interface: bridge101 ===
#=== Interface: vmenet6 ===
#=== Interface: vmenet7 ===
#=== Interface: utun0 ===
#=== Interface: utun1 ===
#=== Interface: utun2 ===
#=== Interface: utun3 ===
#=== Interface: utun4 ===
#=== Interface: utun5 ===
#=== Interface: utun6 ===
#=== Interface: utun7 ===
#=== Interface: utun8 ===
#=== Interface: utun9 ===
#=== Interface: utun10 ===
#=== Interface: utun11 ===
#Total Bytes Sent: 17.71GB
#Total Bytes Received: 30.32GB
