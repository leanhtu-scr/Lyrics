import time
import sys
from colorama import Fore, Style, init

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
    print()

def display_lyrics_timed():
    # Đây là nơi bạn sẽ nhập các mốc thời gian chính xác
    # (thời gian tính bằng giây từ đầu bài hát)
    lyrics_with_timestamps = [
        (0.00, "Tình yêu anh như nắng đợi", Fore.CYAN),
        (2.20, "Tìm về nhau giữa chân mây", Fore.CYAN),
        (4.40, "Dặn lòng không thể lấp đầy", Fore.CYAN),
        (6.60, "Em đi vội chẳng giữ lấy", Fore.CYAN),
        (9.50, "Phải chi anh là kẻ tồi, rời bỏ đi lúc yêu thôi", Fore.YELLOW),
        (11.0, "Thì đôi môi đâu thấy", Fore.YELLOW),
        (14.50, "Con tim đơn côi dối lòng chẳng buông.", Fore.YELLOW),
        (17.00, "Trả lại em những nỗi buồn", Fore.RED),
        (19.60, "Trả lại những niềm đau", Fore.RED),
        (22.10, "Cả những vết thương sâu", Fore.RED),
        (24.00, "Thêm bao lâu thì người sẽ thấu", Fore.RED),
        (26.70, "Trả lại em những ước nguyện", Fore.BLUE),
        (28.10, "Trả em lúc bình yên", Fore.BLUE),
        (29.85, "Cả giây phút thiêng liêng, Bên hiên ôm nắng chiều khẽ rơi", Fore.BLUE)
    ]

    print("Chuẩn bị hiển thị lyrics... Hãy bật nhạc lên!")
    input("\nNhấn Enter để bắt đầu đồng bộ...")

    start_time = time.time() # Ghi lại thời điểm bắt đầu
    
    for i, (timestamp, line, color) in enumerate(lyrics_with_timestamps):
        current_elapsed_time = time.time() - start_time
        
        # Đợi cho đến khi đủ thời gian để hiển thị dòng tiếp theo
        if current_elapsed_time < timestamp:
            time.sleep(timestamp - current_elapsed_time)
            
        typewriter_effect(line, delay=0.035, color=color)

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Hiển thị lời bài hát Nắng Dưới Chân Mây (đã đồng bộ thời gian)")
        print("2. Thoát")
        
        choice = input("Lựa chọn của bạn: ")

        if choice == "1":
            display_lyrics_timed()
        elif choice == "2":
            print(Fore.CYAN + "Tạm biệt!" + Style.RESET_ALL)
            typewriter_effect("Cảm ơn bạn đã sử dụng", delay=0.08)
            break
        else:
            print(Fore.RED + "Lựa chọn không hợp lệ!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
