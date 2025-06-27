from functions.get_files_info import get_files_info

test_1 = get_files_info("calculator", ".")
print(test_1)

test_2 = get_files_info("calculator", "pkg")
print(test_2)

test_3 = get_files_info("calculator", "/bin")
print(test_3)

test_4 = get_files_info("calculator", "../")
print(test_4)