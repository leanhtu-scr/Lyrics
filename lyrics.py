import time
import sys
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored output
init()

def typewriter_effect(text, delay=0.05, color=None):
    if color:
        sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write(Style.RESET_ALL)
    print() # New line after each sentence

def display_lyrics():
    lyrics = [
        ("Tình yêu anh như nắng đời", Fore.CYAN),
        ("Tìm về nhau giữa chân mây", Fore.CYAN),
        ("Dặn lòng không thể lấp đầy", Fore.CYAN),
        ("Em đi vội chẳng giữ lấy", Fore.CYAN),
        ("Phải chi anh là kẻ tồi, rời bỏ đi lúc yêu thôi", Fore.YELLOW),
        ("Thì lòng mới đau thấy", Fore.YELLOW),
        ("Con tim đang cối rối lòng chẳng buông.", Fore.YELLOW),
        ("Trả lại em những nỗi buồn", Fore.RED),
        ("Trả lại những niềm đau", Fore.RED),
        ("Cả những vết thương sâu", Fore.RED),
        ("Em bao lâu từng người sẽ thấu", Fore.RED),
        ("Trả lại em những ân tình", Fore.BLUE),
        ("Trả em lúc bình yên", Fore.BLUE),
        ("Thở dài dự tiếng yêu em bên em nắm trọn thế gian.", Fore.BLUE)
    ]

    print("Số dòng lyrics:", len(lyrics))
    print("Thời gian hiển thị: 2.0 giây")
    print("Thời gian ngắt quãng: 2.0 giây")
    input("\nNhấn Enter để bắt đầu hiển thị lyrics...")

    for i, (line, color) in enumerate(lyrics):
        typewriter_effect(line, delay=0.05, color=color)
        if i < len(lyrics) - 1:
            time.sleep(2) # Pause between lines

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Hiển thị lời bài hát Nắng Dưới Chân Mây")
        print("2. Thoát")
        
        choice = input("Lựa chọn của bạn: ")

        if choice == "1":
            display_lyrics()
        elif choice == "2":
            print(Fore.CYAN + "Tạm biệt! Fore.Cyan, Style.RESET_ALL")
            print(Fore.MAGENTA + "Hiệu ứng fade out cho lời tạm biệt" + Style.RESET_ALL)
            typewriter_effect("Cảm ơn bạn đã sử dụng", delay=0.08)
            break
        else:
            print(Fore.RED + "Lựa chọn không hợp lệ!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
