# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']

sentence = 'Welcome Back to This Tutorial'

print(set(char_list))
print(set(sentence))

print(set(char_list + list(sentence)))

unique_char = set(char_list)
unique_char.add('x')
# unique_char.add(['y', 'z']) this is wrong
print(unique_char)

unique_char.remove('x')    # 返回NOne，如果x不存在会报错
print(unique_char)
unique_char.discard('d')  # 如果d不存在，不会报错
print(unique_char)
unique_char.clear()
print(unique_char)

unique_char = set(char_list)
print(unique_char.difference({'a', 'e', 'i'}))    # unique_char有，{'a', 'e', 'i'}没有的部分
print(unique_char.intersection({'a', 'e', 'i'}))  # 交集