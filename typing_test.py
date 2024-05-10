import curses, time, datetime, random


def draw(screen):
    """ 
    canvas1 = curses.newwin(int(curses.LINES/2), int(curses.COLS/2),                   0,                  0)
    canvas2 = curses.newwin(int(curses.LINES/2), int(curses.COLS/2),                   0, int(curses.COLS/2))
    canvas3 = curses.newwin(int(curses.LINES/2), int(curses.COLS/2), int(curses.LINES/2),                  0)
    canvas4 = curses.newwin(int(curses.LINES/2), int(curses.COLS/2), int(curses.LINES/2), int(curses.COLS/2))

    canvas1.bkgd(' ', curses.color_pair(1))
    canvas2.bkgd(' ', curses.color_pair(2))
    canvas3.bkgd(' ', curses.color_pair(3))
    canvas4.bkgd(' ', curses.color_pair(4))

    height, width = stdscr.getmaxyx()
    if k == curses.KEY_DOWN:
        cursor_y = cursor_y + 1
        cchar = 'v'
    elif k == curses.KEY_UP:
        cursor_y = cursor_y - 1
        cchar = "^"
    elif k == curses.KEY_RIGHT:
        cursor_x = cursor_x + 1
        cchar = ">"
    elif k == curses.KEY_LEFT:
        cursor_x = cursor_x - 1
        cchar = "<"
       
    cursor_x = max(0, cursor_x)
    cursor_x = min(width-1, cursor_x)
    cursor_y = max(0, cursor_y)
    cursor_y = min(height-1, cursor_y)

    menu = [("Start", ),
            ("Settings", ),
            ("Quit", )
    ]
    text = datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S") 
    """
    with open("../../vocabulary.txt", 'r') as file:
        words = [line.rstrip() for line in file.readlines()]

    with open("../../top_results.txt", 'r') as file:
        results = []
        for line in file.readlines():
            res_t = line.rstrip().split()
            results.append((int(res_t[0]), float(res_t[1])))

    # words = [word for word in words if not ('d' in word)]

    word_count = 60
    string = ''.join([random.choice(words)+'\n' if i % 6 == 0 else random.choice(words)+' ' for i in range(1, word_count+1)])[:-1]

    curses.noecho()
    curses.cbreak()
    curses.curs_set(True)

    curses.start_color()
    curses.use_default_colors()
    for i in range(255):
        curses.init_pair(i + 1, i, -1)
    curses.init_pair(1, 7, 0)
    curses.init_pair(2, 2, 0)
    curses.init_pair(3, 0, 7)

    screen = curses.initscr()
    screen.keypad(True)
    screen.clear()
    screen.refresh()
    screen.border()
    screen.bkgd(' ', curses.color_pair(1))
    max_y, max_x = screen.getmaxyx()

    head_scr = curses.newwin(1, max_x, 0, 0)
    head_scr.bkgd(' ', curses.color_pair(3))
    head_scr.addstr(0, 1, f"Typing Speed Test")
    head_text = datetime.datetime.now().strftime("%d.%m.%Y")
    head_scr.addstr(0, max_x-len(head_text)-1, head_text)
    screen.refresh()
    head_scr.refresh()

    main_scr = curses.newwin(max_y-2, int(2*(max_x-2)/3), 1, 1)
    main_scr_offset = 1
    main_scr.keypad(True)
    main_scr.nodelay(False)
    main_scr.bkgd(' ')
    screen.refresh()
    main_scr.refresh()

    side_pan = curses.newwin(max_y-2, int(1*(max_x-2)/3)+1, 1, int(2*(max_x-2)/3)+1)
    side_pan_offset = 1
    side_pan.bkgd(' ')
    side_pan.border()
    s_y, s_x = side_pan.getmaxyx()
    side_pan.addstr(0, 0+int(s_x/2)-int(len("Top results:")/2), "Top results:")
    results.sort(reverse=True)
    for i, res in enumerate(results, start=1):
        if   i == 1: side_pan.addstr(i+side_pan_offset, 1+side_pan_offset,   f"{i}.\t| {res[0]:=3} | {res[1]:=6.02f} |", curses.color_pair(227) | curses.A_REVERSE)
        elif i == 2: side_pan.addstr(i+side_pan_offset, 1+side_pan_offset,   f"{i}.\t| {res[0]:=3} | {res[1]:=6.02f} |", curses.color_pair(232) | curses.A_REVERSE)
        elif i == 3: side_pan.addstr(i+side_pan_offset, 1+side_pan_offset,   f"{i}.\t| {res[0]:=3} | {res[1]:=6.02f} |", curses.color_pair(209) | curses.A_REVERSE)
        else:        side_pan.addstr(i+side_pan_offset, 1+side_pan_offset,   f"{i}.\t| {res[0]:=3} | {res[1]:=6.02f} |")
    screen.refresh()
    side_pan.refresh()    
    
    foot_scr = curses.newwin(1, max_x, max_y-1, 0)
    foot_scr.bkgd(' ', curses.color_pair(3))
    anim_dir = 1
    anim_count = 0
    anim_char = "^_^"
    foot_scr.addstr(0, 0, anim_char)

    screen.refresh()
    foot_scr.refresh()

    for i, line in enumerate(string.split('\n')):
        main_scr.addstr(i+main_scr_offset, 0+main_scr_offset, line)  

    screen.refresh()
    main_scr.refresh()
    main_scr.move(0+main_scr_offset, 0+main_scr_offset)

    key = 0
    curr_y = 0
    curr_x = 0
    text = string.split('\n')
    total_char = sum([len(line) for line in text])
    total_words = sum([len(line.split()) for line in text])
    screen_buffer = [[-1]*(len(line)) for line in text ]
    
    main_scr.addstr(len(text)+1+main_scr_offset, 0+main_scr_offset, "Press enter to start or esc to quit...")
    screen.refresh()
    main_scr.refresh()
    while True:
        key = main_scr.getch()
        if key == 27:
            exit()
        if key == 10:
            break

    main_scr.addstr(len(text)+1+main_scr_offset, 0+main_scr_offset, "                                      ")
   
    flag = 0
    start = time.time()
    while (key != 27):   
        if key > 0 and key not in (8, 9, 10): 
            if chr(key) == text[curr_y][curr_x]:
                main_scr.addch(curr_y+main_scr_offset, curr_x+main_scr_offset, chr(key), curses.color_pair(2))
                screen_buffer[curr_y][curr_x] = 1
            else:
                main_scr.addch(curr_y+main_scr_offset, curr_x+main_scr_offset, chr(key), curses.color_pair(3))
                screen_buffer[curr_y][curr_x] = 0
            if curr_y == len(text)-1 and curr_x == len(text[curr_y])-1:
                flag = 1
                break
            if (anim_count == max_x-len(anim_char)-1 and anim_dir == 1) or (anim_count == 0 and anim_dir == -1):
                anim_dir = -anim_dir
            
            anim_count += anim_dir
            foot_scr.clear()
            foot_scr.addstr(0, anim_count, anim_char)
            
            curr_x += 1
            if curr_x == len(text[curr_y]):
                curr_y += 1
                curr_x = 0
        
        if key == 8: 
            if curr_x == 0:
                curr_y -= 1
                if curr_y < 0:
                    curr_y = 0
                else:
                    curr_x = len(text[curr_y])
            curr_x -= 1
            if curr_x < 0:
                curr_x = 0   
            main_scr.addch(curr_y+main_scr_offset, curr_x+main_scr_offset, text[curr_y][curr_x], curses.color_pair(1))
            screen_buffer[curr_y][curr_x] = -1

        main_scr.move(curr_y+main_scr_offset, curr_x+main_scr_offset)
        screen.refresh()
        main_scr.refresh()
        foot_scr.refresh()
        key = main_scr.getch()

    end = time.time()
    user_time = end - start
    correct_chars = sum([sum(line) for line in screen_buffer])
    user_accuracy = correct_chars / total_char * 100
    user_wpm = total_words / user_time * 60
    user_cps = total_char / user_time

    if flag: 
        main_scr.addstr(22+main_scr_offset, 0+main_scr_offset, f"words per minute -> {round(user_wpm)}")
        main_scr.addstr(23+main_scr_offset, 0+main_scr_offset, f"chars per second -> {round(user_cps)}")
        main_scr.addstr(24+main_scr_offset, 0+main_scr_offset, f"time elapsed     -> {user_time:.2f}s")
        main_scr.addstr(25+main_scr_offset, 0+main_scr_offset, f"accuracy         -> {user_accuracy:.2f}")
    screen.refresh()
    main_scr.refresh()

    if res[1] > 60:
        results.append((round(user_wpm), user_accuracy))
        results = sorted(results, reverse=True)[:20]
        for i, res in enumerate(results, start=1):
            if   i == 1: side_pan.addstr(i+side_pan_offset, 1+side_pan_offset,   f"{i}.\t| {res[0]:=3} | {res[1]:=6.02f} |", curses.color_pair(227) | curses.A_REVERSE)
            elif i == 2: side_pan.addstr(i+side_pan_offset, 1+side_pan_offset,   f"{i}.\t| {res[0]:=3} | {res[1]:=6.02f} |", curses.color_pair(232) | curses.A_REVERSE)
            elif i == 3: side_pan.addstr(i+side_pan_offset, 1+side_pan_offset,   f"{i}.\t| {res[0]:=3} | {res[1]:=6.02f} |", curses.color_pair(209) | curses.A_REVERSE)
            else:        side_pan.addstr(i+side_pan_offset, 1+side_pan_offset,   f"{i}.\t| {res[0]:=3} | {res[1]:=6.02f} |")
        screen.refresh()
        side_pan.refresh()

        with open("../../top_results.txt", 'w') as file:
            for res in results:
                file.write(f"{res[0]} {res[1]:.2f}\n")

    curses.curs_set(False) 
    foot_scr.clear()
    foot_scr.addstr(0, anim_count, "x_x" if user_accuracy < 50.0 else "0_o")
    screen.refresh()
    foot_scr.refresh()

    screen_animate = []
    max_line = max((len(line), i) for i, line in enumerate(screen_buffer))
    for i, y in enumerate(screen_buffer):
        for j, _ in enumerate(range(0, max_line[0])):
            screen_animate.append((i, j))

    for _ in range(len(screen_animate)):
        y, x = screen_animate.pop(random.randint(0, len(screen_animate)-1))
        main_scr.addch(y+main_scr_offset, x+main_scr_offset, random.choice(r"!$%^&*()_+`[];',./#-}{:@<>?"), curses.color_pair(random.randint(4, 256)))
        main_scr.refresh()
        curses.napms(5 )

    screen.refresh()
    main_scr.refresh()
    
    while main_scr.getch() != 27:
        pass

def main():
    curses.wrapper(draw)

if __name__ == "__main__":
    main()