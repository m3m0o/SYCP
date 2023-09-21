import paramiko

with paramiko.SSHClient() as ssh_client:
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_client.connect('127.0.0.1', username='iragelac', password='201016')

    while True:
        stdin, stdout, stderr = ssh_client.exec_command(input('>>> '))

        print()

        if stderr.readlines():
            print(stderr.readlines())
            print()
            
            continue

        for line in stdout.readlines():
            print(line, end='')
        
        print()