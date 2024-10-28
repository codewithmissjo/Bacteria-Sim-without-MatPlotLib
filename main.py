import pygame, sys
from pygame.locals import QUIT
from doctor import Medic
from virus import Virus
import random

pygame.init()
size = (width, height) = (800, 600)
SCREEN = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font_size = 16
font = pygame.font.SysFont('couriernew', font_size)
font2 = pygame.font.SysFont('couriernew', font_size)
boldfont = font2.set_bold(True)
roond = 0
col_len = 10

b_score = 0
d_score = 0

split_time = 500

b_num = 5
d_num = 1

bacteria = pygame.sprite.Group()
doctors = pygame.sprite.Group()


def init():
  for b in range(b_num):
    bacteria.add(
        Virus((random.randint(0, width), random.randint(0, height)),
              split_time))

  for d in range(d_num):
    doctors.add(Medic((random.randint(0, width), random.randint(0, height))))


def newroond():
  global roond
  doctors.empty()
  bacteria.empty()
  roond += 1
  init()


def checkWin():
  global d_score, b_score, b_num, d_num, success, split_time
  if len(bacteria) < 1:
    d_score += 1
    split_time -= 50
    if split_time < 10:
      split_time = 500
      b_num += 5
    return True
  elif len(bacteria) > b_num * split_time // 2:
    b_score += 1
    if roond % 2 == 0:
      d_num += 1
    return True
  return False

def spacingHelp(txt):
  if len(str(txt)) < col_len:
    return str(txt) + (" " * (col_len - len(str(txt))))

def textStuff():
  text1 = font2.render(f"ROUND #{roond}     |  {spacingHelp('DOCTORS')}  |  VIRUSES", True, "black")
  text2 = font.render(f"STARTED W/   |  {spacingHelp(d_num)}  |  {b_num} ", True, "black")
  text3 = font.render(f"CURRENT #    |  {spacingHelp(len(doctors))}  |  {len(bacteria)} ", True, "black")
  text4 = font.render(f"# TO WIN     |  {spacingHelp('0 viruses')}  |  {b_num * split_time // 2} viruses", True, "black")
  text5 = font.render(f"WINS         |  {spacingHelp(d_score)}  |  {b_score} ", True, "black")
  text6 = font.render(f"SPLIT_TIME   |  {spacingHelp('n/a')}  |  {split_time} ticks", True, "black")
  return [text1, text5, text4, text6, text2, text3]


def main():
  global b_num, d_num, tests, success, case_samples, test_data, done, split_time
  newroond()
  # stuff
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

    if checkWin():
      #end of roond
      newroond()

    #Update!
    bacteria.update(bacteria)
    doctors.update()
    pygame.sprite.groupcollide(bacteria, doctors, True, False)

    # DRAW
    SCREEN.fill("#eca1a6")
    bacteria.draw(SCREEN)
    doctors.draw(SCREEN)

    theText = textStuff()
    for stuff in range(len(theText)):
      SCREEN.blit(theText[stuff], (10, 10 + (font_size + 5) * stuff))

    # THE LAST LINE
    pygame.display.update()


if __name__ == "__main__":
  main()
