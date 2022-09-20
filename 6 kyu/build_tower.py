def tower_builder(n_floors):
    return [('*' * i).center(n_floors * 2 - 1) for i in range(1, 2 * n_floors + 1, 2)]
  
