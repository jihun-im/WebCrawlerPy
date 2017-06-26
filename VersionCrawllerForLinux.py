from subprocess import call
from subprocess import check_output
from datetime import datetime
import JiraPageMaker


command_list = []
result_list = []
command_list.append('cat /etc/*-release | sed -n 4p | cut -c 22-39')
command_list.append('java -version 2>&1 | sed -n 1p')
command_list.append('java -version 2>&1 | sed -n 2p')
command_list.append('java -version 2>&1 | sed -n 3p')
command_list.append('git --version ')
command_list.append('gcc --version | sed -n 1p')
command_list.append('mysql -ujihun.im -pmib5team! -h10.164.44.32 VW_MIB3_OI --version')
command_list.append('svn info http://val.lge.com/ivi/svn/vw_mib3_oi/trunk | grep Revision | awk \'{print \"SVN \"$1$2}\'')
command_list.append('echo \"Enterprise Architect version: 13.0.1306 (Build: 1306) - Unicode\"')
command_list.append('apt list --installed')
#command_list.append('dpkg -l')


for command in command_list:
    result_list.append(check_output(command, shell=True).decode('utf-8').rstrip())


content = ""
for result in result_list:
    content = content +  "<p>" + result + "</p>"

pateTitle = datetime.today().strftime('%Y/%m/%d')

result = JiraPageMaker.createContent(pateTitle, content)
print('creating collab page result : ' + str(result))

