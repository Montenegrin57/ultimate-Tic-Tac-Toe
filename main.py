def create_grid(size: int):
    grid = []
    for y in range(size):
        external_row = []
        for x in range(size):
            external_column = []
            for c in range(size):
                internal_row = []
                for v in range(size):
                    internal_column = " "
                    internal_row.append(internal_column)
                external_column.append(internal_row)
            external_row.append(external_column)
        grid.append(external_row)
    return grid
map = create_grid(3)
