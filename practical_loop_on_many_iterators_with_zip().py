# ----------------------------------------------------
# -- practical => loop on many iterators with zip() --
# ----------------------------------------------------



list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "yousef", "Age":23, "Country":"Egypt", "Skill":"python"}

  
for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1)  :
    
    print("list 1 item =>", item1)
    print("list 2 item =>", item2)
    print("tuple 1 item =>", item3)
    print("dict 1 key =>", item4, "value =>", dict1[item4])
  
  