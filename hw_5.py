count_q = True
# ไว้เก็บค่า
count_num = []

#รับค่าเรื่อยๆ
while count_q:
    
    user_input = int(input("Input :"))
    count_num.append(user_input)

    #ถ้ากด -1 ให้ออกโปรแกรม
    if user_input == -1:
        count_q = False
#เก็บค่าความถี่
count_num_seq = {x:count_num.count(x) for x in count_num}
# print(count_num_seq)

#นำค่าkey มากสุด 
max_val = max(count_num_seq,key=count_num_seq.get)

#เอาตัวความถี่มากสุด
max_count = max(count_num_seq.values())
print("Mode is",max_val)
print("Appear",max_count,"times")

