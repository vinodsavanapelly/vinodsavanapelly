# names = ['John', 'maria','','kumar']
# for name in names:
#     if name =='':
#         #print("empty value detected")
#         pass #todo: Handle empty values
#         name = name.replace('','Unknown')
#     print(f'Name = {name}')

# days = ['Mon','Tue','Wed','Sun']
# weekends =['Sat','Sun']
# for day in days:
#     if day in weekends:
#         continue
#     print(f'workingday: {day}')
    
# emails = ['ram@gmail.com',
#          'ram@gmail.com',
#          'fhsdfghdfghdgh;'
#          'kaa@gmail.com']
# for email in emails:
#     if ';' in email:
#         print('SQL injection: Hackaer Attack')
#         break
#     if not(email.endswith('.com')):
#         break
#     print(f'emails are:{email}')


#Else + Break : Use else with loops only when there's a break

# items = [2,4,8]
# for item in items:
#     if item == 5:
#         print('number 5 found')
#         break
# else:
#     print(f'Numbers are: {item}')

file_list = ['report.csv',
             'data.xlsx',
             'summary.docx',
             'report.csv',
             'data.csv']
# for fl in file_list:
#     if len(fl) != len(set(fl)):
#         print(f"Duplicate found:{fl}")

# # duplicate = set()
# # for fl in file_list:
# #     if fl.count(fl)>1:
# #         duplicate.add(fl)
# #         print(f'repeted files name are: {duplicate}')
# #         break
# else:
#     print('all files are unique')


#Nested For loop
#1

# for x in range(3):
#     for y in range(2):
#         for z in range(2):
#             print(f"{x},{y},{z}")

#2
# colors = ['red','blue','green']
# sizes = ['M','S','L']

# for color in colors:
#      for size in sizes:
#         print(f'{color},{size}')

#3 Hierarchy

# years = [2026,2027]
# months = ['jan','feb']
# days= range(1,29)

# for y in years:
#     for m in months:
#         for d in days:
#             print(f'report_{y}_{m}_{d}.csv')

#4
tables =['customers','orders','products','prices']
columns = ['id', 'create_date']
for t in tables:
    for c in columns:
        print(f'select count(*) from {t} where {c} is Null;')


        