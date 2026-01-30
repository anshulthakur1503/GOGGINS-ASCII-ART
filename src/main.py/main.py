WIDTH = 68
HEIGHT = 51

for y in range(51):
    line = ""
    for x in range(WIDTH):

        # Logic for Row 0 (Previous)
        if y == 0:
            char = "."

        # LOGIC FOR ROW 1
        elif y == 1:
            # The colons are at index 29 and 30
            # (centered in the 68-character width)
            if x == 29 or x == 30:
                char = ":"
            else:
                char = "."

        # Placeholder for remaining rows
        elif y == 2:
            # We define the sequence starting from x = 22
            if 22 <= x <= 23:
                char = ":"
            elif 24 <= x <= 25:
                char = "="
            elif 26 <= x <= 31:
                char = "+"
            elif 32 <= x <= 34:
                char = "="
            elif 35 <= x <= 37:
                char = "-"
            elif x == 38:
                char = ":"
            else:
                char = "."

        elif y == 3:
            # The feature starts at x = 20 and ends at x = 41
            if 20 <= x <= 41:
                if 20 <= x <= 21:
                    char = "-"
                elif x == 22:
                    char = "="
                elif 23 <= x <= 24:
                    char = "+"
                elif 25 <= x <= 29:
                    char = "*"
                elif 30 <= x <= 33:
                    char = "+"
                elif 34 <= x <= 39:
                    char = "="
                elif x == 40:
                    char = "-"
                elif x == 41:
                    char = ":"
            else:
                char = "."  # Failsafe
        elif y == 4:
            # The feature spans from x = 17 to x = 43
            if 17 <= x <= 43:
                if x == 17:
                    char = ":"
                elif x == 18:
                    char = "="
                elif x == 19:
                    char = "+"
                elif x == 20:
                    char = "*"
                elif 21 <= x <= 23:
                    char = "#"  # First appearance of high-density stubble
                elif 24 <= x <= 27:
                    char = "*"
                elif 28 <= x <= 31:
                    char = "+"
                elif 32 <= x <= 41:
                    char = "="
                elif x == 42:
                    char = "-"
                elif x == 43:
                    char = ":"
            else:
                char = "."

        elif y == 5:
            # The feature now spans from x = 15 to x = 45
            if 15 <= x <= 45:
                if x == 15:
                    char = ":"
                elif x == 16:
                    char = "="
                elif 17 <= x <= 18:
                    char = "*"
                elif 19 <= x <= 23:
                    char = "#"  # Stubble zone expanding
                elif 24 <= x <= 27:
                    char = "*"
                elif 28 <= x <= 30:
                    char = "+"
                elif 31 <= x <= 44:
                    char = "="
                elif x == 45:
                    char = ":"
            else:
                char = "."

        elif y == 6:
            # The feature now spans from x = 14 to x = 46
            if 14 <= x <= 46:
                if x == 14:
                    char = "="
                elif x == 15:
                    char = "+"
                elif 16 <= x <= 17:
                    char = "*"
                elif 18 <= x <= 22:
                    char = "#"  # High-density texture
                elif 23 <= x <= 27:
                    char = "*"
                elif 28 <= x <= 29:
                    char = "+"
                elif 30 <= x <= 45:
                    char = "="
                elif x == 46:
                    char = ":"
            else:
                char = "."

        elif y == 7:
            # The feature spans from x = 13 to x = 47
            if 13 <= x <= 47:
                if x == 13:
                    char = "="
                elif x == 14:
                    char = "*"
                elif 15 <= x <= 22:
                    char = "#"  # Widened high-density block
                elif 23 <= x <= 27:
                    char = "*"
                elif 28 <= x <= 29:
                    char = "+"
                elif 30 <= x <= 46:
                    char = "="
                elif x == 47:
                    char = ":"
            else:
                char = "."

        elif y == 8:
            if 12 <= x <= 48:
                if x == 12:
                    char = "="
                elif x == 13:
                    char = "*"
                elif 14 <= x <= 17:
                    char = "#"
                elif 18 <= x <= 19:
                    char = "%"  # Forehead skin
                elif 20 <= x <= 22:
                    char = "#"  # Stubble
                elif 23 <= x <= 27:
                    char = "*"
                elif 28 <= x <= 30:
                    char = "+"
                elif 31 <= x <= 47:
                    char = "="
                elif x == 48:
                    char = ":"
                else:
                    char = "="  # Failsafe for mid-range
            else:
                char = "."

        elif y == 9:
            if 11 <= x <= 49:
                if x == 11:
                    char = "-"
                elif x == 12:
                    char = "*"
                elif 13 <= x <= 17:
                    char = "#"
                elif 18 <= x <= 20:
                    char = "%"
                elif 21 <= x <= 22:
                    char = "#"
                elif 23 <= x <= 27:
                    char = "*"
                elif 28 <= x <= 32:
                    char = "+"
                elif 33 <= x <= 48:
                    char = "="
                elif x == 49:
                    char = "-"
            else:
                char = "."

        elif y == 10:
            if 11 <= x <= 49:
                if x == 11:
                    char = "="
                elif 12 <= x <= 16:
                    char = "#"
                elif 17 <= x <= 21:
                    char = "%"
                elif 22 <= x <= 23:
                    char = "#"
                elif 24 <= x <= 24:
                    char = "*"
                elif 25 <= x <= 28:
                    char = "+"
                elif 29 <= x <= 33:
                    char = "="
                elif 34 <= x <= 40:
                    char = "-"
                elif 41 <= x <= 49:
                    char = "="
            else:
                char = "."

        elif y == 11:
            if 11 <= x <= 49:
                if x == 11:
                    char = "+"
                elif 12 <= x <= 14:
                    char = "#"
                elif 15 <= x <= 21:
                    char = "%"
                elif 22 <= x <= 23:
                    char = "#"
                elif 24 <= x <= 25:
                    char = "*"
                elif 26 <= x <= 29:
                    char = "+"
                elif 30 <= x <= 34:
                    char = "="
                elif 35 <= x <= 38:
                    char = "-"
                elif 39 <= x <= 49:
                    char = "="
            else:
                char = "."

        elif y == 12:
            if 11 <= x <= 49:
                if x == 11:
                    char = "="
                elif x == 12:
                    char = "#"
                elif 13 <= x <= 22:
                    char = "%"
                elif 23 <= x <= 24:
                    char = "#"
                elif 25 <= x <= 28:
                    char = "*"
                elif 29 <= x <= 31:
                    char = "+"
                elif 32 <= x <= 36:
                    char = "="
                elif 37 <= x <= 39:
                    char = "-"
                elif 40 <= x <= 48:
                    char = "="
                elif x == 49:
                    char = "+"
            else:
                char = "."

        elif y == 13:
            if 11 <= x <= 49:
                if x == 11:
                    char = "="
                elif x == 12:
                    char = "#"
                elif 13 <= x <= 21:
                    char = "%"
                elif 22 <= x <= 23:
                    char = "#"
                elif 24 <= x <= 25:
                    char = "*"
                elif x == 26:
                    char = "+"
                elif 27 <= x <= 28:
                    char = "*"
                elif x == 29:
                    char = "+"
                elif 30 <= x <= 33:
                    char = "="
                elif 34 <= x <= 37:
                    char = "-"
                elif 38 <= x <= 47:
                    char = "="
                elif 48 <= x <= 49:
                    char = "+"
            else:
                char = "."

        elif y == 14:
            if 11 <= x <= 49:
                if x == 11:
                    char = "="
                elif x == 12:
                    char = "*"
                elif x == 13:
                    char = "#"
                elif 14 <= x <= 21:
                    char = "%"
                elif x == 22:
                    char = "#"
                elif 23 <= x <= 28:
                    char = "*"
                elif 29 <= x <= 34:
                    char = "+"
                elif 35 <= x <= 40:
                    char = "-"
                elif 41 <= x <= 47:
                    char = "="
                elif 48 <= x <= 49:
                    char = "+"
            else:
                char = "."

        elif y == 15:
            if 11 <= x <= 49:
                if x == 11:
                    char = "-"
                elif x == 12:
                    char = "+"
                elif x == 13:
                    char = "*"
                elif x == 14:
                    char = "#"
                elif 15 <= x <= 21:
                    char = "%"
                elif 22 <= x <= 23:
                    char = "#"
                elif 24 <= x <= 30:
                    char = "+"
                elif 31 <= x <= 34:
                    char = "="
                elif 35 <= x <= 39:
                    char = "+"
                elif 40 <= x <= 41:
                    char = "*"
                elif 42 <= x <= 43:
                    char = "+"
                elif 44 <= x <= 47:
                    char = "="
                elif x == 48:
                    char = "+"
                elif x == 49:
                    char = "="
            else:
                char = "."

        elif y == 16:
            if 11 <= x <= 52:
                if x == 11:
                    char = ":"
                elif x == 12:
                    char = "+"
                elif x == 13:
                    char = "*"
                elif 14 <= x <= 17:
                    char = "#"
                elif 18 <= x <= 22:
                    char = "%"
                elif 23 <= x <= 27:
                    char = "@"  # Eye Shadow/Pupil
                elif 28 <= x <= 32:
                    char = "%"
                elif 33 <= x <= 35:
                    char = "#"
                elif 36 <= x <= 40:
                    char = "*"
                elif 41 <= x <= 45:
                    char = "#"
                elif 46 <= x <= 47:
                    char = "*"
                elif 48 <= x <= 51:
                    char = "+"
                elif x == 52:
                    char = "-"
            else:
                char = "."

        elif y == 17:
            if 8 <= x <= 53:
                if 8 <= x <= 10:
                    char = "="
                elif x == 11:
                    char = "*"
                elif x == 12:
                    char = "+"
                elif 13 <= x <= 15:
                    char = "#"
                elif 16 <= x <= 28:
                    char = "%"
                elif 29 <= x <= 33:
                    char = "#"
                elif 34 <= x <= 37:
                    char = "*"
                elif 38 <= x <= 40:
                    char = "+"
                elif 41 <= x <= 42:
                    char = "*"
                elif 43 <= x <= 45:
                    char = "+"
                elif 46 <= x <= 48:
                    char = "="
                elif 49 <= x <= 51:
                    char = "+"
                elif 52 <= x <= 53:
                    char = "*"
            else:
                char = "."

        elif y == 18:
            if 8 <= x <= 54:
                if 8 <= x <= 11:
                    char = "#"
                elif 12 <= x <= 15:
                    char = "@"
                elif 16 <= x <= 21:
                    char = "%"
                elif 22 <= x <= 24:
                    char = "#"
                elif 25 <= x <= 29:
                    char = "%"
                elif 30 <= x <= 32:
                    char = "*"
                elif 33 <= x <= 35:
                    char = "@"  # Core Eye Density
                elif 36 <= x <= 39:
                    char = "*"
                elif 40 <= x <= 45:
                    char = "="
                elif 46 <= x <= 49:
                    char = "-"
                elif 50 <= x <= 54:
                    char = "*"
            else:
                char = "."

        elif y == 19:
            if 8 <= x <= 54:
                if 8 <= x <= 11:
                    char = "#"
                elif 12 <= x <= 14:
                    char = "@"
                elif x == 15:
                    char = "."
                elif 16 <= x <= 18:
                    char = "#"
                elif 19 <= x <= 21:
                    char = "."
                elif x == 22:
                    char = "%"
                elif 23 <= x <= 24:
                    char = "'"
                elif x == 25:
                    char = "*"
                elif 26 <= x <= 28:
                    char = "#"
                elif 29 <= x <= 30:
                    char = "%"
                elif 31 <= x <= 32:
                    char = "#"
                elif 33 <= x <= 34:
                    char = "+"
                elif 35 <= x <= 38:
                    char = "#"
                elif 39 <= x <= 42:
                    char = "*"
                elif 43 <= x <= 46:
                    char = "="
                elif 47 <= x <= 50:
                    char = "-"
                elif 51 <= x <= 54:
                    char = "+"
            else:
                char = "."

        elif y == 20:
            # Row 21 of your design (Index 20)
            if 8 <= x <= 54:
                if 8 <= x <= 11: char = "="
                elif x == 12: char = "#"
                elif 13 <= x <= 14: char = "%"
                elif x == 15: char = "#"
                elif 16 <= x <= 23: char = "%"
                elif x == 24: char = "#"
                elif x == 25: char = "*"
                elif x == 26: char = "+"
                elif x == 27: char = "*"
                elif 28 <= x <= 30: char = "#"
                elif 31 <= x <= 32: char = "%"
                elif x == 33: char = "#"
                elif 34 <= x <= 35: char = "+"
                elif 36 <= x <= 37: char = "="
                elif 38 <= x <= 41: char = "-"
                elif 42 <= x <= 43: char = "+"
                elif 44 <= x <= 45: char = "*"
                elif 46 <= x <= 47: char = "+"
                elif 48 <= x <= 49: char = "="
                elif 50 <= x <= 51: char = "-"
                elif 52 <= x <= 53: char = "="
                elif x == 54: char = "*"
            else:
                char = "."

        elif y == 21:
            # Row 22: ........-#%%#.%%%%%%##***#%%=#+------====------===-+*...............
            if 8 <= x <= 53:
                if x == 8: char = "-"
                elif x == 9: char = "#"
                elif 10 <= x <= 11: char = "%"
                elif x == 12: char = "#"
                elif x == 13: char = "."
                elif 14 <= x <= 19: char = "%"
                elif 20 <= x <= 21: char = "#"
                elif 22 <= x <= 24: char = "*"
                elif 25 <= x <= 27: char = "#"
                elif 28 <= x <= 29: char = "%"
                elif x == 30: char = "="
                elif x == 31: char = "#"
                elif x == 32: char = "+"
                elif 33 <= x <= 38: char = "-"
                elif 39 <= x <= 42: char = "="
                elif 43 <= x <= 48: char = "-"
                elif 49 <= x <= 51: char = "="
                elif x == 52: char = "-"
                elif x == 53: char = "+"
                elif x == 54: char = "*"
                else: char = "."
            else:
                char = "."

        elif y == 22:
            # Row 23: ........:*%%#*%%%%###***#%%==#+-------======---===-=*...............
            if 8 <= x <= 52:
                if x == 8: char = ":"
                elif x == 9: char = "*"
                elif 10 <= x <= 11: char = "%"
                elif x == 12: char = "#"
                elif x == 13: char = "*"
                elif 14 <= x <= 17: char = "%"
                elif 18 <= x <= 20: char = "#"
                elif 21 <= x <= 23: char = "*"
                elif 24 <= x <= 26: char = "#"
                elif 27 <= x <= 28: char = "%"
                elif 29 <= x <= 30: char = "="
                elif x == 31: char = "#"
                elif x == 32: char = "+"
                elif 33 <= x <= 39: char = "-"
                elif 40 <= x <= 45: char = "="
                elif 46 <= x <= 48: char = "-"
                elif 49 <= x <= 51: char = "="
                elif x == 52: char = "-"
                elif x == 53: char = "="
                elif x == 54: char = "*"
            else:
                char = "."

        elif y == 23:
            # Row 24: .........=#%%##%%%%######%%==#+---==============+==+:...............
            if 9 <= x <= 52:
                if x == 9: char = "="
                elif x == 10: char = "#"
                elif 11 <= x <= 12: char = "%"
                elif 13 <= x <= 14: char = "#"
                elif 15 <= x <= 18: char = "%"
                elif 19 <= x <= 24: char = "#"
                elif 25 <= x <= 26: char = "%"
                elif 27 <= x <= 28: char = "="
                elif x == 29: char = "#"
                elif x == 30: char = "+"
                elif 31 <= x <= 33: char = "-"
                elif 34 <= x <= 47: char = "="
                elif x == 48: char = "+"
                elif 49 <= x <= 50: char = "="
                elif x == 51: char = "+"
                elif x == 52: char = ":"
            else:
                char = "."

        elif y == 24:
            # Row 25: .........:+#%##%%%%%####%%=#%#+---==============+=-:................
            if 9 <= x <= 52:
                if x == 9: char = ":"
                elif x == 10: char = "+"
                elif x == 11: char = "#"
                elif x == 12: char = "%"
                elif 13 <= x <= 14: char = "#"
                elif 15 <= x <= 19: char = "%"
                elif 20 <= x <= 23: char = "#"
                elif 24 <= x <= 25: char = "%"
                elif x == 26: char = "="
                elif x == 27: char = "#"
                elif x == 28: char = "%"
                elif x == 29: char = "#"
                elif x == 30: char = "+"
                elif 31 <= x <= 33: char = "-"
                elif 34 <= x <= 47: char = "="
                elif x == 48: char = "+"
                elif x == 49: char = "="
                elif x == 50: char = "-"
                elif x == 51: char = ":"
            else:
                char = "."

        elif y == 25:
            # Row 26: ...........-+**#%%%%%%%%===@@%*+=+**+-==========+-..................
            if 11 <= x <= 50:
                if x == 11: char = "-"
                elif x == 12: char = "+"
                elif 13 <= x <= 14: char = "*"
                elif x == 15: char = "#"
                elif 16 <= x <= 23: char = "%"
                elif 24 <= x <= 26: char = "="
                elif 27 <= x <= 28: char = "@" # High-density shadow
                elif x == 29: char = "%"
                elif x == 30: char = "*"
                elif x == 31: char = "+"
                elif x == 32: char = "="
                elif x == 33: char = "+"
                elif 34 <= x <= 36: char = "*"
                elif x == 37: char = "+"
                elif x == 38: char = "-"
                elif 39 <= x <= 48: char = "="
                elif x == 49: char = "+"
                elif x == 50: char = "-"
            else:
                char = "."

        elif y == 26:
            # Row 27: .............:*#%%%%%%%%%%%%@@%*====--===========:..................
            if 13 <= x <= 50:
                if x == 13: char = ":"
                elif x == 14: char = "*"
                elif x == 15: char = "#"
                elif 16 <= x <= 27: char = "%"
                elif 28 <= x <= 29: char = "@" # Core chin shadow
                elif x == 30: char = "%"
                elif x == 31: char = "*"
                elif 32 <= x <= 35: char = "="
                elif 36 <= x <= 37: char = "-"
                elif 38 <= x <= 48: char = "="
                elif 49 <= x <= 50: char = ":"
            else:
                char = "."

        elif y == 27:
            # Row 28: ..............*#%%%%%%%%%%%%%#***+==============+:..................
            if 14 <= x <= 50:
                if x == 14: char = "*"
                elif x == 15: char = "#"
                elif 16 <= x <= 28: char = "%"
                elif x == 29: char = "#"
                elif 30 <= x <= 32: char = "*"
                elif x == 33: char = "+"
                elif 34 <= x <= 47: char = "="
                elif x == 48: char = "+"
                elif x == 49: char = ":"
                elif x == 50: char = "."
            else:
                char = "."


        elif y == 28:
            # Row 29: ...............#%%%%%%%%%%%%%#++*===============+:..................
            if 15 <= x <= 50:
                if x == 15: char = "#"
                elif 16 <= x <= 28: char = "%"
                elif x == 29: char = "#"
                elif 30 <= x <= 31: char = "+"
                elif x == 32: char = "*"
                elif 33 <= x <= 47: char = "="
                elif x == 48: char = "+"
                elif x == 49: char = ":"
                elif x == 50: char = "."
            else:
                char = "."

        elif y == 29:
            # Row 30: ..............=#%%%%%%%''..,,,#+****+++=========....................
            if 14 <= x <= 47:
                if x == 14: char = "="
                elif x == 15: char = "#"
                elif 16 <= x <= 22: char = "%"
                elif 23 <= x <= 24: char = "'"
                elif 25 <= x <= 26: char = "."
                elif 27 <= x <= 29: char = ","
                elif x == 30: char = "#"
                elif x == 31: char = "+"
                elif 32 <= x <= 35: char = "*"
                elif 36 <= x <= 38: char = "+"
                elif 39 <= x <= 47: char = "="
            else:
                char = "."

        elif y == 30:
            # Row 31: ...............*%%%%%%%%%@@%%%#*+======++======+:...................
            if 15 <= x <= 48:
                if x == 15: char = "*"
                elif 16 <= x <= 24: char = "%"
                elif 25 <= x <= 26: char = "@" # Deep shadow under chin
                elif 27 <= x <= 29: char = "%"
                elif x == 30: char = "#"
                elif x == 31: char = "*"
                elif x == 32: char = "+"
                elif 33 <= x <= 38: char = "="
                elif 39 <= x <= 40: char = "+"
                elif 41 <= x <= 46: char = "="
                elif x == 47: char = "+"
                elif x == 48: char = ":"
            else:
                char = "."

        elif y == 31:
            # Row 32: ...............:#%%%%%%%%%%%%#*++=======+====+++:...................
            if 15 <= x <= 48:
                if x == 15: char = ":"
                elif x == 16: char = "#"
                elif 17 <= x <= 28: char = "%"
                elif x == 29: char = "#"
                elif x == 30: char = "*"
                elif 31 <= x <= 32: char = "+"
                elif 33 <= x <= 39: char = "="
                elif x == 40: char = "+"
                elif 41 <= x <= 44: char = "="
                elif 45 <= x <= 47: char = "+"
                elif x == 48: char = ":"
            else:
                char = "."

        elif y == 32:
            # Row 33: ................*%%%%%%%%%%%%%%%##*+======++++==-:..................
            if 16 <= x <= 49:
                if x == 16: char = "*"
                elif 17 <= x <= 31: char = "%"
                elif 32 <= x <= 33: char = "#"
                elif x == 34: char = "*"
                elif x == 35: char = "+"
                elif 36 <= x <= 41: char = "="
                elif 42 <= x <= 45: char = "+"
                elif 46 <= x <= 47: char = "="
                elif x == 48: char = "-"
                elif x == 49: char = ":"
            else:
                char = "."

        elif y == 33:
            # Row 34: ................=%%%%%%%%%%%%#**+==-======+++===++##=:..............
            if 16 <= x <= 53:
                if x == 16: char = "="
                elif 17 <= x <= 28: char = "%"
                elif x == 29: char = "#"
                elif 30 <= x <= 31: char = "*"
                elif x == 32: char = "+"
                elif 33 <= x <= 34: char = "="
                elif x == 35: char = "-"
                elif 36 <= x <= 41: char = "="
                elif 42 <= x <= 44: char = "+"
                elif 45 <= x <= 47: char = "="
                elif 48 <= x <= 49: char = "+"
                elif 50 <= x <= 51: char = "#"
                elif x == 52: char = "="
                elif x == 53: char = ":"
            else:
                char = "."

        elif y == 34:
            # Row 35: ................:'''%%%%%%%%##**+++=====++++=====+++#+==-:..........
            if 16 <= x <= 57:
                if x == 16: char = ":"
                elif 17 <= x <= 19: char = "'"
                elif 20 <= x <= 27: char = "%"
                elif 28 <= x <= 29: char = "#"
                elif 30 <= x <= 31: char = "*"
                elif 32 <= x <= 34: char = "+"
                elif 35 <= x <= 39: char = "="
                elif 40 <= x <= 43: char = "+"
                elif 44 <= x <= 48: char = "="
                elif 49 <= x <= 51: char = "+"
                elif x == 52: char = "#"
                elif x == 53: char = "+"
                elif 54 <= x <= 55: char = "="
                elif x == 56: char = "-"
                elif x == 57: char = ":"
            else:
                char = "."

        elif y == 35:
            # Row 36: ..............-#%%%%%@%%%%%%%#***#%%%+++++==========+#====--:.......
            if 14 <= x <= 60:
                if x == 14: char = "-"
                elif x == 15: char = "#"
                elif 16 <= x <= 20: char = "%"
                elif x == 21: char = "@" # Deep muscle crease
                elif 22 <= x <= 28: char = "%"
                elif x == 29: char = "#"
                elif 30 <= x <= 32: char = "*"
                elif x == 33: char = "#"
                elif 34 <= x <= 36: char = "%"
                elif 37 <= x <= 41: char = "+"
                elif 42 <= x <= 51: char = "="
                elif x == 52: char = "+"
                elif x == 53: char = "#"
                elif 54 <= x <= 57: char = "="
                elif 58 <= x <= 59: char = "-"
                elif x == 60: char = ":"
            else:
                char = "."

        elif y == 36:
            # Row 37: ..........:-*#%%%%%%%..%%%%%%%%%%%%%##*+=++==========*+=++=------:..
            if 10 <= x <= 65:
                if 10 <= x <= 11: char = ":"
                elif x == 12: char = "-"
                elif x == 13: char = "*"
                elif x == 14: char = "#"
                elif 15 <= x <= 21: char = "%"
                elif 22 <= x <= 23: char = "."  # Negative space highlight
                elif 24 <= x <= 36: char = "%"
                elif 37 <= x <= 38: char = "#"
                elif x == 39: char = "*"
                elif x == 40: char = "+"
                elif x == 41: char = "="
                elif x == 42: char = "+"
                elif x == 43: char = "+"
                elif 44 <= x <= 53: char = "="
                elif x == 54: char = "*"
                elif x == 55: char = "+"
                elif x == 56: char = "="
                elif x == 57: char = "+"
                elif x == 58: char = "+"
                elif x == 59: char = "="
                elif 60 <= x <= 65: char = "-"
            elif 66 <= x <= 67:
                char = "."
            else:
                char = "."

        elif y == 37:
            # Row 38: ......:-+*##%%%@%%%%%%%%%%%;;;;%%#*++===+++==========*++++++====----
            if 6 <= x <= 67:
                if 6 <= x <= 7: char = ":"
                elif x == 8: char = "-"
                elif x == 9: char = "+"
                elif x == 10: char = "*"
                elif 11 <= x <= 12: char = "#"
                elif 13 <= x <= 15: char = "%"
                elif x == 16: char = "@" # Crease shadow
                elif 17 <= x <= 27: char = "%"
                elif 28 <= x <= 31: char = ";" # Semicolon mid-tone transition
                elif 32 <= x <= 33: char = "%"
                elif x == 34: char = "#"
                elif x == 35: char = "*"
                elif 36 <= x <= 37: char = "+"
                elif 38 <= x <= 40: char = "="
                elif 41 <= x <= 43: char = "+"
                elif 44 <= x <= 53: char = "="
                elif x == 54: char = "*"
                elif 55 <= x <= 60: char = "+"
                elif 61 <= x <= 64: char = "="
                elif 65 <= x <= 68: char = "-"
            else:
                char = "."

        elif y == 38:
            # Row 39: ..:=**###%%%%%%@%%%%%%%%%%%%%%%%%#*++===++++=========*++++++++======
            if 2 <= x <= 67:
                if 2 <= x <= 3: char = "."
                elif x == 4: char = ":"
                elif x == 5: char = "="
                elif 6 <= x <= 7: char = "*"
                elif 8 <= x <= 10: char = "#"
                elif 11 <= x <= 16: char = "%"
                elif x == 17: char = "@" # Chest depth shadow
                elif 18 <= x <= 34: char = "%"
                elif x == 35: char = "#"
                elif x == 36: char = "*"
                elif 37 <= x <= 38: char = "+"
                elif 39 <= x <= 41: char = "="
                elif 42 <= x <= 45: char = "+"
                elif 46 <= x <= 54: char = "="
                elif x == 55: char = "*"
                elif 56 <= x <= 63: char = "+"
                elif 64 <= x <= 69: char = "="
            else:
                char = "."

        elif y == 39:
            # Row 40: **##%%%%%%%%%@%%@%%%%@@%%%%%%%###**+++++++++========**+++++++++++*++
            if 0 <= x <= 67:
                if 0 <= x <= 1: char = "*"
                elif 2 <= x <= 3: char = "#"
                elif 4 <= x <= 12: char = "%"
                elif x == 13: char = "@"
                elif 14 <= x <= 15: char = "%"
                elif x == 16: char = "@"
                elif 17 <= x <= 20: char = "%"
                elif 21 <= x <= 22: char = "@"
                elif 23 <= x <= 29: char = "%"
                elif 30 <= x <= 32: char = "#"
                elif 33 <= x <= 34: char = "*"
                elif 35 <= x <= 43: char = "+"
                elif 44 <= x <= 51: char = "="
                elif 52 <= x <= 53: char = "*"
                elif 54 <= x <= 64: char = "+"
                elif x == 65: char = "*"
                else: char = "+"
            else:
                char = " "

        elif y == 40:
            # Row 41: #%%%%%%%%%%%%@@@@@@%%%@@@@%%%%%%#***+++++++++======+++++==+++==+++++
            if 0 <= x <= 67:
                if x == 0: char = "#"
                elif 1 <= x <= 12: char = "%"
                elif 13 <= x <= 18: char = "@" # Pectoral shadow core
                elif 19 <= x <= 21: char = "%"
                elif 22 <= x <= 25: char = "@"
                elif 26 <= x <= 31: char = "%"
                elif x == 32: char = "#"
                elif 33 <= x <= 35: char = "*"
                elif 36 <= x <= 44: char = "+"
                elif 45 <= x <= 50: char = "="
                elif 51 <= x <= 55: char = "+"
                elif 56 <= x <= 57: char = "="
                elif 58 <= x <= 60: char = "+"
                elif 61 <= x <= 62: char = "="
                else: char = "+"
            else:
                char = " "

        elif y == 41:
            # Row 42: %%%%%%%%%%%%%%@@@@@@%%%%%%%%%%%%##*++++++++++++++=+++++====+==++++*+
            if 0 <= x <= 67:
                if 0 <= x <= 13: char = "%"
                elif 14 <= x <= 19: char = "@"
                elif 20 <= x <= 31: char = "%"
                elif 32 <= x <= 33: char = "#"
                elif x == 34: char = "*"
                elif 35 <= x <= 48: char = "+"
                elif x == 49: char = "="
                elif 50 <= x <= 54: char = "+"
                elif 55 <= x <= 58: char = "="
                elif x == 59: char = "+"
                elif 60 <= x <= 61: char = "="
                elif 62 <= x <= 65: char = "+"
                elif x == 66: char = "*"
                else: char = "+"
            else:
                char = " "

        elif y == 42:
            # Row 43: %%%%%%%%%%%%%%@@@@@@@%%%%%%%%%%%%##******+++++++=+*++++++==+++++**+=
            if 0 <= x <= 67:
                if 0 <= x <= 13: char = "%"
                elif 14 <= x <= 20: char = "@"
                elif 21 <= x <= 32: char = "%"
                elif 33 <= x <= 34: char = "#"
                elif 35 <= x <= 40: char = "*"
                elif 41 <= x <= 47: char = "+"
                elif x == 48: char = "="
                elif x == 49: char = "+"
                elif x == 50: char = "*"
                elif 51 <= x <= 56: char = "+"
                elif 57 <= x <= 58: char = "="
                elif 59 <= x <= 63: char = "+"
                elif 64 <= x <= 65: char = "*"
                elif x == 66: char = "+"
                elif x == 67: char = "="
            else:
                char = " "

        elif y == 43:
            if x <= 13:
                char = "%"
            elif x <= 22:
                char = "@"
            elif x <= 34:
                char = "%"
            elif x <= 41:
                char = "#"
            elif x <= 47:
                char = "*"
            elif x <= 54:
                char = "+"
            elif x <= 64:
                char = "*"
            else:
                char = "="

        elif y == 44:
            if x <= 18:
                char = "%"
            elif x <= 23:
                char = "@"
            elif x <= 36:
                char = "%"
            elif x <= 44:
                char = "#"
            elif x <= 50:
                char = "*"
            elif x <= 58:
                char = "+"
            elif x <= 64:
                char = "#"
            else:
                char = "="

        else:
            char = " "

        line += char
    print(line)
