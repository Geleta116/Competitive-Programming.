class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = []
        path = path.split("/")
        print(path)
        for each_path in path:
            if each_path == "" or each_path == ".":
                continue
            elif each_path == "..":
                if len(paths)>=1:
                    paths.pop()
                else:
                    continue
            else:
                paths.append(each_path)
        return "/"+"/".join(paths)
    
