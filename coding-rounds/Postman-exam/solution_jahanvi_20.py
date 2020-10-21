def fetch_logs(string_log):
    last_partition = string_log[string_log.find('"') + 1 :]
    statusAndBytes = [int(element) for element in last_partition[last_partition.find('"') + 2 :].split(" ")]
    print(statusAndBytes)
    if statusAndBytes[1] > 5000:
        return [True, statusAndBytes[1]]
    else:
        return [False, statusAndBytes[1]]
    # print(statusAndBytes)
    # print([string_log[:string_log.find(" - - ")],string_log[string_log.find(" - - ")+5:string_log.find('"')-1],last_partition[:last_partition.find('"')]])


if __name__ == "__main__":
    # string_log='unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985'
    count = 0
    counter = 0
    filename="hosts_access_log_00.txt"
    with open(filename) as f:
        strings = f.readlines()
        for string in strings:
            data = fetch_logs(string)
            # print(data)
            if data[0]:
                count += data[1]
                counter += 1
    with open ("bytes_"+filename, mode="w+") as f:
        # f.write(counter)
        # f.write([str(counter),str(count)])
        f.write(str(counter))
        f.write("\n" + str(count))

