import os

for dir_path, dir_names, file_names in os.walk("."):
    if not any(dir_path.startswith("./" + x) for x in "client rs . infra".split()):
        print(dir_path)
        for file in file_names:
            if file.endswith(".py"):
                path = os.path.join(dir_path, file)
                new_content = open(path).read().replace("render", "render")
                open(path, "w").write(new_content)
    # for file in file_names:
    #     if file.endswith(".py"):
    #         print(os.path.join(dir_path, file))
