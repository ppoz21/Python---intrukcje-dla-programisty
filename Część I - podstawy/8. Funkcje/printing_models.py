def print_models(unprinted_designs, completed_models):
    """
    Symulujemy wydruk poszczególnych projektów, dopóki na liście jest jakikolwiek model.
    Każdy wydrukowany model zostaje przeniesiony na listę completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Symulacja wydruku 3D na podstawie modelu
        print("Wydruk modelu: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Wyświetla wszystkie modele, które zostały wydrukowane."""
    print("\nWydrukowane modele:")
    for model in completed_models:
        print('\t*', model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
