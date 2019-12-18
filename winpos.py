
import win32gui
from time import sleep
import argparse
import win32process
import psutil

hwnd_list = []

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    winname = win32gui.GetWindowText(hwnd)
    isvisible = win32gui.IsWindowVisible(hwnd)
    isenabled = win32gui.IsWindowEnabled(hwnd)
    placement = win32gui.GetWindowPlacement(hwnd)
    iswindow = win32gui.IsWindow(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y

    if isvisible and isenabled and w != 0 and h != 0 and winname != '':
        win = [hwnd, winname, x, y, w, h,isvisible, isenabled,placement,iswindow]
        #print(win)
        hwnd_list.append(win)

def print_window_info(win):
    #print('Handle: {0} '.format(win[0]) + 'Name: {0} '.format(win[1]) + 'Location: ({0}, {1}) '.format(win[2], win[3]) + 'Size: ({0}, {1})'.format(win[4], win[5]))
    print('{0}, '.format(win[0]) + '{0}, '.format(win[1]) + 'Location: ({0}, {1}), '.format(win[2], win[3]) + 'Size: ({0}, {1})'.format(win[4], win[5]))

def main():
    parser = argparse.ArgumentParser(description='Manages your windows positions')
    parser.add_argument('--list', action='store_true', help='Lists the visible windows')
    parser.add_argument('--blink', metavar='N', type=int, action='store', nargs = 1, help='Blinks one window from the list')
    parser.add_argument('--save', metavar='N', type=int, action='store', nargs='+', help='Saves the position of a list of windows')
    parser.add_argument('--restore', action='store_true', help='Restores the position of the saved windows')
    args = parser.parse_args()
    print(args)
    
    win32gui.EnumWindows(callback, None)
    sleep(1)
    if(args.list):
        idx = 0
        for win in hwnd_list:
            proc_id = win32process.GetWindowThreadProcessId(win[0])
            for p in psutil.process_iter():
                if(p.pid == proc_id[1]):
                    if p.status() == psutil.STATUS_RUNNING:
                        print('{0} - {1}'.format(idx, win[1]))
            idx = idx + 1


    elif(args.blink != None):
        win = hwnd_list[args.blink[0]]
        print_window_info(win)
        win32gui.FlashWindow(win[0],1)

    
if __name__ == '__main__':
    main()
