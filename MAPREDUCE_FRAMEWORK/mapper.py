def mapper(lines):

    mapped = []

    for line in lines:

        data = line.strip().split(",")

        if len(data) == 6:

            genre = data[3]

            mapped.append((genre,1))

    return mapped