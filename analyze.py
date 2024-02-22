with open('data.csv', 'r') as file:
    lines = file.readlines()
    print('Read lines into memory.')

    keys = lines[0].split(',')
    sum = 0
    for line in lines[1:]:
        sum += len(line.split(',')[8])
        break
    print('Average line length: ' + str(sum / len(lines)))
