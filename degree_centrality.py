import csv
import math
with open('rg.csv', 'r') as f:
    reader = csv.reader(f,delimiter='\t')
    tup_list =list(reader)
print(len(tup_list))
for i in range(len(tup_list)):
	tup_list[i]=list(tup_list[i][0].split(","))


with open("Full_DT_nodes.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

my_list = list()
for y in content:
	content_sp = y.split('\t')
	content_sp = content_sp+(content_sp[1].rsplit('/', 1))
	del(content_sp[1])
	my_list.append(content_sp[:])

def search1(list1,x):
	for i in range(len(list1)):
		if(my_list[i][1]==x and my_list[i][2]=='NN'):
			return my_list[i]
	for i in range(len(list1)):
		if(my_list[i][1]==x):
			return my_list[i]


numerator=list()
denominator=list()
deg_list=list()
for i in range(len(tup_list)):	
	x=tup_list[i]
	print(x)
	word2_list=search1(my_list,x[1].lower())
	word1_list=search1(my_list,x[0].lower())
	with open("Full_DT_adj_list_proper_merged.txt") as f1:
		for line in f1:
			l,m=line.split("\t")
			m=m.strip()
			s=list(m.split(" "))
			# print(l,m,s)
			try:
				if(word1_list[0]==l):
					listx=s
				flag=1
			except TypeError:
				flag=0
				continue
			try:
				if(word2_list[0]==l):
					listy=s
				flag=1
			except TypeError:
				flag=0
				continue
	# print("listy = ",listy)
	# print("listx = ",listx)
	if(flag==1):
		intersect=set(listy).intersection(listx)

	#cos_sim=len(intersect)/(math.sqrt(len(listx))*math.sqrt(len(listy)))
		deg_cen=float(len(intersect))/(len(listx)+len(listy)-len(intersect))
		denominator.append(len(listx)+len(listy)-len(intersect))
		numerator.append(len(intersect))
		deg_list.append(deg_cen)
		print(deg_list)
		print(numerator)
		print(denominator)
	if(flag==0):
		print("Error! Word can't be found")

csvd=zip(deg_list,numerator,denominator)
csvd1=zip(['Degree_Centrality'],['numerator'],['denominator'])
with open('deg_cen.csv', 'w') as f:
     writer = csv.writer(f, delimiter=';', lineterminator='\n')
     writer.writerows(csvd1)
     writer.writerows(csvd)