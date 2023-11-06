import subprocess
import os

from .sbieini import SbieIni


class Sandboxie:
	def __init__(self, installation_dir=None):
		"""
		Takes installation_dir as an argument,
		if absent, looks for a folder in the environment variable
		or a possible standard Sandboxie-Plus installation

		:param installation_dir:
		"""
		self.installation_dir = installation_dir
		self.start_path = self.installation_dir + r'\Start.exe'
		self.default_sndb_options = {
			'Enabled': 'y',
			'RecoverFolder': '%Desktop%',
			'BorderColor': '#00ffff,ttl,6',
			'Template': 'AutoRecoverIgnore',
			'ConfigLevel': '10',
			'BlockNetParam': 'n'
		}
		self.sbieini = SbieIni(self.installation_dir)

		if 'DefaultBox' not in self.get_sandboxes():
			self.create_default_box()

	def start_execute(self, args, **kwargs):
		"""
		Launch Sandboxie Plus Start.exe

		:param args: list of command and its parameters
		:param kwargs: subprocess.Popen launch arguments
		:return: subprocess.Popen object
		"""

		args.insert(0, self.start_path)
		with subprocess.Popen(args, **kwargs) as proc:
			return proc

	def start(self, proc, box=None, env=None, silent=False, elevate=False, hide_window=False, wait=False, **kwargs):
		"""
		The function is designed to run a process in Sandboxie-Plus emulation

		:param proc: name of the program being launched
		:param box: the name of the sandbox in which the process will run
		:param env: specifying an environment variable, for example VariableName="Variable Value With Spaces"
		:param silent: can be used to eliminate some pop-up error messages
		:param elevate: to run the program with administrator rights
		:param hide_window: hide working window
		:param wait: can be used to run a program, wait for it to finish, and return the exit status from the program
		:param kwargs: specify to pass to subprocess.Popen initialization
		:return: subprocess.Popen object
		"""

		command = []

		if box:
			command.append(f'/box:{box}')
		if env is not None:
			command.append('/env:VariableName=' + env)
		if silent:
			command.append('/silent')
		if elevate:
			command.append('/elevate')
		if hide_window:
			command.append('/hide_window')
		if wait:
			command.append('/wait')

		command.append(proc)

		return self.start_execute(command, **kwargs)

	def terminate(self, box=None):
		"""
		Terminate all programs running in a particular sandbox

		:param box: the name of the sandbox in which the processes will be terminated
		:return: None
		"""

		command = []
		if box:
			command.append(f'/box:{box}')

		command.append('/terminate')
		self.start_execute(command)

	def terminate_all(self):
		"""
		Terminates all programs in all sandboxes

		:return: None
		"""

		self.start_execute(['/terminate_all'])

	def mount(self, key, box=None, protected=False):
		"""
		Mounting an encrypted sandbox image

		:param key: box image password
		:param box: the name of the sandbox to which the mount will be applied
		:param protected: mounts encrypted box images with the Box Root Protection
		:return: None
		"""

		command = []
		if box:
			command.append(f'/box:{box}')

		command.append(f'/key:{key}')

		if protected:
			command.append('/mount_protected')
		else:
			command.append('/mount')

		self.start_execute(command)

	def unmount(self, box=None):
		"""
		These commands unmount encrypted box images or ram disks created by Sandboxie Plus

		:param box: the name of the sandbox to which the unmount will be applied
		:return: None
		"""

		command = []
		if box:
			command.append(f'/box:{box}')

		command.append('/unmount')
		self.start_execute(command)

	def unmount_all(self):
		"""
		Terminates all programs in all encrypted sandboxes and then unmounts all encrypted box images

		:return: None
		"""

		self.start_execute(['/unmount_all'])

	def delete_content(self, box=None, silent=False, phase=None):
		"""
		Removing sandbox content

		:param box: the name of the sandbox in which the content will be deleted, by default DefaultBox
		:param silent: indicates Sandboxie Start should silently ignore any errors and not display any error messages
		:param phase: it is indicated at which stage the deletion will occur (1 or 2), by default both are applied
		:return: None
		"""

		command = []
		if box:
			command.append(f'/box:{box}')
		if silent:
			command.append('delete_sandbox_silent')
		else:
			command.append('delete_sandbox')
		if phase:
			command[-1] += f'_phase{phase}'

		self.start_execute(command)

	def list_pids(self, box=None):
		"""
		List the system process ID numbers for all programs running in a particular sandbox

		:param box: the name of the sandbox from which system process IDs will be listed
		:return: returns list pids
		"""

		command = []
		if box:
			command.append(f'/box:{box}')

		command.append('/listpids')
		return self.start_execute(command).decode('utf-8').split()

	def reload(self):
		"""
		Reloads the sandbox configuration

		:return: None
		"""

		self.start_execute(['/reload'])

	def disable_force(self, proc_path):
		"""
		Running a program outside the sandbox

		:param proc_path: path to the program to be launched
		:return: None
		"""

		self.start_execute(['/disable_force ' + proc_path])

	def create_default_box(self):
		for k, v in self.default_sndb_options.items():
			self.sbieini.set('DefaultBox', k, v)

		self.reload()

	def get_sandboxes(self):
		return self.sbieini.query(specify=True, boxes=True)

	def create_sandbox(self, name, options=None):
		if name not in self.get_sandboxes():
			if not options:
				for k, v in self.default_sndb_options.items():
					self.sbieini.set(name, k, v)
			else:
				for k, v in options.items():
					self.sbieini.set(name, k, v)

		self.reload()

	def delete_sandbox(self, name):
		query = self.sbieini.query(name)
		for option in query:
			self.sbieini.set(name, option)

		self.reload()


if __name__ == '__main__':
	_path = r'C:\Program Files\Sandboxie-Plus'
	sndb = Sandboxie(installation_dir=_path)
