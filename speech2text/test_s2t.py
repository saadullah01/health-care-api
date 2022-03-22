from s2t import main
import time

def test_threads_timing():
    start_time = time.time()
    main(['-c', '8', '-t', '2', '-n', '16'])
    end_time = time.time()
    time_taken = end_time - start_time
    flag = False
    if time_taken < 6:
        flag = True
    assert flag == True
    