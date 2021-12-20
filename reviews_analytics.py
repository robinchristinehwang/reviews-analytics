data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

comment_len = 0
for d in data:
	comment_len = comment_len + len(d)

print('average length is', comment_len/len(data))

new =[]
for d in data:
	if len(d) < 100:
		new.append(d)

print("there are", len(new), "comments which exceed 100 characters")

