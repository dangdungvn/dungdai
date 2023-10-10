def find_duplicate_substring(large_string):
    window_start = 0
    window_end = 0
    char_count = {}
    max_length = 0
    max_length_start = 0

    while window_end < len(large_string):
        current_char = large_string[window_end]

        if current_char in char_count:
            if char_count[current_char] >= window_start:
                window_start = char_count[current_char] + 1

        char_count[current_char] = window_end

        if window_end - window_start + 1 > max_length:
            max_length = window_end - window_start + 1
            max_length_start = window_start

        window_end += 1

    if max_length > 1:
        return large_string[max_length_start:max_length_start+max_length]
    else:
        return None


chuoi = input("Nhập vào bản rõ: ")
d = int(input("Bạn muốn giải thuật hay tìm khóa, ấn 1 hoặc 2: "))
if d == 1:
    chuoimh = ""
    chuoigm = ""
    khoa = input("Nhập vào key: ")
    m = len(khoa)
    for i in range(len(chuoi)):
        ktmh = chuoi[i]
        k = khoa[i % m]
        if chuoi[i] == ' ':
            ktmh = ' '
        else:
            if ktmh.isalpha():
                if ktmh.isupper():
                    chu = ord('A')
                else:
                    chu = ord('a')
                ktmh = chr((ord(ktmh) - chu + ord(k) - chu) % 26 + chu)
        chuoimh += ktmh
    print("Bản mã khi đã được mã hóa: ", chuoimh)
    for i in range(len(chuoimh)):
        ktgm = chuoimh[i]
        k = khoa[i % m]
        if chuoimh[i] == ' ':
            ktgm = ' '
        else:
            if ktgm.isalpha():
                if ktgm.isupper():
                    chu = ord('A')
                else:
                    chu = ord('a')
                ktgm = chr((ord(ktgm) - chu - ord(k) + chu) % 26 + chu)
        chuoigm += ktgm
    print("Bản rõ sau khi được giải mã: ", chuoigm)
else:
    khoa = ""
    chu = 0
    chuoimh = input("Nhập vào bản mã: ")
    chuoisua = chuoi.replace(' ', '')
    for i in range(len(chuoimh)):
        ktgm = chuoimh[i]
        ktmh = chuoisua[i]
        if ktgm.isalpha():
            if ktgm.isupper():
                chu = ord('A')
            else:
                chu = ord('a')
        ktkey = chr((ord(ktgm) - ord(ktmh) + chu) % 26 + chu)
        khoa += ktkey
    print("Key của chuỗi là: ", khoa)
    input_large_string = khoa
    result = find_duplicate_substring(input_large_string)
    if result:
        print("Chuỗi ký tự bị lặp: ", result)
    else:
        print("Không có chuỗi ký tự nào bị lặp trong chuỗi lớn.")
