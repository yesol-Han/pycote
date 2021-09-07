def solution(record):
    rec = [rec.split() for rec in record]
    name_dict = {}
    for tup in rec:
        if len(tup) > 2:
            name_dict[tup[1]] = tup[2]
    def get_command_line(command):
        if 'Enter' == command[0]:
            return f'{name_dict[command[1]]}님이 들어왔습니다.'
        elif 'Leave' == command[0]:
            return f'{name_dict[command[1]]}님이 나갔습니다.'
        
    return [get_command_line(r) for r in rec if r[0] != 'Change']