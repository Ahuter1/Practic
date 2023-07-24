import requests, json, openpyxl
r = requests.get('https://raw.githubusercontent.com/QCplus/practice/main/query.json')
c = requests.get('https://raw.githubusercontent.com/QCplus/practice/main/issues.json')
b = r.text
a = json.loads(b)
issues = json.loads(c.text)["issues"]
slov = []
for elem in a["_embedded"]["results"]["_embedded"]["elements"]:
    for isu in issues:
        if elem['customField4'] == isu['externalId']:
            slov.append({
                'id': isu['id'],
                'name': isu['name'],
                'externalId': isu['externalId'],
                'createdAt': isu['createdAt'],
                'calcedAt': isu['calcedAt'],
                'authorId': isu['authorId'],
                'authorName': isu['authorName'],
                'costs': isu['costs'],
                '_type': elem['_type'],
                'id1': elem['id'],
                'subject': elem['subject'],
                'createdAt1': elem['createdAt'],
                'updatedAt': elem['updatedAt'],
                'customField4': elem['customField4']

            })

#print(slov)


workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = 'ID'
sheet['B1'] = 'Name'
sheet['C1'] = 'ExternalId'
sheet['D1'] = 'CreatedAt'
sheet['E1'] = 'CalcedAt'
sheet['F1'] = 'AuthorId'
sheet['G1'] = 'AuthorName'
sheet['H1'] = 'Costs'
sheet['I1'] = 'Type'
sheet['J1'] = 'ID'
sheet['K1'] = 'Subject'
sheet['L1'] = 'CreatedAt'
sheet['M1'] = 'UpdatedAt'
sheet['N1'] = 'CustomField4'
for i in slov:
    dan = [
        i.get('id', ''),
        i.get('name', ''),
        i.get('externalId', ''),
        i.get('createdAt', ''),
        i.get('calcedAt', ''),
        i.get('authorId', ''),
        i.get('authorName', ''),
        i.get('costs', ''),
        i.get('_type', ''),
        i.get('id1', ''),
        i.get('subject', ''),
        i.get('createdAt1', ''),
        i.get('updatedAt', ''),
        i.get('customField4', ''),
    ]
    sheet.append(dan)
workbook.save('work.xlsx')
