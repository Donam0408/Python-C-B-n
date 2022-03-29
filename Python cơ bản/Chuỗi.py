def main():
    int_1 = 10
    str1 = "NamVipPro"
 # Để xem vị trí của một kí tự trong bảng mã Unicode, ta sử dụng hàm ord()
    VitriChar = ord("a")
 # Lấy kí trong chuỗi str1 <chuỗi>[vị trí bắt đầu : vị trí dừng]
    str2 = str1[None:None]
 # Lấy kí trong chuỗi str1 <chuỗi>[vị trí bắt đầu : vị trí dừng : bước] (Bước nhảy<0 : lấy chuỗi từ phải sang trái với bước nhảy bước nhảy)
    str3 = str1[None:None:-1]
 # Định dạng bằng toán tử %
 # Cú pháp: <chuỗi> % (giá trị thứ 1, giá trị thứ 2, .., giá trị thứ n – 1, giá trị thứ n)
    str4 = "%d. That is %s problem " 
    str5 = "Điểm thi học kì: %.2f " 


 # Table using Format
    # phần định dạng
    row_1 = '+ {:-^6} + {:-^15} + {:-^10} +'.format('', '', '')
    row_2 = '| {:<6} | {:^15} | {:^10} |'.format('ID', 'Ho va ten', 'Noi sinh')
    row_3 = '| {:<6} | {:^15} | {:^10} |'.format('123', 'Kteam', 'TP HCM')
    row_4 = '| {:<6} | {:^15} | {:^10} |'.format('6969', 'Kquiz', 'Da Lat')
    row_5 = '+ {:-^6} + {:-^15} + {:-^10} +'.format('', '', '')
    # phần xuất kết quả
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    print(row_5)
    #title
    str6 = "nam vip pro"
    str7 = str6.title()
    print(str7)


 

if __name__ == "__main__":
    main()
   