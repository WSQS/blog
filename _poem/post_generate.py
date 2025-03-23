import os
import shutil

dir_path = "/home/sophomore/Documents/note/blog/_poem"
post_path = "/home/sophomore/Documents/note/blog/_posts"


def main():
    files = os.listdir(dir_path)
    for file_name in files:
        if not file_name.endswith(".md"):
            continue
        file_path = os.path.join(dir_path, file_name)
        new_file = ""
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")
            date = lines[2].removeprefix("date:").strip()
            year = date[:4]
            month = date[5:7]
            day = date[8:10]
            new_file = f"{year}-{month}-{day}-{file_name}"
            print(new_file)
        shutil.copy2(file_path, os.path.join(post_path, new_file))


if __name__ == "__main__":
    main()
