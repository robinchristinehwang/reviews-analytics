data = []
count = 0
with open('reviews.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000000 == 0:
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
print(new[0])

good = []
for d in data:
	if "good" in d:
		good.append(d)

good = [d for d in data if "good" in d]
bad = ["bad" in d for d in data]

print(len(bad))
print(good[28])
print(bad[8])


#
wc = {} #word_count的空字典
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc: #如果這個字有出現在wc這個字典中
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進字典	 
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc)) #就知道總共有幾個key
print(wc['Robin'])

while True:
	word = input('請輸入你想查的字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, "出現過的次數為", wc[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用')



#print(len(good))
#print(good[5])

