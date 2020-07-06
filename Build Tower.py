def tower_builder(n_floors):
    return [("*"*(i+1)*2)[:-1].center(n_floors*2-1) for i in range(n_floors)]