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


countries = read_countries()#countries.txtを読み込み
pages = read_pages()#pages.txtを読み込み
fixed_pages = pullout_countries(pages,countries)#国名であればその国名を抜き出す
write_pages(fixed_pages)#pages.txtを書き込み
