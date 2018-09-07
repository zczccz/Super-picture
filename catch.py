from PIL import ImageGrab
import time


s = time.time()
for i in range(70000):
    # im = ImageGrab.grab(bbox=(0,86,640,450))
    im = ImageGrab.grab(bbox=(676, 86, 1374, 470))
    # im = ImageGrab.grab(bbox=(75, 84, 520, 330))
    # print(np.asarray(im).tobytes())
    im.save(r'E:\huya\daleilei/'+str(i)+'.jpeg','jpeg')
    time.sleep(0.2)
print(time.time()-s)

import time
import logging
import threading

# file_obj = open("./film_keywords.txt")
# lines = file_obj.readlines()
# for index,line in enumerate(lines):
#     lines[index] = line.strip('\n')
#
# print(lines)

# processing_num = 5
# i = 0
# while True:
#     for kw in lines[i:i+processing_num]:
#         start = time.time()
#         processing_list = []
#
#         print('Processing start:{}'.format(kw))
#         # processing_list.append(Process(target=download_images, args=(kw,)))
#         # for p in processing_list:
#         #     p.start()
#         # for p in processing_list:
#         #     p.join()
#
#         logging.critical('{} download finished cost {} sec.'.format(kw, time.time() - start))
#     i = i+processing_num
#
#     if i >= len(lines)+5:
#         break

# for keywords in [lines[i:i + processing_num] for i in range(0, len(lines), processing_num)]:
#
