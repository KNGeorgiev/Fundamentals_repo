version_list = list(map(int, input().split('.')))
version_list[2] += 1

if version_list[2] > 9:
    version_list[2] = 0
    version_list[1] += 1
    if version_list[1] > 9:
        version_list[1] = 0
        version_list[0] += 1

final_version = [str(x) for x in version_list]
print('.'.join(final_version))
