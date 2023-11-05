import subprocess


class SbieIni:
    def __init__(self, installation_dir=None):
        """
        Takes the path to the installed program as an argument

        :param installation_dir: path to the installed Sandboxie
        """

        self.installation_dir = installation_dir
        self.sbieini_path = installation_dir + r'\SbieIni.exe'

    def execute_sbieini(self, command):
        return subprocess.check_output(self.sbieini_path + f' {command}')

    def query(self, section=None, setting=None, specify=False, expand=False, boxes=False):
        """
        Getting information about the current sandbox

        :param section: the name of your sandbox
        :param setting: name of the setting that will be searched
        :param specify: specify * for section to get a list of sections or setting in the configuration
        :param expand: to expand variables in the value of the setting
        :param boxes: to get a list of sections which correspond to sandboxes
        :return: None
        """

        command = ['query']

        if expand:
            command.append('/expand')
        if boxes:
            command.append('/boxes')
        if section:
            command.append(section)
        if setting:
            command.append(setting)
        elif specify:
            command.append('*')

        return self.execute_sbieini(' '.join(command)).decode('utf-8').split()

    def set(self, section, setting, value=None):
        command = f'set {section} {setting}'

        if value:
            command += f' {value}'

        self.execute_sbieini(command)

    def append(self, section, setting, value):
        self.execute_sbieini(f'append {section} {setting} {value}')

    def insert(self, section, setting, value):
        self.execute_sbieini(f'insert {section} {setting} {value}')

    def delete(self, section, setting, value):
        self.execute_sbieini(f'delete {section} {setting} {value}')


if __name__ == '__main__':
    _path = r'C:\Program Files\Sandboxie-Plus'
    sbieini = SbieIni(_path)
    print(sbieini.query(specify=True, boxes=True))
