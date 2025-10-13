import threading
from math import sqrt
from collections import Counter
 

def is_prime(n):
    """Berilgan sonni tub yoki yo'qligini tekshiradi"""
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check_primes_in_range(start, end, result_list):
    """Berilgan oraliqdagi tub sonlarni topib listga qo'shadi"""
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    result_list.extend(local_primes)


def threaded_prime_checker(start_range, end_range, num_threads=4):
    """Oraliqni threadlarga bo'lib, parallel tarzda tub sonlarni topadi"""
    threads = []
    result_list = []
    step = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start + step - 1 if i != num_threads - 1 else end_range
        t = threading.Thread(target=check_primes_in_range, args=(start, end, result_list))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    result_list.sort()
    print(f"\nPrime numbers between {start_range} and {end_range}:")
    print(result_list)


 

def process_file_part(lines, counter):
    """Har bir thread faylning o'z qismidagi so'zlarni sanaydi"""
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter.append(local_counter)


def threaded_word_count(filename, num_threads=4):
    """Katta fayldagi so'zlarni threadlar orqali sanaydi"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    step = total_lines // num_threads
    threads = []
    counters = []

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i != num_threads - 1 else total_lines
        t = threading.Thread(target=process_file_part, args=(lines[start:end], counters))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    print("\nWord occurrences in file:")
    for word, count in total_counter.most_common(10):  # faqat eng ko‘p 10ta so‘zni chiqaradi
        print(f"{word}: {count}")

 
 

if __name__ == "__main__":
  
    threaded_prime_checker(1, 100, num_threads=4)

   
    threaded_word_count('test.txt', num_threads=4)
