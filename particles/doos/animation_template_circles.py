"""
 Template voor uitdagende opdracht 'deeltjes in een doos' voor
 vak Inleiding Programmeren - Universiteit van Amsterdam.
 Maak dit programma af waar 'YOUR CODE COMES HERE' staat.
 De rest van dit programma is in het Engels.
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from math import *
import random


#====================================
def example_animate_moving_circles():
#====================================

  # ----------------
  #--/ main program:
  # ----------------

  global N_particles
  global x, y, r, vx, vy, m

  #--/ define parameters of the box and figure
  xmin_box = -4
  xmax_box =  4
  ymin_box = -4
  ymax_box =  4
  fig = plt.figure(num=None, figsize=(6, 6), dpi=80, facecolor='w', edgecolor='k')
  ax = plt.axes(xlim=(xmin_box, xmax_box), ylim=(ymin_box, ymax_box))

  #--------------------------------------------------------------------
  # [1] initiate all particles
  #      o x- and y-position for all particles (list x and y)
  #      o x- and y-velocity for all particles (list vx and vy)
  #      o radius for each particle (list r)
  #      o mass for each particle (list m)
  #      o abstract/plotting: a list of circle-objects
  #--------------------------------------------------------------------
  x  = []
  y  = []
  vx = []
  vy = []
  r  = []
  m = []
  circles = []
  radius_balls = 0.1
  mass_balls = 1
  N_particles = 3

  #--/ define starting position (x and y) for each ball and define radius (r)
  for i_particle in range(N_particles):
      x_i = 0.0 + i_particle * 0.1
      y_i = 0.0
      v = 0.15 * random.random()
      angle = 2 * np.pi * random.random()
      vx_i = v * np.cos(angle)
      vy_i = v * np.sin(angle)
      vx.append(vx_i)
      vy.append(vy_i)
      radius_ball = radius_balls
      x.append(x_i)
      y.append(y_i)
      r.append(radius_ball)
      m.append(mass_balls)

  #--/ use the parameters in previous step to define 'real' circles (objects)
  #    and add the circle object to the plot
  for i_particle in range(N_particles):
      if(i_particle == 0):
         circles.append(plt.Circle((xmax_box + 1, ymax_box + 1), radius = r[i_particle], fc = 'red'))   # red ball
      else:
         circles.append(plt.Circle((xmax_box + 1, ymax_box + 1), radius = r[i_particle], fc = 'blue'))   # blue ball
      ax.add_patch(circles[i_particle])


  #----------
  def init():
  #----------
  #--/ stuff entered here stays on the screen forever, so put circles at dummy position
    global N_particles
    print(" init():: entering dummy start values")
    x_dummy = -1.
    y_dummy = -1.
    for i_particle in range(N_particles):
      circles[i_particle].center = (x_dummy, y_dummy)

    return circles

  #-------------------
  def animate(i_time):
  #-------------------
  #--/ this routine is called every time step

    global x, y, r, N_particles, vx, vy

    #--/ at time 0 initiate all circles on the screen at their locations
    if(i_time == 0):
      print(" animate(t==0):: enter start-values for circles from main program")
      for i_particle in range(N_particles):
        circles[i_particle].center = (x[i_particle], y[i_particle])

    #------------------------------------------------
    #--/ [STEP 1] compute new position of the circles
    #------------------------------------------------
    for i_particle in range(N_particles):

      #--/ get position and radius of the circle in question
      xi, yi = circles[i_particle].center
      ri = r[i_particle]
      print(" Time-step: %d   -> position circle %d = (%5.2f, %5.2f) with radius %5.2f" % (i_time, i_particle,xi,yi,ri))

      #--------------------------------------------------
      #--/ compute new position and velocity of the balls
      #--------------------------------------------------

      delta_t = 1.5

      # update position
      #--------------------------------------------------
      # YOUR CODE COMES HERE
      #--------------------------------------------------

      # hitting the wall changes the sign of the velocity
      #--------------------------------------------------
      # YOUR CODE COMES HERE
      #--------------------------------------------------

      # now add in collisions between particles
      #--------------------------------------------------
      # YOUR CODE COMES HERE
      #--------------------------------------------------


    #---------------------------
    #--/ update circle positions
    #---------------------------
    for i_particle in range(N_particles):
        circles[i_particle].center = (x[i_particle], y[i_particle])

    #--/ return (end of simulate_colliding_balls())
    return circles



  #--/ do the actual animation (part of main program)
  anim = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=2000, interval=80, blit=True)

  plt.show()


  return

#----- end example_animate_moving_circles()



# ============
# MAIN PROGRAM
# ============
example_animate_moving_circles()










