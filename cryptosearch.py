from __future__ import print_function
import basc_py4chan

# get the board we want
board = basc_py4chan.Board('biz')

# open a file

commentsfile = open('comments.txt','w')

count = 0

# go through each thread
all_thread_ids = board.get_all_thread_ids()
for t in all_thread_ids:
    thread = board.get_thread(t)
    post = thread.posts
    for p in post:
        words = p.split()
        print (words)
	#for word in words:
	 #   if str(word).lower() == "telcoin":
	  #      count += 1
	   #     print (word)
	    #    print (count)
