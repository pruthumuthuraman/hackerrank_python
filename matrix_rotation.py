def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    num_layers = min(m, n) // 2
    
    for i in range(num_layers):
        layer = []
        # Extract Top -> Right -> Bottom -> Left
        for j in range(i, n - 1 - i): layer.append(matrix[i][j])
        for j in range(i, m - 1 - i): layer.append(matrix[j][n - 1 - i])
        for j in range(n - 1 - i, i, -1): layer.append(matrix[m - 1 - i][j])
        for j in range(m - 1 - i, i, -1): layer.append(matrix[j][i])
        
        # Shift anti-clockwise
        shift = r % len(layer)
        rotated = layer[shift:] + layer[:shift]
        
        # Put back Top -> Right -> Bottom -> Left
        idx = 0
        for j in range(i, n - 1 - i):
            matrix[i][j] = rotated[idx]
            idx += 1
        for j in range(i, m - 1 - i):
            matrix[j][n - 1 - i] = rotated[idx]
            idx += 1
        for j in range(n - 1 - i, i, -1):
            matrix[m - 1 - i][j] = rotated[idx]
            idx += 1
        for j in range(m - 1 - i, i, -1):
            matrix[j][i] = rotated[idx]
            idx += 1

    for row in matrix:
        print(*row)
