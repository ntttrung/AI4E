name = 'Trung is 19 years old. Trung is coding. Trung is studying at HUST Trung Trung'
count = 0
ls = []
sub_name = 'Trung'
while sub_name in name[count:]:
  ls.append(name.index(sub_name,count))
  # print(name.index(sub_name,count))
  # print(count)
  count = name.index(sub_name,count)
# ls=list(set(ls))
# ls.sort()
print(ls)