po_tysiackroc = ['1000000', '2356989', '245158', '65958751']

def convert_number(byleco):
    for i in byleco:
        print(i)
        z_kropkami = ''
        for index, j in enumerate(reversed(i), start=1):
            z_kropkami = j + z_kropkami
            if index % 3 == 0 and index != len(i) and (index+1) % 3 != 0:
                z_kropkami = '.' + z_kropkami
        print(z_kropkami)

convert_number(po_tysiackroc)
