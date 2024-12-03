import re
import codecs
import csv


# задание 1
with open('task1-en.txt', 'r') as f:
    t1txt = f.read()
initial_res_nums = re.findall(r"[-+]?(?:\d+(?:\."
                            r"\d*)?|\.\d+)(?:[eE][-+]?\d+)?", t1txt)
res_numbers = [re.sub(r'[.]$', '', nums) for nums in initial_res_nums]
res_6words = re.findall(r"\b\w{6}\b", t1txt)
res_8words = re.findall(r"\b\w{8}\b", t1txt)
print('Задание 1:', res_numbers, res_6words, res_8words, sep='\n')


# задание 2
file_html = codecs.open("task2.html", "r", "utf_8_sig" )
text = file_html.read()
file_html.close()
initial_res_tags = re.findall(r'\bcontent="\w+"', text)
res_tags = [re.sub(r'content="|"', '', email)
            for email in initial_res_tags]
print('Задание 2:', res_tags, sep='\n')


# задание 3 (с кучей костылей из-за "слипания" данных)
with open('task3.txt', 'r') as f:
    t3txt = f.read()
# dateor - date of registration
res_dateor =  re.findall(r"\d{4}-\d\d-\d\d", t3txt)
t3txt = re.sub(r"\d{4}-\d\d-\d\d", ' ', t3txt)
t3txt = re.sub(r"[a-z]/", ' ', t3txt)
res_url = re.findall(r"http\S+\w+", t3txt)
for x in range(len(res_url)):
    end_letters = {'.ne': '.net', '.inf': '.info',
                   '.co': '.com', '.bi': '.biz', '.or': '.org'}
    res_url[x] = res_url[x].replace(res_url[x]
                                    [(res_url[x].rfind('.')):],
                                    end_letters.get(res_url[x]
                                    [(res_url[x].rfind('.')):]))
t3txt = re.sub(r"http\S+\w+", ' ', t3txt)
res_surname = re.findall(r"[A-Z][a-z]{1,7}", t3txt)
t3txt = re.sub(r"[A-Z][a-z]{1,7}", ' ', t3txt)
initial_res_email = re.findall(r'[a-z0-9]+@'
                        r'[a-zA-Z0-9.-]+\.[a-zA-Z]{,4}', t3txt)
res_email = [re.sub(r'^\d+|\d+$', '', email)
             for email in initial_res_email]
res_id =[i for i in range(1, 10001)]
with open('table.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Фамилия', 'Почта', 'URL',
                     'Дата регистрации'])
    for row in zip(res_id, res_surname, res_email, res_url, res_dateor):
        writer.writerow(row)

print("Задание 3: см. файл table.csv")
