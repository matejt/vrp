# logic to detect the environment

def detect_env():
	if something.exist:
		# extract the env symbol
		env = 'w'

	if env in ('w', 'd', 's', 'c', 'p'):
		return env
	else raise Exception('Unknown environment: {}'.format(env)


envs = {
	'w': {'name': 'local'},
	'd': {'name': 'dev'},
	's': {'name': 'sit'},
	'c': {'name': 'cat'},
	'p': {'name': 'prod'},
}

conf = envs.get(detect_env())
