def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)"""

    line = '-' * tick_length

    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval based upon a central tick length"""

    if center_length > 0:  # stop when length drops to 0
        draw_interval(center_length - 1)  # recursively draw top ticks
        # print("Top ticks", center_length)
        draw_line(center_length)  # draw center tick
        # print("Bottom ticks", center_length)
        draw_interval(center_length - 1)  # recursively draw bottom ticks


def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length"""

    draw_line(major_length, '0')  # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  # draw interior ticks for inch
        draw_line(major_length, str(j))  # draw inch j line and label


draw_ruler(1, 3)
"""
    Another interesting question is how many dashes are printed during that process. 
    Prove by induction that the number of dashes printed by draw_interval(c) is (2^c+1) − c − 2.
    
    Proporcionamos una prueba formal de esta afirmación por inducción (consulte la Sección 3.4.3). De hecho, 
    la inducción es una técnica matemática natural para demostrar la exactitud y eficiencia de un proceso recursivo. 
    En el caso de la regla, observamos que una aplicación del draw_interval(0) no genera salida y que 2 ^ 0−1 = 1−1 = 0. 
    Esto sirve como un caso base para nuestra afirmación. 
    De manera más general, el número de líneas impresas por draw_interval(c) es uno más del doble del número 
    generado por una llamada a draw_interval(c-1), ya que se imprime una línea central entre dos llamadas recursivas de este tipo. 
    Por inducción, tenemos que el número de líneas es entonces 1 + 2 * (2 ^ c − 1 - 1) = 1 + 2 ^ c - 2 = 2 ^ c - 1.
"""