import pygame.cursors, pygame.mouse
Butifara = (
    "        XX              ",  # 24x24
    "       X..X             ",
    "       X..X             ",
    "       X..X             ",
    "       X..X             ",
    "       X..X             ",
    "     XXX..XXX           ",
    "    X..X..X..XX         ",
    "    X..X..X..X.X        ",
    "    X..X..X..X..X       ",
    "   XX........X..X       ",
    "  X.X...........X       ",
    "  X.............X       ",
    "  X.............X       ",
    "  X.............X       ",
    "   X............X       ",
    "   X...........X        ",
    "    X..........X        ",
    "    X..........X        ",
    "     X........X         ",
    "     X........X         ",
    "     XXXXXXXXXX         ",
    "                        ",
    "                        ",
)
Mano=(
    "                        ",  # 24x24
    "     XX                 ",
    "    X..X                ",
    "    X..X                ",
    "    X..X                ",
    "    X..XXX              ",
    "    X..X..XXX           ",
    "    X..X..X..XX         ",
    "    X..X..X..X.X        ",
    "    X..X..X..X..X       ",
    "   XX........X..X       ",
    "  X.X...........X       ",
    "  X.............X       ",
    "  X.............X       ",
    "  X.............X       ",
    "   X............X       ",
    "   X...........X        ",
    "    X..........X        ",
    "    X..........X        ",
    "     X........X         ",
    "     X........X         ",
    "     XXXXXXXXXX         ",
    "                        ",
    "                        ",

)
default = (               #sized 24x24
  " X                      ",
  " XX                     ",
  " XX                     ",
  " X.X                    ",
  " X..X                   ",
  " X...X                  ",
  " X....X                 ",
  " X.....X                ",
  " X......X               ",
  " X.......X              ",
  " X........X             ",
  " X.........X            ",
  " X......XXXXX           ",
  " X.XXX..X               ",
  " XX   X..X              ",
  " X    X..X              ",
  "      X..X              ",
  "       X..X             ",
  "       X..X             ",
  "        XX              ",
  "                        ",
  "                        ",
  "                        ",
  "                        ")
cursor, mask = pygame.cursors.compile(Butifara, "X", ".")
cursorma, maskma =pygame.cursors.compile(Mano,"X",".")
cursorde, maskde =pygame.cursors.compile(default,"X",".")
default_metadata =((24, 24), (1, 1), cursorde, maskde)
mano_metadata =((24, 24), (1, 1), cursorma, maskma)
butifara_metadata = ((24, 24), (1, 1), cursor, mask)
#pygame.mouse.set_cursor(*butifara_metadata)