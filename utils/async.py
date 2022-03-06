from multiprocessing import Pool

def f(x):
    return x*x

def callback():
  print('Async call finished')
  
if __name__ == '__main__':
    pool = Pool(processes=1)         
    result = pool.apply_async(f, [10], callback)
