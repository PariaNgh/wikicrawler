from wikicrawler import crawl
import multiprocessing
import time

start_time = time.time()
seeds = ['https://www.wikipedia.org/', 'https://www.reddit.com/', 'https://stackexchange.com/']


processes = []

if __name__ == '__main__':
    for i in range(len(seeds)):
        p = multiprocessing.Process(target=crawl, args=([seeds[i]], []))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

#
# crawl(seeds, [])

end_time = time.time()
