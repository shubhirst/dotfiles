'''
allocates a lot of memory and visualises the changes in virtual memory and rss over time
'''
import os, psutil
process = psutil.Process()
# print(process.memory_info().rss)  # in bytes

if __name__ == '__main__':
    # keep allocating 1 MB memory till the process is killed
    max_mem_to_allocate_mb = 1024
    mem_allocated_mb = 0
    l = []
    full_mem_output = []
    while mem_allocated_mb < max_mem_to_allocate_mb:
        l.append(['a' for _ in range(1024*1024)]) # list of size 1024*1024 ~ 1MB
        mem_allocated_mb += 1
        full_mem_info = process.memory_full_info()
        print(f'Allocated {mem_allocated_mb} MB of memory')
        print(f'Virt memory usage {(full_mem_info.vms)/(1024*1024)} MB, RSS memory usage {(full_mem_info.rss)/(1024*1024)} MB, out of which system swap is {(psutil.swap_memory().used)/(1024*1024)} MB')
        full_mem_output.append(full_mem_info)

    import matplotlib.pyplot as plt

    plt.figure(figsize=(16,12))

    plt.plot([x.rss/(1024*1024) for x in full_mem_output], label='Resident Set Size in MB')
    plt.plot([x.vms/(1024*1024*1024) for x in full_mem_output], label='Virtual Memory Size in GB')
    # plt.plot([x.available for x in virt_mem], label='Available Memory')
    # plt.plot([x.total for x in swap_mem], label='Total Swap Memory')
    # plt.plot([x.used for x in full_mem_output], label='Used Swap Memory')
    # plt.plot([x.free for x in swap_mem], label='Free Swap Memory')

    plt.legend(loc='best')
    plt.show()
