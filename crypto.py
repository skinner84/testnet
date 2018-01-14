from __future__ import print_function
import basc_py4chan

# get the board we want
board = basc_py4chan.Board('biz')

# open a file

commentsfile = open('comments.txt','w')

# go through each thread
all_thread_ids = board.get_all_thread_ids()
comments = []
for t in all_thread_ids:
	#print (t)
	thread = board.get_thread(t)
	post = thread.posts
	for p in post:
                comments.append(p.text_comment)
#print(comments)

count = 0

for c in comments:
	words = c.split()
	for word in words:
            if str(word).lower() == "tel":
                 count += 1
                 print (word)
print (count)


