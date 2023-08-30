import pygame
import matplotlib.pyplot as plt
import statistics


def plot_graph(screen,data, x_label, y_label,plant,pest):
    fruits = {
        'Tomatoes':pygame.image.load('assets/tomatoesbag.png').convert_alpha(),
        'Corn':pygame.image.load('assets/cornbag.png').convert_alpha()
    }

    back_ground = pygame.image.load('assets/end_game.png').convert_alpha()
    average_fruits = statistics.mean(data)

    survival_rate = average_fruits/80
    pest_killed = pest
    font = pygame.font.SysFont('Arial', 30)
    fruit_text = font.render(f'{average_fruits:.0f}', True, (0, 0, 0))
    survival_text = font.render(f'{survival_rate:.0f}', True, (0, 0, 0))
    pest_killed_text = font.render(f'{pest_killed:.0f}', True, (0, 0, 0))
    fig = plt.figure(figsize=(3.52, 3.36))
    
    plt.plot(data)
    plt.title('A graph of {} grown vs days\n Press space to close graph'.format(plant))
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # save the plot as an image
    plt.savefig('graph.png')

    # load the image and display it on the screen
    load_fruits_planted = fruits[plant]
    load_fruits_planted = pygame.transform.scale2x(load_fruits_planted)
    screen.blit(back_ground,(0,0))
    screen.blit(load_fruits_planted,(64,464))
    screen.blit(fruit_text,(96,464))
    screen.blit(survival_text,(224,464))
    screen.blit(pest_killed_text,(368,464))
    graph_image = pygame.image.load('graph.png')
    screen.blit(graph_image, (80, 80))
    

    # update the display
    pygame.display.update()

    # wait for the user to close the window

# data = [1, 2, 3, 4, 5]
# x_label = 'Days'
# y_label = "Amount of fruits grown"
# plot_graph(data, x_label, y_label,'Tomatoes')
