def mazeRenderer(maze):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in maze]))