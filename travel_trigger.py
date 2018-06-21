import sys

def read_countries():
    countries = []
    with open("countries.txt", "r") as f:
        for line in f:
            if line.split():
                countries.append(line.split())
    return countries

def read_pages():
    pages = []
    with open("pages.txt", "r") as f:
        for line in f:
            if(line.split()):
                pages.append(line.split())
    return pages

def pullout_countries(pages,countries):
    for i in range(len(pages)):
        for country in countries:
            if country[0] == pages[i][1]:
                pages[i].append(country[0])
                break
        pages[i].append("0")
    return pages

def write_pages(pages):
    f = open("pages.txt", "w")
    for i in range(len(pages)):
        for j in range(len(pages[i])):
            if j == len(pages[i])-1:
                f.write(str(pages[i][j]))
            else:
                f.write(str(pages[i][j]) + "\t")
        if i != len(pages)-1:
            f.write("\n")    
    f.close()


def read_links():
    links = []
    index_list = ['0']
    index_num = 0
    with open("links.txt", "r") as f:
        for line in f:
            num = line.split()
            if index_num == int(num[0]):
                index_list.append(num[1])
            else:
                links.append(index_list)
                index_list = [num[0],num[1]]
                index_num = int(num[0])
        links.append(index_list)
            
    return links

def search_triger(tiger,pages):
    triger_boolean = 0
    triger_num = ""
    for page in pages:
        if page[1] == triger:
            triger_boolean = 1
            triger_num = page[0] 
            break
    return triger_boolean, str(triger_num)
    

def bfs(tiger, triger_num, pages):
    countries = []
    checked = []
    next_triger_num = []
    queue = read_test_links(triger_num)
    queue.append("")
    index = 0
    while len(queue) > 0:
        if queue[0] == "":
            index = index + 1
            if len(countries) > 0:
                break
            
            queue = read_test_links(next_triger_num[0])
            next_triger_num = next_triger_num[1:]
            if len(next_triger_num) > 0:
                break
            queue.append("")
        else:
            for check in checked:
                if queue[0] == check:
                    queue = queue[1:]
            if pages[int(queue[0])][2] != "0":
                countries.append(pages[int(queue[0])][2])
            checked.append(queue[0])
            next_triger_num.append(queue[0])
            queue = queue[1:]

    return countries,index

   
    

def read_test_pages():
    pages = []
    with open("test_pages.txt", "r") as f:
        for line in f:
            pages.append(line.split())
    return pages


def read_test_links(triger_num):
    links = []
    index_num = triger_num
    with open("links.txt", "r") as f:
        for line in f:
            num = line.split()
            if index_num == num[0]:
                links.append(num[1])
            
    #print(links)
    return links







#countries = read_countries()#countries.txtを読み込み
#pages = read_pages()#pages.txtを読み込み


#fixed_pages = pullout_countries(pages,countries)#国名であればその国名を抜き出す
#write_pages(fixed_pages)#pages.txtを書き込み


print("\n--------\nWhich countries do you wanna go to ?\nPlease set a trigger.\n")
triger = input("-------- trigger : ")

pages = read_pages()#pages.txtを読み込み
#test_pages = read_test_pages()#test_pages.txtを読み込み

#pages.txt内にトリガーと一致する単語があるか探索
#1...ある→続行
#0...ない→システム終了
(triger_boolean, triger_num) = search_triger(triger, pages)
if triger_boolean == 0:
    print("\n[error]Trigger did not exist in pages.txt\n")
    sys.exit()

(recommendation_countries,index) = bfs(triger,triger_num,pages)


if len(recommendation_countries) == 0:
    print("There was no relationship between trigger and the country....")

else:
    print("\nYou should go to this country !\n----------------------\n")
    for country in recommendation_countries:
        print("   " +country)
    print("\n----------------------\n")
    
    print("Repeat number is  { " + str(index) + " }\nIn other words...\nThe width is   { " + str(index) + " }\n")
