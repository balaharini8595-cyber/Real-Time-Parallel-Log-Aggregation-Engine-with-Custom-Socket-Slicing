def split_data(lines, parts):

    chunk_size = len(lines) // parts

    chunks = []

    start = 0

    for i in range(parts):

        end = start + chunk_size

        if i == parts - 1:
            end = len(lines)

        chunks.append(lines[start:end])

        start = end

    return chunks